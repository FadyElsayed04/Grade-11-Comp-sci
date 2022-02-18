# Name: Fady Elsayed	
# Date: March, 2, 2021	
# File Name: 2.2 Day two, 1.py
# Description: A program that asks for the user's
# age and tells the user their age group.
# Test cases: I used the ages: 6, 14, 41, and 73.

# Input – gets user input for age
age = int(input("Please enter your age: "))

if age < 12 :
    print("\nYou are a child.")
elif age < 19 :
    print("\nYou are a teen.")
elif age < 65 :
    print("\nYou are a adult.")
else:
    print("\nYou are a senior citizen.")
