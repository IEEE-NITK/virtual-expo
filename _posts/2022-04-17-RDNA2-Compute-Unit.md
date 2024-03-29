---
layout: post
title: "RDNA2 Based Compute Unit"
description: 'This project aims to implement the scalar ALU in compliance with RDNA2 ISA.  The RDNA2 ISA is found in the commercial GPUs of AMD which comprises of the Radeon RX6000 series of GPUs. The implemented ALU can run all the supported instruction types as documented in the RDNA2 ISA.'
categories: diode
thumbnail: "RDNA2-compute-unit.png"
year: 2022
gmeet: 'https://meet.google.com/stj-pqqk-qum'
---

### Mentors

- KRUTI DEEPAN PANDA
- RAHUL MAGESH
- ANIRUDH T

### Members

- UTKARSH
- DEEPANSHU GUPTA
- JAYA

## Objectives

- Implementing the Scalar ALU with complete support for all of the flags as specified by the RDNA2 ISA.
- Implementing the Vector ALU with complete support for all of the flags as specified by the RDNA2 ISA.
- Combining the 2 ALUs to implement the Compute Unit
- Setting up test benches to verify our implementation

## Description

This project aims to design a 'compute unit' based on the RDNA2 ISA for AMD GPUs. RDNA2 is the latest architecture of AMD GPUs (RX6000 series). Currently, there are no open-source hardware implementations based on the RDNA2 ISA. However, there exist some open-source projects based on AMD's older ISA (2016 Southern Lake). Having a simple hardware model for reference can enable parallel programmers to work on RDNA2 based GPUs more efficiently.

RDNA 2 (also RDNA2) is the successor to the RDNA microarchitecture. It was first publicly announced in early 2020 with a projected release in Q4 2020. According to statements from AMD, RDNA 2 would be a "refresh" of the RDNA architecture.

RDNA (Radeon DNA) is the codename for a GPU microarchitecture and accompanying instruction set architecture developed by AMD. It is the successor to their Graphics Core Next (GCN) microarchitecture/instruction set. The first product lineup featuring RDNA was the Radeon RX 5000 series of video cards, launched on July 7, 2019. The architecture is also planned to be used in mobile products. It is manufactured and fabricated with TSMC's 7 nm FinFET graphics chips used in the Navi series of AMD Radeon graphics cards.

## Screenshots

#### Synthesis Report - S_ALU

![App Screenshot](/virtual-expo/assets/img/diode/RDNA2-Image-1.png)

#### Schematic - Register File

![App Screenshot](/virtual-expo/assets/img/diode/RDNA2-Image-2.png)

#### Device Utilization Report - Register File

![App Screenshot](/virtual-expo/assets/img/diode/RDNA2-Image-3.png)

## References

1. [The Morgan Kaufmann Series in Computer Architecture and Design] David A. Patterson, John L. Hennessy - Computer Organization and Design RISC-V Edition\_ The Hardware Software Interface (2020, Morgan Kaufmann)
2. Chris Terman. 6.004 Computation Structures. Spring 2017. Massachusetts Institute of Technology: MIT OpenCourseWare, [https://ocw.mit.edu](https://ocw.mit.edu) . License: Creative Commons BY-NC-SA.
3. [RDNA2_Shader_ISA_November2020](https://developer.amd.com/wp-content/resources/RDNA2_Shader_ISA_November2020.pdf)