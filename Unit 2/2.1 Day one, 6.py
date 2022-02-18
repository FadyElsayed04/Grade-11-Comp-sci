# Name: Fady Elsayed	
# Date: February 25, 2021	
# File Name: 2.1 Day one, 6.py
# Description: A program to tell the user if they old enough to drive or not.
# Test cases: I used the numbers: 11, 16, 19

# Input – get users age
user_age = int(input("What is your age?: "))

# Process - calculates the age needed.
age_needed = 16

# Output – Displays if the user can drive or not
print("")
if user_age >= age_needed:
    print("You are old enough to drive.")
else:
    print ("You are not old enough to drive.")
