# Name: Fady Elsayed	
# Date: February 24, 2021	
# File Name: 2.1 Day one, 2.py
# Description: A program to say hello to the user if the user
# has a different name than "Fady".
# Test cases: I used the name Sam, and Fady.

# Input – Get user input for a name.
user_name = input("Please enter your name: ")

# Process - set my own name.
my_name = ("Fady")

# Output – Print the message.
print("")

if user_name == my_name:
        print("Thats my name!")
        
else:
        print("Hello," , (user_name) + "!")

