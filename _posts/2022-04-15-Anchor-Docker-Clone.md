---

layout: post

title: "Anchor : The Docker Clone"

description: "Developing a command-line based tool that can be able to mimic the working of some basic Docker commands by implementing a container engine from scratch."

categories: compsoc

thumbnail: "anchor_docker_clone.png"

year: 2022

gmeet: "https://meet.google.com/njt-vujb-rmc"

---

### Mentors

- Gaurang Velingkar
- Rakshita Varadarajan

### Members

- Shashank S M
- Vikas K Bhat
- Inbasekaran P
- Pranav R S

## Introduction

The aim of this project is to be able to reproduce a working, functional docker clone called Anchor. Docker is an opensource containerization platform that works using OS-level virtualization. It enables developers to easily pack, ship, and run any application as a lightweight, portable, self-sufficient container, which can run virtually anywhere. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.

## Process, Basics of Containerisation

This project, as well as Docker, creates containers where processes can be run in isolation in very specific environments. To understand their workings, it is important to understand what a process is.

A process is just a program is being executed. The process contains instructions, variables, file descriptors, etc. The working of a process can change depending on the host system, that is, what environment it is being run in. That is why sometimes, the same process behaves differently on different machines.

The key idea in containeriation is to run processes in a controlled environment (containers), and these processes should not be able to see resources, processes, etc outside the container.

Containers are built from images of various systems. For example, we can build a container from an ubuntu image, and all containers built from the same image will be nearly identical. Hence, if we run the same process on containers built from the same image on different machines, we will be able to get rid of the variations in process behavior, which makes packaging applications much easier.

## What is Docker?

Docker is an open source platform for developing, shipping and running applications.

Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security allows users to run many containers simultaneously on a given host. Containers are lightweight and contain everything needed to run the application, so there is no need to rely on what is currently installed on the host.

## Docker image

A Docker image is a read-only template that contains a set of instructions for creating a container that can run on the Docker platform. It provides a convenient way to package up applications and preconfigured server environments. It is made up of a collection of files that bundle together all the essentials – such as installations, application code, and dependencies – required to configure a fully operational container environment.

Users can create their own docker images or also use the images created by others and published on docker hub. Docker images are built using Dockerfile. Each instruction in a dockerfile is a layer in the image. When some changes are made in the dockerfile, and the image is rebuilt, only the layers after the changes are done are re-built. This is why building docker images is fast and efficient
All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## Containers

A container is a runnable instance of an image. Users can create, start, stop, move, or delete a container using the Docker API or CLI. It is relatively well isolated from other containers and its host machine.

Because containers are lightweight and only include high level software, they are very fast to modify and iterate on. Containers on Docker Hub can instantly be downloaded and deployed to a local Docker runtime.

The container includes all the code, its dependencies and even the operating system itself. This enables applications to run almost anywhere — a desktop computer, a traditional IT infrastructure or the cloud.
![Container](/virtual-expo/assets/img/CompSoc/Container.png)

![Docker- file-image](/virtual-expo/assets/img/CompSoc/Docker.png)

## Containers over VM

![Containers](/virtual-expo/assets/img/CompSoc/Container_over_vm.png)
In traditional virtualization, a hypervisor virtualizes physical hardware. The result is that each virtual machine contains a guest OS, a virtual copy of the hardware that the OS requires to run and an application and its associated libraries and dependencies. VMs with different operating systems can be run on the same physical server.

Instead of virtualizing the underlying hardware, containers virtualize the operating system (typically Linux or Windows) so each individual container contains only the application and its libraries and dependencies. Containers are small, fast, and portable because, unlike a virtual machine, containers do not need to include a guest OS in every instance and can, instead, simply leverage the features and resources of the host OS.

Both VMs and containers allow developers to improve CPU and memory utilization of physical machines.

## Cgroups and Namespaces

One of the most important aspects of containerisation is that processes inside a container cannot see processes outside the container, and the resources available to processes are the resources allotted to the container. These goals are achieved by using cgroups and namespaces.

Using namespaces, we can restrict certain kernel resources visible from inside a container like mount points, network subsystems, processes that can be communicated with, etc. Processes under a namespace can only see processes and kernel resources under the same namespace.

There are separate namespaces for mount points, network, etc, which allows greater flexibility in managing them.

Usage of resources like CPU, Memory, disk IO, etc, can be limited and managed for containers using cgroups. Processes under a cgroup can use the resource allocated to that cgroup. This prevents containers from hogging the resources of the computer, as well as isolates containers from each other.

## Virtualization

Virtualization is a process whereby software is used to create an abstraction layer over computer hardware that allows the hardware elements of a single computer to be divided into multiple virtual computers.

## Copy On Write file system

The most basic way of making containers from images would be to copy the entire content of the image into the container. However, this takes a lot of time when you want to make several containers from large images. This is sped up by using copy on write filesystem.

In CoW(Copy on Write), the contents are not copied during creation. Instead, the container will contain links to the files on the image. Since the size of the links is much lower than the size of the files, container creation speeds up by a large amount.

When files in the container are edited, a copy of that file is made in the container, and changes are made in that. Next time that file is opened, instead of a link to the image file, this copy of the file will be opened. Since we are copying the file only during edits(or writes), this system is called copy on write.

CoW adds an overhead each time a different file is edited, but it is a tradeoff for a large speedup in the container creation time.

Before CoW:

![Before CoW](/virtual-expo/assets/img/CompSoc/before_cow.png)
After CoW:
![After Cow](/virtual-expo/assets/img/CompSoc/after_cow.png)

## **How to run the setup**

1. Create a VM either on your system using Virtual-Box, or a cloud VM (preferably) using your free Azure or AWS Student Account.

2. Clone the Git repository. You can either clone it directly into the VM or into your system and then `scp` it into the VM.

3. Build and Install the Linux module

   Run the following commands in the base to install the linux module.

   ```bash

   cd setup

   python3 setup.py build

   python3 setup.py install

   cd ..

   ```

4. Execute the following command.

   ```bash

   sudo python3 anchor_run.py run -i ubuntu-export /bin/echo "Hello World"

   ```

   After executing this command will fork a new child process that will

   - Unpack an ubuntu image into a new directory.
   - chroot() into that directory
   - exec ‘/bin/sh’

   While the parent waits for it to finish

   You can also execute the following command

   ```bash

   sudo python3 anchor_run.py run /bin/echo "Welcome to Anchor"

   ```

   This will also fork a new process which will execute ‘/bin/echo’ and will print “Welcome to anchor”.

## Conclusion

Currently our command line based tool is able to mimic the working of the Docker command “run”.  
Our future plan is to be able to mimic the working of the Docker commands of “ps”, “image”, “container”, “rm”, “exec” and implement support for the “volume” command in docker.

## References

1. Docker home page [https://www.docker.com/](https://www.docker.com/)
2. Containers From Scratch by Liz Rice [Containers From Scratch • Liz Rice • GOTO 2018](https://youtu.be/8fi7uSYlOdc)
3. Linux Primitives [Linux Primitives](/vle/presentation/d/10vFQfEUvpf7qYyksNqiy-bAxcy-bvF0OnUElCOtTTRc/edit#slide=id.p)
4. Docker labs [https://github.com/docker/labs](https://github.com/docker/labs)
5. Docker orientation and setup [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
6. Docker Fundamentals [https://www.coursera.org/projects/docker-fundamentals](https://www.coursera.org/projects/docker-fundamentals)
7. Docker for the Absolute Beginner [https://kodekloud.com/p/docker-for-the-absolute-beginner-hands-on](https://kodekloud.com/p/docker-for-the-absolute-beginner-hands-on)
8. Container based virtualization [http://www.ce.uniroma2.it/courses/sdcc1819/slides/Docker.pdf](http://www.ce.uniroma2.it/courses/sdcc1819/slides/Docker.pdf)
9. Docker internals [http://docker-saigon.github.io/post/Docker-Internals/](http://docker-saigon.github.io/post/Docker-Internals/)
10. Cgroups, Namespaces and beyond - [https://youtu.be/sK5i-N34im8](https://youtu.be/sK5i-N34im8)
11. Containers vs VMs : [ Containers vs VMs: What's the difference? - YouTube](https://www.youtube.com/watch?v=cjXI-yxqGTI&t=215s&ab_channel=IBMTechnology)
12. How Docker Works [How Docker Works - Intro to Namespaces - YouTube](https://www.youtube.com/watch?v=-YnMr1lj4Z8&t=2s&ab_channel=LiveOverflow)