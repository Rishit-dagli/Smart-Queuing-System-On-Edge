# Smart-Queuing-System-On-Edge

[![](https://img.shields.io/badge/Rishit-Dagli-brightgreen.svg?colorB=00ff00)](https://www.rishit.tech)
![License](https://img.shields.io/github/license/Rishit-dagli/Smart-Queuing-System-On-Edge)
[![Python Version](https://img.shields.io/badge/Python-3.5|3.6-blue.svg)](https://shields.io/)
![Python Syntax](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/workflows/Python%20Syntax/badge.svg)
![GitHub followers](https://img.shields.io/github/followers/Rishit-dagli?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/rishit_dagli?style=social)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

[![IMAGE ALT TEXT HERE](https://github.com/Rishit-dagli/Smart-Queuing-System-On-Edge/blob/master/images/reatil_cover.JPG)](https://youtu.be/W-DWBYhrwj0)

Click the image above to see a video of the demo or use the link [here](https://youtu.be/W-DWBYhrwj0)

## What it Does

The Smart Queuing System will deomnstrate how to create a video AI solution on the edge using Intel® hardware and software tools. The app
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

## About Intel DevCloud

The Intel® DevCloud for the Edge is a cloud service designed to help developers prototype and experiment with computer vision 
applications using the Intel® Distribution of OpenVINO™ Toolkit. Once registered, developers can access a series of Python and C++ based 
Jupyter Notebook tutorials and sample solutions and execute them directly from a web browser. Then, developers can create their own 
Jupyter Notebooks and quickly try them out on a variety of hosted Intel® hardware solutions specifically designed for deep learning 
inferencing.

The Intel® DevCloud for the Edge provides you with access to everything needed to begin working with sample applications, prototypes and 
tutorials. This includes pre-trained models, source code, test input images, video and data streams. Additionally, users can apply any 
of the pre-trained deep learning models available through the Intel® Distribution of OpenVino™ toolkit, or upload their own customized 
pre-trained deep-learning models to develop and test their own computer vision applications.

## Setup

### Install Intel® Distribution of OpenVINO™ toolkit

Utilize the classroom workspace, or refer to the relevant instructions for your operating system for this step.

- [Linux/Ubuntu](./linux-setup.md)
- [Mac](./mac-setup.md)
- [Windows](./windows-setup.md)
