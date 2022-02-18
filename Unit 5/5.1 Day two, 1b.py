# Name: Fady Elsayed
# Date: Apr 6, 2021
# File Name: 5.1 Day two, 1b.py
# Description: A Program to return a list which contains the numbers withen a
# range.

import random

# Process: Creates funtion to hold list.
def random_list(n, x, y):
    alist = []

# Process: Loops within the range.
    for i in range(n):
        num = random.randint(x, y)

# Process: Adds the random numbers in the range to the list.
        alist.append(num)
    return alist

# Main program
create_random = random_list(10, 3, 12)
print(create_random)
