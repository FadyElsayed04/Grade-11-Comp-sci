# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day two, 4b.py
# Description: A program to determine if any of the three numbers is a 
# multiple of the other two.
# Test cases: I used numbers 12,15,8 and 12,13,15 and 8,12,5


# Input: Gets user input for numbers.
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a second integer: "))
num3 = int(input("Please enter a third integer: "))

# Output: prints if only 2 intergers are greater than 10.
if num1 >= 10 and num2 >= 10 and num3 <= 10:
    print("\nExactly two are greater than 10")

elif num1 >= 10 and num3 >= 10 and num2 <= 10:
    print("\nExactly two are greater than 10")

elif num2 >= 10 and num3 >= 10 and num1 <= 10:
    print("\nExactly two are greater than 10")
