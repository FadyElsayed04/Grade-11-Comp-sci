# Name: Fady Elsayed
# Date: Mar 22 2021
# File Name: 4.1 Day one, 5.py
# Description: A program countdown from 10.

import time

# Process: Creates function with countdown.
def count_down():
    num = 10
    while num >= 0:
        print(num)
        num -= 1
        time.sleep(1)
               
# Main Program.
count_down()
