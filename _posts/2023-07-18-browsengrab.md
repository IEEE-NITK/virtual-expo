---
layout: post
title: "BrowseNGrab"
description: "’Browser Bookmarks Aggregator and Auto-Login Script"
categories: envision
thumbnail: "browsengrab_2023_envision_thumbnail.png"
year: 2023
---
### Mentors

- Mohammed Arfath
- Vignaraj

### Members

- Abhay Lejith
- Nandan Ramesh
- Shashank Gupta
- Ziyan Abdulla

## Aim

The aim of the project is to create a CLI utility/tool  with two functions . One is to consolidate bookmarks from all browsers into a markdown file and the other is to automate the login into NITK net.The utility is provided as a Debian package

## Introduction and Overview

Bookmarks are an essential tool for anyone who spends a significant amount of time browsing the internet. They allow users to quickly and easily access frequently visited websites and pages, saving time and effort. However, over time, as users switch between different browsers, their bookmarks can become scattered and disorganized. Hence, the first functionality of our utility  is aimed at providing the user all their bookmarks at their fingertips by consolidating them into one file. Moreover a user can sort the bookmarks based on the arguments provided with the command  

Further, logging into a work or college WiFi network every single day upon entering the campus is a huge hassle, eating away precious time for a monotonous task. To counteract this, the second functionality  of our utility  equips the user with a tool that not only saves time, but also permits the user to get off to a fresh start to the day rather than having to log into the network everyday.



## Technologies used

1. Bash
2. Python
3. SQLite3

## Implementation:
The [code](https://github.com/Vignaraj-pai/BrowseNGrab) was written in bash. Information about the bookmarks is stored in json files under the corresponding browser directories.The required information was accessed from the json file using <b>jq</b> function.The user can also specify a word as a cmd line argument so that only the links with that word are stored. The links are then stored in a markdown file.
For the auto login function ,when it is run for the first time ,the user is prompted to enter their login details which are then stored in a text file for future use. If login fails then the user is asked to re-enter the details. Wifi status is checked using <b> nmcli</b> and is turned on if it isn't.The login is done using a post request from curl command.  

## Usage:

```
    SYNOPSIS
    bng [-b | -ch | -br | -cr | -e | -o | -f | -n [arguments]]

    Options:
     -h, --help                Show help
     -v, --version             Show version
     -b, --bookmark            Collect all bookmarks from all browsers on the system
     -ch, --chrome             Collect all bookmarks from Chrome browser
     -br, --brave              Collect all bookmarks from Brave browser
     -cr, --chromium           Collect all bookmarks from Chromium browser
     -e, --edge                Collect all bookmarks from Microsoft Edge browser
     -o, --opera               Collect all bookmarks from Opera browser
     -f, --firefox             Collect all bookmarks from Firefox browser
     -n, --nitk 			      login to NITK-NET
     -n -s, --nitk --status          Display NITK-NET login status
     -n -lo, --nitk --logout          Logout from NITK-NET
     -n -c, --nitk --change          Change NITK-NET credentials
```

| ![image 1](/virtual-expo/assets/img/envision/compsoc/browsengrab/bng_b.png) |
|:--:|
| <b>Using the utility from the Terminal</b>|


The bookmarks are stored in 2 formats : bookmarks.md and an exportable bookmarks.html file.
The html file can be imported into a browser of choice.

| ![image 2](/virtual-expo/assets/img/envision/compsoc/browsengrab/bookmarks_md.png) |
|:--:|
| <b>Bookmarks.md file</b>|

| ![image 2](/virtual-expo/assets/img/envision/compsoc/browsengrab/bookmarks_html.png) |
|:--:|
| <b>Bookmarks.html file</b>|


## Conclusion

The members understood the concept and became well-versed with shell scripting and bash, which can be used to automate many tasks. Two such tasks formed the main core of this project, namely centralizing bookmarks and auto-login into a network. The latter is a life-saver that saves heaps of time wasted logging into your work network while the former can be used to get an overview of how the user has managed their bookmarks across different browsers.


## References

1.[W3Schools](https://www.w3schools.com/)

2.[linuxconfig](https://linuxconfig.org/)

3.[stackoverflow](https://stackoverflow.com)

4.[earthly](https://earthly.dev/blog/jq-select/)

5.[makeuseof](https://www.makeuseof.com/connect-to-wifi-with-nmcli/)
