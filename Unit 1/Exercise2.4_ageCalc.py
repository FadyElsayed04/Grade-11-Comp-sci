# Name: Fady Elsayed	
# Date: February 22, 2021	
# File Name: Exercise2.4_ageCalc.py
# Description: Asks the users for their name, age, and current year, then tells the user what year they would be 25, 50, and 75
# Test cases: I Used my own name and age, Fady Elsayed.

# Input – Get user age, name, and current year.
user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))
current_year = int(input("Please enter the current year: "))

# Process – Calculate the years the user will be 25, 50, and 75.
a = (25-user_age) + current_year
b = (50-user_age) + current_year
c = (75-user_age) + current_year

# Output – Print the name, age, and year the user will be 25, 50, and 75.
print("\n")
print("Hello ", user_name, ".", " I see that you are"," ", user_age," ", "years old.", sep="")
print("")
print("You will be 25 at:",a)
print("You will be 50 at:",b)
print("You will be 75 at:",c)
