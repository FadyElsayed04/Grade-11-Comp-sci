# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.2 Day one 2.py
# Description: Program uses a function to determine volume, using 
# length, width and height.

import math
# Process: Calculate the volume of a prism given length, width and height.
def v_rect_prism(length, width, height):
        volume = length * width * height
        return volume

# Main program
volume = v_rect_prism(4,5,10)

# Output: Prints volume
print(volume)
