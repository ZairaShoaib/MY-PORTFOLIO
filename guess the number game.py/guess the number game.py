# -----------------------------------------------MINI PROJECT-------------------------------------------------------------

# ------------------------------------------NUMBER GUESSING GAME----------------------------------------------------------

# PROBLEM STATEMENT :

# Write a Python program that:
# Generates a random number between a specified range (1 to 50).
# Allows the user to guess the number.
# Gives the user exactly 3 attempts to guess correctly.
# After each guess, provides hints to the user:
# If the guess is lower than the secret number → “Too low! Try a higher number.”
# If the guess is higher than the secret number → “Too high! Try a lower number.”
# If the guess is correct → congratulates the user and displays the attempt number.
# If the user fails to guess within 3 attempts, the program reveals the correct number.
# Handles input and comparison in a user-friendly way, giving clear instructions and feedback.

import random

secret_number = random.randint(1, 50)

print("Welcome to Number Guessing Game!")
print("You have 3 attempts to guess the number between 1 and 50.")

for attempt in range(1, 4):

    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed the correct number {secret_number} in {attempt} attempt(s).")
        break  
else:
    print(f"Sorry! You did not guess the number. The correct number was {secret_number}.")


# SAMPLE OUTPUT:

# Welcome to Number Guessing Game!
# You have 3 attempts to guess the number between 1 and 50.

# Attempt 1: Enter your guess: 20
# Too low! Try a higher number.

# Attempt 2: Enter your guess: 40
# Too high! Try a lower number.

# Attempt 3: Enter your guess: 35
# Congratulations! You guessed the correct number 35 in 3 attempts.
