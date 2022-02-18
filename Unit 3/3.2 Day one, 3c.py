# Name: Fady Elsayed	
# Date: March, 9, 2021	
# File Name: 3.2 Day 1, 3c.py
# Description: A program that verifies if the users name is Tim or Sam,
# and tells the user the amount of atempts used.
# Test cases: I used the names: Sam, Fady, Tim.

# Input: Asks for users name.
name = input("Enter your name: ")
attempts = 1

# Process: Prints if Name is Tim or sam, otherwise will
# ask for name again, and will add attempts.
while name != "Tim" and name != "Sam":
  print("You are not Tim/Sam.")
  name = input("\nEnter your name: ")
  attempts += 1
else: 

# Output: prints if the user is Tim or sam, and the amount of sttempts taken.
  print("You are", (name) + ",", "you took", str(attempts), "attempt") 
