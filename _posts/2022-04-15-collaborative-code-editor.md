---
layout: post
title: "Collaborative Code Editor With Audio Rooms"
description: "A website that allows you to collaboratively code"
categories: compsoc
thumbnail: "Collaborative_Code_Editor.jpg"
year: 2022
gmeet: "https://meet.google.com/bxf-mdwr-opd"
---

### Mentors

- Janmansh Agarwal
- Srujan Bharadwaj
- Aryaman

### Members

- Tejaswi Hegde
- Radhika Chhabra

## Aim

We aim to:

- create a website with a code editor
- users can create a room and others are able to join the room
- voice and video and text chat functions
- the code editor is synced across the users in a room

## Introduction

Collaborative code editors are very useful in the software industry. They can be used for
pair programming, debugging, interviews, etc.

Currently, we can find a lot of collaborative code editors online. However, there aren’t
many code editors which have a built-in audio feature. In this project, we aim to build a live
code editor and have a feature of audio rooms within the editor. Hence, there won’t be a
need to use a separate tool or device for audio communication with a peer.

## Frontend

The frontend is what users interact with. This is designed using ReactJS. React is a JavaScript library for building user interfaces. React can be used as a base in the development of single-page, mobile, or server-rendered applications with frameworks like Next.js. However, React is only concerned with state management and rendering that state to the DOM, so creating React applications usually requires the use of additional libraries for routing, as well as certain client-side functionality. React code is made of entities called components. These components are reusable and must be formed in the SRC folder following the Pascal Case as its naming conversion. Components can be rendered to a particular element in the DOM using the React DOM library. When rendering a component, one can pass the values between components through "props".

## WebRTC

WebRTC (Web Real-Time Communication) is a free and open-source project providing web browsers and mobile applications with real-time communication (RTC) via application programming interfaces (APIs). It allows audio and video communication to work inside web pages by allowing direct peer-to-peer communication, eliminating the need to install plugins or download native apps. A connection is established through a discovery and negotiation process called signaling. Establishing a WebRTC connection between two devices requires the use of a signaling server to resolve how to connect them over the internet. A signaling server's job is to serve as an intermediary to let two peers find and establish a connection while minimizing exposure of potentially private information as much as possible.

## Backend Server

For handling of adding users to different rooms and initiating the first
connection we have used golang to build a server. Go is a statically typed, compiled programming language designed. Go is syntactically similar to C, but with memory safety, garbage collection, structural typing, and CSP-style concurrency. The Go language is small, compiles really fast, and as a result it lets your mind focus on the actual problem and less on the tool you are using to solve it.
We have used the gin framework. Gin is a web framework written in Go (Golang). It features a martini-like API with performance that is up to 40 times faster thanks to httprouter. Gin simplifies many coding tasks associated with building web applications, including web services. Gin helps to route requests, retrieve request details, and marshal JSON for responses.

## CRDT

Conflict-free replicated data type (CRDT) is a data structure which can be replicated across multiple computers in a network, where the replicas can be updated independently and concurrently without coordination between the replicas, and where it is always mathematically possible to resolve inconsistencies that might come up. We have used CRDT to sync the code across all users in a room.Conflict-free Replicated Data Types (CRDTs) are used in systems with optimistic replication, where they take care of conflict resolution. CRDTs ensure that, no matter what data modifications are made on different replicas, the data can always be merged into a consistent state. This merge is performed automatically by the CRDT, without requiring any special conflict resolution code or user intervention.

## Conclusion

We are able to create a website with a code editor. Many people can work together on code at the same time. A user can create a new room or join the existing one. The backend is written purely in golang and the gin web framework is used. Apart from code, users are able to interact with each other over chat, audio and video call. We have a webrtc connection among users joining the room. The code editor is synced across all the users in a room. This is done using CRDT. So, this webapp will be helpful for a team project or collaborative coding.

![image 1](/virtual-expo/assets/img/compsoc/collaborative_img_1.jpg)

![image 2](/virtual-expo/assets/img/compsoc/collaborative_img_2.jpg)

![image 3](/virtual-expo/assets/img/compsoc/collaborative_img_3.jpg)

## References

1. Golang - [Link](https://golang.org/)
2. Codemirror - [Link](https://codemirror.net/)
3. Monaco - [Link](https://microsoft.github.io/monaco-editor/)
4. WebRTC/WebSockets - [Link](https://webrtc.org/)
5. GitHub - [Link](https://github.com/IEEE-NITK/codeshare)
6. CRDT - [Link](https://crdt.tech/)
7. React - [Link](https://reactjs.org/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTY5ODczNDI2XX0=
-->

