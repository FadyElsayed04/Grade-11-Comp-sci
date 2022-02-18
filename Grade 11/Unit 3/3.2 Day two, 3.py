# Name: Fady Elsayed	
# Date: March, 9, 2021	
# File Name: 3.2 Day two, 3.py
# Description: A program that determines the largest 2 integers of the amount
# of integers give. If integer is negative the program ends.
# Test cases: I used the numbers: 7, 12, 6, 4, and 8.

# Process: Determines the value of the numbers and num.
num = 0
largest = 0
second_largest = 0

amount = int(input("How many integers are you going to enter?: "))

# Process: Determines which lines will run and which 2 numbers are the largest.
while amount > num:
    user_num = int(input("Please enter a positive integer: "))
    
    if user_num < 0:
        break
    
    elif user_num > largest:
        second_largest = largest
        largest = user_num
        
    elif user_num > second_largest:
        second_largest = user_num
        
    num += 1
    
if amount > 1 and user_num >= 0:
    
# Output: Prints the largest two numbers if the numbers are positive.
    print("\nThe largest integer is", largest)
    print("\nThe second largest integer is", second_largest)
        
