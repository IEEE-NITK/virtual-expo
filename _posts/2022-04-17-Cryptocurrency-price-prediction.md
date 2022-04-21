---
layout: post
title: "Crypto Prediction Exchange App"
description: "Prediction of cryptocurrency prices based on past data in the form of a react-based app"
categories: diode
thumbnail: "Cryptocurrency-Price-Prediction.png"
year: 2022
gmeet: ""
--- 

### Mentors


- Chandan Kumar


### Members


- Chinmaya Sharma 	
- Raghuram Kannan


## Aim

To predict the future prices of cryptocurrency using LSTMs and showcase the predictions in an app.

## Tech Stack

Client: React, React SDK, TailwindCSS

Server: Node, Express, MongoDB, Axios, Binance API, CoinGecko API, Trading View Carts

## Features

- Live prices & charts of over 200 cryptocurrencies
- Buy/Sell indicators for each cryptocurrency built on LSTM model
- Pseudo Exchange of crypto
- User authentication, user dashborad for keeping track of profit/loss

## Introduction

Time series forecasting occurs when you make scientific predictions based on historical time stamped data. It involves building models through historical analysis and using them to make observations and drive future strategic decision-making.

![image](https://www.katacoda.com/kuber-ru/assets/ai-machine-learning/prometheus-timeseries-forecasting/01-time-series-forecasting.png)

Bidirectional LSTMs are an extension of traditional LSTMs that can improve model performance on sequence classification problems. In problems where all timesteps of the input sequence are available, Bidirectional LSTMs train two instead of one LSTMs on the input sequence. The first on the input sequence as-is and the second on a reversed copy of the input sequence. This can provide additional context to the network and result in faster and even fuller learning on the problem.

## LSTMs

Long Short-Term Memory (LSTM) is a concept that was first proposed in 1997 . The LSTM model is a Gated Recurrent Neural Network, and bidirectional LSTM is just an extension of that model. The crucial aspect is that these networks may store information for future cell processing. Consider LSTM to be an RNN with a memory pool that contains two key vectors:
(1) Short-term state: the output is kept at the current time step.
(2) Long-term state: saves, reads, and rejects things intended for long-term storage while traversing the network.


![image 1](https://miro.medium.com/max/1400/1*V630gG25SFelbMQhsrGQDw.png)

	
Instead of training a single model, bidirectional LSTM introduces two. The first model learns the sequence of the specified input, whereas the second model learns the opposite sequence.
Because we have two trained models, we must create a method to integrate them. It is commonly known as the Merge stage. Merging can be used for any of the following purposes:
- Sum
- Multiplication
- Averaging
- Concatenation (default)

## Screenshots 

![image 2](/virtual-expo/assets/img/diode/Crypto-img-2.png)

![image3](/virtual-expo/assets/img/diode/Crypto-img-3.png)

## Conclusion

With the help of LSTM's we can predict prices of various cryptocurrencies based on the past and show if the user should purchase a crypto or not and we show this with the help of meter built with React.The entire application is powered by the React Library and uses web sockets for responsiveness.We use the coingecko API to get the values of realtime crypto's for the app.

## References

- [https://www.coingecko.com/](https://www.coingecko.com/)
- [https://reactjs.org/docs/getting-started.html](https://reactjs.org/docs/getting-started.html)
- [https://www.kaggle.com/c/g-research-crypto-forecasting](https://www.kaggle.com/c/g-research-crypto-forecasting)
- [https://www.binance.com/en](https://www.binance.com/en)
