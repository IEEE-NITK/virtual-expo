---
layout: post
title: "Disk Space Renter"
description: "Platform for decentralized file sharing"
categories: compsoc
thumbnail: "diskSpaceRenter.jpg"
year: 2022
gmeet: "https://meet.google.com/tek-oiyb-nbc"
---

## Mentors

- Ikjot Dhody
- Chaitanya Shyam

## Members

- Tejas Sankpal
- Advaith Prasad Curpod
- Anurag Kumar

## Aim

- Create a decentralized file sharing platform where users (disk space requesters & disk space providers) come together to leverage the benefits of blockchain & trustless decentralization.
- Build an incentive layer on top of IPFS enabling disk space providers to agree to store files of disk space requesters in return for a small fee.
- Create a CLI application to implement the same. 


## Introduction

Disk space renter is an application bridging the gap between a decentralized file sharing protocol and a users requirement for a cloud service to store his files remotely, by incentivising the process of file storage and retrieval. The user (requester) who wants to use the service will have to pay (in ETH) to all the providers who are hosting his content. The amount is directly proportional to the duration of storage and file size.

## Design and Tech Stack

The codebase has 3 parts, CLI Frontend, Intermediate connector connecting Python, IPFS & Ethereum, and Backend which includes the Ethereum Smart Contract written in Solidity. Smart contracts cover the business logic of the application, providing functionalities like space request for the requesters, a list of providers providing for each requester etc.
The Web3 library in python is used to connect the front end code and the smart contract. Smart contracts expose their public address and ABI (Abstract Binary Interface) which acts as an interface/API for the front end code.
IPFS (Interplanetary File Sharing), a content based file sharing protocol works under the hood when a requester requests for space and a provider approves the request. The protocol takes care of secure one-way hashing, easy retrieval of files using the CID.
The project is built on Truffle suite which provides a development environment and a personal blockchain to test and deploy contracts in an EVM like environment.

## Dataflow

All the users are divided into requesters and providers. Every new user can choose to be either a requester or provider. Once a user is registered as a provider or a requester , he/she is provided with a unique account address. All the account addresses are stored in separate arrays for each kind of user. 
Requester’s request i.e., memory requirement, duplications , duration and CID are stored in a separate structure that is mapped with their address similarly, the provider and the space he can rent out are stored in a mapping.
Two separate mappings are maintained to store the provider's address and the requesters he/she is serving and another mapping for storing the list of providers a requester has. 

![List of Public & Private Keys](/virtual-expo/assets/img/compsoc/public-private-keys.jpeg)

![Initialise Request](/virtual-expo/assets/img/compsoc/initialise-request.jpeg)

![Requester Uploads the file](/virtual-expo/assets/img/compsoc/file-upload-by-requester.jpeg)




## Conclusion

Currently our implementation is a very basic prototype and only a CLI application. We need to first set up the website and demonstrate all the features. However, making it scalable such that it can be used by millions of users at the same time would be an interesting challenge. Some improvements that can be made are encrypting the requesters files, a feature to upload multiple files at the same time and have only one CID for all of them etc.



## References 
1. [Base Paper](https://csu-csus.esploro.exlibrisgroup.com/esploro/outputs/graduate/Distributed-resource-sharing-using-the-blockchain/99257831182501671)
2. [Solidity Full Course Playlist](https://youtube.com/playlist?list=PLgPmWS2dQHW9u6IXZq5t5GMQTpW7JL33i)
3. [IPFS File Uploads With Ethereum Smart Contracts](https://youtu.be/SkMH0WeRYtg)
4. [How to Build Ethereum Dapp With IPFS](https://youtu.be/pTZVoqBUjvI)
5. [IPFS Documentation](https://docs.ipfs.io/)
