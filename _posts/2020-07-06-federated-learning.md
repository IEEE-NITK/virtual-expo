---
layout: post
title: "Federated Learning"
year: 2020
categories: compsoc
description: "Federated Learning is a platform that trains an algorithm across multiple decentralized devices or servers holding local data samples, without exchanging their data samples."
thumbnail: "federated-learning.jpg"
---

### Mentors
- Tanmai H
- Abhinav PY

### Members
- Shreeraksha Aithal
- Vineeth Rajesh
- Ansen Antony


# Objectives

To build a platform that facilitates privacy-preserving over a private, distributed dataset and which facilitates Federated Learning and Differential Privacy seamlessly as a part of existing Deep Learning Frameworks.

The demo will consist of two clients and a server, where we train half the machine learning model in one of the clients and the other half on the other client using data present on the client systems respectively. These half models are then brought to the server system where they are combined to make a full-fledged model and predictions are computed on this server and results are sent to the clients.

#  Methodology

Federated learning model was implemented first using Virtual Workers using the APIs provided by PySyft and later by WebSocketClients. The dataset was split and sent to these workers where it was trained independently and the final result(trained model) is sent back after adding some noise. These noises get cancelled when all the models get combined hence preserving Differential Privacy. The final model (at our end) is then taken from these learned models from different workers.


**Equations**
***Differential Privacy**

Federated learning instead allows for machine learning through decentralisation. It’s a solution that enhances user privacy because personal data always remains in local storage, never leaving the devices from which it originates.Differential privacy techniques can be applied to mask personal information before it is sent by encrypted communication to the cloud, where it is then averaged with other user updates to further mask individual data points.

The mathematical definition of Differential Privacy is


![Differential Privacy](/virtual-expo/assets/img/compsoc/differentialprivacy.png)

Epsilon (ε): A metric of privacy loss at a differentially change in data (adding, removing 1 entry). The smaller the value is, the better privacy protection.
Accuracy: The closeness of the output of DP algorithms to the pure output. In the Private Machine Learning with PATE part, I will use the classification accuracy on the test set as a statistic for evaluating accuracy.


# Results
Implemented a privacy-preserving  platform over a private, distributed dataset and which facilitates Federated Learning and Differential Privacy. It involved the PyTorch framework and with the PySyft library.

The deliverable has 3 clients and one server. A custom federated data loader was used to split the data across clients.
The clients train parts of the model with data present on their systems. Training across partial datasets was done using WebsocketWorkers and the model parameters were combined back in the server. 
The encrypted predictions were computed and results sent to clients. 

The model showed an accuracy of 94% after 30 epochs

#  Applications of Federated Learning
Self-driving connected cars can leverage federated learning to drive safely.
Healthcare is one of the best use-cases in federated learning. Here we have got tons of personal data that cannot be shared from hospitals, private doctors, health insurance companies, research institutes, etc. The data concerns sympotics, diseases, their progression, cure, medication, consequences, genetics and many other influencing factors, as well as statements that would be of great value for medicine.
In the age of digital assistants,we can use Federated Learning to train models for better recognition of wake-word and prevent it from listening to us all the time keeping our secrets secret.

#  References and acknowledgements 
- [Google AI’s blog describing Federated Learnings use in their Google Keyboard](http://ai.googleblog.com/2017/04/federated-learning-collaborative.html)
- [An older paper describing what Federated Learning is](https://ai.google/research/pubs/pub45648)
- [281 page book on Differential Privacy by Cynthia Dwork](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf)
- [Differential Privacy Results - Paper by Cynthia Dwork](https://web.cs.ucdavis.edu/~franklin/ecs289/2010/dwork_2008.pdf)
- [Federated Learning to Predict Words on Google Keyboard](https://arxiv.org/abs/1811.03604)
- [Federated Learning: The Future of Distributed Machine Learning](https://medium.com/syncedreview/federated-learning-the-future-of-distributed-machine-learning-eec95242d897)
- [How Federated Learning is going to revolutionize AI](https://towardsdatascience.com/how-federated-learning-is-going-to-revolutionize-ai-6e0ab580420f)
