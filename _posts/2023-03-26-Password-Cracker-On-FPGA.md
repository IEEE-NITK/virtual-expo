---
layout: post
title: "Password-Cracker-On-FPGA"
description: "The project targets FPGA platforms and is designed to crack passwords in a fast and efficient manner."
categories: diode
thumbnail: "no-image.png"
year: 2023
gmeet: "https://meet.google.com/wjc-tqkh-qva"
---

### Mentors

- Jaya Srivastava
- Utkarsh Mahajan

### Members

- Jalak Kamdar
- Priyanshu Bhandari
- V Vignesh Karthik
- Yanvitha Totakura

## Aim

- Implementing a password cracker in Verilog that performs a dictionary attack using various hashing algorithms. The project targets FPGA platforms and is designed to crack passwords in a fast and efficient manner.

## Introduction

- In this project, we built a Password cracker which uses a dictionary list attack that supports multiple hashing algorithms.There is a manual mode for selecting a specific algorithm.

### Features

- Supports SHA256.
- Dictionary attack approach to cracking passwords.

### Requirements

- FPGA development board
- Verilog compiler (Vivado)
- Dictionary file containing possible passwords

## MD5 Algorithm

- MD-5 is a cryptographic hash function algorithm that takes the message as input of any length and changes it into a fixed-length message.
- The algo involves four main steps namely :  
a. Appending Padding bits- Padding means adding extra bits to the original message.  
b. Appending Length bits- After padding, 64 bits are inserted at the end, which is used to record the original input length.  
c. Initializing MD buffers- A four-word buffer (A, B, C, D) is used to compute the values for the message digest.  
d. Processing each block- Each 512-bit block gets broken down further into 16 sub-blocks of 32 bits each. There are four rounds of operations, with each round utilizing all the sub-blocks, the buffers, and a constant array value.  
The operations that are performed are:      
1. Add modulo 2^ (32)
2. D[i] – 32-bit message.
3. B[i] – 32-bit constant.
4. \<<<n – Left shift by n bits.

Auxiliary Functions: Auxiliary functions take three inputs (32-bits word) and give an output of 32-bit word. These functions apply logical AND, OR and XOR to the inputs. The non-linear process above is different for each round of the sub-block.

- Round 1: (b AND c) OR ((NOT b) AND (d))
- Round 2: (b AND d) OR (c AND (NOT d))
- Round 3: b XOR c XOR d
- Round 4: c XOR (b OR (NOT d))

## MD4 Algorithm

- The message of b bits(m0m1m2….mb-1) which is a non-negative number is padded so that its length 448 mod 512. After padding is performed, the 64-bit representation of the message of b bits is appended to the previous result. Now the message is of length 512 bits and the word is made into N words where N is a multiple of 16.

### Initialising MD Buffers

- A, B, C and D
- Auxiliary functions:
- f(X, Y, Z) = XY v (~X)Z
- g(X, Y, Z) = XY v XZ v YZ
- h(X, Y, Z) = X⊕Y⊕Z

#### Rounds of hashing and each round is cycled 16 times

Round1:
- A = (A + f(B, C, D) + X[i] + K[i]) /<< s
- D = (A + f(A, B, C) + X[i] + K[i]) << s
- C = (C + f(D, A, B) + X[i] + K[i]) << s
- B = (B + f(C, D, A) + X[i] + K[i]) << s

Round 2:
- A = (A + g(B, C, D) + X[i] + K[i]) /<< s
- D = (A + g(A, B, C) + X[i] + K[i]) << s
- C = (C + g(D, A, B) + X[i] + K[i]) << s
- B = (B + g(C, D, A) + X[i] + K[i]) << s

Round 3:
- A = (A + h(B, C, D) + X[i] + K[i]) /<< s
- D = (A + h(A, B, C) + X[i] + K[i]) << s
- C = (C + h(D, A, B) + X[i] + K[i]) << s
- B = (B + h(C, D, A) + X[i] + K[i]) << s

#### Outputs AA, BB, CC and DD are added to obtain the final hash

- A = A + AA
- B = B + BB
- C = C + CC
- D = D + DD

#### Output

- The message digest produced is a 128-bit word which is stored with the lower order byte of A and ends with the higher order byte of D

## Conclusion

- We have built a synthesizable hardware model in Verilog HDL which can compute multiple hash types to crack passwords and includes implementing the model on FPGA. Hash compute units for multiple hashing algorithms and then turning it into an individual password cracker unit by adding memory for a dictionary list.

## References

- [md4-verilog](https://github.com/matthiaskonrath/md4-verilog/tree/main/Implementations/Verilog)
- [md5 Algorithm in information security](https://www.comparitech.com/blog/information-security/md5-algorithm-with-examples/)
- [md5-algorithm, simplilearn](https://www.simplilearn.com/tutorials/cyber-security-tutorial/md5-algorithm)
