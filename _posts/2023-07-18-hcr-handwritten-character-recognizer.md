---
layout: post
title: "HCR-Handwritten Character Recognizer"
description: "An DL-powered system that accurately identifies and transcribes handwritten characters into digital text."
categories: envision
thumbnail: placeholder-image.jpg
year: 2023
---

### Project Guide

- (Add name and designation, if any)

### Mentors

- Karan Kumar Bhagat
- Ashinee Kesanam

### Members

- Ansh Malhotra
- Harsh Anand
- Hritik Saraf
- Rahul Kumar Balani
- Sanjay Bhat

## Acknowledgements

We would like to thank IEEE NITK Student Branch for conducting Envision 2023

## Aim
To create a CNN model to recognise handwritten characters using real-time input video feed
## Introduction

This project focusses on real time character recognition application that detects and recognizes the characters from real time video using OpenCV and uses Tensorflow for the model working on the backend


![image 1](/virtual-expo/assets/img/envision/compsoc/hcr-handwritten-character-recognizer/1.jpeg)

## Technologies used
1. Python - Language used to create this entire project
2. Tensorflow - Python library used to create the CNN model
3. OpenCV - Python library used to take the the real-time video feed
4. Flask - Python library used to deploy the model as web application

## Model
After testing multiple model structures and reading some research papers, we came up with this model for one of the highest accuracies for recognising handwritten characters

1.Input Layer: Expects 300x300 RGB images.
2.Convolutional Layer: Applies 16 filters with a 3x3 size and ReLU activation.
3.MaxPooling Layer: Reduces spatial dimensions using a 2x2 pool size.
4.Convolutional Layer: Applies 32 filters with a 3x3 size and ReLU activation.
5.MaxPooling Layer: Reduces spatial dimensions using a 2x2 pool size.
6.Convolutional Layer: Applies 64 filters with a 3x3 size and ReLU activation.
7.MaxPooling Layer: Reduces spatial dimensions using a 2x2 pool size.
8.Convolutional Layer: Applies 64 filters with a 3x3 size and ReLU activation.
9.MaxPooling Layer: Reduces spatial dimensions using a 2x2 pool size.
10.Convolutional Layer: Applies 64 filters with a 3x3 size and ReLU activation.
11.MaxPooling Layer: Reduces spatial dimensions using a 2x2 pool size.
12.Flatten Layer: Converts feature maps into a 1D vector.
13.Dense Layer: Applies 512 neurons with ReLU activation for complex pattern learning.
14.Output Layer: Produces probabilities for 52 classes using softmax activation.

This model gave about 92% accuracy on the test dataset after running on 30 epochs. During model fit the batch size for training was kept 32 and the patience was kept as 15
## Real-Time Video Feed
Real-time video capture and character recognition were achieved by utilizing the OpenCV library. OpenCV, an open-source computer vision library, provided the necessary tools and functions for video processing. The video capture process involved accessing the camera feed, reading video frames, and displaying the video stream. To enhance the accuracy of character recognition, preprocessing techniques were employed on the video frames before passing them to the character recognition algorithm. OpenCV played a crucial role in enabling efficient and effective real-time video capture for character recognition purposes.
### Subheading 2.1

![image_2](/virtual-expo/assets/img/envision/compsoc/hcr-handwritten-character-recognizer/2.jpeg)

![image_3](/virtual-expo/assets/img/envision/compsoc/hcr-handwritten-character-recognizer/3.jpeg)

## Conclusion

- In conclusion, this project successfully implemented a real-time handwritten character recognition system by leveraging the power of TensorFlow and OpenCV. By combining the capabilities of these two powerful libraries, we were able to achieve accurate and efficient character recognition from live video feeds.

- Through the utilization of TensorFlow, a popular deep learning framework, we developed a robust neural network model capable of learning and recognizing various handwritten characters in real-time. The model was trained on a large dataset of handwritten characters, allowing it to generalize well and accurately identify characters in diverse handwriting styles.

- The integration of OpenCV proved invaluable in the real-time video processing pipeline. OpenCV provided essential functionalities for video capture, frame preprocessing, and image manipulation, enabling smooth and seamless character recognition from the live video feed.

## Future Enhancements
Future enhancements can involve expanding the character recognition capabilities to include multiple languages, optimizing the model for better performance, and exploring additional preprocessing techniques to handle different lighting conditions and noise in the video feed.
We can also deploy this project as a web app using Flask

## References

1. Built the CNN model using the resource:, [Link](https://data-flair.training/blogs/handwritten-character-recognition-neural-network/)
2. The real time video capture as generated using opencv tutorial:, [Link](https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/n)
3. The model is deployed using Flask framework, taken reference from the tutorial:, [Link](https://www.youtube.com/watch?v=mzX5oqd3pKA)
