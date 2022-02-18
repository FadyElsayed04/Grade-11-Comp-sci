# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day two, 1.py
# Description: A program that asks for the balance in each account
# and then writes out the service charge to the user.
# Test cases: I used a mix numbers of: 900, 1100, 1400, 1700.


# Input: Gets user input for bank balances.
checking_account_bal = float(input("Please enter your checking account balance: "))
saving_account_bal = float(input("Please enter your savings account balance: "))

# Output: 
if checking_account_bal >1000 or saving_account_bal >1500:
    print("\nYou dont have a service charge for checks")
    
else: 
    print("\nYour service charge is $0.15 per check")
