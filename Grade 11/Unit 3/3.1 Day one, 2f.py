# Name: Fady Elsayed	
# Date: March, 5, 2021	
# File Name: 3.1 Day one, 2f.py
# Description: prints a countdown from user input to 1,
# followed by the message Blast off!
# Test cases: I used the number 20 for sart of countdown.

# input: Gets user unput for length of countdown.
num = int(input("Please enter the start of the countdown: "))
            
# Process: Calculates how where countdown will begin.
for n in range(num, 0, -1):

# Output: prints a countdown.
        print(n)
print("BLAST OFF!")
