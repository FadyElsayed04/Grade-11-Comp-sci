# Name: Fady Elsayed	
# Date: March, 1, 2021	
# File Name: 2.1 Day two, 3.py
# Description: A program to test the user on the concept of the modulo operator,
# Test cases: I used: 9, 6, and 3, and i also used 7, 9, and 23.

# Input – gets user input for numbers, and answer.
num1 = int(input("please enter a number: "))
num2 = int(input("please enter a second number "))

num1str = str(num1)
num2str = str(num2)
print("\nPlease enter the answer to", num1str, "mod", num2str + ":")
user_answer = int(input(""))

# Process - calculates answer.
answer = num1 % num2

# Output – prints the correct anser and explains why or says the user is correct.
print("")
if user_answer == answer:
    print("Correct")
else:
    print("The correct answer is:", answer, "\n" + num1str, "mod", num2str, \
          "works by getting the remainder of the two numbers.")
