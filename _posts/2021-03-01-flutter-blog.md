---
 layout: post
 title: "Blog Application with Flutter"
 description: "This project incorporates the two most popular technologies for App Development today, i.e. the famous Google UI toolkit - Flutter and Google powered Cloud service provider Firebase"
 categories: envision
 thumbnail: "flutter.png"
 year: 2021
---

## Mentors

- Ikjot Singh Dhody
- Sravani Katasani

## Members

- Shashank SM
- Fathima
- Khushi Rathod
- Hritik Mehta

## Introduction

Apps have now become any integral part of all our lives and we have a wide array of apps ranging from entertainment and education. The objective of this project is to make a blog app which would contain blogs on innumerable topics with many features making this app easy to use and one stop for gaining knowledge.

## Overview

- **DART**, an Object-Oriented Programming Language and the **FLUTTER** UI toolkit was used.
- **FIREBASE** DATABASE is initialized inside the application for storing all the data in the backend.
- **HIVE** was used to store data locally.
- Splash Screen includes a GIF.
- The home page consists of all the blogs that are currently present on the backend.
- Clicking on the desired blog on the All Blogs Page (initial route) navigates to author&#39;s blog page.
- **SPECIAL FEATURE** : User can add to favorites (by clicking on a heart icon) and save the desired blog locally on his/her phone.

## Work Flow

The Blog app is built using Flutter. It has a total of 6 screens (Splash Screen, Home, Favourites, Single Blog page, 2 x Loading screens).

### Home Screen

<img alt="img" src = "https://raw.githubusercontent.com/ikjot-2605/blog-app/master/screenshots/all_blogs_page.jpeg?token=ANF347M322Y4NHZAATLUWL3AXPNJO" height = "300">
<img alt="img" src = "https://raw.githubusercontent.com/ikjot-2605/blog-app/master/screenshots/add_to_favorites.jpeg?token=ANF347OGS4LZ6UOVEB4XSTTAXPOBO" height = "300">

- The home screen contains all the blogs added to firebase and is presented in List view.
- Every List element contains a Blog name, Preview and an Icon, which can be used to add the blog to the favourites list and a delete icon to delete that app.
- We have used a Gradient colour for the background
- We have also implemented a pop-up feature that would alert the user if he has added any blog to the Favourite.
- All the blogs are imported from the firebase database.
- The Home screen also contains a drop-down menu to navigate between the Home screen and Favourite Screen

### Favourite Screen

<img alt="img" src = "https://raw.githubusercontent.com/ikjot-2605/blog-app/master/screenshots/favorites_page.jpeg?token=ANF347PQDJ3WHNIK3BWRJN3AXPOD6" height = "300">
<img alt="img" src = "https://raw.githubusercontent.com/ikjot-2605/blog-app/master/screenshots/remove_from_favorites_page.jpeg?token=ANF347P5QJWDOMPE7S7E6KLAXPOEW" height = "300">

- This screen shows all the Blogs which have been added to the favourites list by the user.
- When a user adds a blog to the favourite list, that blog gets stored locally (implemented using Hive), and then the files are derived from this local storage to be displayed on the favourite screen.
- The favourite page also has the same architecture and design as the Home Screen.

### Loading Screens

- Two loading screens are present in this app.
- One Loading screen appears when the app is started and containing a GIF
- The second loading Screen appears when we transit from the home screen to the favourite screen, containing a loading bar.

### Firebase &amp; Hive

<img alt="img" src = "https://raw.githubusercontent.com/ikjot-2605/blog-app/master/screenshots/firebase.png?token=ANF347MSPICQFWU3D3CQPC3AXPONI" height = "250">

- The app uses Firebase to store all the blogs and directly imports blogs from its database which is then displayed in the home screen.
- Hive was used to store some a set of blogs locally which are selected from user and then this local database is used by favorite screen to display its blog.

### Below, is an overview of the running of the application.

<img alt="img" src = "https://raw.githubusercontent.com/ikjot-2605/blog-app/master/screenshots/runthrough_final.gif?token=ANF347KGQH2VJIHHHEUTNETAXPPJQ" height = "400">

## Conclusion

In this project, we have developed an application that lets us upload blogs in an HTML file format onto the backend, and then view them via a Flutter client in the front-end. We use local storage to store the favorites and view them at the offline convenience.
