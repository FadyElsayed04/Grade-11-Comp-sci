# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day one, 5d.py
# Description: A program to determine if the given integer a multiple of 4 or 7.
# Test cases: I used numbers 16, 49, and 11.


# Input: Gets user input for x.
x = int(input("Please enter an integer: "))


# Output: Outputs whether or not if x is a multiple of 4 or 7.
if not((x % 4) == 0 or (x % 7) == 0):
    print("Your number is NOT a multiple of 4 or 7")
    
else:
    print("Your number is a multiple of 4 or 7")
