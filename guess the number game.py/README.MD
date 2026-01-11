# Mini Project: Number Guessing Game

## Objective

The objective of this mini project is to create a game where the user has to guess a randomly generated number. The game provides hints after each guess and limits the user to a fixed number of attempts.

## Problem Statement

Write a Python program that:

- Generates a **random number** between a specified range (1 to 50).  
- Allows the user to **guess the number**.  
- Gives the user **exactly 3 attempts** to guess correctly.  
- After each guess, provides **hints** to the user:
  - If the guess is **lower** than the secret number → “Too low! Try a higher number.”  
  - If the guess is **higher** than the secret number → “Too high! Try a lower number.”  
  - If the guess is **correct** → congratulates the user and displays the attempt number.  
- If the user fails to guess within 3 attempts, the program reveals the **correct number**.  
- Handles input and comparison in a **user-friendly way**, giving clear instructions and feedback.  

## Logic / Working

1. Program generates a **secret random number** between 1 and 50.  
2. The user is given **3 attempts** to guess the number.  
3. For each attempt:
   - User inputs a guess.  
   - Program compares the guess with the secret number.  
   - Provides hint:
     - Guess is too low → “Higher”  
     - Guess is too high → “Lower”  
     - Guess is correct → Congratulates and exits loop.  
4. If the user guesses correctly, the program displays the **number of attempts taken**.  
5. If the user fails after 3 attempts, the program **reveals the secret number**.  

## Conclusion

In this mini project, we have used Python's **random number generation, loops, conditional statements, and user input handling** to create an interactive Number Guessing Game.  
This project helps in understanding **program flow, logic implementation, and user interaction** in Python.

## Tools / Concepts Used

- Python  
- Random Module (`random.randint`)  
- Loops (`for` loop)  
- Conditional Statements (`if-elif-else`)  
- Input / Output  
- Counters / Attempts Tracking

