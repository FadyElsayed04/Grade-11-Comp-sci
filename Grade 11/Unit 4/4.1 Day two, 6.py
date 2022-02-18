# Name: Fady Elsayed
# Date: Mar 23 2021
# File Name: 4.1 Day two, 6.py
def angle(a, b, c):
    import math
    angleAcalc = (b*b + c*c - a*a)/2*(b*c)
    angleA = math.acos(angleAcalc)
    angleAFinal = math.floor(angleA)
    print("The angle is", angleAcalc)

# Main Program
angle(3, 4, 5)
