---
layout: post
title: "TSR Bot"
year: 2020
categories: diode
description: "A Project on Car Automation using Traffic Sign Recognition Technique"
thumbnail: "TSRupdated_thumb.jpg"
---

### Team Members

- Deepanshi
- Jyotsna M
- Karthik Rao
- Kumar Alabhya

![Image of Traffic Sign](/virtual-expo/assets/img/diode/car-automation-img1.jpg)

## Abstract

Car automation is a rising field in the research area today . The previous decade saw a number of algorithm for making self driving car safe enough to run on a road full with pedestrains and obstacles. **Traffic Sign Recognition** is one of the important element required to automate the present automobile industry. Here in our project we have tried the same on a small scale

## Introduction

A lot of luxury car companies including Mercedes and Ford are investing money in the development of Traffic sign recognition techniques. However, as of now they have only allowed automated car which recognizes the sign and warns the driver about it, but a fully automatic car which acts accordingly on recognizing the Traffic sign is yet to hit the road.

![Image of Automated Car](/virtual-expo/assets/img/diode/car-automation-img2.jpg)

## Objective

In this project our prime objective is to make an autonomous car robot that moves on its own and finds the path with the help of Traffic sign it encounters on its way. This robot is supposed to make use of computer vision techniques to detect and segment the traffic sign from its surrounding and with the help of Deep neural network the detected sign is recognized. The processor then makes the car move accordingly.

## Methodology

This project includes two parts namely, **creating a Traffic Sign Recognition(TSR) algorithm**  which can detect and recognize traffic signs in real time and the second part is to **integrate the developed TSR algorithm with the bot**. a detailed methodology of each of these steps is given below

### TSR algorithm

The traffic sign algorithm included 3 main parts,

1. **Detection of Traffic sign** : The first step involves the detection of traffic sign from a video sequence. It should basically prompt the algorithm to move further in case traffic sign is detected otherwise , move to the next video frame. Our algorithm was designed for blue circular shaped traffic sign only hence, we used **HSV color thresholding method to detect the blue color** .Once the detected image passed the blue color test , it was tested for circular shape.**For the circular shape detection contourArea of the detected shape was compared with best fit ellipse of the area** . If the ratio for these two areas comes out to be more than 0.95 , the detected picture was considered of that of a traffic sign.
2. **Segmentation** :**Contour segmentation** from opencv python library was used to take out the traffic sign patch from video sequence. Once the contour was confirmed to be a traffic sign (from step 1) , the **best fit rectangle for the contour was extracted and resized** to the required shape and passed to the classsification part.
3. **Classification** : Deep convolutional neural network was used for the classification of the segmented sign. A **MobileNet architecture** which was pretrained on ImageNet dataset was trained on **german traffic sign dataset** belonging to 3 categories, namely left, right and forward (the sample images are provided in the picture). This architecture was then used to classify and recognize our segmented traffic sign to be one of **the move forward, turn left, turn right sign** . The example for the used dataset is shown in the figure given below

![Image of Traffic Signs](/virtual-expo/assets/img/diode/car-automation-img3.jpg)

### Integration with the bot

The designed algorithm was put into a **Raspberry Pi4, 1GB variant**, which was placed on the bot. To improve the working of MobileNet architecture on RaspberryPi, **Tensorflow Lite** version of the model was used . **Adafruit tb6612 1.2A DC stepper motor driver** was used to drive the motors of the bot. A USb camera was placed on the top of the bot to feed the model with video sequence. This video sequence was passed through the algorithm in RPi .The driver board acted as the control between raspberry pi and motors.

## Model Framework

The framework for the proposed algorithm is as shown in the figure

![Image of Model Framework](/virtual-expo/assets/img/diode/car-automation-img4.jpg)

## Results

- The detection and segmentation algorithm was tried on demo gif which worked pretty well
- The model was succesfully trained on the german traffic sign dataset, The training accuracy graph is as shown in the figure
![Image of Graphs](/virtual-expo/assets/img/diode/car-automation-img5.jpg)
- After that the model was trained and was tested on 18 test images. The model passed for all giving an accuracy of 100% on test dataset. The training and validation accuracy graph and test image results are given below
![Image of Results](/virtual-expo/assets/img/diode/car-automation-img6.jpg)
- The whole algorithm was integrated with the test bot and a successful trial of the bot was done as shown in the [video](https://www.youtube.com/watch?v=oEdGsjnbA50)

## Application and Future works

For a successful run of a self driving car on a road it is very important that it follows traffic signs . This ensures safety of pedestrians as well as of the other vehicles on road. This project provides a way to detect and recognize traffic signs in real time and hence is very useful for the self driving technology
Moving further, we can modify the algorithm to recognize more traffic signs with different color and shape. We may also include traffic light recognition system as well to make it a complete traffic sign follower system.

## References

1. A Robust Algorithm for Detection and Classification of Traffic Signs in Video Data by Thanh Bui-Minh, Ovidiu Ghita, Paul F. Whelan, Senior Member, IEEE, and Trang Hoang
2. Automatic Traffic Sign Detection and Recognition in Video Sequences by Swathi M , K.V. Suresh Dept. of ECE, Siddaganga Institute of Technology, Tumakuru
3. Traffic Sign Recognition for Autonomous Driving Robot Tiago Moura, AntÃ³nio Valente, AntÃ³nio Sousa), VÃ­tor Filipe
4. Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, Liang-Chieh Chen : MobileNetV2: Inverted Residuals and Linear Bottlenecks
