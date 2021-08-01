---
layout: post
title: "Smart Small Firearms System"
year: 2020
categories: piston
description: "To prevent unauthorized use of firearm on another person using computer vision"
thumbnail: "smart-firearm-system.jpg"
---

### Team Members

- Kushagra Rawat
- Naman Agarwal
- Nisarg Bipin Shah
- Abhishek R
- Sharayu Brahmankar

## Abstract

In recent times there has been a steep increase in gun related violence in the US. With the sales of firearms on the rise across the globe, such incidents are only going to increase.

However to tackle this issue a US based startup BioFire has come up with smart guns. Such guns use a fingerprint sensor to unlock the trigger of the gun, ensuring that the gun is used only by the authorised person most likely the owner of the gun. Even though this provides a solution to cases where guns are used by a different person, seeing how easy it is to get a gun in the US, this does not solve the problem at all.

Hence to up the technology a notch, we aim to install a Machine Learning driven trigger locking system on the gun, which would lock the trigger if there is a person in front of the gun but allow the shooter to shoot otherwise at an object or at gun ranges.

Using the fingerprint sensor to lock the trigger shows us that external mechanisms to control the trigger of a gun are possible.

## Objective

To prevent unauthorized use of firearm on another person using computer vision

![image-1](/virtual-expo/assets/img/piston/ssfs-img1.jpg)

## Problem Formulation

![image-2](/virtual-expo/assets/img/piston/ssfs-img2.jpg)

The complete project was broken down into three sub systems, namely:

1. Electronic And Circuitry
2. Part Design And Manufacturing
3. Computer Vision For Human Detection

Discussed below are tasks performed by each subsystem:

### 1. Part Design And Manufacturing

- A bb pellet gun was chosen for the project and was subsequently studied by the design team.
- After careful measurements of all the parts of the firearm and rigorous part drawings a CAD model was created using Catia, according to the dimensions.
- After study of the Firearm shooting mechanism and noting the dimensional constraints using CAD model, a locking mechanism for the firearm was designed in CAD.
- The locking mechanism parts were manufactured using 3D printing off campus.

![image-3](/virtual-expo/assets/img/piston/ssfs-img3.jpg)
<center>Fig1. CADModel Of The Firearm (Made Using Catia)</center>

![image-4](/virtual-expo/assets/img/piston/ssfs-img4.jpg)
<center>Fig 2. CAD Model Firearm Along With The Locking Mechanism (blue and orange components)</center>

### 2. Electronics

- Electronics team was involved in the design of the circuitry associated with driving the linear solenoid actuator, so chosen by the part design team for the locking mechanism of the firearm.
- Upon procurement of the electronics components the electronics team wired and tested all components of the circuit first on a breadboard, then on a permanent circuit on perf board.
- A control signal was provided to the circuit through an Arduino Board.
- The solenoid actuator was tested several times, for its response to signal from the Arduino,heating effects and run cycles.

#### Some of the Electronic Components used

![image-5](/virtual-expo/assets/img/piston/ssfs-img5.jpg)
<center>Fig3. Mini Solenoid Actuator Used In The Project</center>

![image-6](/virtual-expo/assets/img/piston/ssfs-img6.jpg)
<center>Fig4. 7805 Voltage Regulator</center>

![image-7](/virtual-expo/assets/img/piston/ssfs-img7.jpg)
<center>Fig5. NPN Transistor</center>

![image-8](/virtual-expo/assets/img/piston/ssfs-img8.jpg)
<center>Fig6.  3.7 V Lipo batteries </center>

![image-9](/virtual-expo/assets/img/piston/ssfs-img9.jpg)
<center>Fig7. Arduino Board</center>

### 3. Human Detection

- HOG detectMultiScale standard python library with tuned parameter was used to detect human in the
- Live video stream from laptop webcam with 1.2 mp resolution and capturing rate of 30fps.
- It is later planned to use a mini camera mounted on the firearm to capture real time video for human detection.
- The HOG detectMultiScale model performed satisfyingly well with a window stride of (7,7) and a scale of 1.3
- Other good Human Estimation models using Tensor Flow are being evaluated.

![image-10](/virtual-expo/assets/img/piston/ssfs-img10.jpg)
<center>Fig 8. Original Image</center>

![image-11](/virtual-expo/assets/img/piston/ssfs-img11.jpg)
<center>Fig 9. After HOG detectMultiScale</center>

## Setup

![image-12](/virtual-expo/assets/img/piston/ssfs-img12.jpg)
<center>Fig.10 Test Setup</center>

Test setup consists of a laptop to run the Human Detection code which is connected to a Arduino to send the control signal to the electronic circuitry (here fixed on a perf board) and actuates the solenoid actuator embedded inside the firearm.

![image-13](/virtual-expo/assets/img/piston/ssfs-img13.jpg)
<center>Fig. 11 Electronic Circuit</center>

![image-14](/virtual-expo/assets/img/piston/ssfs-img14.jpg)
<center>Fig. 12 Firearm</center>

## Results

The final prototype testing will be documented as a video.
