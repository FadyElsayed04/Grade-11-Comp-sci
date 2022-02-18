# Name: Fady Elsayed
# Date: Apr 6, 2021
# File Name: 5.1 Day two, 2a.py
# Description: A Program to return a list which contains n amount of intergers.

# Process: Creates function that asks user for 10 integers
def user_list():
    user_sum = 0
    alist = []

# Process: Loops input, finds sum, amount of input.
    for i in range(10):

# Input: Asks user for any number
        user_num = int(input("Please enter a number: "))

# Process: Adds all input values together to calculate sum.  
        user_sum += user_num

# Process: Adds all input values to the list.
        alist.append(user_num)

# Process: Calculates average of the values.   
    avg = user_sum / (len(alist))

# Output: Prints the list, and calculations.
    print(alist)
    print("\nThe sum is:", user_sum)
    print("The average is:", avg)
    print("The highest value is:", max(alist))
    print("The lowest value is:", min(alist))

# Main program
user_list()

