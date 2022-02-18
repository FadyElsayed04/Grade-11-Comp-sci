# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.2 Day two 1.py
# Description: Program uses a function to create the full name from a first and last name. 

import math
# Process: Creates full name when given first and last name.
def get_names(first_name, last_name):
        full_name = (first_name + " " + last_name)
        return full_name

# Main program
first_name = input("please enter your first name: ")
last_name = input("please enter your last name: ")
full_name = get_names(first_name, last_name)

# Output: Prints full name
print(full_name)
