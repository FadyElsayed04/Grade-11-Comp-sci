# Name: Fady Elsayed
# Date: Mar 19 2021
# File Name: 3.4 Day two, 2.py
# Description: A program that allows the user to play the
# game “Rock, paper, scissors” against the computer.
# Test cases: I used r, s , p.

# Process: sets values.
import random
num_games = float('inf')
cpu = random.choice("rps")

# Process: Loops to play the game, and asks to play again.
while True:
    cpu = random.choice("rps")
    
    try:
        player = str(input("\nRock, Paper, or Scissors? (r,p,s): "))
        
    except:
        print("Enter r, p or s.")
        continue
        
    if player == "s" and cpu == "p":
        print("\nYou win, I chose:", cpu)
        
    elif player == "p" and cpu == "r":
        print("\nYou win, I chose:", cpu)
        
    elif player == "r" and cpu == "s":
        print("\nYou win, I chose:", cpu)
        
    elif player == cpu:
        print("\nWe tied! I chose:", cpu)

    elif cpu == "s" and player == "p":
        print("\nYou lost, I chose:", cpu)
        
    elif cpu == "p" and player == "r":
        print("\nYou lost, I chose:", cpu)
        
    elif cpu == "r" and player == "s":
        print("\nYou lost, I chose:", cpu)
    else: 
        print("\nYou didn't enter a correct letter! Please play again.", cpu)

# Process: Determines if the user wants to play again.        
    play_again = str(input("\nPlay again? (yes/no): "))
    
    while play_again == "yes":
        cpu = random.choice("rps")
        
        try:
            player = str(input("\nRock, Paper, or Scissors? (r/p/s): "))
            
        except:
            print("Enter r, p or s.")
            continue

        if player == "r" and cpu == "s":
            print("\nYou won! I chose:", cpu)

        elif player == "p" and cpu == "r":
            print("\nYou won! I chose:", cpu)
            
        elif player == "s" and cpu == "p":
            print("\nYou won! I chose:", cpu)
            
        elif player == cpu:
            print("\nWe tied! I chose:", cpu)
            
        else:
            print("\nYou lost, I chose:", cpu)
            
        play_again = str(input("\nWant to play again? (yes/no): "))

# Process: Breaks the loop if the user does not want to play again.
    while True:
       if play_again == "no":
           print("\nGoodbye!")
           break
       elif play_again == "yes":
           print("")
           break
       else:
           print("\nYou didn't enter a correct letter! Try again.")
           play_again = str(input("\nWant to play again? (yes/no): "))
       
