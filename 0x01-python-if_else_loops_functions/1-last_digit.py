#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # This line should not change
last_digit = number % 10  # Get the last digit of the number

# Adjust last_digit for negative numbers
if number < 0:
    last_digit -= 10

# Determine the message based on the last digit
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit}\
 and is less than 6 and not 0")
