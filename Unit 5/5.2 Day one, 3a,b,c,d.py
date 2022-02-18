# Name: Fady Elsayed
# Date: Apr 8, 2021
# File Name: 5.2 Day one, 3a,b,c,d.py

def get_int():
    alist = []
    f = 0

    x = int(input("Please enter a positive Integer. Enter -1 when done: "))
    if x > 0:
        f += 1
        alist.append(x)

    while True:
        if x > 0:
            
            x = int(input("Please enter a positive Integer. Enter -1 when done:\
"))
            f += 1
            alist.append(x)

        elif x < 0 and x != -1:
            print("Invalid Input!")
            x = int(input("Please enter a positive Integer. Enter -1 when done:\
"))
        elif x == -1:
            break

    list1 = []
    
    for num in alist:
        if num > 0:
            list1.append(num)

    print()

    
    return list1

# Main Program
list1 = get_int()

list2 = []
for num2 in list1:
    if num2 % 3 == 0 or num2 % 4 == 0:
        list2.append(num2)

print(list1)
print("New list without values that are multiples of 3 and 4 is: ", list2)

length_of_list2 = len(list2)

if length_of_list2 % 5 == 0:
    print("The amount of integers in the list is a multiple of 5.")
else: 
    print("The amount of integers in the list is not a multiple of 5.")
