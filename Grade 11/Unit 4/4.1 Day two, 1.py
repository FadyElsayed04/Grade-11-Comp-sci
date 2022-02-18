# Name: Fady Elsayed
# Date: Mar 22 2021
# File Name: 4.1 Day two, 1.py
# Description: A program print the day of the week when given a number.
# Tests Cases: I used the numbers: 1, 7, 3, 10, 0, -1.

# Process: Creates function with days matching numbers.
def day_week():
    def day(week):
        if week >= 1 and week <= 7:
            if week == 1:
                print("\nSunday\n")
            elif week == 2:
                print("\nMonday\n")
            elif week == 3:
                print("\nTuesday\n")
            elif week == 4:
                print("\nWednesday\n")
            elif week == 5:
                print("\nThursday\n")
            elif week == 6:
                print("\nFriday\n")
            elif week == 7:
                print("\nSaturday\n")
        elif week < 1 or week > 7:
            print("\nError!\n")

    while True:
        try:
# Input: Asks for number.
            week = int(input("Please enter a number between 1 and 7: "))
            day(week)
            
        except:
            print("\nError!\n")
            
# Main Program.
day_week()
