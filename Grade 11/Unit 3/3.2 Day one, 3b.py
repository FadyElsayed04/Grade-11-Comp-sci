# Name: Fady Elsayed	
# Date: March, 9, 2021	
# File Name: 3.2 Day one, 3b.py
# Description: A program that verifies if the users name is Tim or Sam.
# Test cases: I used the names: Sam, Tim, Fady.

# Input: Asks for users name.
name = input("Enter your name: ")

# Process: Prints if Name is Tim or sam, otherwise will ask for name again.
while name != "Tim" and name != "Sam":
  print("You are not Tim/Sam.")
  name = input("\nEnter your name: ")
else: 

# Output: prints if the user is Tim or sam.
  print("You are", (name))
