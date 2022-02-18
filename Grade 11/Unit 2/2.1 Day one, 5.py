# Name: Fady Elsayed	
# Date: February 25, 2021	
# File Name: 2.1 Day one, 5.py
# Description: A program to test the user on math questions then letting
# the user know what the answer is if they got it wrong.
# Test cases: I used the answers 12, 54, 32, 15, 22, 56



# Input – get users answer for A.
print("17 + 37 = A")
print("")
user_answer_one = int(input("What is A?: "))

# Process - calculates the math.
answer_one = 17 + 37

# Output – Displays if the user's answer is correct and if not,
# it displays the correct answer.
if answer_one == user_answer_one:
    print("You are correct")
else:
    print ("The correct answer is: " , answer_one)
print("")



# Input – get users answer for B.
print("27 - 12 = B")
print("")
user_answer_two = int(input("What is B?: "))

# Process - calculates the math.
answer_two = 27 - 12

# Output – Displays if the user's answer is correct and if not,
# it displays the correct answer.
if answer_two == user_answer_two:
    print("You are correct")
else:
    print ("The correct answer is: " , answer_two)
print("")



# Input – get users answer for C.
print("8 * 7 = C")
print("")
user_answer_three = int(input("What is C?: "))

# Process - calculates the math.
answer_three = 8 * 7

# Output – Displays if the user's answer is correct and if not,
# it displays the correct answer.
if answer_three == user_answer_three:
    print("You are correct")
else:
    print ("The correct answer is: " , answer_three)
print("")
