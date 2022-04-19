---
layout: post
title: "Deep Learning based Trajectory Optimization of Bipedal Robots"
description: "Developing robust environment for the Reinforcement Learning algorithms and attempt to develop a controller for stability and trajectory manipulation"
categories: piston
thumbnail: "BipedalRobotTrajectory.jpg"
year: 2022
gmeet: "https://meet.google.com/zrh-jrvv-sio"
---


### Mentors


- Pranshu Shukla
- Monal Singh
- Viren Varma


### Members


- Aryan Amit Barsainyan
- Nikhil P Reddy
- Siddh Narhari
- Shashank H S

## Aim

The aim of the project is to perform Deep Reinforcement Learning on a biped robot trained in Pybullet, a physics simulator with the realistic setting of a new robot model developed during the phase of the project.

## Introduction
The project is divided into 3 key components:

- Designing a mechanically accurate and robust 3D model of the biped robot.
- The simulation environment and the stability controls with a basic trajectory generator.
- Reinforcement Learning algorithm that is to be integrated into the environment.

## Design

![Bipedal design](/virtual-expo/assets/img/piston/bipedal_design.jpg)

## Simulation

### Phase 1: Creating an environment from scratch.

The initial simulations and tests were conducted in Pybullet. The aim was to create a robust environment for the RL algorithms and attempt to develop a controller for stability and trajectory manipulation.

**Pybullet - Python Interface for the Bullet Physics SDK**

Pybullet is an easy-to-use Python module for physics simulation, robotics, and deep reinforcement learning based on the Bullet Physics Software Development Toolkit (SDK). With PyBullet one can load articulated bodies from URDF, SDF, MJCF, and other file formats. PyBullet provides forward dynamics simulation, inverse dynamics computation, forward and inverse kinematics, collision detection, and ray intersection queries.

The algorithms developed were simulated and tested on an available Bipedal robot URDF in the Pybullet environment. The position control and velocity control algorithms were developed mainly to control joint positions with both dynamic and static time steps.

The next step was to manipulate PID controls for smooth movements of the joints and also fine-tune the parameters for damping and friction.

The stability control development and testing were initially limited to the Pitch movement of the robot and using the torque control to execute the stability maneuvers.


### Phase 2: Setting up an environment in MuJoCo

Due to the unrefined nature of the environment in PyBullet, the focus was shifted to pre-existing environment templates provided by MuJoCo.

MuJoCo is a physics engine that aims to facilitate research and development in robotics, biomechanics, graphics and animation, and other areas where fast and accurate simulation is needed.


## ML Algorithm

OpenAI is an artificial intelligence research laboratory consisting of the for-profit corporation OpenAI LP and its parent company, the non-profit OpenAI Inc. It conducts research in the field of AI with the stated goal of promoting and developing friendly AI in a way that benefits humanity as a whole.

OpenAI conducts research in many domains of Artificial Intelligence. One such project was the OperAI Five. Which is a Reinforcement Learning Bot scaled up using traditional RL algorithms. The Bot was capable of playing DOTA 2, a multiplayer cooperative game, they also  managed to defeat the world champion team in DOTA 2.

[https://openai.com/five/](https://openai.com/five/)


OpenAI Gym

OpenAI is a collection of open-source environments that are used as a standard benchmark for testing RL algorithms. They range anywhere from simple Atari Games like Atari Breakout to complex simulations of Robot arms and walkers. We used the BipedalWalker-v2  for testing the algorithms in the initial phase. After which we moved on to the MuJoCo environment.

[https://gym.openai.com/envs/BipedalWalker-v2/](https://gym.openai.com/envs/BipedalWalker-v2/)


### Algorithms Tested


A2C
A synchronous, deterministic variant of Asynchronous Advantage Actor Critic (A3C). It uses multiple workers to avoid the use of a replay buffer.

ACER
Sample Efficient Actor-Critic with Experience Replay (ACER) combines several ideas of previous algorithms: it uses multiple workers (as A2C), implements a replay buffer (as in DQN), uses Retrace for Q-value estimation, importance sampling and a trust region.

ACKTR
Actor Critic using Kronecker-Factored Trust Region (ACKTR) uses Kronecker-factored approximate curvature (K-FAC) for trust region optimization.

DDPG
Deep Deterministic Policy Gradient (DDPG)

DQN
Deep Q Network (DQN) and its extensions (Double-DQN, Dueling-DQN, Prioritized Experience Replay).

GAIL
The Generative Adversarial Imitation Learning (GAIL) uses expert trajectories to recover a cost function and then learn a policy.
Learning a cost function from expert demonstrations is called Inverse Reinforcement Learning (IRL). The connection between GAIL and Generative Adversarial Networks (GANs) is that it uses a discriminator that tries to separate expert trajectory from trajectories of the learned policy, which has the role of the generator here.
HER
Hindsight Experience Replay (HER)
HER is a method wrapper that works with Off policy methods (DQN, SAC, TD3 and DDPG for example).


PPO1
The Proximal Policy Optimization algorithm combines ideas from A2C (having multiple workers) and TRPO (it uses a trust region to improve the actor).
The main idea is that after an update, the new policy should be not too far from the old policy. For that, ppo uses clipping to avoid too large updates.

PPO2
The Proximal Policy Optimization algorithm combines ideas from A2C (having multiple workers) and TRPO (it uses a trust region to improve the actor).
The main idea is that after an update, the new policy should be not too far from the old policy. For that, PPO uses clipping to avoid too large updates.

SAC
Soft Actor Critic (SAC) Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor.
SAC is the successor of Soft Q-Learning SQL and incorporates the double Q-learning trick from TD3. A key feature of SAC, and a major difference with common RL algorithms, is that it is trained to maximize a trade-off between expected return and entropy, a measure of randomness in the policy.

TD3
Twin Delayed DDPG (TD3) Addressing Function Approximation Error in Actor-Critic Methods.
TD3 is a direct successor of DDPG and improves it using three major tricks: clipped double Q-Learning, delayed policy update and target policy smoothing. We recommend reading the OpenAI Spinning guide on TD3 to learn more about those.

TRPO
Trust Region Policy Optimization (TRPO) is an iterative approach for optimizing policies with guaranteed monotonic improvement.


## Conclusion

Thus we successfully tested out applications of Policy based (DDPG, DQN, PPO1, PPO2, TRPO etc) and custom off-policy Reinforcement learning algorithms on a prebuilt Mujoco 3D environment of a bipedal bot as well as on a 2D box environment. We build our own environment as well using Pybullet to simulate the 3D bot using a custom built physics engine. Modeling on the bipedal was also done on CAD software.


## References

1. Advantage-Weighted Regression: Simple and Scalable Off-Policy Reinforcement Learning Xue Bin Peng, Aviral Kumar, GraceZhang,Sergey Levine
2. [https://github.com/openai/gym/blob/master/gym/envs/mujoco/humanoid.py](https://github.com/openai/gym/blob/master/gym/envs/mujoco/humanoid.py)
3. [https://github.com/openai/gym/blob/master/gym/envs/box2d/bipedal_walker.py](https://github.com/openai/gym/blob/master/gym/envs/box2d/bipedal_walker.py)
4. Learning Linear Policies for Robust Bipedal Locomotion on Terrains with Varying Slopes Lokesh Krishna, Utkarsh A. Mishra, Guillermo A. Castillo, Ayonga Hereid, Shishir Kolathaya
5. [https://github.com/adityasagi/robotics_tutorial](https://github.com/adityasagi/robotics_tutorial)
