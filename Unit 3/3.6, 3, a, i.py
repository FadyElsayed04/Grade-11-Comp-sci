# Name: Fady Elsayed
# Date: Mar 20 2021
# File Name: 3.6, 3, a, i.py
# Description: A program to generates the sum of 2 dice and checks and
# prints which ones are have a sum of at least 9.

# Process: Sets value for total.
total = 0

# Process: Loops the values of the dice.
for die1 in range(1,6):
    for die2 in range(1,6):
        if die1 + die2 >= 9:
            total += 1
            print(die1, die2)
            
# Output: prints the total possible rolls that sum to at least 9.           
print("There are", total, "possible rolls that sum to at least 9.")
