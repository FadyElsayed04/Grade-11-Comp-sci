# Name: Fady Elsayed	
# Date: March, 2, 2021	
# File Name: 2.1 Day two, 5.py
# Description: A program to take orders from the Internet, by taking the
# price and shipping to determine the final cost.
# Test cases: I used: a hotdog, with the prices 10, and 20, and
# overnight shipping and without.

# Input – gets users order cost and shipping preference 
item = input("please enter the item: ")
cost = float(input("please enter the item's cost: "))
shipping = int(input("Do you want overnight shipping? yes=1/no=0): "))


# Process - adds variables for shipping costs
overnight_cost = 5.00
above_ten_cost = 3.00
under_ten_cost = 2.00

overnight_shipping = cost + overnight_cost
shipping_above_ten = cost + above_ten_cost
shipping_under_ten = cost + under_ten_cost

# Process - figures out overnight cost
if cost <= 10:
    overnight_cost = overnight_cost + 2
    
elif cost >= 10:
    overnight_cost = overnight_cost + 3
    
# Output – prints total cost of meal with shipping
print("\n\nInvoice:\n")

if shipping == 1:
    print(item + ": $" + str(cost))
    print("Overnight shipping: $" + str(overnight_cost))
    print("Total: $" + str(overnight_shipping))
        
elif cost <= 10:
    print(item + ": $" + str(cost))
    print("Shipping: $" + str(under_ten_cost))
    print("Total: $" + str(shipping_under_ten))
    
else:
    print(item + ": $" + str(cost))
    print("Shipping: $" + str(above_ten_cost))
    print("Total: $" + str(shipping_above_ten))
