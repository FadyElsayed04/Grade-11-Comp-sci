# Name: Fady Elsayed
# Date: Apr 9, 2021
# File Name: 5.3 Day one, 1d.py

def user_list():
    alist = []
    while True:
        try:
            price = float(input("Please enter your item price, \
enter -1 when done: "))
            while price > 0:
                alist.append(price)
                price = float(input("Please enter your item price, \
enter -1 when done: "))
            if price < 0 and price != -1:
                print("Invalid Input!")
                
            elif price == -1:
                break
        except:
            print("Invalid Input!")

    alist.sort()
    print(alist)

    print("The second most expensive item is: ", alist[-2])

# Main Program
user_list()
