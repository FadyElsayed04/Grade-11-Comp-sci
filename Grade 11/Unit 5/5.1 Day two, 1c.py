# Name: Fady Elsayed
# Date: Apr 6, 2021
# File Name: 5.1 Day two, 1c.py
# Description: A Program to return a list which contains n amount of intergers.

# Process: Function is defined for a list.
def user_list(n):
    alist = []

    # Input: Asks user for number n.
    num = int(input("Enter number: "))

    # Process: Loops n amount of times.
    for i in range (1, num+1):

        # Process: Adds numbers in range of loop to the list.
        alist.append(i)
    return alist

# Main program
nlist = user_list(1)
print(nlist)
