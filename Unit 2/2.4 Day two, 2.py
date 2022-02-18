# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.4 Day two, 2.py
# Description: A program to determine the correct title for a medical conference.
# Test cases: I used name Fady Elsayed and the numbers 1,0 to answer the questions.


# Input: gets the user information
last_name = input("Please enter your last name: ")
docter = int(input("Are you a docter? (yes=1/no=0): "))


# Output: prints the users title, and asks gender if needed.
if docter == 0:
    gender = int(input("Please enter your gender (male=1/female=0): "))
    
    if gender == 1:
        str(print("\nMr." + last_name))
        
    elif gender == 0:
        str(print("\nMs." + last_name))
        
else:
    str(print("\nDr." + last_name))
