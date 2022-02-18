# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.4 Day two, 3b.py
# Description: A program to determine the if the year given is a leap year.
# Test cases: I used 2000, 2004, 2020, 1600.


# Input: gets the year information.
year = int(input("Please enter a year: "))



# Output: prints if the year given is a leap year.
print("")

if(year % 4) == 0:

    if (year % 100) == 0:

        if (year % 400) == 0:
            print(year, "is a leap year")
            
        else:
            print(year, "is not a leap year")
            
    else:
        print(year, "is a leap year")

else:
    print(year, "is not a leap year")
