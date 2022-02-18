# Name: Fady Elsayed
# Date: Mar 29 2021
# File Name: 4.4 Day one 2a,b,c.py
# Description: Program uses a function to find the factorials and prints them until program is terminated.
# Test Cases: I used: 5, 0, -45, "hi"

# Process: Creates function.
def factorial(n, valid):
        
# Process: sets values.
    factorialAnswer = 1
    if valid == 1:
            
# Process:: Calculates the factorial values and returns them.
        while n >= 1:
            factorialAnswer = factorialAnswer * n
            n = n - 1
    return(factorialAnswer)

# Process: Creates function.
def get_n():
        
# Process: sets values.
        valid=0
        loop = 1
        number = 0
        
# Process: Loops program.
        while loop == 1:
                try:
# Input: asks for number amnd error checks input.
                        number = int(input("\nPlease enter your number: "))
                                        
                        valid = 1
                        answer = factorial(number, valid)
                        if number == -1:
                                loop = 0
                        elif number <= 0 and number != -1:
                                raise Exception
                        elif number != -1:
                                
# Output: Prints the factorial number and prints if an error has occured.
                                print('The factorial of ' +str(number) +' is ' +str(answer))
                       
                except:
                        number = print("Error please try again")    

# Main program
get_n()
