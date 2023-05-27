---
gmeet: "https://meet.google.com/ynb-eojr-jaq"
layout: post
title: "Design and Analysis of Wind Turbine Designs"
description: "An integrated approach combining Qblade and Ansys Fluent for designing and analyzing wind turbine blades, from airfoil to CFD and structural analysis"
categories: envision
thumbnail: 2023-05-27-design-and-analysis-of-wind-turbine-designs-thumbnail.jpg
year: 2023
---

### Mentors

- Guddati Sri Sai Akhil
- Rayner Menezes

### Members

- Bharat Patel
- Debargha Biswas

## Aim
Analyzing the design of wind turbines with the help of computer-aided methods to establish efficient design types and find their efficiency based on certain given conditions, followed by simulating real-world conditions to see if they are feasible and if they will hold up.


## Introduction
Wind turbines are one of the most commonly used renewable energy sources right now. Wind turbines come in various sizes and shapes, some being more efficient than others. There are various factors involved in the process of selection of a wind turbine to make it usable in the real world. Here we try to find the most efficient type of wind turbine followed by taking a particular case study with various real-world conditions to test our results.

The two main sub-divisions of wind turbines are HAWT and VAWT. Out of these, it is seen that HAWT is the more efficient variant. The maximum theoretical efficiency of a wind turbine is tested to be around 59.3%. To test these we are going to use ANSYS software and apply finite element analysis, meshing, and CFD to get the outputs based on certain input conditions. This process is followed by static structure testing also performed on ANSYS to find out if the wind turbine can sustain the loads on it and be functional. 


## Methodology
1. ANSYS: It is a CAE/Multiphysics engineering simulation software for product design, testing, and operation. Here we use the geometry function to import the blade design and create a desired flow domain around it, followed by using ANSYS Fluent for CFD analysis, and finally Static Structural testing by transferring loads from the cfd simlulation onto the blades itself to see if they can sustain it.

2. QBlade: Is a public source, cross-platform simulation software for wind turbine blade design and aerodynamic simulation.

We used the example of the GE1.5xle and set boundary conditions as follows:
The radius of rotor: 44.2m
Rotational speed: 2.22 rad/sec clockwise 
Average inlet velocity: 10m/s
The system was solved using the turbulence model SST k-w
The governing equations of the setup are the conservation of mass and the Navier-Stokes equation

For designing our own blade we chose the NACA 63-415 airfoil designed for windblades. We generated and optimised the twist of our blade along the length using Qblade and a cfd simulation was performed on it.

### Validation
We achieved results comparable to the research paper referred under similar boundary conditions and velocity.

![image 1](/virtual-expo/assets/img/envision/piston/design-and-analysis-of-wind-turbine-designs/pressure_ge_ref.png)

Pressure contours of GE 1.5xle Wind Turbine from Ref.

![image 2](/virtual-expo/assets/img/envision/piston/design-and-analysis-of-wind-turbine-designs/pressure_ge.png)

Pressure contours of GE 1.5xle Wind Turbine from Ansys simulation.

## Result
![image 3](/virtual-expo/assets/img/envision/piston/design-and-analysis-of-wind-turbine-designs/velocity_profile_ge.png)

Velocity profile of GE 1.5xle Wind Turbine from Ansys simulation.

![image 4](/virtual-expo/assets/img/envision/piston/design-and-analysis-of-wind-turbine-designs/deformation_ge.png)

Total deformation of GE 1.5xle Wind Turbine from Ansys simulation.

![image 5](/virtual-expo/assets/img/envision/piston/design-and-analysis-of-wind-turbine-designs/Equivalent_Stress_ge.png)

Equivalent stress of GE 1.5xle Wind Turbine from Ansys simulation.

![image 6](/virtual-expo/assets/img/envision/piston/design-and-analysis-of-wind-turbine-designs/velocity_profile_qblade.png)

Velocity profile of Our Wind Turbine from Ansys simulation.

![image 7](/virtual-expo/assets/img/envision/piston/design-and-analysis-of-wind-turbine-designs/pressure_qblade.png)

Pressure contours of Our Wind Turbine from Ansys simulation.





## Conclusion
In this project, we acquired knowledge of wind turbine physics and Betz's limit but also gained hands-on experience with industry-standard software tools.
We employed Ansys Fluent to conduct computational fluid dynamics (CFD) analysis on both the original GE1.5xle and our designed wind turbine blade.
The CFD simulations provided a comprehensive understanding of the flow characteristics, including velocity distribution, pressure distribution, and turbulence effects. These insights along with the static structural simulation were crucial in evaluating the performance of the blade and identifying areas for improvement.

## References

1. Design and analysis of small-scale horizontal axis wind turbine using PVC material, [Link](https://www.sciencedirect.com/science/article/pii/S2214785321055309)
2. Ansys, [Link](https://courses.ansys.com/index.php/courses/wind-blade-analysis-for-wind-power-using-ansys-fluent/)
3. Youtube, [Link](https://youtube.com/playlist?list=PLcu34l7xaPqbP_DZcQosaaXqmGWIk0Gux)
4. Youtube, [Link](https://www.youtube.com/playlist?list=PLa0Lu5W8HP8tBUuqUJgDbDxFYGYMgSDNF)

