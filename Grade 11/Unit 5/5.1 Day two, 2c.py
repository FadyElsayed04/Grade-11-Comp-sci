# Name: Fady Elsayed
# Date: Apr 6, 2021
# File Name: 5.1 Day two, 2c.py
# Description: A Program that prints the sum of n amount of two list length.

# Process: Creates a function to determine sum of two lists.
def list_length():

    alist = []
    blist = []

# Input: Asks the user for the lengths of each list.
    list_length1 = int(input("Please enter the length of the 1st list: "))
    list_length2 = int(input("Please enter the length of the 2nd list: "))

# Process: Loops numbers from 1 to n, and adds numbers to the list.
    for i in range(1,list_length1 + 1):
        alist.append(i)
        
# Process: Loops numbers from 1 to x, and adds numbers to the list.
    for i in range(1,list_length2 + 1):
        blist.append(i)

# Process: Adds the two lists.
    sum_lists = alist + blist

# Output: Prints the sum of the two lists
    print("The two lists added together is", str(sum_lists) + ".")

# Main program
list_length()
    
    
