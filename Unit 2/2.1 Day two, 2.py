# Name: Fady Elsayed	
# Date: March, 1, 2021	
# File Name: 2.1 Day two, 2.py
# Description: A program to create a check for someone eating lunch, with
# the cost of their meal and tax.
# Test cases: I used: $3, $10

# Input – gets users meal cost
cost = float(input("please enter the meals cost: "))
# Process - adds variable for tax and total
sales_tax = 0.08
total = cost * sales_tax+ cost
total = str(total)
            
# Output – prints total cost of meal with or without tax
print("")
if cost > 4:
    print("Your total cost is: $" + total)
else:
    print ("Your total cost is: $", cost)
