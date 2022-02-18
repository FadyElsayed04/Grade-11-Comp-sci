# Name: Fady Elsayed	
# Date: March, 2, 2021	
# File Name: 2.2 Day two, 3.py
# Description: A program that gives the recomended time to microwave for multiple items.
# Test cases: I used the time 60 and the items: 1, 2, and 3.

# Input – gets user input for amount of item and time 
items = int(input("Please enter the amount of items you want to microwave: "))
time = int(input("Please enter the amount of time you need to \
microwave a single item in seconds: "))

# Process - Calculates amount of time needed to microwave items for.
time2 = time + time * 0.5
time3 = time + time

# Output – prints out recomended time to microwave
if items == 1:
    print("\nYou should microwave this for:", time, "seconds.")
elif items == 2:
    print("\nYou should microwave this for:", int(time2), "seconds.")
elif items == 3:
    print("\nYou should microwave this for:", int(time3), "seconds.")
else:
    print("\nMicrowaving over 3 items is not recomended.")
