# Name: Fady Elsayed	
# Date: March, 5, 2021	
# File Name: 3.1 Day two, 2a.py
# Description: A program that reads five marks and calculates the average.
# Test cases: I used the numbers: 90, 98, 76, 77, 68.


# Process: defines the sum and determines how many times the loop will run.
sum = 0
for n in range (5):

# Input: Collects the five marks from the user.
    mark = int(input("Please enter mark: "))
    sum += mark
    avg = (sum/5)

# Ouput: prints the mark average.
print("Your average mark is: " + str(avg) + "%")
