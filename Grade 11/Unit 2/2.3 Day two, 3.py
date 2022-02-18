# Name: Fady Elsayed	
# Date: March, 3, 2021	
# File Name: 2.3 Day two, 3.py
# Description: A cookie order program to order cookies with built in discounts.
# Test cases: I used 5 of each cookie box, and 1 of each cookie box.


# Input: Gets user input for cookie box amount.
amount_of_choco = int(input("Please enter the amount of chocolete chip cookie \
boxes you want to order: "))

amount_of_raisin = int(input("Please enter the amount of raisin cookie \
boxes you want to order: "))

amount_of_short = int(input("Please enter the amount of shortbread cookie \
boxes you want to order: "))

# Process: calculates cost for cookies wiht or without discount.
amount_of_boxes = amount_of_choco + amount_of_raisin + amount_of_short
cost_of_boxes = amount_of_boxes * 6.95

tax = 0.13
discount = cost_of_boxes * -0.10

cost_after = cost_of_boxes * tax + cost_of_boxes
cost_after_discount = (cost_of_boxes + discount) * tax + cost_of_boxes + discount

# Output: prints the cost depending on amount of cookies for discount or not.
if amount_of_choco + amount_of_raisin + amount_of_short >= 10 or \
   amount_of_choco >= 5 or amount_of_raisin >= 5 or amount_of_short >= 5:
    print("\nyour total is:",int(cost_after_discount), "dollars.")
    
else: 
    print("\nyour total is:",int(cost_after), "dollars.")
