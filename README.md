# Redbubble_Coding_Challenge
Redbubble Summer 2019 Internship Coding Challenge

## Purpose
* http://take-home-test.herokuapp.com/new-product-engineer<br>
* To Create a Price Calculator Command Line Application to output the Total Price of the Redbubble Shopping Cart (in Cents) using both the Cart JSON and Base Price JSON Files

## Technologies Used
* Developed on the macOS High Sierra Version 10.13.6 using Visual Studio Code<br>
* Python 3.6.3 for CL Application<br>

## Dependencies Needed
* Python2 or Python3 (Both Compatible)
* argparse library (pip install argparse)
* json library (Already a Built-In Module with Python)
* unittest library (Already a Built-In Module with Python)

## Usage
To get the Total Price of the Redbubble Shopping Cart (in Cents), run: python calculate_the_price.py -c /PATHTOCARTJSON -p /PATHTOBASEPRICEJSON -d /PATHTODISCOUNTJSON<br>
The order of the command line arguments do not matter, use '-h' option for help. Can Specify Local or Absolute Path to the Cart and Base Price JSON Files. If Permission Problems for opening JSON Files, run 'chmod 755 'JSONFILES'<br>
*I Chose to Add the Command Line Options for Clarity for the user on Which File is Which - CART, BASE PRICE, and DISCOUNT*

## TESTING
https://powerfulpython.com/blog/automated-tests-types-for-python/ <br>
Automated Tests in Python -> Unit Testing in Python. <br>
Unit Test - Test a Specific Component in Isolation. <br>
Integration Test - Test How two Components Interact with each other. <br>
End-to-End Test - Test Entire Flow of Application. <br>
Run: python automated_tests.py -v

## Design Implementation
I chose to go the Object - Oriented Route in creating Cart, ProductItem, BasePriceDB, and PriceCalculator Classes since all can be stand alone - for future extendibilty with other Objects. The Classes are all simple with obvious User Interfaces (function names) for anyone to pick up and code (Add and Change Implementations). This design was rather simple with Python's built in JSON Parsing Library and Argument Parser.<br>
<br>
Some Ideas for Further Improvements would be to have the BasePriceDB Connect to a Database on a Server - probably MongoDB since their Stores are similar to JSON Objects. Then, the 'find' access times for Base Prices would improve rather than searching through all the Base Prices like I am doing now (Which is NOT Constant). For Each ProductItem in the Cart, I am searching through all the BASE Prices. If there are N Product Items and M Base Prices, My run-time is actually: O(N*M) <br>
I would improve this with a DataBase Selection for Prices!

## Resources
* https://docs.python.org/3/library/json.html
* https://developer.rhino3d.com/guides/rhinopython/python-xml-json/
* https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
* https://docs.python.org/3/library/argparse.html
* https://docs.python.org/3/library/unittest.html
* https://www.youtube.com/watch?v=ApTZib0L2X8
