# Name: Fady Elsayed
# Date: Mar 20 2021
# File Name: Unit 3 test
# Description: A program to generate a random number between 1-100. This program
# will allow the user to guess the number with an option to quit. The program
# also includes clues to help the user guess.
# Test cases: I used many numbers from 1-100. I also used letters, -1
# and random numbers outside the range.

import random

# Process: Sets values.
won = False
num_tries = 0
num_to_guess = random.randint(1, 100)
stop = False
first = True
# Process: gives the user an option to quit the program.

print("Please enter -1 to quit the program.")

# Process: runs a while loop to get the first number from the user and sees if
# the user wants to quit, got the number right, or if the number is out
# of range.
while first == True:
    try:
        guess = int(input("\nGuess a number between 1 and 100: "))
        num_tries += 1
        if guess == -1:  
            print("Have a nice day!")
            stop = True
            break
        if guess == num_to_guess:
            won = True
            break
        if stop == False:
            print("The random number is:", num_to_guess) 
            
            if guess in range(1,100):
                if guess != num_to_guess:
                    print("This is the first time you ran the program and your guess is incorrect.")
                    break
            if guess not in range(1,100):    
                print("invalid number please try again!\n")
    except:
        print("The random number is:", num_to_guess, "\ninvalid number please try again!\n")

# Output: prints if the user got the number right.
if guess == num_to_guess and num_tries == 1:
    print("You are correct! you took", num_tries, "try to guess", str(num_to_guess) + ".")
    
if guess == num_to_guess and num_tries != 1:
    print("You are correct! you took", num_tries, "tries to guess", str(num_to_guess) + ".")
last_guess = guess

# Process: runs a while loop to get the other numbers from the user and sees if
# the user wants to quit, got the number right, gives clues towards the correct anwser or if the number is out
# of range.
while stop == False:
    try:
        guess = int(input("\nGuess a number between 1 and 100: "))
        num_tries += 1
        if guess == -1:  
            print("Have a nice day!")
            stop = True
            break
        if guess == num_to_guess:
            won = True
            break
        if stop == False:
            print("The random number is:", num_to_guess) 
            
        if guess not in range(1,100):    
            print("invalid number please try again!\n")

            
        while guess != num_to_guess:

            if guess > last_guess and guess > num_to_guess:
                print("Your guess is further away.")
                break
            elif guess < last_guess and guess < num_to_guess:
                print("Your guess is further away.")
                break
            elif guess > last_guess and guess < num_to_guess:
                print("Your guess is getting closer.")
                break
            elif guess < last_guess and guess > num_to_guess:
                print("Your guess is getting closer.")
                break
            elif guess == last_guess:
                print("You already guessed this!")
                break
        
        last_guess = guess
        
    except:
        print("The random number is:", num_to_guess, "\ninvalid number please try again!\n")

# Output: prints if the user got the number right.

if guess == num_to_guess and num_tries == 1:
    print("You are correct! you took", num_tries, "try to guess", str(num_to_guess) + ".")
    
if guess == num_to_guess:
    print("You are correct! you took", num_tries, "tries to guess", str(num_to_guess) + ".")
