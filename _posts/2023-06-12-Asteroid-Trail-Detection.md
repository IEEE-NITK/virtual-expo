---
layout: post

title: "ASTEROID DETECTION USING ML"

description: "Detection of Asteroid trails in Hubble Space Telescope images"

categories: envision

thumbnail: "placeholder-image.jpg"

year: 2022
---

### Project Guide

- Dr.Krishnan CMC

### Mentors

- Gaganashree

- Dharaneedaran

### Members

- Achinthya Krishna B

- Imamhusen H Konasagar

- Sachin Prasanna

- Shreyas Udaya

- Aditya Tyagi

- Karan Kumar Bhagat

## Aim

Using algorithms based on multi-layered deep Convolutional Neural Networks, via transfer learning we hope to achieve an accuracy of 80% and above on validation set while detecting asteroid trails in Hubble telescope images.

## Introduction

We present an application of Deep Learning for the image recognition of asteroid trails in single-exposure photos taken by the Hubble Space Telescope. We aimed to demonstrate that Machine Learning techniques can be very useful in trying to solve problems that are closely related to Astronomy and Astrophysics, but that they are still not developed enough for very specific tasks.

## Dataset Production

A major task that was inherent to this project was dataset production, considering there is no sorted data pre-available for this particular project. We tried the very straightforward approach of trying to use image processing to sort the data and then had to use data sorting website

### Image processing approach

Since the asteroid trails are seen as straight lines in the telescopic images, we decided to use straight line detection using hoffmann transform in hopes of getting the line since there weren’t much visible lines to us except the ones of the asteroid trail, but there were some issues.

![Raw images](/virtual-expo/assets/img/envision/diode/ATD-2.jpg)

![line detected image](/virtual-expo/assets/img/envision/diode/ATD-1.jpg)

As can be observed in the image above, the line detected were multiples except the main asteroid trail, this posed an issue of how to classify the images.

### Roboflow

We then used Roboflow to classify the data, this became messy because we didn’t have enough time to classify the data manually and had to use the training solution provided by them which wasn’t the best solution.

## Implementation Model

We used YOLOv5 model to implement the ML model

### YOLOv5

Compared to other region proposal classification networks (fast RCNN) which perform detection on various region proposals and thus end up performing prediction multiple times for various regions in a image, Yolo architecture is more like FCNN (fully convolutional neural network) and passes the image (nxn) once through the FCNN and output is (mxm) prediction. This the architecture is splitting the input image in mxm grid and for each grid generation 2 bounding boxes and class probabilities for those bounding boxes.

YOLOv5 is a family of compound-scaled object detection models trained on the COCO dataset, and includes simple functionality models trained on the Augmentation, model ensembling, hyperparameter evolution and export to ONNX, coreML and TFLite

![YOLO architecture](/virtual-expo/assets/img/envision/diode/ATD-3.png)

## Result

## Conclusion

- The project didn’t reach its full potential.

- It was highly realised that the project needs more time, there are several better implementation and ways to sort the data.

- We could use better use of the Image processing method and use manual data sorting to better the dataset to let the model learn better.

## References

1. Detection of asteroid trails in Hubble Space Telescope images using Deep Learning by Parfeni, Caramete, Dobre Mach

2. The Hubble Asteroid Hunter project on Zooniverse
