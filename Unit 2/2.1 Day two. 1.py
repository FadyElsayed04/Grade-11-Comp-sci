# Name: Fady Elsayed	
# Date: March, 1, 2021	
# File Name: 2.1 Day two, 1.py
# Description: A program to ask the user for two numbers and adds 5 to the
# the first number if the second number is greater than 10.
# Test cases: I used, 2 and 5, 4 and 22.

# Input – gets user input for numbers
num1 = int(input("please enter a number: "))
num2 = int(input("please enter a second number "))
# Process - adds variable for +5
extra = 5

# Output – prints on conditions with the second number being above or below 10
print("")
if num2 > 10:
    print(num1 + extra, num2)
else:
    print (num1, num2)
