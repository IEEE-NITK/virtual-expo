---
layout: post
title: "Virtual Rockstar - Simulating Guitar Effect Pedals"
description: "A simulation of guitar effect pedals"
categories: envision
thumbnail: "guitar-sim.jpeg"
year: 2021
---

### **Project Mentors**

- Anirudh T
- Rahul Magesh

### **Project Members**

- Prerana Prakash

## **Abstract**

The tonal versatility of a guitar is majorly due to effect pedals, which are ideally analog circuits. They process the clean output of a guitar to generate contrasting, distorted tones. These stomp boxes are small, portable, interchangeable and are used in varied combinations to create a guitarist’s signature tone. We intend to implement one pedal (Ibanez TS808 Tube Screamer) using LTSpice. The Tube Screamer TS808 by Ibanez is the most famous overdrive guitar pedal. It is suitable for blues and all range of rock music, adding a classic standard tone characterized by the tubelike distortion, good sustain, and smooth overdrive. The frequency response is tailored to emphasize the mid frequencies, creating a hump that helps to keep the guitar sound over the general mix of the band.

## **Circuit Design**

<img src="https://i.ibb.co/d2pyNxV/1.png" alt="1" border="0">

The Tube Screamer circuit is divided into four main sections -

1. Input buffer
2. Clipping stage
3. Tone/volume stage
4. Output buffer

The functionality of each stage is simple - The input buffer isolates the
pedal from the guitar, keeping the signal fidelity. Then, the clipping stage
incorporates the distortion to the signal and the tone/volume block will
add the tonal bass/treble adjustment. Finally, the output buffer will
prepare the signal to be injected into another pedal or amplifier.

**Input Buffer** - The task of the input stage buffer is to create a high input
impedance to preserve signal integrity, avoiding high-frequency signal
loss. It is implemented as an emitter follower.

**Clipping Stage** - The clipping amplifier is the core of the circuit, and it is formed by a variable non - inverting op amp with two diodes to perform
the clipping action and two filters in the feedback loop (passband filter)
to shape the amount of clipping and the frequency at which it occurs.

**Tone/Volume Stage** - This stage is formed by a passive main low pass
filter, an active tone circuit, and a passive volume circuit in order to
provide tone adjustment and volume control to the pedal. The
functionality is very elegant - The main passive low pass filter cuts off
the harsh overtones previous to the tone circuit. Then the active tone
control will boost the treble trying to flatten the response to
compensate and level the effects of the previous passive filter.

**Output Buffer** - The task of the output buffer is to create a unit gain, lowoutput impedance path to keep the signal integrity in the
guitar-pedals-amp chain. Like the input stage, it is implemented with an
emitter follower.

What makes the Tube Screamer very distinctive is mainly the frequency
selective distortion and the signal filtering -

1. In the clipping amplifier Stage, the bass is rolled off by the active
high pass filter in the feedback loop. With this approach, the
frequencies above 720Hz get the full distortion, and harmonics
below it get progressively less distortion, so the distortion is
frequency selective.
2. The treble is shaved off after the distortion stage with a passive
low pass filter, generating the distinctive mid frequencies boost.

## **Circuit Testing**

LTSpice allows the use of .wav files in voltage sources.
A sample audio file was used as the input and the output voltage
was exported as a .wav file. The input and output waveforms are shown
below. The output sound was pleasantly distorted and it is consistent
with the output one would expect with a real pedal.

Input -
<img src="https://i.ibb.co/G58Ddnx/2.png" alt="2" border="0">

Output - 
<img src="https://i.ibb.co/YyQGq80/3.png" alt="3" border="0">

Audio Files - 
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1264823680&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/anirudh-t-333464504" title="Anirudh" target="_blank" style="color: #cccccc; text-decoration: none;">Anirudh</a> · <a href="https://soundcloud.com/anirudh-t-333464504/sets/envision-expo" title="Envision Expo" target="_blank" style="color: #cccccc; text-decoration: none;">Envision Expo</a></div>
