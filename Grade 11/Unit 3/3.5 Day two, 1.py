# Name: Fady Elsayed
# Date: Mar 19 2021
# File Name: 3.5 Day two, 1.py
# Description: A program that asks user for temps and outputs the average.
# Test cases: I used the temps, 50, 30, 20.

# Process: Sets values.
total = 0
temp_amount = 0
temp = 0

# Process: Loops code and tells user how to get average.
print("type 'done' to get temp average")
while True:
  try:

# Process: checks if temps are vaild
    while temp != ("done"):

      temp = int(input("Enter the temperature: "))

      if temp < -50.0:
          print("Too cold")
 
      elif temp > 200.0:
          print("Too hot")
          
      elif temp > -50.0 and temp < 200.0:
          total += temp
          temp_amount += 1

# Output: prints average temp.
      elif temp ==("done"):
          avg = total / temp_amount
          print("The average temperature is", avg, "degrees Celius.")
    break

# Process: Error checks.
  except:
    print("\nplease enter a number!\n")


