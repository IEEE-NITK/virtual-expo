---
layout: post
title: "Blind Assistance using Haptic Feedback"
year: 2020
categories: diode
description: "A project to develop a robotic system which helps people to handle objects efficiently through a feedback system provided with an object recognition system."
thumbnail: "blindassistance1_thumb.jpg"
---

### Mentors

- Manan Sharma
- Anirudh BH
- Anirudh Sundar

### Members

- Saikumar Dande
- Bhaskar Vyas
- Rahul Hanchate

## Objectives

The aim of this project is to develop a robotic system which helps people to handle objects efficiently through a feedback system provided with an object recognition system. It helps identify several pick & place objects to be lifted in a stable manner and nullifies any difficulty encountered.

## Methodology

This project consisted of two major parts: object detection and robotics. The object detection system was achieved by implementing a Yolo network which had a pretty decent performance of 2 frames per second. By using the concept of Multiprocessing we were able to achieve a better performance of 5 frames per second. Using the same, the required item in the frame is detected, and depending on the measurements from the rectangle at the centre and obtained rectangle around the object, the instructions regarding movement were sent to nodeMCU (esp8266) setup. The microcontroller code was written in such a way that the motor vibrators which were strapped around the lower hand, would vibrate in a fashion countering along with the hand towards the object. This would make the user’s hand go towards the object. But this wouldn’t ensure the stability of the system. A feedback mechanism, where motor vibration intensity was controlled to achieve a better sense of distance for the person, had to be implemented.

![image-1](/virtual-expo/assets/img/diode/bauhf-img1.jpg)
<center>Angular description of vibration direction and intensity obtained for a test run</center>

## Conclusion

A dominant object was selected of the image and was focused. Depending upon the position of the object in the image and the location it would move, commands were sent to the nodeMcu setup.
The completed haptic platform performs with very little perceivable lag and provides an interactive experience for movement of hand.

## Applications

This project has a lot of applications in various fields of interests. For example, It can be very helpful for old aged people who suffer from hand tremors to pick up things easily. Also, the system can be used for mimicking human hand movements for a robot.
The same concept can be used to make a device which can be used to visualize virtual objects and be able to touch the virtual objects.
Also, it can be further developed by embedding a voice recognition system so that when a person having this band could be able to just say name of object and this will help to guide movement.

## References and Acknowledgements

- [Visual impairment aid using haptic and sound feedback](https://ieeexplore.ieee.org/document/7918924)
