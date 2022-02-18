# Name: Fady Elsayed
# Date: Mar 22 2021
# File Name: 4.1 Day one, 4.py
# Description: A program to ask for the name
# Fady and ends the program once user enters Fady.
# Test Cases: I used the names: Fady, and Joe.

# Process: Creates function.
def check_name():
    user = False
    while user == False:
# Process: asks the user for name.
        name = input("Please enter your name: ")
# Process: If the users is 'Fady' loop ends.
        if name == "Fady":
            user = True
# Main Program.
check_name()
