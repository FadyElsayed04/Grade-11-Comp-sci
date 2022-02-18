# Name: Fady Elsayed
# Date: Apr 9, 2021
# File Name: 5.3 Day one, 2a.py

list1 = [1, 2, 3, 5, 0]

list2 = [7, 2, 4, 1, 5]

list3 = []

def common(a, b):   
    for i in list1:
        if i in list2:
            list3.append(i)

    print(list3)

# Main Program
common(list1, list2)
