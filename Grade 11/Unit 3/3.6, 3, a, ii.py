# Name: Fady Elsayed
# Date: Mar 20 2021
# File Name: 3.6, 3, a, ii.py
# Description: A program to generates the sum of 2 dice and checks and
# prints which ones are not divisible by 3 or 5.

# Process: Sets value for total.
total = 0

# Process: Loops the values of the dice.
for die1 in range(1,6):
    for die2 in range(1,6):
        if (die1 + die2) % 3 == 0 or (die1 + die2) % 5 == 0:
            pass
        else:
            total += 1
            print(die1, die2)
            
# Output: prints the total possible rolls that are not divisible by 3 or 5.
print("There are", total, "possible rolls that are not divisible by 3 or 5.")

