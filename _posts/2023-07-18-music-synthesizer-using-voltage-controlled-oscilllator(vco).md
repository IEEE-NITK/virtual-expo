---

layout: post

title: "Music Synthesizer using Voltage Controlled Oscilllator(VCO)"

description: "ONE LINER DESCRIPTION"

categories: envision

thumbnail: placeholder-image.jpg

year: 2023

---

### Project Guide

- Apurva S

IAS chair

### Mentors

- Venugopal R

- Harshak Sachdeva

- Kaushik Srivastava

### Members

- Adithya Kasal

- Aditya Raj Pandia

- Gururaj Vijay Shimpi

- Vaibhav Santhosh

## Acknowledgements

We would like to thank the envision team and seniors of diode for their constant support throughout the project.

## Introduction

Analog music synthesis, renowned for its warm and organic sound, continues to captivate musicians despite the rise of digital technologies. Central to Analog synthesis is the voltage-controlled oscillator (VCO), which generates fundamental waveforms and enables precise control over pitch through voltage modulation. This project aims to design and implement a VCO using bipolar junction transistors (BJTs) and operational amplifiers (op-amps). The objective is to develop a VCO circuit that accurately translates linear voltage changes to logarithmic frequency perception, aligning with human auditory expectations, using a linear to exponential voltage converter and a VCO. This project combines theoretical analysis and circuit simulation to assess the VCO's performance in terms of frequency linearity, stability, and tuning range.

## Linear to Exponential Voltage converter using Differential Amplifier

> ### Why do we need a linear to exponential voltage converter

A linear-to-exponential converter is an essential part of many music synthesizers, as it provides a way to convert a linear voltage input into an exponential voltage output. This allows one to control various aspects of the sound produced by the synthesizers, such as pitch, amplitude, and filter cut-off frequency, in a more intuitive way. The pitch of a sound is typically controlled by a voltage-controlled oscillator (VCO), which generates a waveform at a frequency proportional to the input voltage. However, because the human ear perceives pitch logarithmically, a linear voltage input does not result in a linear change in pitch. To solve this problem, a linear to exponential converter is used to convert the linear voltage input into an exponential voltage output, which is then used to control the frequency of the VCO. By applying 5 volts of linear input to the converter, the resulting exponential output voltage can be used to control the pitch of the VCO in a more musically meaningful way.

![Octaves of note "A" visualised on a frequency graph](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/octaves.png)

### Amplifier circuit

The specific circuit used for the linear-to-exponential converter will depend on the specific requirements of the synthesizer. However, a basic circuit may consist of a differential amplifier and an op-amp. The input voltage is applied to the non-inverting input of the differential amplifier, while the inverting input is grounded.

![Linear to exponential voltage converter](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/lte.png)

The output of the differential amplifier is then fed into the non-inverting input of the op-amp and the output of the op-amp is the exponential voltage output.
The output voltage can then be used to control the frequency of the VCO using a voltage-controlled filter or other voltage-controlled modules in the synthesizer. By adjusting the input voltage, one can create a variety of sounds with different pitches and dynamic characteristics. Each input voltage corresponds to a different note in
the musical scale. 

### Temperature variation

The reasoning behind why we use two BJTs in the design is that we need to eliminate the variation in the output due to changes in temperature. This can be done by matching the two transistors exactly such that their parameters such as gain vary similarly with change in temperature. To deal with this variation, we use two perfectly matched transistors as shown. Both of them need to have the same, or nearly same, temperature coefficients and gains.

![Differential Amplifier](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/Diff_amplifier.jpg)

## Voltage Controlled Oscillator

### What is a VCO?

A Voltage Controlled Oscillator (VCO) is an electronic oscillator that generates a waveform whose frequency can be controlled by a voltage input. The output frequency of the oscillator is determined by an input voltage that controls the tuning of the oscillator circuit. The VCO is a fundamental building block in many electronic systems, including radios, synthesizers, and communication systems.
VCOs are available in various types, such as voltage-to-frequency converters, re-laxation oscillators, and crystal oscillators. They can operate at different frequencies ranging from a few Hertz to several gigahertz, depending on the application.

###Circuit Diagram of VCO

The circuit used in the project takes in the input voltage (coming from the linear to exponential voltage converter) and generates a triangular waveform and a square waveform. The triangular waveform is generated using an integrator circuit and the square waveform is generated using an inverting Schmitt Trigger

![VCO Circuit diagram](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/vco.jpg)

### Working of the VCO

As the input is fed into the integrator, the output waveform is triangular. The capacitor gets charged in this process. The generated triangular waveform is then given as input to the Schmitt Trigger. As long as the voltage doesn't go beyond the upper threshold voltage of the Schmitt Trigger, the second output is +Vsat (Saturation Voltage). Due to this, the base-emitter junction of the transistor is in forward bias and the circuit is complete. The instant it crosses the upper threshold voltage value, second output is -Vsat. This causes the base-emitter junction of the transistor to become reversed-biased and break the circuit. Now, the capacitor discharges, and the output 1  drops linearly. This continues until the voltage drops below the lower threshold voltage and the 2^nd^ output is again +Vsat. Alternating +Vsat and -Vsat gives the square waveform as the output, which is given to the speaker.

![Output wave](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/outwaveforms.png)

## Simulation and Result

The circuit shown above is the one that was simulated for the project. It utilizes all the components discussed previously including the integrator, differential amplifier,
Schmitt trigger, and others. The simulation was done in LTSpice.

![Final schematic of the Music synthesizer](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/ms.jpg)

First input signals Key, Tune, and LFO were sent into the adder Op-Amp and then led to the differential amplifier. Following the linear to exponential conversion, the  signal was sent as input to the VCO. At the VCO, the two waveforms, square and triangle, is the output of the synthesizer.

![Combined input signal](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/combinput.jpg)

![Linear to exponential converter signal](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/expoinput.jpg)

![Triangle waveform](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/triangle.jpg)

![Square waveform](/virtual-expo/assets/img/envision/diode/music-synthesizer-using-voltage-controlled-oscilllator(vco)/Square.jpg)

## Conclusion

In conclusion, this project has successfully designed and implemented a voltage-controlled oscillator (VCO) using bipolar junction transistors (BJTs) and operational amplifiers (op-amps). By incorporating a linear to exponential voltage converter, the VCO achieved accurate frequency control that aligns with human auditory perception. 
The comprehensive analysis confirmed the reliability and precision of the VCO's performance, meeting the requirements for real-world musical applications.

Each member involved in this project learned the working of BJTs, OpAmps, and their application circuits. This gives them a solid foundation in analysing Analog electronic circuits and designing them.

## References

1.1V/octave VCO, [Link](https://www.allaboutcircuits.com/projects/diy-synth-series-vco/)

2.Voltage controlled oscillator, [Link](https://synthesizeracademy.com/voltage-controlled-oscillator-vco/)
