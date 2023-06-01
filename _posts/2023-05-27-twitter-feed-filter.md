---
gmeet: "https://meet.google.com/xjy-hhac-xio"
layout: post
title: "Twitter Feed Filter"
description: "Twitter feed filter, a web-based application that allows users to filter irrelevant tweets making their feed clean which in turn improves the user experience while using the application."
categories: envision
thumbnail: 
year: 2023
---

### Mentors

- Pulkit Gupta
- Ankit Dash 

### Members

- Naga Mukesh
- Aditya Bhagwat
- Rahul Bhimakari
- Anurag Verma

## Acknowledgements

We would like to thank IEEE NITK Student Branch for conducting Envision 2023

## Aim
The project aims to identify the irrelevant tweets with respect to a particular trend and remove them from the user’s feed which will help in keeping the feed clean and improve the user experience while using the application.

## Introduction
The Twitter Feed Filter project is a web-based application that allows users to filter and search Twitter feeds based on specific keywords, hashtags, and user mentions. The application is built using Python, natural language processing techniques to identify and extract relevant tweets from a large pool of tweets containing the specified hashtags. The application uses a go lang scraper to fetch trending tweets. The application is designed to help users manage their Twitter feeds more effectively and efficiently, and to enable them to stay up-to-date with the latest news and trends. The filtered tweets are displayed on the web page.

## Objective
The objective of the project is to create a user-friendly application that enables users to search for tweets on a specific topic or keyword without being overwhelmed by irrelevant tweets. The project aims to provide a solution that streamlines the process of filtering Twitter feeds, making it easier for users to access relevant tweets.

## Features
The Twitter Feed Filter application comes with the following features:
1. **Trending Hashtags:** The application fetches the trending hashtags from twitter and uses them as filters for tweets.
2. **URL Scraping:** The application scrapes URLs related to each hashtag from Google
3. **Word Extraction:** The application scrapes URLs related to each hashtag from Google.
4. **Tweet Scraping:** The application scrapes tweets for each hashtag and saves them in separate .csv files.
5. **Natural Language Processing:** The application uses natural language processing techniques to embed the documents and words from the tweets and scraped URLs.
6. **Machine Learning:** The application uses machine learning algorithms to filter important words from the tweets based on the embedding distance between the document and each word of the tweet.
7. **Threshold-based Filtering:** The application filters tweets based on a certain threshold distance between the embedding of the document and each word.
8. **Flask Web Framework:** The application uses Flask web framework for front-end and back-end development.

## Architecture
The Twitter Feed Filter application is built using the following technologies:

1. **Python 3:** The application's back-end logic is written in Python 3 programming language.
2. **Beautiful Soup:** The application uses Beautiful Soup to scrape tweets from Twitter.
3. **NLTK:** The application uses the Natural Language Toolkit (NLTK) to perform natural language processing on the scraped tweets.
4. **Flask Web Framework:** The application uses Flask web framework for front-end and back-end development.
5. **HTML, CSS, and JavaScript:** The application uses HTML, CSS, and JavaScript for the front-end design and interactivity.

The application follows a modular architecture, where each module is responsible for a specific task, such as scraping tweets, performing natural language processing, and filtering tweets. Flask is used to serve the front-end interface and interact with the back-end modules.



## Conclusion

In conclusion, the Twitter Feed Filter project is an effective solution for managing Twitter feeds based on specific hashtags. The application's use of web scraping and natural language processing techniques allows users to quickly and easily filter through a large number of tweets to identify the most relevant content. Overall, the Twitter Feed Filter project is a practical and useful tool for anyone looking to stay up-to-date with the latest news and trends on Twitter.
During this project, each member has learned basic concepts of machine learning, NLP, web scraping and they also familiarize themselves with the use of version control systems like Git/Github.

## References

1. [Twitter Scraper](https://github.com/n0madic/twitter-scraper)
2. [Word Embedding and Word2vec](https://towardsdatascience.com/introduction-to-word-embedding-and-word2vec-652d0c2060fa)
3. [Natural Language Processing](https://youtube.com/playlist?list=PLZoTAELRMXVNNrHSKv36Lr3_156yCo6Nn)