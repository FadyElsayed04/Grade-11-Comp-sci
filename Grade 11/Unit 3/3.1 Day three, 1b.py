# Name: Fady Elsayed	
# Date: March, 8, 2021	
# File Name: 3.1 Day three, 1b.py
# Description: A program determine the factors of given number, ir
# if the number is prime.
# Test cases: I used the numbers 7, and 50.

# Process: sets prime to 0.
prime = 1

# Input: Asks the user for an integer between 1-50.
num = int(input("Enter a number between 1 and 50: "))

# Process: determines if the given number is prime.
if num > 1:
  
    for n in range(2, num):
        if (num % n) == 0:
            prime = 0
            break
# Process: Loops modulo operators to determine the factors.
if prime == 0:
    for n in range(1, num + 1):
        if(num % n) == 0:

# Output: Prints the factors of the number given, or if the 
            print(n)
else:
    print(num, "is a prime number")
