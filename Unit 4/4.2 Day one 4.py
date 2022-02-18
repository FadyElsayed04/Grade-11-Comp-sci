# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.2 Day one 4.py
# Description: Program uses a function to determine time, using velocity and height.

import math
# Process: Function is created and uses the quadratic formula to find time.
def find_time(v, h):
    time = ((-1) * v - (math.sqrt(v ** 2 - (4 * -4.9 * h)))) / -9.8

# Process: Returns value of time.
    return time

# Main program
t = find_time(10, 1)

# Output: Prints time
print(round(t, 2))
