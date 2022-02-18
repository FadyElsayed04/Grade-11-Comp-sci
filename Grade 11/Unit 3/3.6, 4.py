# Name: Fady Elsayed
# Date: Mar 20 2021
# File Name: 3.6, 4.py
# Description: A program to generate a pattern with a given odd number.
# Test cases: I used many odd and even mnumbers.


# Process: Sets even to True.
odd = False

# Input: Gets users number and asks again if user entered an odd number
while odd == False:
   num = int(input("Enter a odd number: "))
   while num % 2 == 0:
      num = int(input("Invailed Please Try Again!\nEnter a odd number: "))
      if num % 2 == 1:
         odd = True
   odd = True
   
# Process: Prints the pattern.
print()
numberOfRows = (num - 1) // 2 + 1
for i in range(0, numberOfRows):
    print(" "*(2 + numberOfRows-i), "*", end="")
    
    for j in range(1, i+1):
        print("**", end="")
        
    print("")
    
# Process: Sets vaues.
k = 0
l = 0

# Process: Prints the pattern.
for i in range(1, numberOfRows):
    l += 1
    k += 1
    print(" "*(3 + l), "*", end="")
    
    for j in range(1, numberOfRows - k):
        print("**", end="")
        
    print("")
