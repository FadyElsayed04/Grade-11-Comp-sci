# Name: Fady Elsayed	
# Date: March, 10, 2021	
# File Name: 3.2 Day three, 2.py
# Description: A Program that applies the Collatz algorithm until
# the number given reaches 1.
# Test Cases: I used the numbers 2, 5, and 8.

# Process: Sets count to 0.
count = 0

# Input: Asks user for number.
num = int(input("Please enter a small positive number: "))

# Input: Asks user for number again if Invalid.
while num < 1:
    num = int(input("Number Invalid. Please enter a small positive number: "))

# Process: Applies the Collatz algorithm until the number given reaches 1.
print("\n"+str(num))
start_num = num
while num > 1:
    if num % 2 == 0:
        num = num // 2
        count += 1
        
# Output: Prints the current number in the process.
        print(num)
        
# Process: Applies the Collatz algorithm until the number given reaches 1.
    else:
        num = num * 3 + 1
        count += 1
        
# Output: Prints the current number in the process and amount of iterations.
        print(num)
print("\nYour digit of", start_num, "took", count, \
      "iterations to get to the number 1.")
