---
layout: post
title: "Anti-Anti-Masker"
description: "A mid-pandemic attempt to innovate a drone that can pick out the unmasked among a crowd of people."
categories: piston
thumbnail: "anti-anti-masker.jpeg"
year: 2022
gmeet: https://meet.google.com/rgr-smga-wvk
---

### Project Guide

Dr. K. R. Guruprasad, Department of Mechanical Engineering

### Mentors


- Shobuj Paul
- Diptesh Banerjee


### Members


- Shivani Chanda
- Spandan Patkar
- Sunaina Sunil


## Acknowledgements


As executive members of IEEE NITK, we are extremely grateful for the opportunity to learn and work on this project under the prestigious name of IEEE NITK Student Chapter and under the apprenticeship of Dr Guruprasad K. R. It was a novel experience to work towards solving a real world problem related to the COVID-19.

## Aim

Anti-Anti-Masker aims to simulate a drone that will roam in crowded city areas and search for people who are breaking COVID-19 protocol by not wearing masks.This drone will have a camera that will have a face recognition system to detect faces with and without a mask.


## Introduction


The COVID-19 pandemic saw a surge in the number of cases of the SARS-COV-2 virus infection all across the globe. It was quite surprising to notice that despite knowing that the possibility of infection could be reduced by a huge margin through hygienic habits like washing hands with soap regularly, maintaining social distance and wearing a mask in public spaces, a huge number of people refuse to do something as simple as wear a mask, because of many unintelligent and baseless reasons.

The project ‘Anti-Anti-Maskers’ is an attempt to deal with such a situation, wherein we use a drone utilizing Artificial Intelligence for automatic detection of and differentiation between Masked and Unmasked people.


## Literature Survey

### Robot Operating System (ROS)

ROS is an open-source, meta-operating system to operate robots. ROS provides the services of an operating system such as hardware abstraction, low-level device control, implementation of commonly-used functionality, message-passing between processes, and package management. ROS also provides tools and libraries for obtaining, building, writing and running code across multiple computers. ROS currently only runs on Unix-based platforms. Software for ROS is primarily tested on Ubuntu and Mac OS X systems, though the ROS community has been contributing support for Fedora, Gentoo, Arch Linux and other Linux platforms.

### Basic Terminology:

- Nodes: A node is an executable that uses ROS to communicate with other nodes.
A ROS Node can be a Publisher or a Subscriber. A Publisher puts the messages of a standard message type to a particular topic. The Subscriber, on the other hand, subscribes to the topic and receives the messages that are published to the topic.
- Messages: ROS data type used upon subscribing or publishing to a topic.
- Topics: Nodes can publish messages to a topic as well as subscribe to a topic to receive messages.
- Master: Name service for ROS (i.e. helps nodes find each other)
- rosout: ROS equivalent of stdout/stderr
- roscore: Master + rosout + parameter server (parameter server will be introduced later)

Client libraries needed:
rospy: python client library
roscpp: c++ client library


### Turtlesim:
Turtlesim is a simple simulator used to understand ROS. Turtlesim gives a basic idea of what one can do with a real robot using ROS. Simulating turtlesim can be done using python code or a keypad. To execute teleoperation in turtlesim, turtle_teleop_key is used.

![turtlesim_teleop_key](/virtual-expo/assets/img/piston/turtlesim_teleop_key.png)

The Anti-Anti-Masker drone can be described as a turtlebot driven at a height.

## Prerequisites on PC

- Ubuntu 20.04
- ROS Noetic

Computer Vision Dependencies:
- Tensorflow 2.3.0
- CuDNN
- CUDA 10.1
- OpenCV 4.5.x


## Prerequisites on PC

- Ubuntu 20.04
- ROS Noetic

Computer Vision Dependencies:
- Tensorflow 2.3.0
- CuDNN
- CUDA 10.1
- OpenCV 4.5.x

## Computer Vision

The computer vision for the drone uses Convolutional Neural Networks for realtime image processing.A Neural Network is a series of algorithms made of units called 'nodes' which help in pattern recognition and machine learning. The type used in this project,Convolutional Neural Networks is among the most popular deep learning algorithm, widely used for image processing. Being more specific, the code uses MobileNetV2 architecture for doing the same. Owing to the use of MobileNetV2 architecture, it is very easy to deploy the pre-trained model on to embedded hardwares like Arduino and RasberryPi and making a real-life working model for this project. The model has been deployed employing Keras Dense layers (tf.keras.layers.Dense), with 128 dense layers of 'RELU' activation function and 2 additional layers of 'Softmax' activation function. The model gives a final train accuracy of 99.22% and a test accuracy of 98.19% for the dataset used.

- For Additional Details on Convolutional Layers used,refer
[Detection Model Block](https://github.com/IEEE-NITK/Anti-Anti-Masker/blob/model2/drone_vision/notebooks/Detection_Model_Readme.md).

The model code: [The notebook](https://github.com/IEEE-NITK/Anti-Anti-Masker/blob/model2/drone_vision/notebooks/Detection_Model.ipynb)

The model structure:
```
input = keras.layers.Input(shape=(224,224,3))
baseModel = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3), input_tensor= input)

headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(7, 7))(headModel)
headModel = Flatten()(headModel)
headModel = Dense(128, activation="relu")(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(2, activation="softmax")(headModel)
model = Model(inputs=baseModel.input, outputs=headModel)

for layer in baseModel.layers:
   layer.trainable = False
```
The CNN model parameter specifications are as follows:
- Total parameters: 2,422,210
- Trainable parameters: 164,226
- Non-trainable parameters: 2,257,984

 Training Loss and Accuracy plot:

![accuracy curve](/virtual-expo/assets/img/piston/accuracy curve.png)


<!--For TensorFlow 2 installation refer to this link: [TensorFlow Installation](drone_vision/README.md)-->



## Training Dataset

- The Dataset used is : [With/Without Mask Dataset](https://www.kaggle.com/niharika41298/withwithout-mask); which has been taken from Kaggle.
- The Training dataset for this particular model has been created with the help of the repository : [Masking code](https://github.com/prajnasb/observations/tree/master/mask_classifier/Data_Generator)
- The Training dataset includes both non-masked and masked images (black and white coloured masks used).
- The model has been trained on grayscale images stretched to 224x224 resolution, augmented to include:
1. Outputs per training example: 3 </t>
2. Rotation: Between -10° and +10°</t>
3. Shear: ±10° Horizontal, ±10° Vertical</t>
4. Blur: Up to 1.5px</t>
5. Noise: Up to 1% of pixel</t>
- Augmentation has been carried out using [Roboflow](https://app.roboflow.com/)

### Sample Images from dataset:
![Sample_Dataset](/virtual-expo/assets/img/piston/Sample_Dataset.png)

## Drone

### Drone Model:
The drone model used in this project is a quadcopter consisting of four rotors and sensors attached to the body of the drone.

The design of the quadcopter was developed on Fusion360, a 3D modelling CAD software. It was then directly exported as a URDF (Unified Robotic Description Format) file, accompanied by .stl files of the model as well as .launch and .yaml files to simulate it on Gazebo. The URDF is an XML file format used in ROS to describe all elements of a robot and can be generated using URDF_Exporter.

![drone_model_gazebo](/virtual-expo/assets/img/piston/drone_model_gazebo.jpg)


The drone is simulated in Gazebo, an open-source 3D robotics simulator that performs physics computations, generates synthetic sensor data and offers convenient interfaces to construct, introspect and interact with simulations. Within Gazebo, a physics engine is used to define realistic elements of an environment such as illumination, gravity and inertia.

The drone model includes two sensors, namely; a LIDAR system and a camera, mounted at the center of the quadcopter body.

A LIDAR (Light Detection and Ranging) system is centered around a sensor that sends out pulses of laser light using oscillating mirrors to measure the exact time it takes for these pulses to return as they bounce from the ground as well as the intensity of that reflection. The observed LIDAR data is used to locate obstacles in the path of the robot and navigate smoothly while avoiding the obstacles.

We use Gazebo plugins to provide the URDF models with greater functionality and to tie in ROS messages and service calls for sensor output and motor input. A GPU Laser plugin simulates the laser range sensor by broadcasting LaserScan message which comes under the topic sensor_msgs. The broadcasted LaserScan message displays relevant observation such as the range and intensity data. Meanwhile, the raw video feed from the camera link is obtained using a camera plugin. The camera plugin enables camera functionality and publishes the image to a ROS message under the topics image_raw and camera_info.

In order to make proper use of the data collected by devices such as sensors and cameras, the environment of the drone is mapped out in RViz. ROS Visualization (RViz) is the primary visualizer in ROS that enables us to visualize data gathered from the sensors and camera by setting up virtual environments. Using Rviz plugins, we can picture features such as local position and lidar data within the virtual environments.

![drone_sensor_rviz](/virtual-expo/assets/img/piston/drone_sensor_rviz.png)

### Drone Dynamics:

The quadcopter or quadrotor helicopter is a helicopter consisting of four equally spaced and independently controlled rotors mounted at the corners of a rigid planar cross frame. The unique configuration of quadcopters enables smooth vertical take-off and stable hovering in air. Each pair of opposite propellers attached to the rotor shafts rotates in one direction to avoid yaw torque during roll and pitch movements.

The quadcopter is maneuvered by manipulating the thrust and torque generated by the engines. The position and orientation of the quadcopter is controlled by varying the speed of the four engines. The quadcopter is under-actuated, with four engines and six degrees of freedom (three translational and three rotational).

### Drone Control:
The controller used for drone control in this project is the PID (proportional–integral–derivative) controller. A PID controller is a control loop feedback mechanism that calculates the difference between a desired setpoint and the actual output from a process, and uses the result to apply a correction to the process. It receives desired velocity commands on the cmd_vel topic as well as the global position from the odometry message and then carries out the drone movement. The PID controller objective is to reduce the error by adjusting a variable, such as the position of a robot arm or a robot car.


## Conclusion

The drone model was successfully simulated in an environment set up on Gazebo. The deep learning model was trained on a dataset of about 2000+ images and can achieve a Train accuracy of 99.22% and a Test accuracy of 98.19%. Combining the two, we have effectively completed the simulation of a drone that can smoothly traverse an area and classify the people present as masked and unmasked in real time.

The simulation of the Anti-Anti-Masked Drone has further scope to be implemented into a working model. This can be easily achieved using prevalent platforms such as Arduino or RaspberryPi. Ideally, the working model of the drone would be a significant contribution towards improving not only the Covid situation but also the mindsets of people, helping them realise their moral obligation towards society.


## References


1. [Di Puglia Pugliese, L., Guerriero, F., Zorbas, D.et al. Modelling the mobile target covering problem using flying drones. Optim Lett 10, 1021–1052(2016)](https://doi.org/10.1007/s11590-015-0932-1)
2. F. Schroff, D. Kalenichenko and J. Philbin, "FaceNet:A unified embedding for face recognition and clustering," 2015 IEEE Conference on ComputerVision and Pattern Recognition (CVPR),2015, pp. 815-823, doi: 10.1109/CVPR.2015.7298682.
3. Casado, R., & Bermúdez, A. (2020). A Simulation Frameworkfor Developing Autonomous DroneNavigation Systems. Electronics, 10, 7.
4. [UBUNTU 20.04 INSTALLATION](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/)
5. [ROS NOETIC INSTALLATION](http://wiki.ros.org/noetic/Installation/Ubuntu)
6. UDEMY COURSES FOR ROS :
	i.  [Course 1](https://www.udemy.com/course/ros-essentials/)
	ii. [Course 2](https://www.udemy.com/course/ros-navigation/)
7. [https://github.com/smitkesaria/vitarana_drone](https://github.com/smitkesaria/vitarana_drone)
8. [https://github.com/ipazc/mtcnn](https://github.com/ipazc/mtcnn)
9. [https://github.com/tahsinkose/sjtu-drone](https://github.com/tahsinkose/sjtu-drone)
