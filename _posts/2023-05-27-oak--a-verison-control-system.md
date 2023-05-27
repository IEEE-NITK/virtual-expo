---
gmeet: "https://meet.google.com/ecw-hook-evv"
layout: post
title: "OAK: A Verison Control System"
description: "OAK, a Python-based version control system, useful for understanding basic git internals. Our aim is to make a simpler version of Git, one that focuses on local files and repositories."
categories: envision
thumbnail: 2023-05-27-oak--a-verison-control-system-thumbnail.jpg
year: 2023
---

### Mentors

- Calvin Fernandes
- Tejashree Chaudhari


### Members

- Akshat Mishra
- Ashutosh Shukla
- Rajmani Pandey
- Upasana Nayak


## Introduction

A version control system (VCS) is a tool that helps developers track and manage changes to their code over time, allowing them to identify and fix mistakes quickly. A VCS becomes extremely important as the code grows in size and complexity. It is essential in projects which involve frequent updates with multiple contributors, as it helps to prevent conflicts and improve collaboration. By keeping a record of all changes, we can revert to previous versions if something goes wrong.
Our VCS is similar to git, a widely used open-source distributed version control system that helps manage projects. Git is a tool that lets developers manage different versions and save their code. Git is designed with performance, security, and flexibility in mind. 

## Project Description

Oak is a Python-based version control system, useful for understanding basic git internals. Our aim is to make a simpler version of Git, one that focuses on local files and repositories. The commands we have defined are similar to Git's in terms of functionality.

Oak's internal data representation is inspired from Git, but differs in 3 main ways:
1. Git compresses file contents stored before further processing, while Oak doesn't. This is to make our project more approachable as the contents inside the hidden .oak folder are in a readable form.
2. Git stores metadata such as file creation\modification time, Author name, user ID, hardware device ID, file access permissions, while Oak doesn't, as Oak was meant to handle local files and repositories, hence the lack of need for storing user info or permissions.
3. Git stores and manipulates data at the binary bite level, while Oak stores and manipulates data in the usual ASCII form.

## Deliverables

We have implemented the following functions which can be called from the command line:

- Init: This command creates a hidden .oak folder to store all versions of the files, hence initiating the repository, allowing other oak functions to work.
- Add: This command adds all files to an index to be committed.
- Status: This command lists the status of all files in the repository. The status of a file can be one of six: Modified, Untracked, New, Added, Deleted, and Unmodified
- Commit: This command saves all files and folders in their current condition as objects, with a relevant comment and the time of committing. All commits in a repository except the first one point to their parent commit.
- Log: This command displays the list of a few commits to the user. We have also implemented short log which is similar to log but displays information concisely.
- Restore: This command can be used if the user wants to get back the contents of a file or a directory corresponding to their contents when a particular commit was made.


## Libraries Used

- os module: The use of this module is to implement miscellaneous operating system functionality. We mainly used the os.getcwd() method, to get the current working directly at any time, and the os.chdir() method, to change the working directory as needed.
- hashlib module: The use of this module is to implement various secure hashing algorithms. We used the hashlib.sha1() method from this module, which implements the sha1 hashing algorithm.
datetime module: The use of this module is to manipulate dates and times. We used the datetime.- - -
- datetime.now() method from this module, which finds the current time in your local timezone.
- colorama module: The use of this module is to change displayed text to various colors, to  beautify it.
- shutil: It provides a set of high-level file operations for efficiently copying, moving, and removing files and directories. We have used it to iteratively delete directories in our functions.



## Desing and Implementation

We made our project similar to git by encoding our files/objects using the SHA-1 (secure hash algorithm-1) hash function which takes an input and converts it into a 160-bit hash value which we render as 40 hexadecimal digits i.e, myfile.txt may translate to something like “addf120b430021c36c232c99ef8d926aea2acd6b”, here the first two letters will be the object file name “ad”, and in this folder will be the text file named as the remaining 38 letters i.e.,”df120b430021c36c232c99ef8d926aea2acd6b” with all the information about the object. All the information about the objects and INDEX file are stored in the hidden folder .oak initialized when the command init is given. 

There are 4 types of objects in git: 
Blob
Tree
Commit
Tag
Out of these, the first 3 are essential building blocks of a VCS like git, hence we will be focusing on them. Tag object can be used for convenience.

Blob - It translates to a Binary Large object which roughly stores all the data in a file in binary form. It does not store the metadata, but is only a collection of pure data contents of the file. We convert pure files to blobs using the create_blob function that works in the following manner:
Fetch the file from the working directory
Convert the contents into a sha-1 hash 
Store it as a blob in the objects folder inside the .oak folder

![blob](/virtual-expo/assets/img/envision/compsoc/oak--a-verison-control-system/blob.png)

Tree - It is a data structure to connect the various object in a synchronised and organised way, it creates a hierarchy between the oak files and lets us efficiently access our work. Tree works in the following way:
It will search the objects folder for the existing objects 
It will create a record of the objects in another text file by storing the details of the objects present
The text file is encoded as a sha-1 hash and stored as an object in .oak/objects folder

A tree can be said to represent a directory’s state. Just as a directory is made up of files and other directories, a tree contains hash IDs of blobs and other trees (repersenting subfolders).

![tree](/virtual-expo/assets/img/envision/compsoc/oak--a-verison-control-system/tree.png)

Commit - It is a snapshot of the work which has been done till now, it points to the tree and along with that also has the information about the date and time and a comment with additional information about the reason for committing.

Commit works in the following way:
It retirieves necessary information i.e., the updated tree hash, the parent commit details, the date and time and the comment
It then stores it all into a text file
The text file is encoded as a sha-1 hash and stored as an object in .oak/objects folder

![commit](/virtual-expo/assets/img/envision/compsoc/oak--a-verison-control-system/commit.png)

![commit](/virtual-expo/assets/img/envision/compsoc/oak--a-verison-control-system/structure.png)

Index - The index file is stored in .oak folder as well containing information about the tracked/added files. It contains information about the files that were added to the staging area by the user after the previous commit, files removed, or files untouched by the user after the last commit. The commit command uses the index file to get necessary content for the commit object.

We chose to structure our objects and the index as follows:
```
    Blob structure:
    Line1.................."blob"
    Line2 onwards...content

    Tree structure:
    Line1…….........."tree"
    Line2 onwards...<object type>…..tab…..<name>…..tab…..<hash>

    Commit structure:
    Line1...........”commit”
    Line2...........<hash of main dir tree>
    Line3...........<hash of parent commit>
    Line4...........<timestamp>
    Line5...........<comment>

    Index structure:
    Line1 onwards...<relative file path>...tab...<hash>
```
By storing and retrieving information from the objects and the index file, we can save ‘snapshots’ of our directory, track changes across time and restore any desired components.

## Images

![img1](/virtual-expo/assets/img/envision/compsoc/oak--a-verison-control-system/img1.png)

![img2](/virtual-expo/assets/img/envision/compsoc/oak--a-verison-control-system/img2.png)

## Future Work

We plan to expand the functionality of Oak by implementing the following commands in the future:
- diff.
- branching and merging.
- oak-ignore.

## References

FreeCodeCamp blog on 'A Visual Guide to Git Internals - Objects, Branches, and How to Create a Repo From Scratch' by Omer Rosenbaum.
Git Internals by Scott Chacon.
Git from the bottom up by John Wiegley.
Building Git by James Coglan (a detailed study).



## References

1. FreeCodeCamp blog on ['A Visual Guide to Git Internals - Objects, Branches, and How to Create a Repo From Scratch'](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/#:~:text=In%20git%20%2C%20the%20contents%20of,creation%20time%20remains%20the%20same) by Omer Rosenbaum.
2. [Git Internals](https://github.com/pluralsight/git-internals-pdf) by Scott Chacon.
3. [Git from the bottom up](https://jwiegley.github.io/git-from-the-bottom-up/) by John Wiegley.
4. Building Git by James Coglan (a detailed study).

