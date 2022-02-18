# Name: Fady Elsayed	
# Date: February 22, 2021	
# File Name: Exercise2.3_address.py	
# Description: A program to format an address for a postcard.
# Test cases: I Used my own address,
# 7373 Doverwood Dr. Mississauga, Ontario, L5N 6N4.

# Input – Get user input for address.
province = input("Please enter your province:")
postal_code = input("Please enter your postal code:")
city = input("Please enter your city:")
street_name = input("Please enter your street name:")
street_number = input("Please enter your street number:")

# Output – Print the address.
print("")
print(street_number, street_name)
print(city + ",", province)
print(postal_code)
