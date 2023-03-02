---
layout: post
title: "PATH FOLLOWING ROBOT"
description: "Simulation of a robot that follows a specified path"
categories: envision
thumbnail: "thumbnail.jpeg"
year: 2022
---

<!-- ### Project Guide

-(Add name and designation,if any) -->

### Mentors

- Shivani Chanda
- Spandan Patkar
- Sunaina Sunil

### Members

- Pratham Kiran K
- Joel Jojo Painuthara
- M Shreyas Shennoy
- Sreehari Krishnan
- Siddhardha V Sreeramagiri
- Gulshan Goyal

<!-- ## Acknowledgements

(If you have a guide, acknowledge it here) -->

## Aim

This project as a part of Envision organized by IEEE NITK Chapter, aims to create the successful simulation of a bot with the purpose of following a path specified previously. The project is a small attempt at mimicking the basic function of industrial bots which are designed to haul heavy loads along stipulated paths in working environments dealing with large amounts of goods of different varieties, like warehouses.

## Introduction

The present world is heavily reliant on automation, especially in places where it's dangerous for humans to work. One such example is huge warehouses. Moving large quantities of products across huge warehouses in perfect coordination is difficult to be achieved by humans. This is where autonomous robots come in.
This project aims to explain how these robots work on a basic level, following a path specified by us. These types of bots have uses that far exceed warehouses from delivery robots to even self-driving cars.

## Literature Survey

### Robot Operating System(ROS)

ROS is an open-source, meta-operating system to operate robots maintained by Open Robotics. ROS provides the services of an operating system such as hardware abstraction, low-level device control, implementation of commonly-used functionality, message-passing between processes, and package management. ROS also provides tools and libraries for obtaining, building, writing and running code across multiple computers. ROS currently only runs on Unix-based platforms. Software for ROS is primarily tested on Ubuntu and Mac OS X systems, though the ROS community has been contributing support for Fedora, Gentoo, Arch Linux and other Linux platforms. Keeping in mind the latest developments and package statuses in ROS versions - we opted for ROS Noetic, compatible with Ubuntu 20.04.
Basic Terminology of ROS:

- Nodes: A node is an executable that uses ROS to communicate with other nodes. A ROS Node can be a Publisher or a Subscriber. A Publisher puts the messages of a standard message type to a particular topic. The Subscriber, on the other hand, subscribes to the topic and receives the messages that are published to the topic.
- Messages: ROS data type used upon subscribing or publishing to a topic.
- Topics: Nodes can publish messages to a topic as well as subscribe to a topic to receive messages.
- Master: Name service for ROS (i.e. helps nodes find each other)
- rosout: ROS equivalent of stdout/stderr
- roscore: Master + rosout + parameter server (parameter server will be introduced later)

## Turtlebot

Turtlebot is a low-cost, personal robot kit with open-source software.
It is a ROS standard platform robot. It uses Raspberry Pi as its default computer but is also compatible with Jetson Nano SBC.
![turtlebot3](/virtual-expo/assets/img/SIG/turtlebot3.png)

### Turtlebot Dynamics

A TurtleBot generally has two independent parallel motor driven wheels. To move forward or backwards, the wheels rotate in the same direction and at the same speed. To turn or change directions, either of the wheels rotate in a particular direction or the wheels rotate in the opposite directions.
In the project, TurtleBot was simulated using gazebo. The bot was controlled using ROS nodes by passing values such as linear velocity and angular velocity.
Since the software simulates real world environments, small inconsistencies arise causing motion in unexpected directions. This issue is solved by continuously cross checking the actual position from the expected positions, and correcting it accordingly.
![simulation of bot](/virtual-expo/assets/img/envision/piston/world.png)

### Working of ROS

- All the code which controls the working of the TurtleBot is written in the form of nodes. Each node can be executed using the command line. We can have multiple nodes running simultaneously.
- Each node can subscribe or publish to a topic, for data exchange with other nodes and with the TurtleBot itself.
- The TurtleBot publishes the image details received from the camera and into a certain topic.
- A node subscribes to the said topic, processes the information and plans the path accordingly.
- Finally, motion commands for this path are published into the topic which contains information about the TurtleBot's motion.
- Some of the most frequently used topics are:

#### i)/cmd_vel: Data published to this topic is used to drive the bot.

#### ii)/odom: This topic contains the data about the bot's position and motion.

#### iii)/scan:This topic contains the data obtained by the LIDAR sensor mounted on the TurtleBot.

#### iv)/camera/rgb/image_raw: This topic contains the video that is obtained by the camera mounted on the bot.

## Computer Vision

The detection class first and foremost obtains an image from the turtlebot in the simulated environment , performs color thresholding , masking and centroid detection to communicate the required direction for the robot to move in.

This is achieved by using OpenCV, a python library dedicated to the purpose of real time computer Vision and optimization especially for applications in the field of Machine learning and Artificial Intelligence.

The ROS simulation makes use of the OpenCV module prepared in Python for achieving the purpose of line detection, differentiation and path following. It also makes use of rospy and cv_bridge for integration with ROS and making the simulation in the GAZEBO environment possible.

Some of the explanation of the codes are:

rospy.Subsriber: Designates the Camera input as ‘Subscriber’

cv2.Moments: finds the centroid of the given shape, in this case it is the line which the bot needs to follow

cv2.circle: indicates the centroid approximately by a circle of given dimension,color and thickness. In this case, it is a red coloured circle.

## Conclusion

The robot has been exported to the Gazebo environment successfully.The robot simulation showed successful path tracking.

## Scope

- The robot repository can be integrated with the help of suitable hardware components, such as Raspberry PI, into a working model. Since the model uses path following technicality, the working model of the robot can be implemented with rather cheap parts like a webcam for successful deployment.
- The Computer Vision code can be edited to provide line following for different shades, like red, blue, etc.
- The functionality of the bot can be customized as per personal needs by building onto the basic path following system. For example, it could be customized to reach one out of many possible goals by following additional commands set by the operator.

## References

- https://github.com/sudrag/line_follower_turtlebot
- Robot operating system Documentations, [Link](http://wiki.ros.org/Documentation)
- https://github.com/DougUOW/line_follower_pkg/tree/master/src
- https://github.com/arjunskumar/Line-Follower--ROS
- OpenCV API, [Link](https://opencv.org/)
