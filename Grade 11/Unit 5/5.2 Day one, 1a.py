# Name: Fady Elsayed
# Date: Apr 8, 2021
# File Name: 5.2 Day one, 1a.py

alist = ["Joe", "Ben", "Jay", "Bob", "Jack"]
print(alist)
f = 0
amount = int(input("How many names do you want to add?: "))

while f != amount:
   names = str(input("What are those names?: "))
   alist.append(names)
   f += 1

print(alist)
