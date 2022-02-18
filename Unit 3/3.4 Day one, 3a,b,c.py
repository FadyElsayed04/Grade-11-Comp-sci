# Name: Fady Elsayed	
# Date: March, 15, 2021	
# File Name: 3.4 Day one, 3a,b,c.py
# Description: A Program that flips a coin 20 times and calculates the amount
# of sequence changes, consecutive tosses, and number of heads and tails flipped.

import random

# Process: Sets values to 0
heads = 0
tails = 0

heads_con = 0
tails_con = 0

head_con_score = 0
tail_con_score = 0
change = 0
change_amount = 0

# Process: Determines how much this loop will run.
for flips in range(20):

# Process: Determines if the coin is heads or tails.
    coin = random.choice("TH")
    
# Output: If the coin is heads, the program will print heads.
    if coin == "H":
        print("Heads")

# process: calculates the heads and tails, and amount of consecutive tosses.
        heads += 1
        flips += 1
        heads_con += 1
        tails_con = 0
        if heads_con > head_con_score:
            head_con_score = heads_con
            
# process: calculates the amount of sequence changes.        
        if flips == 1:
            change = coin
        if change != coin:
            change_amount += 1
        change = coin
# Output: If the coin is tails, the program will print tails.       
    if coin == "T":
        print("Tails")
        
# process: calculates the heads and tails, and amount of consecutive tosses.
        tails += 1
        flips += 1
        heads_con = 0
        tails_con += 1
        if tails_con > tail_con_score:
            tail_con_score = tails_con
            
# process: calculates the amount of sequence changes.
        if flips == 1:
            change = coin
        if change != coin:
            change_amount += 1
        change = coin

# Output: Prints the amount of heads and tails flipped, the amount the sequence
# changed, and the consecutive coin tosses.
print("")            
print(heads, "heads and", tails, "tails flipped.")

print("The sequence changed", (change_amount), "times.")

print("There was", head_con_score, "consecutive head tosses.")
print("There was", tail_con_score, "consecutive tail tosses.")
