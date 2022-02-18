# Name: Fady Elsayed
# Date: Mar 19 2021
# File Name: 3.5 Day two, 2.py
# Description: A program that asks user for marks and outputs the average.
# Test cases: I used the marks, 50, 30, 20.

# Process: Sets values.
total = 0
mark_amount = 0
mark = 0

# Process: Loops code and tells user how to get average.
print("type -1 to get mark average")
while True:
    try:

# Process: checks if marks are vaild and might print avergage mark.
        while mark != -1:
            mark = int(input("Enter the your mark: "))
            
            if mark == -1:
                avg = total / mark_amount
                print("\nYour average mark is", str(round(avg, 3)) + "%.")
                
            if mark == -1:
                False
                break
            elif mark >= 0 and mark <= 100:
                mark_saved = mark
                total += mark
                mark_amount += 1
            else:
                print("\nplease enter a number between 0-100!\n")
        
# Process: Error checks.
    except:
        print("\nplease enter a number between 0-100!\n")

# Output: prints average mark.
if mark == -1:
    avg = total / mark_amount
    print("Your average mark is", str(round(avg, 3)) + "%.")
      
