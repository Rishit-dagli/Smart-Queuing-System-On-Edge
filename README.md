# Smart-Queuing-System-On-Edge

[![](https://img.shields.io/badge/Rishit-Dagli-brightgreen.svg?colorB=00ff00)](https://www.rishit.tech)
[![Python Version](https://img.shields.io/badge/Python-3.5|3.6-blue.svg)](https://shields.io/)
[![GitHub license](https://img.shields.io/github/license/Rishit-dagli/Smart-Queuing-System-On-Edge)](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/LICENSE)
![Python Syntax](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/workflows/Python%20Syntax/badge.svg)
![GitHub followers](https://img.shields.io/github/followers/Rishit-dagli?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/rishit_dagli?style=social)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

[![IMAGE ALT TEXT HERE](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/images/reatil_cover.JPG)](https://www.youtube.com/watch?v=W-DWBYhrwj0)

Click the image above to see a video of the demo or use the link [here](https://www.youtube.com/watch?v=W-DWBYhrwj0)

## Table of Contents

- [What it Does](#what-it-does)
- [How it Works](#how-it-works)
- [Requirements](#requirements)
  * [Hardware](#hardware)
  * [Software](#software)
- [Intel DevCloud](#intel-devcloud)
  * [Benefits of The Intel® DevCloud for the Edge](#benefits-of-the-intel-devcloud-for-the-edge)
- [Setup](#setup)
  * [Install Intel® Distribution of OpenVINO™ toolkit](#install-intel-distribution-of-openvino-toolkit)
  * [Get started with DevCloud](#get-started-with-devcloud)
- [Run the application](#run-the-application)
  * [Step 1 - Person Detection](#step-1---person-detection)
  * [Step 2 - Job Submission](#step-2---job-submission)
  * [Step 3 - Submitting the job](#step-3---submitting-the-job)
    + [Submit to an Edge Compute Node with an Intel CPU](#submit-to-an-edge-compute-node-with-an-intel-cpu)
    + [Submit to an Edge Compute Node with CPU and IGPU](#submit-to-an-edge-compute-node-with-cpu-and-igpu)
    + [Submit to an Edge Compute Node with a Neural Compute Stick 2](#submit-to-an-edge-compute-node-with-a-neural-compute-stick-2)
    + [Submit to an Edge Compute Node with IEI Mustang-F100-A10](#submit-to-an-edge-compute-node-with-iei-mustang-f100-a10)
  * [Step 4 - Compare performance](#step-4---compare-performance)

## What it Does

The Smart Queuing System deomnstrates how to create a video AI solution on the edge using Intel® hardware and software tools. The app
detects people in a specified area and accordingly detects the number of people in a queue. It would then also notify whether a person
would need to change the queue to reduce congestation. I strongly recommend you to read the 
[WRITEUP](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/WRITEUP_Choosing_the_right_hardware.pdf)

## How it Works

The [people counter script](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/person_detect.py) 
will use the Inference Engine included in the Intel® Distribution of OpenVINO™ Toolkit. To test out the script and determine which 
hardware would be best for a particular use case we use a 
[job submission script](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/queue_job.sh) 
Intel DevCloud to test the scripts on different hardware. To propose a hardware we take a note of the model loading time, inference time 
and FPS to do so.

## Requirements

### Hardware

* This project makes the use of Intel DevCloud to test on CPU, GPU, FPGA and VPU so no specific hardware is required..

### Software

* Intel® Distribution of OpenVINO™ toolkit 2019 R3 release.
* Python > 3.5, 3.6

## Intel DevCloud

The Intel® DevCloud for the Edge is a cloud service designed to help developers prototype and experiment with computer vision 
applications using the Intel® Distribution of OpenVINO™ Toolkit. Once registered, developers can access a series of Python and C++ based 
Jupyter Notebook tutorials and sample solutions and execute them directly from a web browser. Then, developers can create their own 
Jupyter Notebooks and quickly try them out on a variety of hosted Intel® hardware solutions specifically designed for deep learning 
inferencing.

The Intel® DevCloud for the Edge provides you with access to everything needed to begin working with sample applications, prototypes and 
tutorials. This includes pre-trained models, source code, test input images, video and data streams. Additionally, users can apply any 
of the pre-trained deep learning models available through the Intel® Distribution of OpenVino™ toolkit, or upload their own customized 
pre-trained deep-learning models to develop and test their own computer vision applications.

### Benefits of The Intel® DevCloud for the Edge

* Reduced time to access comprehensive Intel® development solutions, hardware and software, for deep learning and computer vision
application development with just an internet connection.
* Access to fully configured physical edge machines pre-installed with the Intel® Distribution of OpenVINO™ Toolkit (CPU, iGPU, VPU and
FPGA) hosted in the cloud powered by Intel® Xeon® Scalable processors.
* Ability to evaluate and choose the right Intel® hardware acceleration option for your application.
* A vast library of pre-trained models from the Intel® Distribution of OpenVINO™ Toolkit and ability to upload your own custom pre-
trained models to evaluate the best framework, topology, and hardware acceleration solution for your unique application.

## Setup

### Install Intel® Distribution of OpenVINO™ toolkit

- [Linux/Ubuntu](./linux-setup.md)
- [Mac](./mac-setup.md)
- [Windows](./windows-setup.md)

### Get started with DevCloud

Much of the Intel® DevCloud for the Edge documentation can be accessed without registering. You will need to register for an Intel®
DevCloud for the Edge account to explore, run the examples, upload your own code and test the hardware.

* On the Home page, click Sign in on the top right corner.
* Click Register and follow the prompts to enter the information requested.
* Within 48 hours you will receive an invitation email to your Intel® DevCloud for the Edge account.
* For increased security, the Intel® DevCloud for the Edge is protected by 2-factor authentication. Please check your email for the 6-
digit security code. Copy/paste the full URL from that email containing the uuid argument into a browser window. All current web 
browsers are supported.
* Follow the prompts to complete your Intel DevCloud account registration.
* Once you have completed account registration, you can return any time to the Home page and click Sign in at the top right corner to 
access your account.
* Each time you sign in, the top right corner displays the total number of days you have access to the Intel® DevCloud for the Edge 
resource. You can request an extension from within the portal.

## Run the application

The figure below illustrates the user workflow for code development, job submission and viewing results.

![](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/images/How-DevCloud-works.svg)

<details open>
<summary>Credits</summary>
<br>
<a href="https://devcloud.intel.com/edge/">Intel DevCloud website</a>
</details>

### Step 1 - Person Detection

The [person_detect.py](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/person_detect.py) file does the person
counting part for you. Try to experiment around with the threshold value and see how the predictions turn up.

### Step 2 - Job Submission

The [queue_job.sh](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/queue_job.sh) is the utility which  
helps in the submission of the job to multiple devices on the DevCloud.

### Step 3 - Submitting the job

The project majorly includes 3 notebooks for different use cases-

* [Retail Scenario](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/Retail_Scenario.ipynb)
* [Manufacturing Scenario](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/Manufacturing_Scenario.ipynb)
* [Transportation Scenario](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/Transportation_Scenario.ipynb)

Each of the above notebooks follow this process, be sure to change the original video location according to your system in each case.

#### Submit to an Edge Compute Node with an Intel CPU

We write a script to submit a job to an 
[IEI Tank* 870-Q170](https://software.intel.com/en-us/iot/hardware/iei-tank-dev-kit-core) edge node with an [Intel Core™ i5-6500TE processor](https://ark.intel.com/products/88186/Intel-Core-i5-6500TE-Processor-6M-Cache-up-to-3-30-GHz-). 
The inference workload should run on the CPU.

```sh
cpu_job_id = !qsub queue_job.sh -d . -l nodes=1:tank-870:i5-6500te -F "[model_path] CPU [original_video_path] /data/queue_param/manufacturing.npy [output_path] 2" -N store_core
```

#### Submit to an Edge Compute Node with CPU and IGPU

We write a script to submit a job to an [IEI Tank* 870-Q170](https://software.intel.com/en-us/iot/hardware/iei-tank-dev-kit-core) edge
node with an [Intel® Core i5-6500TE](https://ark.intel.com/products/88186/Intel-Core-i5-6500TE-Processor-6M-Cache-up-to-3-30-GHz-). The
inference workload should run on the Intel® HD Graphics 530 integrated GPU.

```sh
gpu_job_id = !qsub queue_job.sh -d . -l nodes=tank-870:i5-6500te:intel-hd-530 -F "[model_path] GPU [original_video_path] /data/queue_param/manufacturing.npy [output_path] 2" -N store_core
```

#### Submit to an Edge Compute Node with a Neural Compute Stick 2

We write a script to submit a job to an [IEI Tank 870-Q170](https://software.intel.com/en-us/iot/hardware/iei-tank-dev-kit-core) edge
node with an [Intel Core i5-6500te CPU](https://ark.intel.com/products/88186/Intel-Core-i5-6500TE-Processor-6M-Cache-up-to-3-30-GHz-).
The inference workload should run on an [Intel Neural Compute Stick 2](https://software.intel.com/en-us/neural-compute-stick) installed 
in this node.

```sh
vpu_job_id = !qsub queue_job.sh -d . -l nodes=tank-870:i5-6500te:intel-ncs2 -F "[model_path] MYRIAD [original_video_path] /data/queue_param/manufacturing.npy [output_path] 2" -N store_core
```

#### Submit to an Edge Compute Node with IEI Mustang-F100-A10

We write a script to submit a job to an [IEI Tank 870-Q170](https://software.intel.com/en-us/iot/hardware/iei-tank-dev-kit-core) edge
node with an [Intel Core™ i5-6500te CPU](https://ark.intel.com/products/88186/Intel-Core-i5-6500TE-Processor-6M-Cache-up-to-3-30-GHz-).
The inference workload will run on the [IEI Mustang-F100-A10 FPGA](https://www.ieiworld.com/mustang-f100/en/) card installed in this 
node.

```sh
fpga_job_id = !qsub queue_job.sh -d . -l nodes=1:tank-870:i5-6500te:iei-mustang-f100-a10 -F "[model_path] HETERO:FPGA,CPU [original_video_path] /data/queue_param/manufacturing.npy [output_path] 2" -N store_core
```

### Step 4 - Compare performance

We then compare performance on these devices on these 3 metrics-

* FPS
* Model Load Time
* Inference Time
