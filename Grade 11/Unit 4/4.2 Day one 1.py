# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.2 Day one 1.py
# Description: Program uses a function to find the area of a circle
# with the radius.

import math
# Process: Calculate the area of a circle given the radius
def area_circle(r):
        area = math.pi * r**2
        return area

# Main program
area1 = area_circle(1)
area2 = area_circle(5)
print(area1, area2)
