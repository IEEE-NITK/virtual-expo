---
layout: post
title: "CF_Analytics"
description: "CF_Analytics: Unleash the power of Codeforces API to effortlessly track your performance and gain valuable insights"
categories: envision
thumbnail: 2023-07-18-cf_analytics-thumbnail.jpg
year: 2023
---

### Mentors

- Harsha Narayana P
- Praveen Kumar P

### Members

- Tanvi Poddar
- Meher shireen
- Madhav Dhingra
- Khushi Choudhary



## Aim

CF Analytics is an online project designed to offer Codeforces users a platform for monitoring their performance, visualizing their progress, and comparing their achievements with other users. Its primary aim is to inspire users to maintain consistency, solve more problems, and derive motivation from the process.

## Introduction

Codeforces is a popular competitive programming platform that attracts a large number of users from around the world. CF Analytics is a web-based project dedicated to enhancing the Codeforces experience for users. It offers a comprehensive platform that allows users to monitor their performance, visualize progress, and compare achievements with peers. By providing valuable insights and fostering healthy competition, CF Analytics aims to inspire users to maintain consistency, solve more problems, and derive motivation from their programming journey.

With CF Analytics, users gain the ability to track their progress over time and identify strengths and weaknesses through advanced data visualization techniques. The platform encourages friendly competition by enabling users to benchmark their achievements against others, promoting continuous improvement and growth.


## Implementation
The user enters his codeforces handle name. Using the handle name, his/her codeforces rating and other statistics are displayed using chart.js javascript library. The user info is fetched through codeforces API.

The features of the website are:
Display the username
Plot verdicts, languages used, tags, levels and problem ratings of the user.
Tabulate the statistics of the user like number of questions solved, number of questions tried, number of contests in which the user participated, best rank, worst rank etc.
Display the heatmap of the user.

In addition to the above features, we display the statistics of the problems solved in the form of stars.

Total points = 
∑((Number of questions solved of a particular level in a particular div)*(Point value for that level of question in that div)) 
For example
A user solves 
- 5 questions of level A in div 3 
- 4 questions of level B in div 3 
- 3 questions of level C in div 3 
- 3 questions of level A in div 2 
- 2 questions of level B in div 2 
- 1 question of level A in div 1 
Total points = (5*10)+(4*20)+(3*30)+(3*20)+(2*40)+(1*30) = 390 
![Distribution of points per each category of problem](/virtual-expo/assets/img/envision/compsoc/cf_analytics/table_cf.jpg)


The following logic is used to decide the number of stars for a user.

![cut off points for number of stars](/virtual-expo/assets/img/envision/compsoc/cf_analytics/stars_table_cf.jpg)

Below are images of the statistics displayed in the home page

![Verdicts and Languages of the user](/virtual-expo/assets/img/envision/compsoc/cf_analytics/tags.jpg)

![Tags of user](/virtual-expo/assets/img/envision/compsoc/cf_analytics/tags.jpg)

![Problem ratings of user](/virtual-expo/assets/img/envision/compsoc/cf_analytics/problem_ratings.jpg)
![Levels of user](/virtual-expo/assets/img/envision/compsoc/cf_analytics/levels.jpg)

## Future Work
We aim to complete the compare section and apply machine learning techniques to find the optimal practice strategy for a codeforces user.

## Conclusion

In conclusion, CF_Analytics is a powerful web-based project that utilizes the Codeforces API to enable users to track their performance, visualize progress, and compare achievements. By entering their Codeforces handle, users gain valuable insights like ratings, verdicts, languages, tags, levels, and problem ratings. The user-friendly interface, powered by chart.js, presents information effectively. Tabulated statistics include questions solved, attempts, contest participation, and best/worst ranks. The heatmap provides an intuitive overview of activity. Unique features include assigning points based on problem difficulty and awarding stars using predetermined cutoffs. CF_Analytics is a valuable tool for Codeforces users to gain insights, improve, and make data-driven decisions in their competitive programming journey.


## References

1. Chart.js, [Link](https://youtube.com/playlist?list=PLBG4BJt8bo9rrPibhKLbpe-z1Dkk2VJjO)
2. HTML, [Link](https://www.w3schools.com/html/default.asp)
3. CSS, [Link](https://www.w3schools.com/css/default.asp)
4. JS, [Link](https://www.w3schools.com/js/default.asp)
