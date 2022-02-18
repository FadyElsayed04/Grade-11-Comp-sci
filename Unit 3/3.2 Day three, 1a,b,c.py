# Name: Fady Elsayed	
# Date: March, 10, 2021	
# File Name: 3.2 Day three, 1a,b,c.py
# Description: A Program contains 3 usernames and passwords. It checks to
# see if the user enters the correct info. If the user fails to enter the
# correct info 3 times, the program locks the user out.
# Test Cases: Tested with multiple usernames and passwords. 


# Input: Asks the user for their credentials
user_name = input("Please enter your username: ")
password = input("Please enter your password: ")

# Process: Sets tries to 0 and determines what conditions the following
# code will run
tries = 1

while tries < 3:
    
# Output: Prints "Correct username and password" if the correct 
# credentials are given.      
    if (user_name == "Fady" and password == "Fady123") or (user_name == "Tim" \
                        and password == "Tim123"):
        print("\nCorrect username and password.")
        break
    
    else:

# Output: Tells user that the credentials they entered are incorrect.
        print("\nInvalid Username or Password!")

# Input: Asks the user for their credentials again
        user_name = input("Please enter your username: ")
        password = input("Please enter your password: ")

# Process: Adds 1 to "tries".
        tries += 1
        

if tries == 3:
    print("\nYou have intered your username or password wrong too many times,\
This account is temporarily locked out.")
