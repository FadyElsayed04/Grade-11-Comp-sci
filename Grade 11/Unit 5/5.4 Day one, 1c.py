# Name: Fady Elsayed
# Date: Apr 19, 2021
# File Name: 5.4 Day one, 1c.py

def distance_mean(l):
    alist = []
    avg = (sum(l) / len(l))
    for i in l:
        i = i - avg
        alist.append(i)
    print(alist)

    
my_list = [0, -12, 4, 18, 9, 10, 11, -23]
print(distance_mean(my_list))
