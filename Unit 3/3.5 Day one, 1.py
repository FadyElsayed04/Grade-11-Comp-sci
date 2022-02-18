# Name: Fady Elsayed
# Date: Mar 19 2021
# File Name: 3.5 Day one, 1.py
# Description: A program that asks the user the amount of numbers they want
# to be added out of a certain range, then prints the sum.
# Test Cases: I used numbers from 1 to 10.

# Process: Sets the value for x.
x = 0

# Process: Determines conditions the code will run.
while True:
    try:

# Input: Asks the user for the amount of numbers they want to be added.
        num_sum = int(input("How many numbers do you want to be added: "))
        
# Process: Determines the conditions the code will run.
        if num_sum < 0:
            raise Exception

# Process: Creates a loop and changes the x value.
        for num_sum in range (1, num_sum + 1):
            x += num_sum

# Output: Prints the sum of the first n integers.
        print("The sum of the first", num_sum, "integers is", x)
        break

# Process: Determines under what conditions the following code will run.
    except Exception:

# Output: Tells the user if they need to enter a number greater than 0.
        print("You must enter an integer greater than 0!")
