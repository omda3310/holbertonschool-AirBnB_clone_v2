AirBnB Clone - README
This project is an AirBnB clone, which aims to replicate some of the functionalities of the popular online marketplace for accommodation rentals. It is built using Flask, a web framework for Python.

Concepts
Before starting this project, it is recommended to be familiar with the following concepts:

Web Frameworks
Building a web framework with Flask
Defining routes in Flask
Templates and rendering templates
Variables and handling variables in routes
HTML response creation in Flask using templates
Dynamic templates (loops, conditions, etc.)
Displaying data from a MySQL database in HTML
Requirements
Python Scripts
All files should be written in Python 3.8.5
All files should end with a new line
The first line of all files should be #!/usr/bin/python3
Your code should follow the PEP 8 style guide and use pycodestyle (version 2.7.*) for code formatting
All files must be executable
The length of your files will be tested using wc
All modules, classes, and functions should have documentation explaining their purpose
HTML/CSS Files
All files should end with a new line
Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
All CSS files should be in the styles folder
All images should be in the images folder
You are not allowed to use !important or id (#...) in the CSS file
All tags must be in uppercase
Screenshots have been taken on Chrome 56.0.2924.87
No cross-browsers support is required
MySQL Default charset issues
If you encounter Flask errors after running curl commands, it might be due to the DEFAULT CHARSET. If it's set to DEFAULT CHARSET=latam1, you should change it to DEFAULT CHARSET=utf8mb4 in the server's config file or in the CREATE DATABASE statement.

Installation
To install Flask, run the following command:

ruby
Copy code
$ pip3 install Flask
Manual QA Review
It is your responsibility to request a review for this project from a peer before the project's deadline. If no peers are available for review, you can request a review from a TA or staff member.