---
layout: post
title: "Covid Tracker"
description: ""
categories: envision
thumbnail: "covid-tracker.jpg"
gmeet: "https://meet.google.com/emu-gyyq-tmq"
---

## About

For people dealing with uncertainty regarding the pandemic situation in the near future, this website provides them with the current covid status, recovery scenario. Furthermore, it interpolates the data to give insights into the possible situation in the next few months.

This is basically a website that displays plots and analytics by scraping relevant data from government data portals to give an insight into the current state-wise pandemic situation and recovery status in India.

## Members

- [Samyak Sanjay Sand](https://github.com/samyaksand)
- [Shashank S K](https://github.com/shashanksk)
- [L Koushik](https://github.com/LKoushik2003)
- Nitin Singh
- Arjun Gowda A G

## Libraries/Softwares Used

| Libraries/Softwares | Description |
| --- | --- |
| Plotly |  Python Library that makes interactive, publication-quality **maps**.|
| Pygal | Python Library that creates highly **interactive graphs**. |
| Pandas | Python library used for performing **data analysis.** |
| Jinja | Jinja is a fast, expressive, extensible **templating engine for Python**. |
| Flask | It is a **micro web framework** for building web applications with Python. |

## How It Works

- The website is **dynamically hosted using flask**.
- Data was loaded and **extracted using the official API** from [Ministry of Health](https://www.mohfw.gov.in/) website as a .json file which is converted into a dictonary and used throught the program.
- The **display of maps** was made using **plotly library** using pandas to organise the data dictionary data.
- The India map is a **geojson file** that is updated with the data from the .json dictionary **arranged by panda data frame**, rendered, saved as an HTML file which is later embedded into the main HTML document.
- **Plots** were created by the **Pygal library** where a specific data was separated from the data sorted then rendered a scalable vector graphics (.svg) to preserve quality while zooming, later passed as an object element.
- The data in the table is **dynamically loaded using the web template language Jinja**, where only one column is created, and the rest is loaded by looping the rest of the rows.  

## Screenshots

### 1) The Main Page

![image](https://user-images.githubusercontent.com/62803746/119883313-7532ae80-bf40-11eb-9a7d-23ab07dc6929.png)

### 2) Live Covid Map Tracker

![image](https://user-images.githubusercontent.com/62803746/119883519-b1fea580-bf40-11eb-8968-03b0361a4b87.png)

### 3) Live COVID Cases Statistics

![image](https://user-images.githubusercontent.com/62803746/119883792-fd18b880-bf40-11eb-8575-a1fc0d5e9bea.png)

### 4) Live COVID STATEWISE STATUS

![image](https://user-images.githubusercontent.com/62803746/119883948-29ccd000-bf41-11eb-9991-387fc41af987.png)

### 5) About us

![image](https://user-images.githubusercontent.com/62803746/119886810-71089000-bf44-11eb-896c-e84642303237.png)

Github Link : [https://github.com/Janmansh/Covid-Tracker-IEEE](https://github.com/Janmansh/Covid-Tracker-IEEE)
