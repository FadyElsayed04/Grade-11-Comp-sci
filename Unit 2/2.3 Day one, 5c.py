# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day one, 5c.py
# Description: A program to determine if the given integer is
# divisible by both 3 and 5.
# Test cases: I used numbers 15, amd 11.

# Input: Gets user input for interger.
x = int(input("Please enter an integer: "))

# Output: Outputs if that value of x is divisible by both 3 and 5 or not.
if (x%3) == 0 and (x%5) == 0:
    print("It is divisible by 3 and 5")
    
else:
    print("It is not divisible by 3 and 5")
