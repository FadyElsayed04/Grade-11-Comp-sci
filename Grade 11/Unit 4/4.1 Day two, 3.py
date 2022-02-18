# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.1 Day two, 3.py

# Process: Creates function.
def sum_first_odd(n):
    y = 0
    for i in range (1, n*2, 2):
        y += i
    print("The sum is:", y)

# Main Program
sum_first_odd(10)
