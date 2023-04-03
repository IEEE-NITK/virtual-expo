---
layout: post
title: "Voice Swapper"
description: "Real-time voice conversion using GANs implemented on a WebApp"
categories: "diode"
thumbnail: "2023_voice-swapper.png"
year: "2023"
---

# Project Mentors

- Palgun N P
- Nikhil P Reddy
- Harish Gumnur

## Project Members

- Charu Samir Shah
- Viraj Singh Kalra

# Aim

To build the generative adversarial network model from scratch. To implement these models on a web application. To perform voice swapping (conversion) in real-time.

# Introduction

## A voice-changing dictaphone

Voice-Swapper is a Dictaphone that will be used to convert the user’s voice(source) to a target voice without any loss of linguistic information. VC is useful in many applications, such as customizing audio book and avatar voices, dubbing, voice modification, voice restoration after surgery, and cloning of voices of historical persons. VC models are primarily implemented with Generative Adversarial Networks (GANs) which provide promising results by generating the user fed-in statements in the target’s voice. We aim to build these models from scratch and implement them on a web application hosted using streamlit, a commonly used, python library, for easy ML integration. This project is an inter-sig project between Diode and Compsoc.

![VOICE](/virtual-expo/assets/img/diode/voice.png)

## Model Architecture

**CycleGAN**

One of the important characteristics of speech is that it has sequential and hierarchical structures, e.g., voiced or unvoiced segments and phonemes or morphemes. An effective way to represent such structures would be to use an RNN, but it is computationally demanding due to the difficulty of parallel implementations. Instead, we configure a CycleGAN using gated CNNs that not only allow parallelization over sequential data but also achieve state-of-the-art in speech modeling. In a gated CNN, gated linear units (GLUs) are used as an activation function. A GLU is a data-driven activation function, and the gated mechanism allows the information to be selectively propagated depending on the previous layer states.

![CYCLEGAN](/virtual-expo/assets/img/diode/cyclegan.jpg)