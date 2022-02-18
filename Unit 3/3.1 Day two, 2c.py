# Name: Fady Elsayed	
# Date: March, 5, 2021	
# File Name: 3.1 Day two, 2c.py
# Description: A program that is a given an amount marks and calculates the
# average if the input given is correct.
# Test cases: I used the amount of marks 2, and the marks 80, and 78.

# Process: defines x, and sum
x = 0
sum = 0
# Input: Collecting amount of marks the user wants to average.
mark_amount = int(input("how many marks do you want to average?: "))

# Process: Determines if and how many times the loop will run.
if mark_amount > 0:
    
    for n in range (mark_amount):

# Input: Collects the marks from the user.
        mark = int(input("Please enter a mark between 0 and 100: "))
        
# Process: Makes sure user has inputed the marks correctly and calculates the \
# average.
        if mark <0 or mark >100:
            print("you have entered a incorrect mark. Please try again.")
            x = 1
            break
        
        sum += mark
        
    if x == 0:
        avg = (sum/mark_amount)

# Ouput: prints the mark average or shows a incorrect message.

        print("\nYour average mark is: " + str(avg) + "%")
else:
    print("you have entered a incorrect amount of marks. Please try again.")
