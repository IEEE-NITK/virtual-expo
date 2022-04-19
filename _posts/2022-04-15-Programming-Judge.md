---
layout: post
title: "Programming Judge"
description: "Application to solve CP questions"
categories: compsoc
thumbnail: "Programming_Judge.jpg"
year: 2022
gmeet: "https://meet.google.com/qko-ggja-bjc"
---

## Mentors

- Dharmick Sai
- Anirudh Achal
- Adithya Rajesh

## Members

- Sathvik Hebbar
- Rakshith M
- Madhav Kumar
- Kavya Bhat
- Dhruvil Lakhtaria

## Aim

- Create a functional programming judge system  which compiles and executes code. The judge should be able to test all the submissions with all predefined test cases.
- Create isolated environments using Docker Containers in which submitted code should be run with time and memory restrictions while addressing all security concerns. 


## Introduction

Programming judge is a robust code execution system in which users can submit and test programming questions. The judge wil evaluate the submissions on predefined test cases and display the results with the help of isolated environments. Although there are many other judges online, in this project our end goal was to create a website that contained all the problems asked in on-campus interviews in NITK and allowed users to practice solving them.

![image_1](/virtual-expo/assets/img/compsoc/Programming_Judge_img_1.jpeg)

## Design and Tech Stack

The codebase is split into Frontend, Backend and Evaluator. Frontend component is written in ReactJS. For the backend we have used Go along with its Gin framework and Postgres as the database. The Evaluator component is written in Go and makes use of Docker.<br>

The dataflow of the system is as follows: client requests such as submitting code, viewing problem and getting verdict are sent to the backend. From there the necessary data is fetched from the database and then sent back to the client. When a file is uploaded for code submission it is stored in the storage file system and then a request is sent to the evaluator to compile and execute the code. Once completed the verdict is sent back and stored in the database.<br> 

![image_2](/virtual-expo/assets/img/compsoc/Programming_Judge_img_2.jpeg)

## Problem Set

The application provides functionalities to create new problems, view them and submit solutions, and also modify and delete them. Each problem in the set clearly states the input and output parameters, time and memory limits.

![image_3](/virtual-expo/assets/img/compsoc/Programming_Judge_img_3.jpeg)

## Getting Verdict

To make sure that the submitted code cannot perform any malicious activities on the system, it has to be executed in a sandboxed environment. To implement this, we will be using Docker Containers which will have an initial memory limit, with preset network permissions and time limit for the container. They also provide protection against security concerns such as fork, bomb etc.<br>

The submitted solutions are then compiled and run inside the docker containers against multiple test case files mounted from the storage file system. We have made standard imagefiles to support popular languages such as C, C++, Python, Java. We also check for error codes such as time limit exceeded, memory limit exceeded, wrong answer with respect to the expected output, compilation error, and also runtime errors.<br>


![image_4](/virtual-expo/assets/img/compsoc/Programming_Judge_img_4.jpeg)


## Conclusion

There is a lot of scope to extend our application. Making it scalable such that it can be used by millions of users at the same time would be an interesting challenge. Some improvements that can be made is including an editor for writing code instead of only allowing to upload files. Another major feature to improve scalability would be to introduce a message queue between the backend and evaluator that will store the submissions. This will ensure that requests don't fail when there is high load on the website.




## References 
1. [Cp Judge (explained by Gaurav Sen)](https://www.youtube.com/watch?v=eg0nlYcbLpo)
2. [IEEE Research paper on a code execution engine](https://ieeexplore.ieee.org/document/9245310)
3. [Golang tutorial](https://tour.golang.org/lis)
4. [Docker tutorial](https://docs.docker.com/get-started/)
5. [Gin](https://github.com/gin-gonic/gin)