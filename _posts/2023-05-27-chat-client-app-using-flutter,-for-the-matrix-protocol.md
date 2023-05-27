---
gmeet: "https://meet.google.com/dnb-hejp-tfp"
layout: post
title: "Chat Client app using Flutter, for the Matrix protocol"
description: "Using Flutter to create an app which acts as a client for the decentralised MAtrix protocol"
categories: envision
thumbnail: 2023-05-27-chat-client-app-using-flutter,-for-the-matrix-protocol-filename.jpg
year: 2023
---

### Mentors

- Abhishek Satpathy
- Siddharth Bhat

### Members

- Akshat Chaturvedi
- Swati Bhat
- Shreesha M Budhya
- Har

## Acknowledgements

We are deeply grateful to IEEE, CompSoc and for giving us an opportunity to work with juniors!

## Aim

We aim to build a reliable and user friendly Flutter based app to act as a client, and enable users to connect to servers running on the decentralised [Matrix](https://matrix.org/) protocol.

## Introduction

The Matrix protocol is an open-source, decentralised protocol that enables real time communication between users, devices and services, and was created as an alternative to centralised communication services such as WhatsApp, Telegram and Slack.   

The Matrix protocol essentially defines a set of open APIs for decentralised communication which anyone can implement, subscribing to a global open federation of servers with no single point of control. Servers and clients which support this API in essence are running on the Matrix protocol.

We have implemented a Flutter based chat app, where users can connect to a Matrix homeserver using an username, and send End to End Encrypted text messages to each other. The implementation of the Matrix API is simplified by the [Matrix Dart SDK](https://matrix.org/docs/projects/sdk/matrix-dart-sdk)


![image 1](https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Diagramme_Matrix_en.svg/800px-Diagramme_Matrix_en.svg.png)

## Design

## Logging In

Every user is initially asked to log in with a username and password, and choose a particular Matrix "Homeserver" where all their credentials are stored. When a user sends a messgae to another user on a different homeserver, the senders homeserver is responsible to send the message to the reciever's homeserver.

## Home Screen

After logging in, the user is met with a homescreen where all the chats with users will be visible as cards.

![Home Screen](/virtual-expo/assets/img/envision/compsoc/chat-client-app-using-flutter,-for-the-matrix-protocol/HomeScreen.jpeg)

## User Chat
Messages exchanged between users are displayed in message bubbles.

![User chat](/virtual-expo/assets/img/envision/compsoc/chat-client-app-using-flutter,-for-the-matrix-protocol/UserChat.jpeg)

## Invite user page

To start chats with new users, a button to add new users with the help of their Matrix ID is available at the bottom of the screen.
A QR code is also generated and displayed, which when scanned shows the Matrix ID if the user! The QR code can also be shared/copied to clipboard as well!

![QRCode](/virtual-expo/assets/img/envision/compsoc/chat-client-app-using-flutter,-for-the-matrix-protocol/QRCode.jpeg)

## Profile page

The profile page will display the user's profile picture, username. It will also allow the user to edit the abovementioned details. The Log Out button can also be found here.

![Profile page](/virtual-expo/assets/img/envision/compsoc/chat-client-app-using-flutter,-for-the-matrix-protocol/profile.jpeg)


## Future plans

- Add support to send images and videos, and file sharing in general.
- Add support to form groups. Matrix servers already support the creation and moderation of groups.
- Add support to view Statuses.
- Possibly add support read-recipt, and the enabling and disabling of it.

## References

1. Matrix protocol specifications [here](https://spec.matrix.org/latest/)
2. Matrix protocol Dart package [here](https://pub.dev/packages/matrix)
3. [Flufflychat](https://fluffychat.im/), and open source Flutter based Matrix client
4. [Synapse server setup](https://matrix-org.github.io/synapse/latest/setup/installation.html) information
6. Resources to [learn Flutter](https://www.youtube.com/watch?v=1ukSR1GRtMU&list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ)
7. More resources to [learn Flutter](https://www.youtube.com/watch?v=VPvVD8t02U8)
8. Want to setup your own Matrix server? [Look no farther!](https://www.youtube.com/watch?v=Yvrts8us4OU)


