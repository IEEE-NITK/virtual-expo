---
layout: post
title: "THE GALACTIC WIDE WEB"
description: "’Space Invaders’, a fun space themed game where the player’s goal is to shoot the asteroids while avoiding the planets"
categories: envision
thumbnail: "thumbnail_galactic-wide-web.jpg"
year: 2022
---

### Mentors

- Advaith Prasad Curpod
- Akheel Muhammed
- Swetha Mary Thomas

### Members

- Alex Moby Philip
- Bhavya Jain
- Gautum Raj
- Kushangi Sharma
- Pulkit Gupta
- Vignaraj Pai

## Aim

To design a space themed game ‘Space Invaders’ using HTML, JavaScript and Phaser3, a 2D game framework.

## Introduction and Overview

Game Development and Web Design are certain trajectories of coding that tend to get highlighted due to how unique they are. While people tend to equate game development to high graphics experiences like Horizon, Farcry etc, they tend to forget about the simpler games that we see on the web. All of us must have played space games like the asteroid dodging game, space invaders, etc., available online, but just think of how much more exciting it would be to create a game like this.

In the ‘Space Invaders’ game that we have developed, the player’s objective is to navigate the spaceship using the arrow keys, destroy the asteroids and avoid the floating planets. The asteroids can be destroyed by firing bullets using the spacebar key, which will increase the player’s score. The bullet firing will halt after some time and the player has to wait for a while before he/she is able to fire again. Also, after each life is lost, the number of planets on the screen increases. We have used HTML, CSS, and JavaScript to implement this game.

## Technologies used

1. HTML - A standard markup language used for structuring and creating web pages.
2. CSS - A style sheet language used for modifying the presentation and design of a webpage.
3. Javascript - It is a scripting/programming language that is often used for more complex operations and functions in web design. It can help create dynamically updated content.
4. Phaser - It is a 2D game framework used for making HTML5 games that can be used for games in browsers, mobile and desktop. It is a framework that is growing popular that is built in Javascript and is written in the same. In this particular project, we use the latest version ie: Phaser3.

## Game Implementation

ew Jekyll site using the command below.

The game has a total of 3 visible scenes : title scene, game scene and end game scene

### titleScene

This is the first scene that the user sees. The scene consists of the game name, a space background and a start button, which on clicking would start the game.

![image 1](/virtual-expo/assets/img/envision/compsoc/GWW-1.jpg)

### gameScene

This scene is the heart of the game and is where the gameplay operates.

The scene consists of :-

i) The player sprite, which is a spaceship

ii) A moving space background

iii) The asteroids to be destroyed (n=30)

iv) A text that shows number of lives left (n=5)

v) A text that shows number of points gained

vi) The planet(s) to be destroyed (n<=5)

Every time the player sprite crashes into a planet, a life is lost and an extra planet is generated. The objective of the game is to shoot all the asteroids, avoiding the planets. However, if the player loses all the 5 lives before this is achieved, the game is over.

While this is the basic idea of the scene, there are additional features that we have implemented:

- When the player is down to the last life, the text for number of lives turns red as a warning for the player.
- Sound effects have been added for when the player respawns, when the player shoots a bullet and when an explosion takes place.
- Instead of unlimited bullet fire from the player, there is a limit on the number of bullets that can be fired at a stretch, after which the player has to wait until the bullets have been reloaded.

When the game is over, the scene blacks out and switches to the end scene

![image 2](/virtual-expo/assets/img/envision/compsoc/GWW-2.jpg)

### endScene

This is the final scene that the user sees. This scene consists of the moving space background, a game over text, the player’s final score and two buttons:- (i) a replay button which on clicking would take the user back to a fresh start of the game, and (ii) a home button which on clicking would take the user to the title scene.

![image 3](/virtual-expo/assets/img/envision/compsoc/GWW-3.jpg)

### Controls

Left arrow key - Move player left

Right arrow key - Move player right

Up arrow key - Move player up

Down arrow key - Move player down

Space bar - Shoot bullet

## Future Ventures

Like any project, this project can also be developed into more interesting versions with some great features that could be added.

These include:-

i) Background music specific to each scene.

ii) A pause button to pause the game while playing

iii) Game levels of varying difficulties (Easy, Medium and Hard)

iv) Backend programming to store user scores and establish a basic scoreboard using Django.

v) A help scene to go over how to play the game

## Conclusion

In this project, we have developed an arcade style space themed game using HTML, Javascript and Phaser3. During this project, each member has learned basic concepts of web design and game development using the above technologies and they also familiarize themselves with the use of version control systems like Git/Github.

## References

1. W3Schools, [Link](https://www.w3schools.com/)
2. StackOverflow, [Link](https://stackoverflow.com/)
3. Phaser3 Examples, [Link](https://phaser.io/examples)
4. Getting Started With Phaser, [Link](https://www.youtube.com/watch?v=UMNW5X2zF5w&list=PLBt_NhU615eRb-TJe5xx-f2Nx1UqJggqO&index=2)
