---
layout: post
title: "Real Time Lane Detection"
description: "A Road Lane Detection System for Self Driving Cars"
categories: envision
thumbnail: "thumbnail_lane-detection.jpg"
year: 2022
---

### Mentors

- Pranav M Koundinya
- Palgun N P

### Members

- Achyut Agarwal
- Anirudha Bhat Nekkare
- Prasanna Kumar
- Samarth S Namdeo
- Vivek Mishra

## Aim

The aim of the project is to create a real time road lane detector using technologies like Numpy, Matplotlib and OpenCV.

## Introduction

In recent times many technological advancements are coming in the domain of road safety as accidents have been increasing at an alarming rate and one of the crucial reasons for such accidents is lack of driver’s attention. Technical advancements should be there to reduce the frequency of the accidents and stay safe. One of the ways to achieve the same is through Lane Detection Systems which work with the intention to recognize the lane borders on the road and further prompts the driver if he switches and moves to erroneous lane markings. Lane boundaries are detected using a camera that captures the view of the road, mounted on the front of the vehicle. The approach used in this paper changes the image taken from the video into a set of sub-images and generates image-features for each of them which are further used to detect the lanes present on the roads.

## Implementation

The lines on the road that show us where the lanes are act as our constant reference. We employ Canny Edge Detection-Hough Line Transform based lane detection.
The following flowchart depicts the process in its entirety:

![image_1](/virtual-expo/assets/img/envision/diode/LD-1.jpg)

Firstly it would include capturing and decoding the video, remove noise and use edge detection to find where the road is. Making use of Hough Line Transform to detect straight lines.
This model will be able to automatically detect lanes in a video stream from a front-facing camera mounted on a car.
Canny Edge detector needs grey scale images, hence we need to convert our image into grey scale. We are collapsing 3 channels of pixel value (Red, Green, and Blue) into a single channel with a pixel value range of [0,255]. Then we will create Gaussian blur over gray scale image .

![image_2](/virtual-expo/assets/img/envision/diode/LD-2.jpg)

This is how our image looks after Gaussian Blur.Next we will use canny to detect the edge of the lane.

## Processing of Image

### **Greyscale image**

Complexity of gray level images is lower than that of color images. We can talk about lots of features of an image's brightness, contrast, edges, shape, contours, texture, perspective, shadows, and so on, without addressing color. After presenting a gray-level image model , it can be extended to color images.

### **Gaussian Filter**

The purpose of using the Gaussian filter is to reduce noise in the image. We do this because the gradients in Canny are really sensitive to noise, so we want to eliminate the most noise possible.

### **Canny-edge detection**

Fundamental idea is to detect sharp changes in luminosity such as shift from black to white, white to black and will define it as edges. Noise reduction, Intensity Gradient, Non-Maximum suppression, Hysteresis thresholding. It has 3 parameters:

The img parameter defines the image that we’re going to detect edges on.

The threshold-1 parameter filters all gradients lower than this number (they aren’t considered as edges).

The threshold-2 parameter determines the value for which an edge should be considered valid.

Any gradient in between the two thresholds will be considered if it is attached to another gradient who is above threshold-2.

This is how our image looks after canny edge detection.

![image_3](/virtual-expo/assets/img/envision/diode/LD-3.jpg)

### **Hough line transform**

This one line of code is the heart of the whole algorithm. It is called Hough Transform, the part that turns those clusters of white pixels from our isolated region into actual lines.

Parameter 1: The isolated gradients

Parameter 2 and 3: Defining the bin size, 2 is the value for rho and np.pi/180 is the value for theta

Parameter 4: Minimum intersections needed per bin to be considered a line (in our case, its 100 intersections)

Parameter 5: Placeholder array

Parameter 6: Minimum Line length

Parameter 7: Maximum Line gap

Finally we will merge the Gaussian blurred image and the image obtained after Hough line transform using addWeighted command in OpenCV.

![image_4](/virtual-expo/assets/img/envision/diode/LD-4.jpg)

This is what our final image looks like.

## Conclusion

We were able to build a real time road lane detector using the following technologies and got some experience with image processing and Opencv.

## Future Work

Approach the same problem using AI by trying to obtain the Region of Interest(RoI) using neural networks.

## References

1. Real-time lane detection [Link](https://www.geeksforgeeks.org/opencv-real-time-road-lane-detection/)
2. OpenCV Tutorial, [Link](https://youtube.com/playlist?list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K)
