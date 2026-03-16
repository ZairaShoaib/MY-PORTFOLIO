# Mini Project: Temperature Converter

## Objective

The objective of this mini project is to take a temperature value from the user and convert it between Celsius and Fahrenheit according to the user's choice.

## Problem Statement

Write a Python program that:

* Asks the user to enter a temperature.
* Lets the user choose the type of conversion:

  * Celsius to Fahrenheit
  * Fahrenheit to Celsius
* Checks that the user enters a valid choice (1 or 2).
* Converts the temperature using the correct formula:

  * Celsius → Fahrenheit: F = (C × 9/5) + 32
  * Fahrenheit → Celsius: C = (F − 32) × 5/9
* Displays the result clearly to the user.
* Handles invalid input or wrong choices gracefully.

## Logic / Working

* The program first asks the user for the temperature value.
* Then it asks the user to choose the conversion type (1 for C→F, 2 for F→C).
* If the choice is not valid (other than 1 or 2), the program shows an error message.
* If the choice is valid:

  * For C→F conversion, the program multiplies the temperature by 9/5 and adds 32.
  * For F→C conversion, the program subtracts 32 from the temperature and multiplies by 5/9.
* The converted temperature is displayed clearly with proper units.
* Optional: The result can be rounded to 2 decimal places for easier reading.

## Conclusion

In this mini project, we have used Python's if-elif-else statements to create a real-life temperature conversion system. This project is very useful and helps in understanding basic programming concepts like input/output, variables, and conditional statements.

## Tools / Concepts Used

* Python
* Variables
* Input / Output
* Conditional Statements (if-elif-else)
* Arithmetic Operations
