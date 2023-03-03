---
layout: post
title: "ML based Assembly Bot"
description: "The project aims to develop a robotic arm, in simulation, with an objective of segregation of different items based on size, shape and color scattered in a basket."
categories: envision
thumbnail: "placeholder-image.jpg"
year: 2022
---

### Mentors

- Aryan Amit Barsainyan
- Shashank H S

### Members

- Anish Kumbhar
- Harshit Ravindra Gawade
- Omkar Jungade
- Sathya P
- Shreyas Singh

## Aim

A robotic arm is a type of mechanical arm, usually programmable, with similar functions to a human arm. A robotic arm can be used for automating various tasks which reduces human effort which in turn will increase productivity. The project aims to develop a robotic arm, in simulation, with an objective of segregation of different items based on size, shape and color scattered in a basket using Machine Learning. This could further be implemented as a simplified warehouse mobile robot, which picks up and segregates the desired objects scattered in a room.

## Introduction

The idea is to create a basic version of the robots used in assembly areas in a product manufacturing industry, which could detect and sort objects automatically based on given criteria such as shape, color, etc. The project will make use of computer vision, a technology from the domain of Machine Learning, to solve the problem of detecting objects and getting their exact location. The robotic automation would be achieved through programming the robotic manipulators using inverse kinematics for the coordinates received through the ML model.

## Environment Setup

The project aims at integration of Robotics and Machine Learning. The Convolutional Neural Networks (CNNs) and OpenCV/PyTorch functions will be used for detecting objects in a basket and finding their locations using a bounding box. Then use a robotic arm to move the objects from one basket to the other.

![Env Setup](/virtual-expo/assets/img/envision/compsoc/environment_setup.png)

**PyBullet** was used in the project as the physics engine which comes along with the graphics renderer for visualization. PyBullet is an easy to use Python module for physics simulation for robotics, games, visual effects and machine learning. PyBullet provides forward dynamics simulation, inverse dynamics computation, forward and inverse kinematics, collision detection and ray intersection queries. We have used the Robotic Arm URDF that comes with the PyBullet package in this project.

## Heading 1

## Heading 2

### Subheading 2.1

<!-- ![image_2](/virtual-expo/assets/img/SIG/img2.jpg)

![image_3](/virtual-expo/assets/img/SIG/img3.jpg) -->

### Subheading 2.2

#### Subsubheading 2.2.1

## Heading 3

## Conclusion

- Conclusion1
- Conclusion2

## References

[Intro to Machine Learning by Andrew Ng](https://shorturl.at/nLT56)
[Neural Networks by 3Blue1Brown](https://shorturl.at/ovzBG)
[Deep Learning by New York University(NYU)](https://lnkd.in/eZFGQuGZ)
[Convolutional Neural Networks](https://shorturl.at/deqwP)
[Pybullet](https://www.youtube.com/watch?v=KaiznOkKkdA)
[Get Camera Image in PyBullet](https://towardsdatascience.com/simulate-images-for-ml-in-pybullet-the-quick-easy-way-859035b2c9dd)
[Bounding Box Prediction](https://towardsdatascience.com/bounding-box-prediction-from-scratch-using-pytorch-a8525da51ddc)
