---
layout: post
title: "Detecting Metal Surface Defects using ML"
description: "Predicting the type of defects found in steel manufacturing by making a Custom Convolutional Neural Network"
categories: envision
thumbnail: "MetalDefectsUsingML.png"
year: 2021
---

### Project Mentors
- Diptesh Banerjee
- Viren Varma

### Members
- Saee Sholapurkar
- Sujant Kumar
- Kyathi Charvi Vallampati

## Abstract
We utilize machine learning to design and train a Deep Neural Network for detecting metal surface defects and classifying them.The classifier is based on the **Xception** (*deep convolutional neural network architecture*). The model allows *classifying* images of real world flat metal surfaces from manufacturing industry with defects of common ten classes with the general accuracy of 93.31%. With line graphs, we visualize how the training and validation accuracy progresses as the model learns with subsequent epochs.

## Aim
*To train an effective Neural Network Model using python libraries like Tensorflow,Keras to identify the ten most common  defects on metal sheets.*

The need for identification of metal defects is of extreme relevance in the manufacturing industry & in study of material sciences and its applications. Our prime focus is on the ten most common defects, namely :-
- *Crease*           
- *Crescent gap*
- *Oil spot*
- *Inclusion*
- *Water spot*
- *Rolled pit*
- *Punching hole*
- *Silk spot*
- *Water spot*
- *Waist folding*
- *Welding lines*

![Typical-surface-defect-samples-in-the-dataset.png](/virtual-expo/assets/img/envision/piston/Typical-surface-defect-samples-in-the-dataset.png)

## Methodology

### Importing all necessary modules
**Tensorflow** and **Keras** modules are imported to design the basic architecture of our model.<br>The model we have created is a **sequential model**, with different layers having their activation functions & parameters as *Dense, Flatten, Max Pooling, Conv2D* etc.<br>Hence, we import these modules as well. Optimizers like *Adam* to minimize loss and the use of the *ImageGenerator* module to augment our data for better results.

### Data Augmentation using ImageGenerator and Introduction of 10 classes in our model
The *ImageGenerator* function is called to augment our data belonging to three different files namely- TEST, TRAIN & VALID.

We also introduce the **ten defect classes** by declaring their names in the class parameter of *ImageGenerator*.

### Building the model

The model comprises several layers, major ones being input and output in addition to numerous hidden layers. Every layer consists of nodes/neurons. A weight is associated with every node, which can be said to be the strength of the connection between any two connected nodes.Activation functions map nodes’ inputs to their corresponding outputs.
Output = activation(weighted sum of inputs)
*This corresponds to every single node in the network.*

Every input traverses through this network to finally emerge from one of the output nodes classified as some defect. The purpose of the model is to *optimise these weights* as well as to tailor a network of suitable layers and functions so that the predicted output matches with the actual expected output.

We have imported the Xception model which acts as a reference/ base for our model.

![Xception Model.png](/virtual-expo/assets/img/envision/piston/Xception-Model.png)

The **Xception's** model from Imagenet shows highest accuracy and renders itself  useful for this particular project. <br>
- Our model is primarily made of *‘Dense’* layers.
- The activation functions used are *‘relu’* and *‘softmax’*.
 *‘Dropout’* layer has been used to avoid overfitting. Mainly used for regularisation, It randomly eliminates some nodes in the layers which helps in reducing overfitting. 
 - *Adam*(Adam Adaptive Moment Estimation) optimiser with learning rate 0.0003 implemented in order to maximise accuracy and minimise loss.
- 0.2% of total numbers parameters are set to be non-trainable to avoid overfitting & give an optimal fit (*we don’t want an underfit either)*.

![Training Accuracy over the epochs.png](/virtual-expo/assets/img/envision/piston/metal-defects-ml-3.png)

This is what the model summary looks like:

![model summary.png](/virtual-expo/assets/img/envision/piston/metal-defects-ml-1.png)

## Result

<figure class="image" style="text-align: center; color: gray;"><img src="/virtual-expo/assets/img/envision/piston/metal-defects-ml-2.png" alt="img">Training Accuracy has substantially increased during the entire training cycle.</figure>

<figure class="image" style="text-align: center; color: gray;"><img src="/virtual-expo/assets/img/envision/piston/Validation-Accuracy-Vs-Epochs.png" alt="img">Validation Accuracy has substantially increased during the entire training cycle, but not as much as the training accuracy but seemed to not saturate by running on more epochs.</figure>

<figure class="image" style="text-align: center; color: gray;"><img src="/virtual-expo/assets/img/envision/piston/MSE-Vs-Epoch.png" alt="img">MSE lowers as we run the epochs for both Accuracy and Validation.</figure>

![Validation Loss Vs Epochs.png](/virtual-expo/assets/img/envision/piston/Validation-Loss-Vs-Epochs.png)


## Conclusion
The purpose of this project was to *identify defects on metal surfaces using the power of a machine learning model* ,here, **convolutional deep neural network for classification**. Based on the results, graphs & analysis conveyed earlier, it can be concluded that the project works in phases :

- Firstly, *we get the data & preprocess it*,like getting the dimensions of images correct so its compatible with the leaning algorithm, 
- Then, *we fit our model* (based on the XCEPTION architecture) to our preprocessed data & getting the required parameters.
- And lastly, *we infer on unseen new data to get our prediction* accuracy & final thoughts on its performance.

While concluding,we would also reflect on the project work done. For us, preprocessing & getting the data correct was one of the toughest part of the puzzle. We familiarized ourselves with various libraries, functions and their parameters & also the mathematical intuition behind it. To add, we are glad to be exposed to this infinitely useful & vast field which we all use daily in some form of algorithm running on our systems but totally unaware. 

**So wrapping up with results of our metal defect image classifier, we have classified the test images with a training accuracy of 93.31% and a validation accuracy of 64.1%.**


## References
- [Kaggle dataset that we used](https://www.kaggle.com/zhangyunsheng/defects-class-and-location?select=images)
- [Machine learning course by Andrew NG (for Mathematical references)](https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)
- [Implementation](https://www.youtube.com/watch?v=tDaGT4N4aCA&list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL)