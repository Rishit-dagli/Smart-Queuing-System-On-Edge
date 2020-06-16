
import numpy as np
import time
from openvino.inference_engine import IENetwork, IECore
import os
import cv2
import argparse
import sys


class Queue:
    """
    Class for dealing with queues.
    
    Performs basic operations for queues like adding to a queue, getting the queues 
    and checking the coordinates for queues.
    
    Attributes:
        queues: A list containing the queues data
    """
    
    def __init__(self):
        self.queues=[]

    def add_queue(self, points):
        """
        Add points to the queue.

        Args:
            points: A list of points to be added.

        Raises:
            TypeError: points is None.
        """
        
        self.queues.append(points)

    def get_queues(self, image):
        """
        Get queues from images.

        Args:
            image: A list of the image.

        Yields:
            A list containing each frame.
        """
            
        for q in self.queues:
            x_min, y_min, x_max, y_max=q
            frame=image[y_min:y_max, x_min:x_max]
            yield frame
    
    def check_coords(self, coords, initial_w, initial_h):
        """
        Check coordinates for queues.

        Args:
            coords: A list of the coordinates.
        """
        
        d={k+1:0 for k in range(len(self.queues))}
        
        dummy = ['0', '1' , '2', '3']
        
        for coord in coords:
            xmin = int(coord[3] * initial_w)
            ymin = int(coord[4] * initial_h)
            xmax = int(coord[5] * initial_w)
            ymax = int(coord[6] * initial_h)
            
            dummy[0] = xmin
            dummy[1] = ymin
            dummy[2] = xmax
            dummy[3] = ymax
            
            for i, q in enumerate(self.queues):
                if dummy[0]>q[0] and dummy[2]<q[2]:
                    d[i+1]+=1
        return d


class PersonDetect:
    """
    Class for the Person Detection Model.
    
    Performs person detection and preprocessing.
    
    Attributes:
        model_weights: A string containing model weights path.
        model_structure: A string conatining model structure path.
        device: A string conatining device name.
        threshold: A floating point number containing threshold value.
        input_name: A list of input names.
        input_shape: A tuple of the input shape.
        output_name: A list of output names.
        output_shape: A tuple of the output shape.
        core: IECore object.
        net: Loaded net object.
    """

    def __init__(self, model_name, device, threshold=0.60):
        """
        Inits PersonDetect class with model_name, device, threshold.
        """
        
        self.model_weights=model_name+'.bin'
        self.model_structure=model_name+'.xml'
        self.device=device
        self.threshold=threshold

        try:
            self.model=IENetwork(self.model_structure, self.model_weights)
        except Exception as e:
            raise ValueError("Could not Initialise the network. Have you enterred the correct model path?")

        print('Creating model...')
        self.input_name=next(iter(self.model.inputs))
        self.input_shape=self.model.inputs[self.input_name].shape
        self.output_name=next(iter(self.model.outputs))
        self.output_shape=self.model.outputs[self.output_name].shape

    def load_model(self):
        """
        Loads the model.
        """
        
        self.core = IECore()
        self.net = self.core.load_network(network=self.model, device_name=self.device, num_requests=1)
        print('Network loaded...')
        
    def predict(self, image):
        """
        Make asynchronous predictions from images.

        Args:
            image: List of the image data.

        Returns:
            The outputs and the image.
        """
        
        input_name = self.input_name

        input_img = self.preprocess_input(image)
              
        input_dict={input_name: input_img}  
        
        # Start asynchronous inference for specified request.

        infer_request_handle = self.net.start_async(request_id=0, inputs=input_dict)
        infer_status = infer_request_handle.wait()
        if infer_status == 0:
            outputs = infer_request_handle.outputs[self.output_name]
            
        return outputs, image
    
    def draw_outputs(self, coords, frame, initial_w, initial_h):
        """
        Draws outputs or predictions on image.

        Args:
            coords: The coordinates of predictions.
            image: The image on which boxes need to be drawn.

        Returns:
            the frame
            the count of people
            bounding boxes above threshold
        """
        
        current_count = 0
        det = []
        
        for obj in coords[0][0]:
            
            # Draw bounding box for the detected object when it's probability 
            # is more than the specified threshold
            if obj[2] > self.threshold:
                xmin = int(obj[3] * initial_w)
                ymin = int(obj[4] * initial_h)
                xmax = int(obj[5] * initial_w)
                ymax = int(obj[6] * initial_h)
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 55, 255), 1)
                current_count = current_count + 1
                
                det.append(obj)
                
        return frame, current_count, det

    def preprocess_outputs(self, outputs):
        """
        Preprocess the outputs.

        Args:
            outputs: The output from predictions.

        Returns:
            Preprocessed dictionary.
        """
        
        output_dict = {}
        for output in outputs:
            output_name = self.output_name
            output_img = output
            output_dict[output_name] = output_img
        
        return output_dict
    
        return output
        

    def preprocess_input(self, image):
      
        input_img = image
        
        # Preprocessing input
        n, c, h, w = self.input_shape
        
        input_img=cv2.resize(input_img, (w, h), interpolation = cv2.INTER_AREA)
        
        # Change image from HWC to CHW
        input_img = input_img.transpose((2, 0, 1))
        input_img = input_img.reshape((n, c, h, w))

        return input_img


def main(args):
    model=args.model
    device=args.device
    video_file=args.video
    max_people=args.max_people
    threshold=args.threshold
    output_path=args.output_path

    start_model_load_time=time.time()
    pd= PersonDetect(model, device, threshold)
    pd.load_model()
    total_model_load_time = time.time() - start_model_load_time

    queue=Queue()
    
    try:
        queue_param=np.load(args.queue_param)
        for q in queue_param:
            queue.add_queue(q)
    except:
        print("error loading queue param file")

    try:
        cap=cv2.VideoCapture(video_file)
    except FileNotFoundError:
        print("Cannot locate video file: "+ video_file)
    except Exception as e:
        print("Something else went wrong with the video file: ", e)
    
    initial_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    initial_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_len = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out_video = cv2.VideoWriter(os.path.join(output_path, 'output_video.mp4'), cv2.VideoWriter_fourcc(*'avc1'), fps, (initial_w, initial_h), True)
    
    counter=0
    start_inference_time=time.time()

    try:
        while cap.isOpened():
            ret, frame=cap.read()
            if not ret:
                break
            counter+=1
            coords, image= pd.predict(frame)
            frame, current_count, coords = pd.draw_outputs(coords, image, initial_w, initial_h)
            print(coords)
        
            num_people = queue.check_coords(coords, initial_w, initial_h)
            print(f"Total People in frame = {len(coords)}")
            print(f"Number of people in queue = {num_people}")
            
            out_text=""
            y_pixel=25
            
            for k, v in num_people.items():
                print(k, v)
                out_text += f"No. of People in Queue {k} is {v} "
                if v >= int(max_people):
                    out_text += f" Queue full; Please move to next Queue "
                cv2.putText(image, out_text, (15, y_pixel), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                out_text=""
                y_pixel+=40

            out_video.write(image)
            
        total_time=time.time()-start_inference_time    
        total_inference_time=round(total_time, 1)
        fps=counter/total_inference_time

        with open(os.path.join(output_path, 'stats.txt'), 'w') as f:
            f.write(str(total_inference_time)+'\n')
            f.write(str(fps)+'\n')
            f.write(str(total_model_load_time)+'\n')

        cap.release()
        cv2.destroyAllWindows()
        
    except Exception as e:
        print("Could not run Inference: ", e)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--model', required=True)
    parser.add_argument('--device', default='CPU')
    parser.add_argument('--video', default=None)
    parser.add_argument('--queue_param', default=None)
    parser.add_argument('--output_path', default='/results')
    parser.add_argument('--max_people', default=2)
    parser.add_argument('--threshold', default=0.60)
    
    args=parser.parse_args()

    main(args)