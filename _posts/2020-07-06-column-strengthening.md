---
layout: post
title: "RCC Structure Strengthening"
year: 2020
categories: piston
description: "It is a known fact that rehabilitation of old buildings is more economical than rebuilding them. Both time and cost can be saved. To make a good decision on this, proper knowledge of the behavior of strengthening techniques is required."
thumbnail: "column-strength-cover_thumb.jpg"
---

### Team Members

- Ekta Ramnani
- Raj Gupta

## Abstract

A large number of buildings collapse when a major earthquake occurs. The reason attributed to this was the poor design and poor construction of these structures. Since the frequency of earthquakes is increasing every year, extensive research is being carried out in this field. Laboratory based research has shown that damage in reinforced concrete structures was mainly due to:

- inadequate detailing of reinforcement
- lack of transverse steel
- confinement of concrete in structural elements

Typical failures of these structures occur due to:

- brittle nature
- inadequate capacity to dissipate and absorb inelastic energy
- Structure incapable of taking torsion and shear force.

## Problem Statement

It is a known fact that rehabilitation of old buildings is more economical than rebuilding them. Both time and cost can be saved. To make a good decision on this, proper knowledge of the behavior of strengthening techniques is required.

## Objective

The aim of this project is to develop a 3D non-linear (non-uniform cross section) finite element model of reinforced concrete columns which are externally strengthened with CFRP (Carbon Fibre Reinforced Polymer). The commercially available Finite Element Modelling software ANSYS has been used to investigate the behavior of these columns.

## Introduction

A reinforced concrete (RC) column is a structural member designed to carry compressive loads. These are composed of concrete with an embedded steel frame to provide reinforcement. Several types of cracks occur in concrete beams due to shear stress (shear crack), insufficient concrete cover, corrosion, increased bending stress and compression failure. To reduce the occurrence of these cracks we need to improve the strength of concrete.

After reading the available literature on this problem, the authors concluded that it will be beneficial to externally strengthen the RC columns using Fiber Reinforced Polymers. External reinforcement saves time and cost as it would not be necessary to construct the columns again which would have to be done for internal strengthening. Internal strengthening can still be used for those columns whose construction is yet to be done.

Fiber Reinforced Polymer (FRP) is a composite material made of a polymer matrix reinforced with fibres. The authors studied different types of FRP such as glass fiber reinforced polymer (GFRP) and carbon fiber reinforced polymer (CFRP). From existing literature, it was found that CFRP was best suited for this purpose. It has a greater advantage over the others. It is easily available and of low cost as compared to the other materials. It  is of ductile nature which will help in resisting the development of cracks. The important advantage of this polymer is that it can resist forces in all directions i.e it has good resistance to flexure, shear, torsion and bending stresses.

## General composition of fibers: Fiber+Resin polymer

Different types of carbon fibres were studied. Some of them include short, long, chopped and woven fibres. It was found that woven or long fibres provide good external strength to RC columns.

### Common thermoset Resin types are

- Polyester: Lowest cost
- Vinyl Ester: Industry standard
- Polyurethane: Premium cost
- Epoxy: Highest cost, commonly used in aerospace applications.

![image-1](/virtual-expo/assets/img/piston/column-strength-img1.jpg)
<center>Short Fibres</center>

![image-2](/virtual-expo/assets/img/piston/column-strength-img2.jpg)

## Geometry

By taking advantage of the symmetry of the column, a quarter of the column was used for modeling. This approach reduced computational time and computer disk space requirements significantly. The concrete column was modeled as volumes, CFRP layers were modeled as areas, and steel reinforcement were modeled as lines figures. Since a quarter of the column is being modeled, the model is 500 mm long, with a cross‐section of 125 mm x 125 mm. The CFRP fabric layer bonded to the column was modeled as an area. The quarter of the entire model including the created volumes for the column model is shown.

![image-3](/virtual-expo/assets/img/piston/column-strength-img3.jpg)
<center>Fig 1:Geometry as shown by Author Arduini M and Nanni A[5]</center>

![image-4](/virtual-expo/assets/img/piston/column-strength-img4.jpg)
<center>Fig 2:Cross section of beam as shown by Author Arduini M and Nanni A[5]</center>

To obtain good results, a rectangular mesh is used as per IS 2000 standard. Therefore, the mesh is set up such that square or rectangular elements are created.

### Reinforcement

Ideally, the bond strength between the concrete and steel reinforcement should be considered. However, in this study, it was assumed that a perfect bond between materials exists. To provide the perfect bond, the link element for the steel reinforcing was connected between nodes of each adjacent concrete solid element, so the two materials shared the same nodes.

### CFRP Fabric Layer

CFRP sheets were meshed as shell elements. Care was taken to ensure that the nodes were oriented with adjacent concrete solid elements in order to satisfy the perfect bond assumption.

![image-5](/virtual-expo/assets/img/piston/column-strength-img5.jpg)
<center>Fig 3:Mesh of concrete and steel plates shown by Author  Arduini M and Nanni A[5]</center>

![image-6](/virtual-expo/assets/img/piston/column-strength-img6.jpg)
<center>Fig 4:Meshing of CFRP Layer as shown by Author Arduini M and Nanni A[5]</center>

### Loading

The force, P, applied at the steel plate is applied across  the entire centerline of the loading plate. In nonlinear analysis, the load applied to the structures must be increased gradually to avoid non‐convergence.

![image-7](/virtual-expo/assets/img/piston/column-strength-img7.jpg)
<center>Fig 5:Loading Plate as shown by Author Arduini M and Nanni A [5]</center>

## Materials Used

The following materials were used to obtain the desired results:

![image-8](/virtual-expo/assets/img/piston/column-strength-img8.jpg)

## Design (Used for this Project)

Steel reinforcement with vertical 2 legged stirrups and external CFRP reinforcement were used.

![image-9](/virtual-expo/assets/img/piston/column-strength-img9.jpg)

Limit state of collapse values were referred from IS 456:2000 standard to design the structural member.

## Result 1

![image-10](/virtual-expo/assets/img/piston/column-strength-img10.jpg)

The increase in strength of the structural member after providing CFRP reinforcement can be clearly observed.

## Result 2

![image-11](/virtual-expo/assets/img/piston/column-strength-img11.jpg)

## Conclusions

1. The results of the finite element analysis showed substantial increase in the axial compressive strength and ductility of the FRP-wrapped RC columns compared with the un-strengthened columns.
2. Strengthening the RC column by bonding a single layer of CFRP to  the tension face of the column increases strength of the column by 20%.
3. Increasing the number of CFRP layers bonded to the column soffit  increases the stiffness of the column and increases its ultimate capacity.
4. Strengthening the RC column by bonding two layers of CFRP to the faces of the column increases the strength of the column by 25%. **(Most economical)**
5. Strengthening the RC column by bonding three layers of CFRP fabric to the faces of the column increases the strength of the column by 32%.

## References

1. ACI Committee 440. 440R-07: Report on Fiber-Reinforced Polymer (FRP) Reinforcement for Concrete Structures.
2. ANSYS Mechanical APDL Manual Set 2014). Release 14.5. Southpointe: ANSYS Inc.
3. ASTM A615 / A615M-20, Standard Specification for Deformed and Plain     Carbon-Steel         Bars for Concrete Reinforcement, ASTM International, West Conshohocken, PA, 2020
4. M. R. Adimi, A. H. Rahman, and B. Benmokrane. New method for testing fiber-reinforced polymer rods under fatigue. Journal of Composites for Construction, 4(4):206–213,2000.
5. Arduini M, Nanni A. Behavior of precracked RC beams strengthened with carbon FRP sheets. Journal of Composites for Construction.
6. M.Arduini and A.Nanni. Behavior of precracked rc beams strengthened with carbon frp sheets. Journal of Composites for Construction, 1(2):63–70,1997.
7. Arockiasamy, M., Sowrirajan, R., Shahawy, M., & Beitelman, T. E. (1995). Repair of damaged pretensioned solid slab using CFRP laminates. In RILEM PROCEEDINGS (pp. 492-492). CHAPMAN & HALL.
8. Chandel, Akshay. (2019). IS 456 (2000): Plain and Reinforced Concrete.
