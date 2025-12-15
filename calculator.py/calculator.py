# -----------------------------------------------MINI PROJECT-------------------------------------------------------------

# -----------------------------------------ELECTRICITY BILL GENERATOR-----------------------------------------------------

# # PROBLEM STATEMENT :

# Write a Python program that:
# Takes two numbers as input from the user.
# Asks the user to choose an operation: Addition (+), Subtraction (-), Multiplication (*), or Division (/).
# Performs the chosen operation and displays the result.
# Handles invalid inputs or division by zero gracefully.

# CODE :

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /):")

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2

if operator == '+':
    print("Result:", add )

elif operator == '-':
    print("Result:", subtract)

elif operator == '*':
    print("Result:", multiply)

elif operator == '/':
    if num2 != 0:
        print("Result:", divide )
    else:
        print("Error: Division by zero is not allowed!")

else:
    print("Invalid operator!")


# SAMPLE OUTPUT:

# Enter first number: 4
# Enter second number: 6
# Enter operator (+, -, *, /): +

# Result: 10
