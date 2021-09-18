---
layout: post
title: "Contextual Sarcasm Detection"
year: 2020
categories: compsoc
description: "A robust deep learning model that detects sarcasm in online discussion forums (Reddit) utilizing both content and contextual information."
thumbnail: "sarcasm-detection.jpg"
---

### Mentors
- Chandana
- Sakshat

### Members
- Krishna Swaroop
- Shruthan R
- Akshara P

## Objective
Build a robust deep learning model to detect sarcasm in online discussion forums (Reddit) utilizing both content and contextual information.

## Methodology

The detection of sarcasm is done by passing a unified vector representation of the comment by a user in a discussion forum to a CNN. The vector representation captures information about the text of the comment, the user who wrote the comment, and the other comments in the discussion forum. Each of them is described below:

**Text of the comment:**

To capture details about the text of the comment, we have used Sentence Transformers which is a pre-trained model that fine-tunes Bidirectional Encoder Representations from Transformers (BERT) embeddings with a siamese or triplet network structure to produce semantically meaningful sentence embeddings that can be used in unsupervised scenarios. This gives a 768-dimensional embedding of the comment.

**Information about the user:**

Information about the user is obtained by a fusion of the user&#39;s stylometric and personality features. Each person has a unique authorship style affected by their gender, diction, syntactic influences, etc., which is reflected in their writing. These stylometric features are obtained by gathering all the comments by the user in a document and applying an unsupervised learning method called ParagraphVector (Le and Mikolov, 2014) on the document which can effectively capture the user&#39;s writing style. ParagraphVector can be applied to variable-length texts and is known to be effective for sentiment classification tasks. Personality detection of the user helps in identifying the user&#39;s behavior and thought patterns and hence their sarcastic tendencies. We iterate over each comment of the user and pass it through a CNN which is pre-trained on a benchmark corpus developed by Matthews and Gilliland (1999) which contains 2, 400 essays and is labeled with the Big-Five personality traits, i.e., Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism (OCEAN). After the training, this CNN model is used to infer the personality traits present in each comment by extracting the activations of CNN&#39;s last hidden layer vector. The above stylometric and personality features are fused together using Canonical Correlation Analysis (CCA) (Hotelling, 1936) which captures maximal information between two views and creates a combined representation.

**Information about the discussion forum:**

The discourse of comments belonging to a certain discussion forum very likely contain contextual information relevant to the sarcasm detection. For example, a discussion on politics is more likely to have sarcastic comments than a discussion on the details of a pandemic. All comments in a discussion forum are consolidated in a document and as with stylometric features, ParagraphVector is used to generate discourse representations for each discussion forum.

**Final Prediction - Is the comment sarcastic?**

The representations of the text of the comment, the user embeddings for the author of the comment, and the discourse feature vector for the discussion forum in which the comment is posted are all concatenated together to form the unified vector representation of the comment. The CNN used for extraction of this vector has the same design as the CNN we used to extract personality features. Finally, the vector is projected to the output layer having two neurons with a softmax activation. This gives a softmax-probability over whether a comment is sarcastic or not. This probability estimate is then used to calculate the categorical cross-entropy which is used as the loss function.

## Result

The above model gives an F1 score of 0.7825 on a balanced dataset which is an improvement over the F1 score in the referenced paper.

## Applications

Sarcasm detection is of great importance in understanding people&#39;s true sentiments and opinions. Application of sarcasm detection can benefit many areas of interest of NLP applications, including marketing research, opinion mining and information categorization. However, sarcasm detection is also a very difficult task, as it&#39;s largely dependent on context, prior knowledge and the tone in which the sentence was spoken or written.

## References:

1. CASCADE: Contextual Sarcasm Detection in Online Discussion Forums by [Devamanyu Hazarika](https://arxiv.org/search/cs?searchtype=author&amp;query=Hazarika%2C+D), [Soujanya Poria](https://arxiv.org/search/cs?searchtype=author&amp;query=Poria%2C+S), [Sruthi Gorantla](https://arxiv.org/search/cs?searchtype=author&amp;query=Gorantla%2C+S), [Erik Cambria](https://arxiv.org/search/cs?searchtype=author&amp;query=Cambria%2C+E), [Roger Zimmermann](https://arxiv.org/search/cs?searchtype=author&amp;query=Zimmermann%2C+R), [Rada Mihalcea](https://arxiv.org/search/cs?searchtype=author&amp;query=Mihalcea%2C+R) ([https://arxiv.org/abs/1805.06413](https://arxiv.org/abs/1805.06413)).
2. Distributed Representations of Sentences and Documents by Quoc Le and Tomas Mikolov([https://cs.stanford.edu/~quocle/paragraph\_vector.pdf](https://cs.stanford.edu/~quocle/paragraph_vector.pdf))
3. Sentence Transformers: Multilingual Sentence Embeddings using [BERT](https://github.com/UKPLab/sentence-transformers)
4. Gerald Matthews and Kirby Gilliland. 1999. The personality theories of hj eysenck and ja gray: A comparative review. Personality and Individual differences, 26(4):583–626