# Name: Fady Elsayed	
# Date: March, 2, 2021	
# File Name: 2.1 Day two, 4.py
# Description: A program to Tell the user if the number they inserted
# is even or odd.
# Test cases: I used the numbers: 4 and 5.

# Input – gets user input for numbers, and answer.
user_num = int(input("Enter a positive number: "))

# process - does the math to figure out if the number is even or odd.
if (user_num % 2) == 0:
    
# output - prints if the number is even or odd.
   print(user_num, "is a even number")
else:
   print(user_num, "is a odd number")
