# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.4 Day two, 1b.py
# Description: A program to determine which of the three numbers is the largest
# Test cases: I used numbers 1,2,3 and 1,3,2 and 3,2,1.


# Input: gets the intergers from the user.
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a second integer: "))
num3 = int(input("Please enter a third integer: "))


# Output: prints which integer is the largest.
if num1 > num3 or num2 > num3: 
    if num1 > num2:
        print(num1, "is the largest.")
        
    elif num2 > num1:
        print(num2, "is the largest.")
        
elif num3 > num1 and num3 > num2:
    print(num3, "is the largest.")
