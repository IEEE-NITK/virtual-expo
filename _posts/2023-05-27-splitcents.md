---
layout: post
title: "SPLITCENTS"
description: "Splitcents: A web app for effortless management of shared expenses among groups, clubs, and teams."
categories: envision
thumbnail: 2023-05-27-splitcents-filename.jpg
year: 2023
---

### Project Guide

-

### Mentors

- Harshit
- Abhishek

### Members

- Hariharan
- Amruth
- Gouri
- Farhan

## Acknowledgements

## Aim

This project aims to build a web app Splitcents which allows for easy management of shared expenditure among friend groups, clubs, and teams. It provides a way to log the payments made on behalf of the group, and settlements made by its members. Group members can see all the transactions made and their share in them, as well as keep track of how much they owe to other members. The app also implements an algorithm to minimise the number of transactions required to settle all balances, making it easier to pay everyone back.

## Introduction

Sharing expenditure among friends and colleagues is becoming increasingly common in today’s world, especially with the increase in online and digital payments. Hence, it is also becoming harder to keep track of all these payments and dues to everyone across multiple groups and friends. By developing Splitcents, it allows everyone to be able to easily remember and pay all the people they know, and also log all the transactions made. This also helps with keeping track of the expenditure for events and other plans, and making an account of where money was spent for them.

![image 1](/virtual-expo/assets/img/envision/compsoc/splitcents/img1.jpg)

## TECHNOLOGY USED

React
React is a frontend JavaScript framework used for creating reactive user experiences. It allows us to bind the data in JavaScript to reactive components which represent the UI. It Simplifies the process of developing data-based web applications with interactive user interfaces.

Tailwind CSS
Tailwind is a CSS framework which provides a wide range of utility classes which allows us the flexibility and convenience to easily style a web app. It synergises well with React and eliminates the need for external CSS files and unique class names in HTML.

Firebase Firestore
Firestore is a document-based cloud database which can be used in frontend applications using a powerful JavaScript SDK. It is the technology we use to store and display data, as well as keep track of groups and expenses.

Firebase Authentication
Firebase Auth facilitates login and signup using both email and through Google. It helps keep track of registered users and their login status, and authorize data-fetches from the database. It hence allows us to secure the data in the database such that only the owner of the data can access it.

## Features

### Login

A user navigates to an application and is presented with a login page as a way to gain access to the application.Here the user can login via email address and password or through google account.If the login is successful the user is redirected to the groups page, if not successful an error message is shown.

### Sign Up

A user who doesn't have an account can go to the signup page where he/she can create a new account by entering the username, email address and giving the new password.

### Groups

In this page, the multiple groups which the user is part of is displayed with the net amount of money which the user is owed or owes in that group.
There is also a button for creating new groups.The user can navigate to the specific group page by clicking on the group.

### Create Groups

Here the user is able to enter the name of the new group and also select other users from their friends and create a new group.

### Specific Group

The information regarding the previous Expenses added to this group and the transactions made in that group is displayed ordered by their dates.The list of members of that group which the user owes and how much is displayed with a pay button.There are options for adding an expense and viewing group members.

### Transaction

This is a modal which pops up with the information about the payee with the amount which is owed.On clicking the pay button the user is redirected to the specific page and this information is updated in the database.

### Add Expense

This is a modal with input boxes for description and amount.The default payer is the user but there is an option for changing the payer.The user can select the members from the group members and then submit the expense to the group.This updates the information regarding how much group members owe each other.

### Group Members

This page contains the list of members in the group.It also has an option for adding new members to the group from the users friends list.

### Friends

This page contains the list of friends of the user.It also has the list of pending friend requests sent to the user and also sent by the user.It has a textbox for searching for the users email-id and then sending a new friend request to that person.

![login](/virtual-expo/assets/img/envision/compsoc/splitcents/login.jpeg)

![signup](/virtual-expo/assets/img/envision/compsoc/splitcents/signup.jpeg)

![groups](/virtual-expo/assets/img/envision/compsoc/splitcents/groups.jpeg)

![add_expense](/virtual-expo/assets/img/envision/compsoc/splitcents/new_expense.jpeg)

## Future Work

### Minimum Transaction Algorithm

Optimise the settling of dues by group members is a very useful feature which removes redundant transactions and saves the hassle of multiple payments. This can be achieved using a sophisticated algorithm which minimises the number of transactions that have to be made to settle the dues.

### PWA and Offline Support

Converting a web app into a PWA involves making the website mobile-friendly and responsive, as well as adding offline support. This makes the web app installable on mobile devices, just like native mobile apps. This can significantly improve the user experience, as most of the users will use such utility apps on phones itself.

### Notification Support

The app can send notifications to users when expenses are added, transactions are made, or even when friend requests are sent or accepted. This will allow the user to stay up-to-date with the activities of their groups.

### Integration with Payment Platforms

The app can integrate payment providers such as PayTM, GooglePay or PhonePe, making it easier for the users to settle their dues, and also documenting their transactions more efficiently.

## Conclusion

By offering a user-friendly interface and leveraging modern web technologies, Splitcents aims to streamline the process of managing shared expenses, making it convenient for users to track, record, and settle their financial obligations within groups.

## References

1. https://www.w3schools.com/
2. https://mongoosejs.com/docs/
3. https://tailwindcss.com/docs
4. https://www.freecodecamp.org/
5. https://reactjs.org/docs/getting-started.html
6. https://workat.tech/machine-coding/editorial/how-to-design-splitwise-machine-coding-ayvnfo1tfst6
