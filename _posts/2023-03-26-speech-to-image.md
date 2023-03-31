---
layout: post
title: "Speech to image"
description: "Converting speech to image by integrating two deep learning models that are speech to text using ASR and StackGAN based text to image model. "
categories: diode
thumbnail: "2023_speech_to_image.png"
year: 2023
---

### Mentors

- Raghuram Kannan
- Vasanth M

### Members

- Omkar Patil
- Vishal Marwade
- Abhiraj
- Kaushik Srivastava

## Speech-to-Image

<summary>Table of Contents</summary>
  <ol>
      <li>
          <a href="#Introduction">Introduction</a>
      </li>
      <li>
        <a href="#Step-1 Speech to Text">Speech to Text</a>
        <ul>
                <li><a href="#Transformer Model Architecture">Transformer Architecture</a></li>
        </ul>
      </li>
      <li>
          <a href="#Step-2 Text to Image">Text to Image</a>
          <ul>
              <li><a href="#About Dataset">Dataset</a></li>
              <li><a href="#Text Embedding Model">Text Embedding Model</a></li>
              <li><a href="#Architecture">Architecture</a></li>
          </ul>
      </li>
      <li>
          <a href="#References">References</a>
      </li>
  </ol>

## Aim

To develop deep learning models to generate images for given audio input using speech to text and then text to image .

## Introduction <a name = "Introduction"></a>

In this project we attempt to translate the speech signals into image signals in two steps. The speech signal is converted into text with the help of Automatic speech recognition (ASR) and then high-quality images are generated from the text descriptions by using StackGAN.

## Step-1 Speech to Text <a name = "Step-1 Speech to Text"></a>

Automatic speech recognition (ASR) consists of transcribing audio speech segments into text. ASR can be treated as a sequence-to-sequence problem, where the audio can be represented as a sequence of feature vectors and the text as a sequence of characters, words, or subword tokens.

The Dataset we are using is the [<b>LJSpeech dataset</b>](https://keithito.com/LJ-Speech-Dataset/) from the LibriVox project. It consists of short audio clips of a single speaker reading passages from 7 non-fiction books. Our model is similar to the original Transformer (both encoder and decoder) as proposed in the paper,[<b> "Attention is All You Need"</b>](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf).

## Transformer Model Architecture <a name = "Transformer Model Architecture"></a>

Transformer model architecture follows seq-to-seq model using encoder-decoder structure along with multi head attention.
It takes input and gives output t in a parallel manner. Hence increasing the efficiency compared to conventional RNN model. This model was introduced in "Attention is all you need" paper in 2017 and since then this architecture has been the first choice for modelling speech recognition.

![Transformer_Architecture](/virtual-expo/assets/img/diode/Speech_to_image/Transformer_Architecture.png)

## Training Result

Following word error rate(wer) was achieved after training speech to text model.
![WER](/virtual-expo/assets/img/diode/Speech_to_image/WER.png)

## Step-2 Text to Image <a name = "Step-2 Text to Image"></a>

### Create 3 folders (test, weights,results_stage2) in your current working directory

1. <b>weights </b> (your model weights will be saved here)
2. <b>test </b> (generated images from our stage I GAN)
3. <b>results_stage2 </b> (generated images from stage II fo GAN)

## About Dataset <a name = "About Dataset"></a>

### Dataset Name: CUB_200_2011

Download from : <https://data.caltech.edu/records/65de6-vp158>

#### Text Embedding Model <a name = "Text Embedding Model"></a>

Download char-CNN-RNN text embeddings for birds from : <https://github.com/hanzhanggit/StackGAN>

1. char-CNN-RNN-embeddings.pickle — Dataframe for the pre-trained embeddings of the text.
2. filenames.pickle — Dataframe containing the filenames of the images.
3. class_info.pickle — Dataframe containing the info of classes for each image.

## Architecture <a name = "Architecture"></a>

![Text to Image Architecture ](/virtual-expo/assets/img/diode/Speech_to_image/text_to_image_architecture.jpg)

- Stage 1
Generator :
The text-to- image model learns from the features that capture important visual details. Based on the visual details described in the text, it generates images which look real.
The text description is converted to a text embedding(vector of real numbers of fixed length) using Word2Vec pretrained model. The embedded text is concatenated with a random noise vector and is input to the generator. This generator generates a fake image as per the text description. The generated fake images along with the text description is input to the discriminator. The discriminator classifies whether the sample is fake or real. In stage-I GAN, the generator generates a low resolution 64*64 RGB image. This image captures low level features like color and shape of the object.
  - Steps in stage 1
    - Text Encoder Network
      - Text description to a 1024 dimensional text embedding
      - Learning Deep Representations of Fine-Grained Visual Descriptions [Arxiv Link](https://arxiv.org/abs/1605.05395)
    - Conditioning Augmentation Network
      - Adds randomness to the network
      - Produces more image-text pairs
    - Generator Network
    - Discriminator Network
    - Embedding Compressor Network
    - Outputs a 64x64 image

- Stage 2
Discriminator:
The output images of the stage-I generator and the embedded noise(vector) become the inputs to the stage-II generator. The sage-II generator tries to refine the image of stage-I generator and provides a high resolution $256*256$ RGB image. The high level features of the text descriptions are generated here. The image generated by this generator along with text embeddings is input to the discriminator similar to stage-I discriminator. This acts as a classifier differentiating fake and real images.
Since image generation takes place in 2 stages, the model generates high resolution images.
  - Steps in stage 2
    - Text Encoder Network
    - Conditioning Augmentation Network
    - Generator Network
    - Discriminator Network
    - Embedding Compressor Network
    - Outputs a 256x256 image
![discriminator ](/virtual-expo/assets/img/diode/Speech_to_image/discriminator.png)

## Conclusion

- Speech to text model was trained to achieve considerable word error rate for given size of dataset. Text to Image model also has been able to achieve desirable results.

### References <a name = "References"> </a>

1. <b>Attention is All You Need</b> [[Arxiv Link](https://arxiv.org/abs/1706.03762)]
2. <b>Very Deep Self-Attention Networks for End-to-End Speech Recognition</b> [[Arxiv Link](https://arxiv.org/pdf/1904.13377.pdf)]
3. <b>Speech-Transformer</b> [[IEEE Xplore](https://ieeexplore.ieee.org/document/8462506)]
4. **StackGAN: Text to photo-realistic image synthesis** [[Arxiv Link](https://arxiv.org/pdf/1612.03242.pdf)]
