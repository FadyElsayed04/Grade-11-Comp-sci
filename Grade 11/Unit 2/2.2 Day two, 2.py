# Name: Fady Elsayed	
# Date: March, 2, 2021	
# File Name: 2.2 Day two, 2.py
# Description: A program that asks for the user's
# weight and tells the user their weight group.
# Test cases: I used the weights: 91, 67, and 34.

# Input – gets user input for age
weight = int(input("Please enter your weight(Kg): "))

if weight > 80:
    print("\nYou are heavy weight.")
elif weight > 60:
    print("\nYou are medium weight.")
else:
    print("\nYou are light weight.")
