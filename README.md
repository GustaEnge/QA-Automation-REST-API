
<h1 align="center">

  <br>
  Zyte Project
  <br>
</h1>

# Product QA Trial

## Technical Assessment 
Consider a scenario where the business analyst did not create a well detailed documentation. It lacks some pieces of information however as a QA Engineer the challenge is to connect some points and fill as many gaps as you can in order to test the main use cases properly.

## SUT (system or subject under test)
Json Server repository: https://github.com/typicode/json-server
Data Model:

```
{
    "posts": [
        { "id": 1, "title": "json-server", "author": "typicode" }
    ],
    "comments": [
        { "id": 1, "body": "some comment", "postId": 1 }
    ],
    "profiles": [{ "name": "typicode" }]
}
```

## Main Use Cases
1. As a user, I want to create new user profile
    - Method: POST 
    - Url: http://localhost:3000/profile
    - Body: 
        ```{ "name": "any name" }```
    - Refer for further documentation on how API works on the github repo

2. As a user, I want to post new content
3. As a user, I want to comment on post of someone else
4. As a user, I want to see my post by post id
5. As a user, I want to see the comments on my post by post id
6. As a manager, I want to be able to search profiles by name in order to validate if they exist

## Challenge
1. Extract tests from the provided information
    - Create as many tests as you can
    - Write down the tests in english
    - Save them in the repo in the format of your choice
2. Automate as many tests as you can using the technologies of your choice
    - All instructions needed to run the automated tests should be in a file README.md

<h2 align="center">

  <br>
  Solution
  <br>
</h2>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](screen-capture.gif)


## Test Plan & Test Cases

[Test Plan](https://docs.google.com/document/d/1YtnoL2g4OToV-7GQkNB_V-JdaCMcJErhLt8R20SFvLk/edit?usp=sharing)


## Key Features

* API_Adapter Module - where you will find API_Core class to perform all API operations depending on the Verb and action you want
  - Create, Get, Update and Delete **Posts**
  - Create, Get, Update and Delete **Comments**
  - Create, Get, Update and Delete **Profiles**

* Data_Adapter Module - Unfinished module to create a Test DataBase and generate random data for your fuutre test (need to be adapted for this project)

* Test_Cases - where you will find the automated tests built on RobotFramework

* Requirements.txt - all dependencies/modules required to run this project if you want to know more, but I used a virtual enviroment (venv) for this project

* Cross platform
  - Windows, macOS and Linux ready.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone 

# Go into the repository
$ cd Zyte_Project

# Install dependencies
$ npm install

# Run the app
$ npm start
```

## Credits

This software uses the following open source packages:

- [Robot Framework](https://robotframework.org/robotframework/)
- [Node.js](https://nodejs.org/)
- [Python](https://docs.python.org/3/)


