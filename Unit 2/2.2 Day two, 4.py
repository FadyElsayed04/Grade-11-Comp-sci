# Name: Fady Elsayed	
# Date: March, 2, 2021	
# File Name: 2.2 Day two, 3.py
# Description: A program that gives the user their weekly salary depending
# on the amount of hours worked including overtime.
# Test cases: I used the number of hours: 32, and 46.

# Input – gets user input for amount of hours worked
hours = int(input("Please enter the amount hours worked: "))

# Output – prints out earned pay.
if hours > 40:
    pay = (hours - 40) * 15 + 480 
    print("\nYour weekly salary is: $" + str(pay))
elif hours <= 40:
    pay = hours * 12
    print("\nYour weekly salary is: $" + str(pay))
