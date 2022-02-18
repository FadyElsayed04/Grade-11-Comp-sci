# Name: Fady Elsayed	
# Date: March, 9, 2021	
# File Name: 3.2 Day one, 3a.py
# Description: A program that verifies if the users name is Tim.
# Test cases: I used the names: Fady, Tim

# Input: Asks for users name.
inputName= input("Enter your name ")
attempts=1

# Process: Prints if Name is Tim, otherwise will ask for name again.
while inputName != "Tim":
  print("You are not Tim")
  inputName= input("Enter your name ")
  attempts+=1
else: 

# Output: prints if the user is Tim.
  print("You are Tim", "you took ",attempts," attempt") 
