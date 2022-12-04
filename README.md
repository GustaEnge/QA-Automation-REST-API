
<h1 align="center">

  <br>  
  QA Automation for REST API
  <br>
</h1>

## SUT (system or subject under test)
Regarding the Json Server repository: https://github.com/typicode/json-server , I built in Python this solution for performing API testing


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


