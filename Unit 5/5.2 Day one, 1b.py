# Name: Fady Elsayed
# Date: Apr 8, 2021
# File Name: 5.2 Day one, 1b.py

import random
alist = []
die = 0
f= 0
while die != 6:
    die = random.randint(1, 6)
    alist.append(die)

print(alist)

avg = sum(alist) / len(alist)

print("The average of the list is", round(avg,2))
