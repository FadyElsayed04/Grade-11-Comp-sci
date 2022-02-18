# Name: Fady Elsayed	
# Date: March, 4, 2021	
# File Name: Unit 2 assignment.py
# Description: A programm that determines whether a givin point is on a the
# given slope with the equation y = mx+b.
# Test cases: I used the numbers: 3,4,1,7 and 1,-2,10,-6.

# Input: gathers user input for slope, y intercept, X intercept, and x and y
# coordinates.
slope = int(input("Please enter the slope of the line: "))
y_inter = int(input("Please enter the y-intercept of the line: "))
x_coord = int(input("Please enter the x-coordinate of the line: "))
y_coord = int(input("Please enter the y-coordinate of the line: "))

# Process: This calclulates the mx + b part of y = mx + b
coordinate = slope * x_coord + y_inter

# Output: Prints the equation and if the point is on the line if y = mx + b
print("\nThe equation of the line is: y =", str(slope) + \
      "x +", str(y_inter))

if coordinate == y_coord:
    print("The point (" + str(x_coord) + "," + str(y_coord) + \
               ") is on the line.")
else:
    print("The point (" + str(x_coord) + "," + str(y_coord) + \
               ") is not on the line.")
