# Name: Fady Elsayed
# Date: Mar 24 2021
# File Name: 4.2 Day one 2.py
# Description: Program uses a function to find the surface area of a circle
# with the radius and hieght.

import math
# Process: Calculate the surface area of a circle given the radius and hieght.
def sa_cylinder(r,h):
        sa_area = 2 * math.pi * r * h + 2 * math.pi * r ** 2
        return sa_area

# Main program
sa_area1 = sa_cylinder(10,4)
sa_area2 = sa_cylinder(1,1)

# Output: Prints surface area
print(sa_area1, sa_area2)
