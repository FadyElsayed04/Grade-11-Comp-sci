# Name: Fady Elsayed	
# Date: March, 8, 2021	
# File Name: 3.1 Day three, 1a.py
# Description: A program determine the factors of given number.
# Test cases: I used the numbers 23, and 45.

# Input: Asks the user for an integer between 1-50.
num = int(input("Enter a number between 1 and 50: "))

# Process: Loops modulo operators to determine the factors.
for x in range(1, num + 1):
    if(num % x) == 0:

# Output: Prints the factors of the number given.
        print(x)
