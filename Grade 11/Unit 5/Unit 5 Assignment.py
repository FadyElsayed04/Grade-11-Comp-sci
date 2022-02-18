# Name: Fady Elsayed
# Date: Apr 21, 2021
# File Name: Unit 5 Assignment.py
# Description: A program that generates 10 random numbers between 1 to 10 and
# stores them into a list. The program returns the median of the list, the
# smallest and largest numbers in the list, and the amount of numbers greater
# than 5.
# Test Cases: Program is accurate. 

import random

# This function generates 10 random numbers between 1 and 10 and stores them
# in a list.
def random_ten():
    global random_list
    random_list = []
    
    for i in range (10):
        num = random.randint(1,10)
        random_list.append(num)

    return random_list


# This function calculates and returns the median of the list.
def median_list(random_list):
    global median_of_list
    sorted_list = sorted(random_list)
    median_of_list = (sorted_list[4] + sorted_list[5]) / 2
    
    return median_of_list


# This function calculates the largest and smallest number of the
# list and returns them.
def largest_and_smallest(random_list):
    global largest_num, smallest_num
    smallest_num = min(random_list)
    largest_num = max(random_list)

    return largest_num, smallest_num


# This function calculates and returns the amount of numbers larger than 5
# in the list.
def greater_than_five(random_list):
    global greater_than_five_list
    greater_than_five_list = []
    
    for i in random_list:
        if i > 5:
            greater_than_five_list.append(i)
          
    return greater_than_five_list


# Main Program

# Input: Calls the function that generates a list of random numbers from 1-10.
random_nums = random_ten()

# Process: Calls the functions that calculate the median of the list, the
# amount of integers greater than 5, and the largest and smallest number.
median_list(random_list)
largest_and_smallest(random_list)
greater_than_five(random_list)

# Output: Prints the list.
print(random_list)

# Output: Prints the median of the list.
print("\nThe median of the List is:", median_of_list)

# Output: Prints the smallest number in the list.
print("The smallest number is:", smallest_num)

# Output: Prints the largest number in the list.
print("The largest number is:", largest_num)

# Output: Prints the amount of numbers greater than 5 in the list.
print("There are", len(greater_than_five_list), "numbers greater than 5.")
