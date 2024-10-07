# python-automation
Welcome to the python-automation repository! This repository is a collection of pyhton script and designed to help you learn Python programming through examples and exercises.

## Table of Contents
- Introduction
- Installation
- Steps to Learn Python
- Python Roadmap
- Learning Structure

## Introduction
This repository contains a collection of Python programming examples and exercises. It is intended for beginners who want to learn Python and and want to brush up on their skills.

## Installation
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/neeraj-p/python-automation-repo.git
cd python-automation-repo
```
## Steps to Learn Python
Step 1- Learn the Basics - Syntax, Variable, Data Types and conditionals

Step 2- Learn Loops, functions, Built in functions

Step 3- Data Structure - Lists, Tuples, Sets, Dictonaries

Step 4- OOP - Class, inheritence, Objects

Step 5- Advance Topics - RegEx, Decorators, Lambda

Step 6- Advance Topics 2 - Modulers, iterators

Step 7- Learn Python Libraries

## Python Roadmap
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/neeraj-p/python-automation/blob/main/Python%20Roadmap.jpg">
 <source media="(prefers-color-scheme: light)" srcset="[YOUR-LIGHTMODE-IMAGE](https://github.com/neeraj-p/python-automation/blob/main/Python%20Roadmap.jpg)">
 <img alt="YOUR-ALT-TEXT" src="[YOUR-DEFAULT-IMAGE](https://github.com/neeraj-p/python-automation/blob/main/Python%20Roadmap.jpg)">
</picture>


## Learning Structure
Week 1: Python Fundamentals

Day 1: Introduction to Pytho

``` Day 1: Introduction to Python

Learn how to install Python and set up a development environment (IDEs like PyCharm or VS Code).

Topics: Variables, Data Types, and Basic I/O.

Exercises:

Write a script that prints "Hello, World!"

Create a script that takes user input and prints a formatted message.
```
Day 2: Control Flow (Conditionals and Loops)
``` 

Topics: if, elif, else statements; for and while loops.

Exercises:

Write a script that checks if a number is even or odd.

Create a script that prints numbers 1 to 10 using a loop.
```
Day 3: Functions
```

Topics: Defining functions, function arguments, return values.

Exercises:

Write a function that calculates the factorial of a number.

Create a function that accepts two numbers and returns their sum.
```


Day 4: Lists and Tuples
```

Topics: Lists (mutable), Tuples (immutable), basic list methods.

Exercises:

Write a script that takes a list of numbers and prints the largest number.

Create a script that takes a tuple and prints each element.
```


Day 5: Dictionaries and Sets
````

Topics: Key-Value pairs in dictionaries, sets (unique elements).

Exercises:

Write a script that counts the occurrences of each character in a string.

Create a dictionary with sample data and retrieve values by key.
````


Day 6: File Handling
```

Topics: Reading from and writing to files.

Exercises:

Write a script that reads content from a file and prints it.

Create a script that writes user input to a text file.
```


Day 7: Review & Mini-Project
````

Review all concepts from the week.

Mini-project: Create a simple script that reads a file with user data and prints a formatted report (e.g., name, age, city).

````


Week 2: Intermediate Python Concepts

Day 8: Object-Oriented Programming (OOP) Basics

```
Topics: Classes, objects, methods, and inheritance.

Exercises:

Write a class Car with attributes (make, model, year) and methods (start, stop).

Create a subclass ElectricCar that inherits from Car and adds specific behavior.
```


Day 9: Error Handling and Exceptions
```

Topics: try, except, finally blocks, raising exceptions.

Exercises:

Write a script that catches division by zero errors.

Create a function that raises an exception if the input is negative.
```


Day 10: Modules and Packages
```

Topics: Importing modules, creating your own modules.

Exercises:

Write a module for basic mathematical operations and import it into another script.

Use built-in Python modules like math and random to generate random numbers.
```


Day 11: Virtual Environments and Pip
```

Topics: Setting up virtual environments, installing packages with pip.

Exercises:

Create a virtual environment and install the requests package.

Write a script using requests to fetch data from a sample API.
```


Day 12: Working with APIs
```

Topics: Making GET and POST requests, parsing JSON.

Exercises:

Write a script that sends a GET request to a public API and prints the response data.

Send a POST request with JSON data to an API and print the response.
```


Day 13: Introduction to Testing with unittest
```

Topics: Writing unit tests, understanding assertions, running test cases.

Exercises:

Write a unit test for a function that adds two numbers.

Create test cases for the factorial function from Day 3.
```


Day 14: Review & Mini-Project
```

Review all intermediate topics.

Mini-project: Build a small application that fetches data from a public API, processes the data, and writes the results to a file (include error handling and test cases).
```


Week 3: Introduction to Automation

Day 15: Introduction to Selenium for Web Automation
```

Topics: Installing Selenium, WebDriver basics.

Exercises:

Write a script that opens a browser, navigates to a website, and closes the browser.

Automate filling a form on a sample webpage.
```


Day 16: Navigating Web Pages with Selenium
```

Topics: Locating elements using Xpath, CSS selectors, IDs.

Exercises:

Write a script that navigates to a website and clicks a button.

Extract text from a web page and print it.
```


Day 17: Interacting with Web Elements
```

Topics: Sending inputs, clicking buttons, interacting with forms.

Exercises:

Automate logging into a demo website.

Write a script that fills out a form and submits it.

```

Day 18: Handling WebDriver Waits and Exceptions
```

Topics: Implicit and explicit waits, handling exceptions in Selenium.

Exercises:

Write a script that waits for a specific element to load before interacting.

Handle common Selenium exceptions (e.g., NoSuchElementException).
```


Day 19: Introduction to pytest for Automation
```

Topics: Setting up pytest, writing test functions, using fixtures.

Exercises:

Write a basic pytest function to test a simple Python script.

Automate a test case for a login page using Selenium and pytest.
```


Day 20: Running Automated Tests with pytest
```

Topics: Parameterized tests, running test suites.

Exercises:

Write parameterized tests for different input data in a login form.

Run multiple test cases using pytest.
```


Day 21: Review & Mini-Project
```

Mini-project: Create a simple automation framework using Selenium and pytest to automate login, form submission, and basic user interactions on a sample website.
```


Week 4: Advanced Automation and Frameworks

Day 22: Building a Test Automation Framework (Part 1)
```

Topics: Structuring a test automation framework, Page Object Model (POM).

Exercises:

Create a base structure for your automation framework using POM.

Implement page classes for login and registration pages.
```


Day 23: Building a Test Automation Framework (Part 2)
```

Topics: Utilities, test data, and reporting.

Exercises:

Write utility functions for handling data inputs.

Add a reporting mechanism for test results.

```

Day 24: API Testing with requests and pytest
```

Topics: Automating API testing, asserting responses.

Exercises:

Write test cases for a public API using the requests library and pytest.

Automate the validation of JSON responses.
```


Day 25: Continuous Integration (CI) with Jenkins
```

Topics: Setting up Jenkins for running automated tests.

Exercises:

Integrate your test automation framework with Jenkins.

Set up Jenkins to run your Selenium tests after every code commit.
```


Day 26: Parallel Test Execution with pytest-xdist
```

Topics: Running tests in parallel to reduce execution time.

Exercises:

Install pytest-xdist and run your Selenium tests in parallel.
```


Day 27: Finalizing and Enhancing Your Automation Framework
```

Topics: Improving your framework with logging and advanced utilities.

Exercises:

Add logging to your automation framework.

Enhance the framework by handling browser configurations and data-driven tests.
```


Day 28: Final Project
```

Build a complete automation project from scratch, automating an end-to-end test scenario (web or API) using Selenium, pytest, and CI with Jenkins.
```




