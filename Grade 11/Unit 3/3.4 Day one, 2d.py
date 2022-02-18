# Name: Fady Elsayed	
# Date: March, 15, 2021	
# File Name: 3.4 Day one, 2d.py
# Description: A Program that gets 3 random letters 
# and checks if 2 are vowels.



# Process: Gets 2 random letters from my name.
import random
letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num = 0

print("The letters are:", letter1, letter2, letter3)

# Process: Checks if 2 of the random letters are vowels.
if letter1 == "A" or letter1 == "E" or letter1 == "I" or letter1 \
   == "O" or letter1 == "U":
    num += 1
    
if letter2 == "A" or letter2 == "E" or letter2 == "I" or letter2 \
   == "O" or letter2 == "U":
    num += 1

if letter3 == "A" or letter3 == "E" or letter3 == "I" or letter3 \
   == "O" or letter3 == "U":
    num += 1
    
if num == 2:

# Process: Prints if there are only 2 vowels.
    print("\nThere are exactly two letters are vowels.")
