# Mini Project: Student Result Management System

## Objective

The objective of this mini project is to take student information and marks as input, validate them, and calculate the total, average, and percentage of the marks. It also generates a structured report of the student's performance.

## Problem Statement

Calculate and display student results based on the following:

- Take student information: **name, age, and ID**.
- Enter marks for multiple subjects.
- Validate marks:
  - Marks cannot be negative.
  - Marks cannot exceed 100.
- Store and display the marks.
- Calculate:
  - **Total marks**
  - **Average marks**
  - **Percentage**
- Handle invalid marks or missing data gracefully.
- Generate a **complete student performance report**.

## Logic / Working

- Program asks for student **name, age, and ID**.
- User enters **marks for subjects**.
- Marks are validated:
  - Negative marks or marks above 100 are rejected.
  - User is prompted to re-enter invalid marks.
- Once valid, program calculates:
  - **Total marks** using `sum()`.
  - **Average marks** = total / number of subjects.
  - **Percentage** = (total marks / total maximum marks) * 100.
- Program prints a **structured student report**:
  - Name, Age, ID, Marks
  - Total, Average, Percentage

## Conclusion

In this mini project, we have used **Python's Object-Oriented Programming (OOP)** concepts, including **classes, methods, and static methods**, to create a **real-life student performance system**.  
This project helps in understanding **data validation, arithmetic calculations, and report generation**.

## Tools / Concepts Used

- Python  
- Classes & Objects  
- Methods & Static Methods  
- Lists  
- Input / Output  
- Conditional Statements  
- Basic Arithmetic Calculations
