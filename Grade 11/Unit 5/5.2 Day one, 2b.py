# Name: Fady Elsayed
# Date: Apr 8, 2021
# File Name: 5.2 Day one, 2b.py

def user_list(n):

    alist = []

    global user

    user = 0

    for i in range (1, n + 1):
        num = int(input("Enter a number: "))
        alist.append(num)

    print(alist)

    return alist

# Main Program

n = int(input("How many integers do you want to read?: "))

alist = user_list(n)

alist.sort()
print("\nThe largest number in the list is", alist[-1])
print("The 2nd largest number in the list is", alist[-2])
print("The 3rd largest number in the list is", alist[-3])
