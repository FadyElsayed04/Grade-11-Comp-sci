# Name: Fady Elsayed
# Date: Apr 6, 2021
# File Name: 5.1 Day two, 2b.py
# Description: A Program that adds random numbers from 1 to 5, into a list And
# determines if the list is in descending order.

import random

# Process: Function is created with a list with random values between 1 and 5.
def random_list():
    alist = []

# Process: Loops five times.
    for i in range(5):
        num = random.randint(1,5)
        alist.append(num)
        
# Process: Determines if list is in descending order.
    if alist[0] >= alist[1]:
        if alist[1] >= alist[2]:
            if alist[2] >= alist[3]:
                if alist[3] >= alist[4]:
                    print("The list is in a descending order!")

# Output: Prints list.
    print(alist)

# Main program
random_list()
