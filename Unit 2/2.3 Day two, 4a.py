# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day two, 4a.py
# Description: A program to determine if any of the three numbers is a 
# multiple of the other two.
# Test cases: I used numbers 1,1,2 and 10,5,15, and 2,7,22.


# Input: Gets user input for numbers.
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a second integer: "))
num3 = int(input("Please enter a third integer: "))

# Output: prints if the intergers are a multiple of the other two numbers.
if num1 % (num2 and num3) == 0:
    print("\nOne of your three numbers are a multiple of the other two")

elif num2 % (num1 and num3) == 0:
    print("\nOne of your three numbers are a multiple of the other two")

elif num3 % (num1 and num2) == 0:
    print("\nOne of your three numbers are a multiple of the other two")

else:
    print("\nNone of your three numbers are a multiple of the other two")
