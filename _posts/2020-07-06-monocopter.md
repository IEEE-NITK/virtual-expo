---
layout: post
title: "Design and Development of Monocopter UAV"
year: 2020
categories: piston
description: "Design and Develop an Unmanned Aerial Vehicle (UAV) which has higher efficiency than normal multirotor drones."
thumbnail: "monocopter.jpg"
---

### Team Members

- Manash Sharma
- Smit Rambhiya
- Chandran N
- Ekta R
- Impna V A

## Abstract

UAVs have become an integral part of today’s world disciplines, be it military or toys. Fixed wing aircrafts though offer higher flight times but can’t hover which limits their applications to only open areas. Whereas multirotors despite their flexibility of use causes lack practical flight times due to multiple motors drawing power to lift the aircraft.

Luckily nature has some brilliant solutions for almost every problem if we are keen enough to find. The maple seed is a winged seed that has evolved excellent aerofoils for its propagation. The design is very simple and effective. The same design could be used to build a UAV which is very efficient and yet simple. The one can be the design of a monocopter which is a single-wing rotary flight system which has the capability of hovering.

## Objective

Design and Develop an Unmanned Aerial Vehicle (UAV) which has higher efficiency than normal multirotor drones by reducing the number of power drawing parts and thus decreasing complexity.

## Introduction

A Monocopter or gyropter is a rotorcraft that uses a single rotating blade. The concept is similar to the whirling helicopter seeds that fall from some trees. The name Gyropter is sometimes applied to monocopters in which the entire aircraft rotates about its center of mass as it falls. It utilizes a single, asymmetric airfoil that is powered by a tip propeller to rotate around its center of mass, thereby producing lift.

Monocopters provide unique capabilities that are not met by current UAV systems. A controlled monocopter is capable of the same degrees of freedom as that of a  helicopter - hover, and controlled flight in any direction but it is mechanically simpler than a helicopter. The simplicity of a monocopter’s design allows for rapid fabrication at a low cost.

## Components Needed

- Arduino UNO
- Brushless motors 2300KV
- Propellers
- Servo Motors
- Bluetooth Module
- Gyroscope
- Basic electronics and wires
- Foam board (To make aerofoils)
- Wood, wire, metal rods (To make Styrofoam cutter)
- Battery

## Software Used

- Catia V5
- XFLR5
- Arduino IDE

## Designing and Manufacturing

After reading the available literature on aerofoils, it was found that NACA 4412 is the best suited for this project. A CAD model was made in the CATIA for the aerofoil whose cross section was printed on paper and used as a reference to cut the required shape of aerofoil from the foam board.

A Styrofoam cutter was made using the wood, wire and metal rods. The reference paper containing the design of the aerofoil was pasted on the foam and hot wire technique was used to cut the foam into the required. Some parts (like base support, caps) were 3D printed and assembled. XFLR 5 was used to find important components of aerofoil like critical angle, pitch, angle of attack so as to position the aerofoil in such a way that it can generate more lift. Motor testing was done using the Arduino IDE to check its rpm. The components were assembled and a bluetooth module was used to control the flight of the monocopter.

## Results

![Design of aerofoil](/virtual-expo/assets/img/piston/monocopter_img1.jpg)
<center>Fig 1: Design of aerofoil (NACA 4412)</center>

![3D printed base of monocopter](/virtual-expo/assets/img/piston/monocopter_img2.jpg)
<center>Fig 2: 3D printed base of monocopter</center>

![Monocopter before assembly after completing all the part tests](/virtual-expo/assets/img/piston/monocopter_img3.jpg)
<center>Fig 3: Monocopter before assembly after completing all the part tests</center>

## Applications

1. Aerial package delivery
2. Camera surveillance and cinematography

## Future Work

1. Attaching a camera underneath will give 360 degree aerial photography or videography
2. Adding ailerons to the aerofoil will give greater degrees of freedom so that the monocopter can even move laterally under control from the user
3. Further research can be done by adding more sensors to the monocopter to closely measure the RPM, height, etc. and optimize the same for different aerofoils
4. Work on the control system can also be done to have better control on the flight

## References

1. [https://www.researchgate.net/publication/237758639_Fly-by-wire_Control_of_a_Monocopter](https://www.researchgate.net/publication/237758639_Fly-by-wire_Control_of_a_Monocopter)
2. [https://waset.org/publications/10000143/an-experimental-procedure-for-design-and-constructi%20on-of-monocopter-and-its-control-using-optical-and-gps-aided-ahrs-sensors](https://waset.org/publications/10000143/an-experimental-procedure-for-design-and-constructi%20on-of-monocopter-and-its-control-using-optical-and-gps-aided-ahrs-sensors)
3. [https://www.youtube.com/watch?v=5LqSWiatV0Q](https://www.youtube.com/watch?v=5LqSWiatV0Q)
4. [https://www.roflcopter.tech/docs/roflCopterISEF_FrederikDunschen.pdf](https://www.roflcopter.tech/docs/roflCopterISEF_FrederikDunschen.pdf)
