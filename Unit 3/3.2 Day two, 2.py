# Name: Fady Elsayed	
# Date: March, 9, 2021	
# File Name: 3.2 Day two, 2.py
# Description: A program that sums the squares of the intergers.
# Test cases: I used the numbers, 5, 4, 3, 0.

# Process: Sets the num_sum to 0.
num_sum = 0

# Input: Gets gets user input for first interger.
num = int(input("Please enter an integer: "))

# Process: Determines if the while loop will run, and if so 
# it calculates the sum of the squared intergers, and asks for another interger.
if num >= 1:
    while num > 0:
            num_sum += num * num
            num = int(input("Please enter an integer: "))
            if num < 1:
                break

# Output: Prints the sum of the squares of all positive the integers.
    print("The sum of the squares of all the positive integers is", num_sum)

