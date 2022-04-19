---
layout: post
title: 'Simulation of a SDR with CR Technique'
description: 'Simulation of a basic software defined radio with cognitive radio technique using MALTALB/Simulink'
categories: diode
thumbnail: "QPSK.png"
year: 2022
gmeet: ''
---

### Mentors

- MOHA MANKAD

### Members

- HRISHIKESH KULKARNI
- RISHEE K

## Objectives

- Trying to implement a simple SDR on Simulink and also have spectrum sensing technique of cognitive radio in it.

## Description

Cognitive radio is a type of wireless communication in which a transceiver can identify which channels are in use and which are not, and move onto unused channels while avoiding occupied ones. This makes the best use of available radio-frequency spectrum while minimising interference to other users. This is a wireless communication paradigm in which the network or node's transmission or reception settings are modified to avoid interference from licenced or unlicensed users. A spectrum hole is a non-interfering, multidimensional area within frequency, time, and space that is commonly referred to as a spectrum hole. The key problem for secondary radio systems is to detect spectrum holes while operating in such frequency regions.

Since its discovery and invention, radio has captivated human beings. It gives low-cost information and entertainment to individuals all around the world. Digital technologies and advanced computer systems highlighted and began moving system implementation from digital hardware to software. With the introduction of software, digital signal processing (DSP) has played a pivotal role in the design and execution of many practical systems. DSPs may do a wide range of tasks with the same hardware. Today, digital signal processors (DSPs) are available and can work at extremely fast speeds at intermediate and radio frequencies. The concept of software radio was born with the introduction of software into radio systems. Software radios have ushered in a new era in radio engineering.On the same hardware, it is now possible to define numerous radio functionalities using appropriate software. Software Defined Radio is the name given to such radios (SDR).

Today SDR is widely used to implement Cognitive Radio FUnctionality.

![image CR.png](/virtual-expo/assets/img/diode/CR.png)

## Implementation

We used Verilog to write a simple CR controller code that would allocate bands based on data presence in lisenced part. If data is absent, it would allocate some of the unlisensed traffic to lisensed part. Then we made a Simulink model that would transmit and receive this data using QPSK Modulation. We also studied AWGN noise in communication channel.
Following are the screenshots of the output of verilog code and simulink model.

![image](/virtual-expo/assets/img/diode/QPSK.png)
![image](/virtual-expo/assets/img/diode/Verilog.png)

## References

1. [Ahmad Ali Tabassam; Muhammad Uzair Suleman; Sumit Kalsait; Sheheryar Khan, Building cognitive radios in MATLAB Simulink — A step towards future wireless technology](https://ieeexplore.ieee.org/document/5983278)
2. [Jakir Hussain, Simulation of a Cognitive Radio System By Using MATLAB](https://www.researchgate.net/publication/319186141_Simulation_of_a_Cognitive_Radio_System_By_Using_MATLAB)
3. [John Polson, COGNITIVE RADIO APPLICATIONS IN SOFTWARE DEFINED RADIO](https://www.wirelessinnovation.org/assets/Proceedings/2004/2004-sdr04-1-5-3-polson.pdf)