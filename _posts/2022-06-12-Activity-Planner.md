---
layout: post
title: "PLAN IT - A Daily Planner"
description: "A daily activity planner to keep track of tasks and to-do lists"
categories: envision
thumbnail: "thumbnail_activity-planner.png"
year: 2022
---

### Mentors

- Rakshith M
- Kavya Bhat
- Sathvik Hebbar

### Members

- Kesanam Ashinee
- Meghana Gupta
- Harsha Narayana P
- Chetan Maheshwari
- Subith Sathish

## Aim

To design an activity planner similar to Todoist, while learning basics of web development along the way.

## Introduction

In this busy and fast growing world, it is very important to plan your schedule for the whole day in advance. So with this motto we have come up with a basic daily activity planner to keep a track of all your day-to-day activities and help you reach your goals. This project was taken up with the aim of introducing web development, along with libraries and frameworks such as ReactJS and Django.

Django is a Python-based free web framework that is used to construct the backend of our web application. We have used ReactJS to build the user interface, and interact with the backend server.

## Implementation

### Database Design

The base schema is as follows:

![image 1](/virtual-expo/assets/img/envision/compsoc/AP-1.jpg)

### User Authentication

User authentication was implemented using inbuilt Django functions. The user object takes three parameters - username, email and password.

![image 2](/virtual-expo/assets/img/envision/compsoc/AP-2.png)

#### Views

- The homepage of our website displays the inbox, if the user is logged in. All pending tasks are displayed here. <br>
  ![image 3](/virtual-expo/assets/img/envision/compsoc/AP-3.png)

- A user can view the tasks that are due today or in the future, using the `Today` and `Upcoming` tabs. <br>
  <!-- ![image 4](/virtual-expo/assets/img/envision/compsoc/) <br> -->

  ![image 5](/virtual-expo/assets/img/envision/compsoc/AP-5.png)

- Users can add and edit tasks, or mark them as completed:
  <!-- ![image 6](/virtual-expo/assets/img/envision/compsoc/) <br>
  ![image 7](/virtual-expo/assets/img/envision/compsoc/) -->

- A user has the ability to group their tasks into task lists, to ease management. <br>
  <!-- ![image 8](/virtual-expo/assets/img/envision/compsoc/) -->

Axios, a HTTP client, is used to send the respective requests to the Django API endpoints, which then returns the relevant data.

## Future Work

This project could be improved further by adding the following features:

- Add the ability to easily move tasks between different lists.
- Sort tasks by priority, and generate reminders based on the same.

## Conclusion

In this project, we have created a useful activity planner for task management. The members have learnt the basics of both frontend and backend development using ReactJS and Django, and familiarized themselves with the usage of Git and GitHub.

## References

1. [CRUD operations in Django](https://towardsdatascience.com/build-a-django-crud-app-by-using-class-based-views-12bc69d36ab6)
2. [ReactJS Tutorial](https://reactjs.org/tutorial/tutorial.html)
