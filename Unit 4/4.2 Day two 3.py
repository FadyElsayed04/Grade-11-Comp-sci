# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.2 Day two 3.py
# Description: Program uses a function to get roots of quadratic equation from 3 numbers.
import math

# Process: Creates function to get roots of quadratic equation.
def roots(num1, num2, num3):
    
    positive = round((-1*num2 + (math.sqrt(num2 ** 2 - (4 * num1 * num3)))) / 2 * num1, 2)
    minus = round((-1 * num2 - (math.sqrt(num2 ** 2 - (4 * num1 * num3)))) / 2 * num1, 2)
    
    return positive, minus
    
# Main program (input for easier testing)
num1 = int(input("please enter a: "))
num2 = int(input("please enter b: "))
num3 = int(input("please enter c: "))

roots = roots(num1, num2, num3)

# Output: Prints the roots.
print(roots)
