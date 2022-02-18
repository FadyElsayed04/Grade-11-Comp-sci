# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.4 Day one, 2.py
# Description: A program to determine if any of the three numbers is a 
# multiple of the other two.
# Test cases: I used numbers 12,15,8 and 12,13,15 and 8,12,5


# Input: gets the temp from the user.
temp = int(input("Please enter a temperature: "))

# Process: sets the max and min temp.
max_temp = 100
min_temp = 5

# Output: Outputs if the porridge is too hot, cold, or just right.
if temp <= max_temp and temp >= min_temp:
    if temp < 10:
        print("Too cold")
    elif temp > 10:
        print("Just right")
    else:
        print("Too hot")
else:
    print("Temp is not valid")
