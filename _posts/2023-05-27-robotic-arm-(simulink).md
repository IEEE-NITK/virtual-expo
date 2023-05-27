---
gmeet: "https://meet.google.com/kiq-pdrv-tci"
layout: post
title: "Robotic Arm (Simulink)"
description: "We aim to develop a robotic arm, using Fusion360 & Simulink, with an objective of pick and place mechanism."
categories: envision
thumbnail: 2023-05-27-robotic-arm-(simulink)-thumbnail.jpeg
year: 2023
---
### Project Guide
Shivani Chanda - RAS Chair
### Mentors
Krisha Shah,
D Jagannadha Reddy
### Members
Navitha R,
Suksha Kiran,
Rohit Karatagi,
Pranav Sudheer
## Acknowledgements
https://in.mathworks.com/help/robotics/ug/pick-and-place-workflow-using-stateflow.html
## Aim
The project aims to develop a robotic arm, in simulation, with an objective of pick and place mechanism.
## Introduction
A robotic arm is a type of mechanical arm, usually programmable, with similar functions to a human arm. A robotic arm can be used for automating various tasks which reduces human effort which in turn
will increase productivity.

![image](https://github.com/DJR-18/I04/assets/122470780/5522385e-4698-4553-ac40-2a70794c7922)
## Trajectory Generation
The aim of the trajectory generation is to generate inputs to the motion control system which ensures that the planned trajectory is executed. We chose a polynomial trajectory generation method to
produce a trajectory with the waypoints, timepoints and velocity points given as an input to the control system. The output translation vector goes as an input to the Inverse Kinematics block.
![WhatsApp Image 2023-05-14 at 22 55 29](https://github.com/DJR-18/I04/assets/122470780/faf201f4-5877-47ba-a6cc-141ca11f36a7)
## Inverse Kinematics
Inverse kinematics is the use of kinematic equations to determine the motion of a robot to reach a desired position. In this block system, the “Coordinate Transformation Conversion” block receives a
translation vector which gets converted to a homogeneous matrix which is provided as an input to the “Inverse Kinematics” block which extracts the angles from the matrix. Hence, the inverse Kinematics
System object creates an Inverse Kinematic (IK) solver to calculate joint configurations for a desired end- effector pose based on a specified rigid body tree model.
![WhatsApp Image 2023-05-08 at 17 52 40](https://github.com/DJR-18/I04/assets/122470780/07db4b4e-b316-4ddc-9e2f-9bfd7172f934)
## Robot arm manipulator
The model is an RRRR 4 DOF Robot Manipulator. We used “Rigid Transform” Blocks to keep shifting the World Frame to the centre of the bodies.It consists of a fixed base plate, a rotating base, and 3
links with revolute joints rotating in a direction perpendicular to rotation of the base. A rigid end effector was attached to the end of the last link for pick and place functionality. This block
system receives the joint angles from inverse kinematics block which are passed on to the forward kinematics block.
![WhatsApp Image 2023-05-08 at 17 52 39](https://github.com/DJR-18/I04/assets/122470780/bc820556-da53-4fe1-b00e-d9ad8516d0ca) ![WhatsApp Image 2023-05-14 at 22 55 28](https://github.com/DJR-18/I04/assets/122470780/0ad1503c-3bbc-4bfc-9ae8-f327f4535ab1)
## Forward Kinematics
Forward Kinematics refers to the use of kinematic equations of a robot to compute the position of the end effector from specified values for the joint parameters. We simulated the forward kinematics
using Simulink Robotics Toolkit blocks which uses DH parameters to develop a transformation matrix consisting of four parameters primarily, providing us with the coordinates of the joints at respective
joint angles and length parameters. In this control system, the “Get Transform” block receives the angles and provides a homogeneous transformation matrix as an input to the next block namely
“Coordinate Transformation Conversion” block which converts the input to a translation matrix whose data is provided to the “Scope” block. The graph appearing on the Scope helps us rectify the actual
motion versus the ideal motion it was supposed to travel.
![WhatsApp Image 2023-05-14 at 22 55 28](https://github.com/DJR-18/I04/assets/122470780/63ac77fe-ec1b-4e76-84c9-d0b8fdc83e11)
## Final block system
This is the final block system where first port of scope is the actual motion second port gives the ideal motion and the third port gives the velocity.
![WhatsApp Image 2023-05-08 at 17 52 41](https://github.com/DJR-18/I04/assets/122470780/24cff656-6c7d-4269-be67-7d87f8f8fe92)
## Conclusion
A robotic arm system can provide greater reliability in polishing workpieces and smart manufacturing. The robot  controller  dynamics  and  dynamics  are then analyzed  and  simulated  in  the
Matlab/Simulink environment with the Robotics toolkit. In the future, we will study the creation of robotic trajectories and control forces in industrial applications.
## References
https://ch.mathworks.com/help/sm/getting-started-with-simmechanics.html

https://ch.mathworks.com/help/simulink/slref/pidcontroller.html

https://ch.mathworks.com/help/sm/ug/joints.html

https://ch.mathworks.com/help/stateflow/getting-started.html?s_tid=CRUX_lftnav
