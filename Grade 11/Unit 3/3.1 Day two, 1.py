# Name: Fady Elsayed	
# Date: March, 5, 2021	
# File Name: 3.1 Day two, 1.py
# Description: A program that askes the user for the amount and cost of
# their grocery bill and calculates the total cost of the bill with tax.
# Test cases: I used 3 as the amount of items, and the costs, 2, 3 and 6.


# Process: Defines the sum.
sum = 0

# input: Gets user unput for amount of items on their grocery bill.
items = int(input("How many items were on your grocery bill?: "))
            
# Process: Collects amount times program will run
for n in range(items):

# input: collects price of items.
        item_cost = float(input("Enter the cost of each item: "))

# Output: Caculates the total cost wtih tax.
        sum += item_cost
        total_cost = sum * 1.13

# Output: Prints the total cost including tax
print("\nThe total cost for grocery bill is: $" + str(total_cost))
