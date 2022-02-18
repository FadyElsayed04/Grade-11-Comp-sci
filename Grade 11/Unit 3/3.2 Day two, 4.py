# Name: Fady Elsayed	
# Date: March, 9, 2021	
# File Name: 3.2 Day two, 4.py
# Description: Program displays a given message a givin amount of times.
# along with a option to terminate.
# Test cases: I used the words "hi", "hello" and "food".

# Input: Asks the user for the amount of words, the word, and if the user
# wants the program terminated.
num = int(input("Enter a small number: "))
word = input("Enter a word: ")
stop = input("Do you want to terminate the program (yes/no): ")

# Process: Determines if the program will stop and prints the word as many
# times as the user stated.
while stop == "no":
    print("\n" + num * word)
    word = input("Enter a word: ")
    
# Output: Prints goodbye.
print("\nGoodbye!")
