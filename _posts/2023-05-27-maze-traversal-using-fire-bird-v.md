---
gmeet: "https://meet.google.com/roq-hzvz-dxn"
layout: post
title: "Maze Traversal using Fire Bird V"
description: "A project aimed as an opportunity to delve into Embedded Systems programming and basic robotics using FIRE BIRD V platform"
categories: envision
thumbnail: 2023-05-27-maze-traversal-using-fire-bird-v-thumbnail.jpg
year: 2023
---

### Mentors

- Alex Moby Philip
- Gagan Malhotiya


### Mentees

- Ritapragya Biswas
- Dhanush Shetty
- Abhinith D
- Pawankumar S

## Aim

To learn how to work with the basics of a FIRE BIRD V to use the learnings to make it traverse a maze and possibly backtrack in the optimal path.


## Abstract

Embedded Systems is a domain of electronics that has impacted our lives more than we realize. Numerous devices such as smartphones, digital cameras, home appliances, automotive systems and medical devices involve the presence of such embedded systems and are responsible for executing specific tasks. They enable devices to interact with the environment, process data etc.  It allows for us to condense larger processes into smaller efficient single task based systems of lower power and better efficiency for the task required.

Embedded Systems often bleed into other domains, one of the most common among them being robotics. This is usually because embedded systems often play an integral part of robotic systems. One such area of interest is Robotic Research Platforms. Robotic Research Platforms refer to systems designed to serve as a foundation for conducting various studies onto the field of robotics, allowing researchers to experiment, develop and test various algorithms, methods and applications. It can help us explore domains like perception, navigation, human robot interaction, Artificial Intelligence and Machine Learning.

The platform we want to work with for this project is the FIRE BIRD V, a platform best for experimentation in algorithm development and testing. Through this project, we hope to understand the basics of Embedded Systems programming and algorithm developnment to serve for a specific task, which in this case is to be able to traverse a maze of white lines on its own, and then possibly backtrack using the optimal path. 

![Basic FIRE BIRD V Robot](/virtual-expo/assets/img/envision/diode/maze-traversal-using-fire-bird-v/FB01.jpg)

## Technologies used

1. FIRE BIRD V - A robotic research platform from Nex Robotics, specifically the fifth in its series of robots. The one we are working with uses the ATMEGA 2560 (AVR) microcontroller.
2. Microchip Studio - An Integrated Development Environment (IDE0 for developing and debugging AVR and other related microcontroller applications
3. AVR Bootloader  - Software from Nex Robotics that is used to load .hex files onto a microcontroller
4. Serial Port Driver - Used to connect the FIRE BIRD V robot to the USB port of the computer.


## An introduction to FIRE BIRD V
FIRE BIRD V is a popular microcontroller-based robotic platform that is used for educational and research purposes. It is designed and developed by the Indian Institute of Technology (IIT) Bombay and is a part of the e-Yantra Project. The Firebird V platform is based on the ATMEGA 2560 microcontroller and provides a range of sensors and actuators that can be used to build and program a variety of robotic applications. It is an open-source platform and provides easy integration with other tools and technologies. As said before, FIRE BIRD is a platform that provides an environment best for algorithm development and testing. It is a perfect introduction for beginners to delve into basic embedded system and robotics. Its research areas include Artificial Intelligence Control Systems, Autonomous Navigation, Real Time Systems, Collaborative Technologies etc.

## ATMEGA 2560:
The ATMEGA 2560 is a popular 8-bit microcontroller from the AVR family, developed by Atmel Corporation. It is a high-performance microcontroller that provides a range of features and functionalities that make it suitable for a wide range of applications, including robotics, automation, and industrial control systems. The ATMEGA 2560 is based on the Harvard architecture and has a clock speed of up to 16 MHz It has 256 KB of flash memory for storing the program code, 8 KB of SRAM for data storage, and 4 KB of EEPROM for non-volatile storage. It also provides a range of on-chip peripherals, including 16-bit timers, 10-bit ADC, UART, SPI, I2C, PWM, and more. The ATMEGA 2560 is widely used in embedded systems and robotics due to its ease of use, low power consumption, and high performance. It can be programmed using various programming languages, including C, C++, and Assembly, and can be integrated with various development environments and tools, making it an ideal choice for developing advanced embedded systems.

![ATMEGA2560 Pinout diagram](/virtual-expo/assets/img/envision/diode/maze-traversal-using-fire-bird-v/FB02.jpg)

## Algorithm for Traversal

The algorithm which we are going to use is "LSRB" Algorithm.
This is the algorithm used by the robot to solve the maze. L means for 'LEFT,' S is for 'STRAIGHT,' R stands for RIGHT, and B stands for 'BACK' or BACKWARD. The robot moves in the following directions: LEFT, RIGHT, STRAIGHT, and BACK. This Algorithm is straightforward. The LEFT direction has the highest importance in this algorithm, while the BACK (U-Turn) direction has the lowest. Let's have a look at this algorithm:
+ Step 1: Always follow LEFT whenever there is a turn possible
+ Step 2: If LEFT is not possible go STRAIGHT.
+ Step 3: If LEFT and STRAIGHT both are not possible take RIGHT.
+ Step 4: if LEFT, STRAIGHT, and RIGHT are not possible go BACK( or it means take a U-Turn)

This means that whenever robot is on a turning point or an intersection it will always go LEFT whenever possible. if LEFT is not possible then STRAIGHT and if both are not possible then RIGHT. If all the three turns are not possible then and then only BACK. This is the only thing you need to understand the LSRB algorithm. Based on this there are 8 scenarios possible. Let's take a look one by one:

1. Simple or Straight lane: Here LEFT is not possible but the STRAIGHT path is. so robot will follow the Straight Path.
2. Left Turn(left only): As the name suggests it's a left turn so LEFT is possible here. According to LSRB algorithm robot should follow left whenever possible. so robot will take left turn here.
3. Right Turn(right only): Again as the name suggests it's a right turn so LEFT and STRAIGHT path are both not possible so according to LSRB Algorithm robot will take Right turn.
4. T intersection(T): This intersection has a T like shape so it's called T intersection. Here Robot can take the left turn as you can see in the picture. So by algorithm Robot will take a Left Turn.
5. Left T Intersection(straight or left): Again by image, we can see Robot can take left path so Robot will take left turn here.
6. Right T Intersection(Straight or right): Here Left is not possible but the Straight path is. so the robot will take left turn
7. Dead End: Here LEFT, STRAIGHT, and RIGHT all three are not possible. so Robot will take U Turn here.
8. Four lane intersection(Cross): Here again by the image Left turn is possible so the robot will take left turn here.
9. End of Maze: Here the maze ends so the robot will stop here.

![Algorithm Visual Logic](/virtual-expo/assets/img/envision/diode/maze-traversal-using-fire-bird-v/FB04.jpg)

## Working with FIRE BIRD V

As said before, FIRE BIRD is a platform that provides an environment best for algorithm development and testing. It is a perfect introduction for beginners to delve into basic embedded system and robotics. Its research areas include Artificial Intelligence Control Systems, Autonomous Navigation, Real Time Systems, Collaborative Technologies etc.

The bot consists of an Atmel ATMEGA2560 microcontroller, position encoders, LCD, white line sensors, proximity sensors, buzzers and other additional specifications for various uses.

For our tasks, we will be mostly looking into motion control, position encoding, pulse wave modulation and analog to digital conversions.  

### Buzzer Programming

This is a function we wish to incorporate when the buzzer successfully completing the traversal / backtracking the optimal path.

The bot has a buzzer already built in, connected in its PORTC. So there will be inclusion of code to use buzzer by giving a 'buzzer on' logic, followed by a 'buzzer off' logic with a delay added in between to make the different state transitions audible. The code involves manipulating registers in the PORTC of the bot and is a great first code to try learning the basics of embedded coding because it covers basics like setting and clearing bits and how we use them to give specifications to certain pins.



### Motion Control

The most important portion of the code is for enabling the bot to move in the directions it needs to. The FIRE BIRD V has two motors that are controlled by L293D motor controller. Basic motion control can be affected by manipulating PORTA and PORTL.  The following are the basic motions possible:
- forward
- back
- left
- right
- soft left
- soft right
- stop
These different motions are achieved by changing the individual rotation directions of the two wheel, which specifically come under PORT A.


### Velocity Control
When coding the velocity control for the individual motors, we use the concept of Pulse Wave Modulation (PWM). PWM is a technique used to encode information in a digital signal by varying the width of signal's pulses while keeping the overall frequency constant. This is where the PORTL mentioned previously comes under our notice. By varying the duty cycle in PWM, we can vary the power given to the motors which result in varying velocity. Whats more, we can give different rotational speeds for individual wheels which helps achieve interesting motion paths that cant be achieved otherwise.
We also need to make use of the built in timers in the bot, specifically Timer 5 which is a 16bit timer. By manipulating the associated registers, we can achieve a variety of PWM modes and prescaler values for different operational needs but the one we tend to work with for a start would be FAST PWM mode.

![Pulse Wave Modulation](/virtual-expo/assets/img/envision/diode/maze-traversal-using-fire-bird-v/FB05.jpg)


### Position Encoding
The FIRE BIRD V has two position encoders associated with each wheel/motor. They have the function of helping us travel specific measured distances or rotate in exact measured degrees. Without using them, we are unable to precisely make measured pre programmed paths and motions for the bot.

The position encoders work on the logic of interrupts. There is an IR led and a phototransistor that form a position encoder. The make of the wheel and the rim is such that there is regular oscillation between uninterrupted light passage to the detector and light blockage. This results in any rotation of wheel resulting in pulses. Based on the translational/rotational motion that is being undertaken, we can make a resolution for the motions. for example, forward motion resolution is such that each pulse results in approx. 5 mm distance covered.

Each pulse acts like an interrupt which is serviced by an Interrupt Service Routines (ISR) that we code and use the pulse count to help make required actions and / or stop exactly at certain pulse counts to cover measured distances.

While coding, we manipulate various registers related to the interrupts and we are specifically using interrupts INT4 and INT5. We also manipulate PORTE.

![Position Encoders](/virtual-expo/assets/img/envision/diode/maze-traversal-using-fire-bird-v/FB03.jpg)

### Sensing via ADC
Another concept we have to work with is ADC conversion i.e. Analog to Digital conversions. This is how we are able to read the data from the sensors built in the FIRE BIRD V. The bot has three white line sensors, one Sharp IR range sensors, eight Analog IR proximity sensors and a battery voltage sensor just to name some. All of these sensors give analog output and we need to convert them to digital readings for our use.

For the ATMEGA 2560, we have to manipulate 16 single ended voltage inputs from the pins of PORTF and PORTK, and manipulate the values in many associated registers like ADCSRA, ADCSRB, ADMUX and ACSR. For our specific task, our objective was to make use of the White Line Sensors.


## Future Additions

#### Current Project Status
- Buzzer, basic motion control and PWM velocity control have been tested successfully.
- Currently working on debugging Position Encoding logic and White Line Sensing, after which we will implement the maze traversal algorithm.
Like any project, this project can also be developed into more interesting versions with some great features that could be added. 

These include:- 

i) Master Slave interactions: Where one bot traverses the maze and once the optimal path is found, the other bot can directly make use of that path.
ii) Maze Mapping: Where we could look into possibility of the bot wirelessly communicating with device so that we get real time mapping of maze.


## Conclusion

In this project, we have tinkered with the FIRE BIRD V bot to learn the basics of embedded system programming with respect to ATMEGA 2560. During this project, each member has learned basic concepts of beginner robotics and algorithm development. This project has provided the participants with hands-on experience in working with real-world hardware and software., including learning how to use the ATMEGA 2560 microcontroller, program it using embedded C, etc.,


## References

1. E-Yantra, [Link](http://elsi.e-yantra.org/resources)
2. Maze Solving Robot (3 IR Sensors), [Link](https://www.hackster.io/Varun2905/maze-solving-robot-3-ir-sensors-9ada3b#:~:text=%22LSRB%22%20Algorithm,-Line%20Maze&text=This%20is%20the%20algorithm%20by,directions%20that%20the%20robot%20follows)
