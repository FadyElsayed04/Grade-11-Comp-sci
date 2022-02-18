# Name: Fady Elsayed
# Date: Mar 29 2021
# File Name: 4.4 Day one 1a,b,c,d.py
# Description: Program uses a function to find the area, and circumference of a circle
# with the radius.
# Test Cases: I used: 5, 12, yes, no, hi.

# Process: Inports math and sets values.
import math
play_again = True

# Process: Calculate the area of a circle given the radius
def area_circle(radius):
        area = math.pi * radius**2
        return area

# Process: Calculate the circumference of a circle given the radius
def cir_circle(radius):
        circumference = 2 * math.pi * radius
        return circumference

# Main program

# Process: Loops program.
while play_again == True:
        
# Process: Sets values.
        check = True
        valid = False
        
# Process: Runs loop to get to get vaild input.
        while check == True:
                try:
                        radius = input("Please enter a radius: ")
                        radius = int(radius)
                        check = False
                except:
# Output: Prints error.
                        print("Error please try again\n")
                        
# Process: Runs function to get area and circumference.
        area = area_circle(radius)
        circumference = cir_circle(radius)
# Output: Prints radius, area, and circumference.
        print("\nThe radius is:", radius)
        print("The area is:", round(area,2))
        print("The circumference is:", round(circumference,2))
# Process: Runs loop to get to get vaild input.
        while valid == False:
# Process: Asks to play again.
                again = input("\nDo you want to play again?: ")
                if again == "no":
                        play_again = False
                        valid = True
                elif again == "yes":
                        valid = True
                        check = True
                else:
# Output: Prints error.
                        print("Error please try again")
                
                
