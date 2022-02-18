# Name: Fady Elsayed
# Date: Mar 29 2021
# File Name: 4.4 Day one 3a,b,c.py
# Description: Program uses a function to find if the n amount of numbers are
# even or odd
# Test Cases: I used: 5, 12, 50, hi, yes, no.

# Process: sets values.
play_again = True
import random

# Process: prints random numbers and checks which numbers are even.
def is_even(number):
        count = 0
        print()
        for i in range(1, number + 1):
                rand = random.randint(1,101)
                print(rand)
                if rand % 2 == 0:
                        count += 1
# Process: returns count.
        return count

# Process: Loops program.
while play_again == True:
        
# Process: Sets values.
        check = True
        valid = False
        
# Process: Runs loop to get to get vaild input.
        while check == True:
                try:
                        number = input("Please enter a number: ")
                        number = int(number)
                        check = False
                except:
# Output: Prints error.
                        print("Error please try again\n")
                        
# Process: Runs function to get even and odd number. Prints the random numbers
# Main program
        even = is_even(number)

# Process: calculates odd numbers.
        odd = number - even
        
# Output: Prints the amount of numbers that is even and odd.
        print("\nThere were", even, "even numbers and", odd, "odd numbers.")
        
# Process: Runs loop to get to get vaild input.
        while valid == False:
                
# Process: Asks to play again.
                again = input("\nDo you want to play again?(yes/no): ")
                if again == "no":
                        play_again = False
                        valid = True
                elif again == "yes":
                        valid = True
                        check = True
                        
# Output: Prints error.
                else:
                        print("Error please try again")
