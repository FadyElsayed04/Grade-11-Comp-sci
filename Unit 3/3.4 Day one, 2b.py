# Name: Fady Elsayed	
# Date: March, 15, 2021	
# File Name: 3.4 Day one, 2b.py
# Description: A Program that adds a random tax rate from 10% to 20% onto a givin price.
# Test cases: I used the prices: 8, 10, 20.

import random

#Input: Gets users item price.
price = float(input("Please enter the price of your item: "))

# Process: Gets the random tax rate from 10%-20%
tax = random.uniform(0.1,0.2)

price += price * tax
tax_percent = tax * 100

# Process: Prints the cost of the item with tax.
print("Your total cost is: $" + str(price), "(Tax:" + str(round(tax_percent, 4)) + "%)")
