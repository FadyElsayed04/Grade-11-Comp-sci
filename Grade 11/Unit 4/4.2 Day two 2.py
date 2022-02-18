# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.2 Day two 2.py
# Description: Program uses a function to create quotient and remainder from
# two numbers. 

import math
# Process: Creates function to get quotient and remainder
def quot_rem(num1, num2) :
        quotient = num1 // num2
        remainder = num1 % num2
        return quotient,remainder

# Main program
num1 = int(input("please enter num1: "))
num2 = int(input("please enter num2: "))
quot_rem = quot_rem(num1, num2)

# Output: Prints the quotient and remainder
print(quot_rem)
