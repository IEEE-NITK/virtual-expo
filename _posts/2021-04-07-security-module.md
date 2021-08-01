---
 layout: post
 title: "Security module for a RISC processor"
 description: "This project tries to implement a strategy to prevent unwanted snooping on physical memory."
 categories: diode
 thumbnail: "security-module.jpeg"
 year: 2021
---

### Mentor
- Karthik Rao

### Members

- Kruti Deepan Panda
- Rahul Magesh
- Sankarsh R

# Abstract

With the world becoming increasingly IoT-driven, it is crucial to ensure
that the data in lower-end processors is safe from external threats. Attackers
can steal data without even accessing the processor by probing the memory
bus. This project tries to implement a strategy to prevent unwanted snooping on physical memory.
A simple 32-bit RISC processor, the ‘β’, is implemented from scratch to
demonstrate this strategy. This processor supports arithmetic, bitwise, comparison, and branching operations and can handle loads and stores. Every
transaction to the memory is secured with an AES encryption block.

# Demo

<iframe src="https://www.youtube.com/embed/5WTDkMDSMI8" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Theory

**RISC**, or **Reduced Instruction Set Computer**. is a type of microprocessor architecture that utilizes a small, highly-optimized set of instructions, rather than a more specialized set of instructions often found in other types of architectures. RISC processors have the following features-

- **Large number of registers**: The RISC design philosophy generally incorporates a larger number of registers to prevent expensive interactions with memory. 
- **Fixed instruction width**: Most RISC architectures have fixed-length instructions (commonly 32 bits) and a simple encoding, which simplifies fetch, decode, and issue logic considerably.

RISC architectures are highly popular in the embedded systems market. Examples of processors with the RISC architecture include ARM, MIPS, PowerPC, Atmel’s AVR, and the Microchip PIC processors.

**AES** stands for **Advanced Encryption Standard**, and is a specification standard by the National Institute of Standards and Technology (NIST) for the security of data. AES is a widely recognized and adapted cryptographic module used in the U.S., Canada and worldwide by military, government, financial institutions, and organizations all around the world as the standard for encrypting and decrypting of data. There are different degrees of AES hardware encryption, for example 128-bit, 192-bit, and 256-bit, with each key size providing an increased level of protection and complexity. Essentially, AES encryption is a block of algorithms that "scrambles" the data into unreadable code for transport, then when reconnected to the user, is unscrambled again by the same algorithm when the right keys are provided.

There are two main kinds of physical memory attacks: snooping on a live RAM bus or modifying data on the bus, and dumping the RAM content. With hardware encryption on microprocessor chips, the AES encryption process is handled automatically, built right in with a hardware module inside the core itself. Once original data is encrypted, it becomes undecipherable in the background and is locked away under encrypted storage. If a thief were to try to gain access to the data without knowledge of the key, the attempt is by all practical means impossible. 

We plan to demonstrate this strategy using toy examples. We have implemented a RISC processor which is discussed in [this](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/) course. We have then built a hardware encryptor-module using AES with 128-bit key and integrated it with the β processor. A simple assembler is also built for easier machine code generation.

# Results obtained

The whole project was implemented using Verilog. The source files can be found [here](https://github.com/IEEE-NITK/security-module-for-risc-processor).

The RTL design is illustrated below.

![img](/virtual-expo/assets/img/diode/security_module1.png) 

The assembler in action for a simple program which calculates the sum of the first 'n' integers.

![img](/virtual-expo/assets/img/diode/security_module2.png)

The generated machine code will be 128 bits long, as shown below. This will be stored in the physical memory, not the actual instruction.

![img](/virtual-expo/assets/img/diode/security_module3.png)

The following waveform is obtained when the above code is run on the processor.

![img](/virtual-expo/assets/img/diode/security_module4.jpg)
![img](/virtual-expo/assets/img/diode/security_module5.jpg)
![img](/virtual-expo/assets/img/diode/security_module6.jpg)
# References

- Chih-Pin Su, Tsung-Fu Lin, Chih-Tsiun Huang and Cheng-Wen Wu, "A high-throughput low-cost AES processor," in IEEE Communications Magazine, vol. 41, no. 12, pp. 86-91, Dec. 2003, doi: 10.1109/MCOM.2003.1252803.
- [Rijndael-AES](https://csrc.nist.gov/csrc/media/projects/cryptographic-standards-and-guidelines/documents/aes-development/rijndael-ammended.pdf)
- [Computation Structures 6.004](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/)
