# Name: Fady Elsayed
# Date: Apr 9, 2021
# File Name: 5.3 Day one, 1c.py

import random

list1 = []
list2 = []

n = int(input("How many elements do you want in each list?: "))

for i in range(0, n):
    random1 = random.randint(1, 100)
    list1.append(random1)

print(list1)

for i in range(0, n):
    random2 = random.randint(1, 100)
    list2.append(random2)

print(list2)

list1.sort()
print("First list:", list1)
print("Second list:", list2)
