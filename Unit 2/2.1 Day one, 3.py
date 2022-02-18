# Name: Fady Elsayed	
# Date: February 24, 2021	
# File Name: 2.1 Day one, 3.py
# Description: A program to tell which of the two numbers is larger. it asks for two numbers as input 
# and prints the larger number.
# Test cases: I used the numbers: 2, and 3, and 5, and 5.

# Input – Get user input for two numbers.
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))


# Output – Print which number is bigger.
print("")

if num1 == num2:
	print("Those are the same numbers.")

if num1 > num2:
        print(num1, "is the bigger number.")
        
if num1 < num2:
        print(num2, "is the bigger number.")
