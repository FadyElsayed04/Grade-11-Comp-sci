# Name: Fady Elsayed
# Date: Apr 9, 2021
# File Name: 5.3 Day one, 1b.py

def get_int():
    alist = []
    num = 0
    vowel_count = 0
    while num != -1:
        try:
            num = int(input("How many letters would you like to enter?: "))
            for i in range (1, num+1):
                user_letter = input("Please enter a UPPERCASE letter. \
Type 'Done' to quit: ")
                alist.append(user_letter)

                if user_letter == "A" or user_letter == "E" or \
                   user_letter == "I" or user_letter == "O" or \
                   user_letter == "U":
                    vowel_count += 1
                    
                elif user_letter == "Done":
                    num = -1
                pass
            if user_letter == "Done":
                num = -1
                pass        
                
        except:
            print("Invalid number!")
    print(alist)

# Main program
alist = get_int()

    
