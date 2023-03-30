---
layout: post
title: "Concerto Web Editor"
description: "An Open Source Web Editor built in React to Edit and Visualize Concerto data models."
categories: compsoc
thumbnail: "2023_concerto_web_editor_thumbnail.png"
year: 2023
gmeet: "https://meet.google.com/naa-zdom-jpp"
---

### Mentors
- Akheel Muhammed
- Mohammed Ayman Nawaz

### Members
- Deepak Varma


<!-- 
## Acknowledgements
NA -->


## Aim
To develop a GUI interface that will let non technical users design contract data in the form of concerto models more effectively.


## Introduction

This project involves the development of a Graphical User Interface (GUI) for editing a data modeling language called Concerto. Concerto is an open-source modeling language developed by Accord Project for creating smart contracts, digital assets, and other business process models. The GUI has been developed using ReactJS, a popular JavaScript library for building user interfaces. The main objective of the project is to provide a user-friendly interface for editing and manipulating Concerto models. The GUI allows users to enter data through a form-based interface, which is then used to update the serializable Abstract Syntax Tree (AST) of the Concerto model. The AST is a data structure that represents the Concerto model in a way that can be easily manipulated by software programs. The project aims to simplify the process of creating and editing Concerto models, making it accessible to a wider range of users, including those with limited programming experience. The GUI also allows for easier collaboration between multiple users working on the same model. Overall, this project represents an important step forward in making the Concerto modeling language more accessible and user-friendly, and has the potential to facilitate the development of smart contracts and other business process models for a wide range of industries.


![image-alternative text](\virtual-expo\assets\img\compsoc\2023_concerto_web_editor_thumbnail.png)

## Accord Project

![AccordProject](\virtual-expo\assets\img\compsoc\2023_concerto_web_editor_accordlogo.png)

Accord Project is a non-profit organization that is dedicated to the development of open-source software tools and frameworks for smart legal contracts. The organization's goal is to promote the use of smart contracts in various industries by providing standardized tools and frameworks for creating, managing, and executing these contracts. Accord Project is known for developing the Concerto modeling language, which is used to define the data structures and business logic of smart legal contracts. The organization also provides various tools for generating and executing smart contracts, including Cicero, a templating engine for creating executable legal documents, and Ergo, a domain-specific language for writing contract clauses.

## Concerto

![Concerto](\virtual-expo\assets\img\compsoc\2023_concerto_web_editor_thumbnail.png)

Overall, Concerto represents an important step forward in the development of smart contracts and other business process models. Its simplicity, flexibility, and support for code generation make it a powerful tool for creating and managing complex business processes, while its open-source nature ensures that it remains accessible and available to a wide range of users and developers.

Concerto provides a simple yet flexible syntax for defining data structures and business logic. It supports a wide range of data types, including primitive types such as strings, integers, and booleans, as well as more complex types such as arrays, maps, and enumerations. It also supports the definition of functions, events, and transactions, which can be used to define the behavior of smart contracts and other business process models. One of the key features of Concerto is its support for code generation. The language can be used to generate code in a variety of programming languages, including JavaScript, TypeScript, Java, and Go. This makes it easy to integrate Concerto models with existing software systems and platforms. 


### Concerto Web Editor

Concerto Web Editor provides 3 different views to the lawyer & programmer user-base, the code, forms & diagram views.

![Code](\virtual-expo\assets\img\compsoc\2023_concerto_web_editor_code.png)

 - The code view is primarily for the programmers if there arises a need for final re-evaluation of the schema by a professional well versed in both fields. 

![Form](\virtual-expo\assets\img\compsoc\2023_concerto_web_editor_form.png)

- The forms view is where lawyers would ideally interact with. Here the user can define new namespaces (groups of related concepts in a contract), define new concepts all together (to better suit the agreement), and add or change attributes within contracts, which help store the overall state of that concept within the contract. Concerto also allows users to perform tasks like nesting & extending concepts, inheriting certain attributes from other concepts, and adding properties to attributes, where some attributes are absolutely required for a concept in a clause to function or provide default values for others. With the Web Editor, all these programming paradigms and functionalities, including error handling, are now able to be performed just by interacting with the form view. 

![Diagram](\virtual-expo\assets\img\compsoc\2023_concerto_web_editor_diagram.png)

- Finally we have the diagram view, this allows for a simpler visualisation of the various concepts defined by the user that are in play in the contract. It not only shows you the schema but also their attributes, and their relationships with one another. This allows for easier cross verification before finalising a schema and also allows for easy collaboration since a new user can understand the models by looking at the view of the overall contract schema rather than lengthy codes or nested forms. 




Apart from the above mentioned, the web editor is now also newly equipped with functionality by way of which the user can also export their concerto model to the language of their choice using the export button. The internal mechanisms use a mermaid visitor that writes to a zip file to be downloaded, making the whole process seamless across multiple programming language spaces.


## Conclusion

The GUI interactability of the editor will enable users to create data models with ease and without needing to understand the complex syntax of the Concerto language. This will significantly improve the usability of the language and make it accessible to a wider range of users, including those with little to no programming experience.

The simplified interface provided by the GUI will enable users to focus on the business logic and data structures they want to model, without having to worry about the technical details of the underlying language. This will help to accelerate the development and adoption of smart contracts, digital assets, and other business process models that can be created using Concerto.


## References

1. Accord Project, [Accord Project](https://accordproject.org/)
Note: The alternative text will be displayed on the website, and clicking it will take you to the given link address. Use correct brackets for text and link respectively as shown above. Use the above line to embed links in any part of your report. 
For example,
		[Head over to YouTube](https://www.youtube.com/)
2. Concerto, [Concerto](https://accordproject.org/projects/concerto/
3. ReactJS, [ReactJS](https://react.dev/)
4. React Dev Flow for UML generation, [React Dev Flow][https://reactflow.dev/]