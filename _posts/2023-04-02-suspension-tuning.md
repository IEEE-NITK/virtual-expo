---
layout: post
title: "Suspension Tuning of an Automobile: A Critical Analysis"
description: 'Suspension of the vehicle defienes the quality of ride comfort which is very essential for smooth handling characteristics. Other aspect of suspension is to improve the performance by minimising the stabilisation time which is achieved with the help of destructive resonance of front and rear vibrations.'
categories: piston
thumbnail: "placeholder-image.jpg"
year: 2023
gmeet: 'https://meet.google.com/stj-pqqk-qum'
---

# Suspension Tuning of an Automobile: A Critical Analysis

Suspension of the vehicle defienes the quality of ride comfort which is very essential for smooth handling characteristics. Other aspect of suspension is to improve the performance by minimising the stabilisation time which is achieved with the help of destructive resonance of front and rear vibrations. 

## Project Mentors

- Abhilash Bharadwaj K

## Project Members

- Adithya Srihari Rao
- Dhiren V Bhandary
- Prathamesh Kiran Anvekar 

## Aim

To design and optimise the suspension system of an automobile for an increased ride comfort and to achieve the better stabilisation time.

## Introduction

Suspension system in the vehicles often decides the comfort of the driver and passengers and it is governed by simplified set four differential equations which accounts for the vertical motions of the sprung masses and unsprung masses of the vehicle along with body pitch. Pitch motion is taken into account with respect to the angle of tilt with respect to the centre of mass. 

## Project Work

### Development of Quarter Car Model
A regular spring mass damping system is taken as the inspiration for setting up the physical equation of the Quarter-Car which literally means one - fourth of the vehicle. An improvement on the single degree of freedom system has led to the Quarter Car Model by adding an additional mass called as 'unsprung mass' which is a dual degree of freedom system. Models were built in Simulink for better user interactive experience. Model assumes a particular step input and the motion of the sprung and unsprung masses are as shown in the figure. 

![image-1](/virtual-expo/assets/img/piston/2023_suspension_tuning/QCM_SIMULINK.png)

![image-2](/virtual-expo/assets/img/piston/2023_suspension_tuning/comparision.png)

### Upgrade to Half Car Model
  
Half Car Model is the extension of the Quarter Car Model where the front and rear ends of the unsprung masses are considered along with the pitch motion of the sprung mass which is a 4-Degree of Freedom system to extract the data with improved accuracy.

### Data Extraction & Refining

Data has been collected for parametrised road input and velocity with different damping factors which give various stabilisation times for different damping coefficients. Body is considered stable when the displacement amplitude reaches 2% of its max amplitude. Data is refined with this constraint considering the values of different stabilisation times with various damping coefficients and applied the regression analysis to generate a 3 dimensional surface form the generated data. 

### Optimization & Implementation

Regression analysis is performed over the refined data to plot a 3-dimensional surface and the least stabilisation time is found over the surface with particular set of values of damping coefficients in the front and rear ends of the vehicle with the point of projection on the plane of damping coefficients. Further, in actual implementation dampers are fed with specific pressures inside the chambers to give that damping factor which makes the vehicle to stabilise faster. 

## Conclusion

At any point, the road profile, velocity, spring stiffnesses can be altered in the process for the ease of analysis for various types of systems. 

Skills acquired:

1. Establishing mathematical equations and solutions for physical problems from preliminary laws
2. Solving ordinary differential equations in Simulink
3. MATLAB coherence with Simulink
4. Exposure to data acquisition
5. Markdown and LaTeX languages for professional documentation of various mathematical equations and matrices  

## References

1. [Half Car Model: A 4 DoF system](https://in.mathworks.com/matlabcentral/fileexchange/106045-half-car-model?s_tid=prof_contriblnk)
2. [Developing QCM in Simulink](https://youtu.be/xiR_WORuILQ)
3. Fundamentals of vehicle dynamics by Thomas D. Gillespie