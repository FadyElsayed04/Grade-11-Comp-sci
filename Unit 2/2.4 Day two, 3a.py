# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.4 Day two, 3a.py
# Description: A program to determine the correct discount plasma and LCD TVS.
# Test cases: I used yes, no, and 30, 42.


# Input: gets the tv information.
plasma = input("Is it plasma TV?(yes/no): ")



# Output: prints the discount for the TV.
if plasma == "no":
    size = int(input("what is the size of the TV?): "))
    
    if size == 30:
        print("\nThere is a 8% discount.")
        
    elif size == 42:
        print("\nThere is a 10% discount.")
              
    else:
        print("\nThere is no discount on this TV.")
        
elif plasma == "yes":
    print("\nThere is a 5% discount.")
