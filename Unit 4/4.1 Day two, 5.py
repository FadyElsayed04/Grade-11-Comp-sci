# Name: Fady Elsayed
# Date: Mar 23 2021
# File Name: 4.1 Day two, 5.py
def area(a, b, c):
    import math
    z = ((a + b + c) / 2)
    areaNum = math.sqrt(z * (z - a) * (z - b) * (z - c))
    print("The area is", areaNum)

# Main Program
area(3, 4, 5)
