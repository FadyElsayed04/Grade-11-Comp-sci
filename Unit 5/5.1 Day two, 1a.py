# Name: Fady Elsayed
# Date: Apr 6, 2021
# File Name: 5.1 Day two, 1d.py
# Description: A Program to return a list which holds the numbers from 1 to n.

# Process: Creates funtion to hold list
def linear_list(n):
    alist = []

# Process: Loops within a range.
    for i in range(1, n+1):

# Process: Adds the looped range to the list.
        alist.append(i)
    return alist
    
# Main program
num_linear_list = linear_list(8)
print(num_linear_list)
