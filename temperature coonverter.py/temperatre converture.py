# -----------------------------------------------MINI PROJECT-------------------------------------------------------------

# -------------------------------------------TEMPERATURE CONVERTER--------------------------------------------------------

# PROBLEM STATEMENT :

# Write a Python program that asks the user for a temperature, lets them choose between Celsius-to-Fahrenheit 
# or Fahrenheit-to-Celsius, checks the input, converts the temperature using the right formula, and shows the
# result clearly with proper error messages.

# CODE :

temperature = float(input("Enter the temperature value: "))

print("Choose conversion type:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
choice = int(input("Enter 1 or 2: "))

if choice != 1 and choice != 2:
    print("Invalid choice! Please enter 1 or 2.")

else:
    if choice == 1:
        fahrenheit = (temperature * 9/5) + 32
        print(f"{temperature}°C is equal to {round(fahrenheit, 2)}°F")
    
    elif choice == 2:
        celsius = (temperature - 32) * 5/9
        print(f"{temperature}°F is equal to {round(celsius, 2)}°C")

# SAMPLE OUTPUT:


# Example 1: Celsius → Fahrenheit

# Enter the temperature value: 30
# Choose conversion type:
# 1 - Celsius to Fahrenheit
# 2 - Fahrenheit to Celsius
# Enter 1 or 2: 1
# 30°C is equal to 86.0°F


# Example 2: Fahrenheit → Celsius

# Enter the temperature value: 100
# Choose conversion type:
# 1 - Celsius to Fahrenheit
# 2 - Fahrenheit to Celsius
# Enter 1 or 2: 2
# 100°F is equal to 37.78°C


# Example 3: Invalid choice

# Enter the temperature value: 50
# Choose conversion type:
# 1 - Celsius to Fahrenheit
# 2 - Fahrenheit to Celsius
# Enter 1 or 2: 3
# Invalid choice! Please enter 1 or 2.
