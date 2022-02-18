# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day two, 2.py
# Description: A program that asks for the pressure in each tire
# and then writes out if the inflation is ok.
# Test cases: I used the numbers 50, and 45.


# Input: Gets user input for bank balances.
front_right_tire = float(input("Enter right front pressure: "))
front_left_tire = float(input("Enter left front pressure: "))

back_right_tire = float(input("Enter right back pressure: "))
back_left_tire = float(input("Enter left back pressure: "))

# Output: 
if front_right_tire == front_left_tire and back_right_tire == back_left_tire:
    print("\nInflation is OK")
    
else: 
    print("\nInflation is NOT OK")
