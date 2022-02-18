# Name: Fady Elsayed
# Date: Mar 31 2021
# File Name: Unit 4 Assignment.py
# Description: A program that calculates both the sum of the first n
# integers and the sum of the squares of the first n inegers. The program can
# also be terminated and does not allow invailed numbers to be inputed.
# Test Cases: I used the numbers 10, 3, -10, -1, 0, 232.

# Process: Creates function to calculate the sum of the first n integers or
# squares.
def fancy_sum(num):
    total_sum = 0
    total_square = 0
    for i in range (1, num+1):
        total_sum += i
        total_square += i ** 2
        
# Process: Returns values for sums.
    return total_sum, total_square

# Output: prints an intro/title to the program.
print("Welcome to the Fancy Sum Program. Enter a positive integer or -1 to \
quit.")

# Process: Sets values.
num = 0

# Process: loops program until user enters -1.
while num != -1:
    
# Input: Asks user for number
    try:
        num = int(input("\nEnter number: "))
    
# Main Program: Runs function and gets values of sums.  
        total_sum, total_square = fancy_sum(num)
            
# Process: Error checks and make sure the number is above or
# equal to 1 or if the number is -1.
        if num != -1:
            if num > 0:
                
# Output: Prints the sums of the first n intergers/squares.
                print("The sum of the first", num, "integers is:", total_sum)
                print("The sum of the first", num, "squares is:", total_square)
                
# Output: Lets user know a invailed integer was entered.
            else:
                print("Please enter an integer greater than or equal to 1.")
                
# Output: Lets user know program was ended.              
        else:
            print("Program Terminated")

# Process; Error checks to only allow valid inputs.
    except:
        print("Please enter an integer greater than or equal to 1.")
