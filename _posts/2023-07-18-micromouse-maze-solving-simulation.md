---
layout: post
title: "Micromouse Maze Solving Simulation"
description: " The Micromouse Maze Solving project aims to develop and implement an autonomous robot capable of navigating and solving complex mazes efficiently "
categories: envision
thumbnail: 2023-07-18-micromouse-maze-solving-simulation-thumbnail.jpeg
year: 2023
---


### Mentors

- Dev Goti
- Pooja M

### Members

- Hemang Jamadagni
- Madhav Kedia
- Pushkaran D
- Adithya Ubaradka


## Aim

To make the micromouse robot capable of reaching the centre of the given maze in the shortest possible time using maze solving algorithms.

## Introduction

The maze solving has gained increasing attention in the field of Micromouse competition and Intelligent Robot.
The goal for Micromouse maze solving is to reach the destination cell with minimum cost of resources, such as time and steps. The Micromouse is an automated robot which has to find its way through the arbitrary maze within the least amount of time.


##  Objectives
The main objectives of the project are as follows:
Develop a simulated maze environment using ROS Gazebo.
Implement the floodfill algorithm for maze exploration and pathfinding.
Enable the simulated mouse to navigate through the maze using floodfill.
Determine and visualize the shortest path from the start point to the destination.

## Methodology
The project followed the following methodology to achieve its objectives:

### 3.1 Maze Generation
A maze generation algorithm was employed to create random mazes for simulation purposes. The generated mazes consisted of walls and open passages.

### 3.2 Floodfill Algorithm
The floodfill algorithm was implemented to solve the maze. It involves two phases: maze exploration and pathfinding.

Maze Exploration:

Mark the starting cell as visited.
Check neighboring cells (up, down, left, and right) for open passages.
If an unvisited open passage is found, move to that cell and recursively apply the floodfill algorithm.
If no unvisited open passage is found, backtrack to the previous cell and continue the search.
   

   B) Pathfinding:
After the maze is fully explored, the floodfill algorithm traces back from the destination to the start point, selecting the neighboring cell with the lowest value until the start point is reached. This determines the shortest path from the start to the destination.

### 3.3 ROS Gazebo Simulation Environment
A virtual simulation environment was created using ROS Gazebo to visualize the maze and the mouse's movement. Gazebo provides a powerful framework for simulating robotic systems, and it was utilized to create a realistic and interactive environment for the maze-solving simulation.

## Implementation

The project was implemented using the following technologies:

ROS (Robot Operating System)
Gazebo simulation environment
Python programming language

ROS provided the framework for communication between different components of the simulation, while Gazebo served as the simulation environment. Python was used for implementing the floodfill algorithm and controlling the mouse's navigation in the maze.

##  Results

The Miromouse Maze Solving Simulation Project successfully achieved its objectives. The floodfill algorithm effectively explored the maze and found the shortest path from the start point to the destination. The ROS Gazebo simulation environment provided a realistic representation of the maze, the mouse's movement, and the shortest path.

## Conclusion

The project successfully demonstrated the implementation of the floodfill algorithm for solving a maze and navigating a simulated mouse from the start point to the destination using ROS Gazebo and Python. The simulation environment enhanced the understanding of the algorithm's execution and facilitated visualization of the maze-solving process. The project could serve as a foundation for further developments in autonomous navigation and maze-solving algorithms using ROS.

## Future Work
Some potential future enhancements for the Miromouse Maze Solving Simulation Project could include:

Integration of more advanced pathfinding algorithms, such as A* or Dijkstra, to compare their performance with the floodfill algorithm.
Integration of different maze generation algorithms to create diverse maze structures.

## References

[ROS Wiki]()
[Algorithm - Maze Traversal]()
