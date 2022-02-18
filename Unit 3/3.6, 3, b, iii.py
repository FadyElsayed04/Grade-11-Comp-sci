# Name: Fady Elsayed
# Date: Mar 20 2021
# File Name: 3.6, 3, b, iii.py
# Description: A program to generates the sum of 3 dice and checks and
# prints which ones are prime.

# Process: Sets value for total.
total = 0

# Process: Loops the values of the dice.
for die1 in range(1,6):
   for die2 in range(1,6):
      for die3 in range(1,6):
         sum_dice = die1 + die2 + die3
         if (sum_dice % 2 != 0 and sum_dice % 3 != 0) or sum_dice == 3:
            total += 1
            print(die1, die2, die3)

# Output: prints the total possible rolls that sum to prime numbers.
print("There are", total, "possible rolls that sum to prime numbers.")
