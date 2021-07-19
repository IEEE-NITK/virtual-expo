---
layout: post
title: "Nano Mass Sensor"
year: 2020
categories: piston
description: "The Project looks into the response of a nano mass sensor and the effect of nonlinearities on the response of the system"
thumbnail: "nano-mass-sensor.jpg"
---

### Team Members

- Shaswata Bose
- Avinash Kumar
- Impna V.A.
- Akash Waitage

## Introduction

Resonance is a key phenomenon that is frequently used in lots of fields. Particularly in the field of MEMS and NEMS, it is used for mass spectroscopy, chemical detection and even molecular transport through CNTs. The linear FEM models we use to predict the behaviour of these devices hold true until the device shrinks to Nano scale. Nonlinearities and other interactions are no longer small enough to be neglected. In this project, we explore the effect of nonlinear stiffness and nonlinear damping on the frequency response of a nano mass sensor and observe the variation of the natural frequency with the nonlinearities.

## Methodology

### A. Conceptual Design Of The Nano Mass Sensor

The vibration of mass sensor when modelled without the nonlinearities takes the form below:-

![image-1](/virtual-expo/assets/img/piston/nano-mass-sensor-img1.jpg)

Where *m* is the mass of the sensor, *c* is the effective damping present in the system, *k* is the is the stiffness of the system and *f(t)* is the input force to the system. If the actuating force is sinusoidal in nature, them the frequency for which resonance will occur is given by:-

![image-2](/virtual-expo/assets/img/piston/nano-mass-sensor-img2.jpg)

Where *f(t)* is given by:-

![image-3](/virtual-expo/assets/img/piston/nano-mass-sensor-img3.jpg)

Where ∅ is the phase angle.

However, the equation takes the form below for a nonlinear mass sensor:-

![image-4](/virtual-expo/assets/img/piston/nano-mass-sensor-img4.jpg)

Where α and β are the coefficients of nonlinear stiffness and nonlinear damping respectively. The frequency response of the linear and the nonlinear system is shown in the figure:-

![image-5](/virtual-expo/assets/img/piston/nano-mass-sensor-img5.jpg)
<center>Fig 1:- Frequency Response for (a) Linear System, Nonlinear system with (b) positive stiffness coefficient and with (b) Negative stiffness coefficient</center>

Due to the nature of the frequency response, there are two possible frequencies depending on the frequency being swept from lower value to higher value (also known as forward sweep) or vice versa. For this project, we have used forward sweeps for the study.

### B. Design and Simulation of the Sensor

The mass sensor is modelled using the equations and the system is solved for a range of frequencies. We are interested in the resonant frequencies and how they are shifting for change in the values of α and β. The equation is nondimensionalized for further simplification of the range of α and β between -1 and 1. All the simulations were performed in MATLAB.The plots for the frequency response of the system for variation in α is shown below:-

![image-6](/virtual-expo/assets/img/piston/nano-mass-sensor-img6.jpg)
<center>Fig 2:- Variation of the frequency response of the system for variation in α</center>

## Results and Discussion

The resonant frequency is noted down for different values of the nonlinear stiffness and the nonlinear damping and a plot between the variables is obtained. The respective plots are shown below:-

![image-7](/virtual-expo/assets/img/piston/nano-mass-sensor-img7.jpg)
<center>Fig 3:- Variation of the resonance frequency of the system for variation in α</center>

![image-8](/virtual-expo/assets/img/piston/nano-mass-sensor-img8.jpg)
<center>Fig 4:- Variation of the resonance frequency of the system for variation in β</center>

The variations can be used to develop an empirical relation between the natural frequency of the system and the nonlinear parameters. This is useful for predicting the sensitivity of the Nano mass sensor and for nonlinear FEM analysis.

## Conclusion

The project is a step towards modelling and predicting the effects of nonlinear parameters in nanoscale devices. Since the equation used for this project is a standard form of the duffing equation, the results can be extended for other applications of the equation too.

## References

1. Frequency fluctuations in silicon nanoresonators by Marc Sansa, Eric Sage, Elizabeth C. Bullard, Marc Gély, Thomas Alava, Eric Colinet, Akshay K. Naik, Luis Guillermo Villanueva, Laurent Duraffourg, Michael L. Roukes, Guillaume Jourdan, Sébastien Hentz
2. Nonlinear Oscillations by Nayfeh
3. Internal resonances and nonlinearities in atomically thin resonators by Chandan Samanta
4. Fundamentals of nanomechanical Resonators by Villanueva
5. Nonlinear Damping in a micromechanical oscillator by Stav Zaitsev,∗ Oleg Shtempluk, and Eyal Buks
