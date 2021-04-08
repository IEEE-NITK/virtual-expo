---
layout: post
title: "Sports Video Analysis using Computer Vision"
description: "To build frameworks that detect objects and events in sports videos"
categories: diode
thumbnail: "player-tracking.jpg"
---

### Mentors

- Suraj Kulkarni
- Nikhil Nair

### Members

- Shreyas Rao
- Rohan Mallya

# Abstract

The field of sports analysis is rich and filled with opportunities for innovation. With the amount of video data available for sport developing algorithms and related models for efficient data extraction and storage, it becomes an interesting research problem.

# Implementation

This project has two broad components namely, ball tracking and pose estimation. Let&#39;s look at them one by one

## Ball Tracking

The objective here is to detect a moving ball in video frames and trace out its trajectory. The major problem we had to tackle was that usually, moving balls are not clearly visible in the frames and are often distorted. So, we took two main approaches to this problem.

### Approach 1:

Using sparse optical flow to detect key features in the frames and track them using various feature matching techniques.

Sparse optical flow selects a sparse feature set of pixels (interesting features such as edges and corners) to track its velocity vectors (motion). The extracted features are passed in the optical flow function from frame to frame to ensure that the same points are being tracked.There are various implementations of sparse optical flow, including the Lucas-Kanade method, the Horn-Schunck method, the Buxton–Buxton method, etc.

### Approach 2:

We train a random forest classifier to detect the presence of cricket balls using a dataset we found online.

The Random forest Classifier is a supervised learning algorithm which can be used both for classification and regression. It is also the most flexible and easy to use algorithm. A forest is comprised of trees. It is said that the more trees it has, the more robust a forest is. The classifier creates decision trees on randomly selected data samples, gets prediction from each tree and selects the best solution by means of voting. It also provides a pretty good indicator of the feature importance.

We first preprocess every frame by eliminating scene changes, adding gaussian blur and detecting contours. This way, the ball would be detected as one of the contours in the image. Next, we input this preprocessed image into the random forest classifier to detect the cricket ball amongst the contours and append the location of the ball onto a deque data structure. Using this list of locations, we trace out the ball&#39;s trajectory on the video.

From the results obtained, we felt that the second approach was more robust in detecting features and extracting the exact location of the moving ball.

## Final Result

![](/virtual-expo/assets/img/diode/ball_tracking.gif)

# Pose Estimation

To detect players in a video and estimate pose using a trained model.

We use YOLO to detect and segment out players. YOLO is an algorithm based on regression, instead of selecting the interesting part of an image, it predicts classes and bounding boxes for the whole image in one run of the Algorithm.

Next, we pass the segmented players into a model called OpenPose.OpenPose is an opensource real-time multiple-person detection library, that jointly detects human body, face, and foot keypoints.

As you can see in the below image, keypoints such as elbows, shoulders, knees and ankles are detected and joined together.

![](/virtual-expo/assets/img/diode/pose1.jpeg)

# Conclusion

Techniques like ball tracking and pose estimation can be used by sport analysts and critics to evaluate and give feedback regarding various aspects of the sport. We believe that the future direction of sports video analysis will concentrate on a more specialized, but also more in-depth analysis.  For the enrichment and 3D reconstruction of sports events, current systems exist for specialized applications. Probably, more emerging topics will appear to enhance the quality and value of the sports videos in the near future. Thank you!

# References

- [Event Detection in Tennis matches based on Video Data Mining ](https://ieeexplore.ieee.org/abstract/document/4607725?casa_token=-c5zQYjJ-ZAAAAAA:lFoO2sygX33U-4uzHhMGxYRU2YG8WkD36E5jYY1dWPQTx_N0AyiYVhEvmu_3WUWlteJx9rcLQA)
- [Trajectory Based Event Tactics Analysis in Broadcast Sports Video ](https://dl.acm.org/doi/pdf/10.1145/1291233.1291250)
- [Artificial Intelligence for Sport Actions and Performance Analysis using RNN with LSTM](https://dl.acm.org/doi/abs/10.1145/3297097.3297115?casa_token=wEUwfSpzV4gAAAAA:UxAe4iSml3z2ukWouTgE7WpIumyvLGuIz505JBuGz8Wvy-jltZK1Ic234sns3izwgJmZ5DodOxYG)