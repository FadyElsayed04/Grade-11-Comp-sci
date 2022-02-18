# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day one, 5e.py
# Description: A program to tell the user if two given integers are both
# positive, both negative, or one positive and one negative.
# Test cases: I used the numbers 2 and 4, -2 and -4, 2 and 4, 2 and -4.


# Input: Gets user input for two intergers.
num1 = int(input("Please enter a interger: "))
num2 = int(input("Please enter a second interger: "))

# Output: Prints depending on if both intergers are both positive,
# both negative, or one positive and one negative.
if num1 >0 and num2 >0:
    print("\nBoth numbers are positive")
    
if num1 <0 and num2 <0:
    print("\nBoth numbers are negative")
    
if num1 >0 and num2 <0:
    print("\n" + str(num1), "is positive, and", num2, "is negative")

if num1 <0 and num2 >0:
    print("\n" + str(num1), "is negative, and", num2, "is positive")



