# Name: Fady Elsayed	
# Date: March, 5, 2021	
# File Name: 3.1 Day two, 2a.py
# Description: A program that is a given amount marks and calculates the
# average.
# Test cases: I used the numbers: 90, 98, 76, 77, 68.

# Input: Collecting amount of marks the user has.
mark_amount = int(input("how many marks do you want to average?: "))
# Process: defines the sum and determines how many times the loop will run.
sum = 0
for n in range (mark_amount):

# Input: Collects the five marks from the user.
    mark = int(input("Please enter a mark between 0 and 100: "))
    sum += mark
    avg = (sum/mark_amount)

# Ouput: prints the mark average.
print("\nYour average mark is: " + str(avg) + "%")
