---
layout: post
title: "3D Map Fed Robot"
description: "Simplifying Self-Localization with Feature Based Mapping"
categories: piston
thumbnail: "3d-map-robot.png"
---

### Mentors
-   Chandran Nandkumar

### Members

-   Pranshu Shukla
-   Viren Verma


# Abstract

In the field of robotics and automation systems - localization, navigation and path planning algorithms are some of the most interesting and exciting topics which are also currently under research. Especially in military applications, we often come to situations wherein we need to localize our current location and henceforth perform navigation and other operations. These problems involving self-localization are known as Kidnapped Robot Problem and in this project, we aim to present one solution using feature maps.

# Aim

The aim of this project to use implement self-localization and path planning on a known environment using the concept of feature based and particle maps, that is, given the floor map and the location of certain features of the room in the map – we intend to determine the location of our bot and finally perform path planning using to reach our desired destination or target.

# Methodology

To achieve the desired features and aspects of the project, we carefully considered the pros and cons of different frameworks and tools. Depending on the application and purpose, we divided the utilities into following categories:

### Simulation and Testing

For the purpose of implementing this project and simulating the results, we used the Robot Operating System (ROS) framework. It is an open-source development platform for robotics comprising a multitude of packages and software for building, writing and testing systems and processes. Keeping in mind the latest developments and package statuses in ROS versions - we opted for ROS Melodic Morenia, compatible with Ubuntu 18.04.

  

For attaining results which closely resembles the real world, Gazebo is used as the 3D simulator. Gazebo comes with ROS to provide frameworks that are able to generate a 3D scenario on your computer with robots, obstacles and many other objects utilizing properties of the physical engine for illumination, gravity, inertia, etc.

![](/virtual-expo/assets/img/piston/3DBOT_blog_1.png)  

For the purpose of simulating the project, we chose to use an open-source map “Office”. To meet with the objectives of the project of self - localization, we designated each room with different obstacles and identified them with names from Letters A to H. This was done to establish an ease of self-localization and have better results.

 
### Turtlebot3 - Waffle


TurtleBot is the standard robot platform in ROS and it comprises different sets of robots that can be used for a wide range of applications. Given the features of our project, we needed a robot that is featured with both Lidar and image sensors which led us to utilizing waffle as our standard robot.

![](/virtual-expo/assets/img/piston/3DBOT_blog_2.png)

  
TurtleBot3 waffle is a small and compact robot from the Turtlebot3 series. The TurtleBot3 can be customized as per requirements into various applications by reconstructing the location and behaviours of the input sensors. The Turtlebot3 package is also equipped with SLAM (simultaneous localization and mapping), Navigation and Manipulation etc.

### Mapping and Autonomous Navigation

Once the robot has successfully been able to recognize its surroundings, we wanted our robot to navigate out of the surrounding environment and reach the target location set initially. To achieve this, we needed to have the map of the environment ready beforehand. A map is the representation of the environment where the robot will be operating.

To create a map of the surroundings from a moving robot, it requires the readings to be “stitched” together from previous locations and keep track of all the measurements and movements of the robot. This technique is implied in SLAM - Simultaneous Localization and Mapping. It estimates the map of the environment and the trajectory of a moving device using a sequence of sensor measurements.

Alot of various SLAM techniques are available such as Gmapping, Hector mapping, Cartographer, Rtab mapping etc. For simplicity and robustness of the project, we opted for “Gmapping ''. This package provides laser-based techniques and is compacted as a ROS node called slam_gmapping using which a 2-D occupancy grid map can be generated.


![](/virtual-expo/assets/img/piston/3DBOT_blog_3.png)
  

To simplify the working of this package, it takes the measurement readings from odometry and laser scan, it tries to localize the bot along with the laser scan matching and then using Extended Kalman Filter (EKF) it estimates the output by fusing odometry and laser scan matching values. Along with this, it uses a particle filter for localization.


### Mapping and Localization with AMCL

AMCL or Adaptive Monte Carlo Localization is an algorithm that uses a known map of the environment (generated above using Gmapping), range sensor data from turtlebot3 - waffle and odometry sensor data to localize the robot. As mentioned above, this algorithm uses a particle filter to estimate the next position of the robots. The particles act as a representation of the probabilistic distribution of the likely states for the robot. 

![](/virtual-expo/assets/img/piston/3DBOT_blog_4.png)

By repetitive comparisons from sensor and odometry readings, AMCL recalculates the number of particles required for every iteration depending on where the results are most likely to occur and shifts the distribution more closely to that region.

### Object Detection and RTOA

Opencv was extensively used in the project starting from taking in the video feed from the turtle bot camera and using frame by frame images of the while loop to first resize and reshape to make it compatible with CNN’s input layer to classify which object does the image contain to further use Opencv to call Custom build Cascades previously built using opencv and Haarcascade builder GUI to use opencv’s detectMultiScale() function, being the most important function here as it scans the areas and tells us which object is present from the classes and where it is present in the frame

Now if both the layers of detection of the object fail assuming the CNN classifies the object incorrectly and so does the haarcascade (cause as we know the haarcascade is known to classify the Mars Rover and Quadcopter as the same object or detecting an object that’s not there by the CNN) then we use the tracker function in Opencv along with the bounding box option and taking the video feed from the camera and increasing brightness and save the images in a folder to create a dataset to retrain the model to increase its accuracy.

We also used Opencv to calculate the centroid of each object by using contour detection and Also very extensively by drawing on the images.

# Result

In this project we use concepts of Semi Supervised Learning and Reinforcement learning to strengthen our models' understanding of the object we are feeding into it. As a start we started to observe the classes that should be in our Neural Network as in all the objects that we are going to need to be detected which we settled on to be:

![](/virtual-expo/assets/img/piston/3DBOT_blog_5.png)

1. Mars Rover
2. Quadcopter 
3. Bowl 
4. Boxes
    

So, first things first we collected a lot of images from our virtual environment and manually labelled to make our training set. It was only a set of 60-70 images that had very less variation but seemed appropriate for the goal we were trying to achieve in unsupervised learning.

![](/virtual-expo/assets/img/piston/3DBOT_blog_6.png)


We then started making our custom CNN which could classify which object is present in our frame. So, after a lot of trial and error with neural network architecture (where we first made a model too complex for the images which saw massive overfitting and further, we reduced the complexity so that there is just enough overfitting that can be countered by adding more varied data later by our scanner which I will explain further). So once we got the 96% accuracy on our training data.

  
  
![](/virtual-expo/assets/img/piston/3DBOT_blog_7.png)

![](/virtual-expo/assets/img/piston/3DBOT_blog_8.png)

![](/virtual-expo/assets/img/piston/3DBOT_blog_vid.mp4)


