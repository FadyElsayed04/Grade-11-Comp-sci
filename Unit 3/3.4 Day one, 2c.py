# Name: Fady Elsayed	
# Date: March, 15, 2021	
# File Name: 3.4 Day one, 2c.py
# Description: A Program that gets 2 random letters from "FADY"
# and checks if they are the same.



# Process: Gets 2 random letters from my name.
import random
letter1 = random.choice("FADY")
letter2 = random.choice("FADY")

# Output: prints 2 random letters from my name.
print(letter1, letter2)

# Output: Checks if the 2 random letters from my name match and if so print.
if letter1 == letter2:
    print("Both letters are the same.")
else:
    print("The letters are not the same.")
