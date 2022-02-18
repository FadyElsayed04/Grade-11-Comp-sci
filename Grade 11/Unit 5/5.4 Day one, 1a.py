# Name: Fady Elsayed
# Date: Apr 19, 2021
# File Name: 5.4 Day one, 1a.py
import random

def every_other(l):
    del(l[1::2])
    print(l)

    
my_list = [0, -12, 4, 18, 9, 10, 11, -23]
print(every_other(my_list))
