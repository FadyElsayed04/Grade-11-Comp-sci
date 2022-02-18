# Name: Fady Elsayed
# Date: Apr 8, 2021
# File Name: 5.2 Day one, 2a.py


def linear_list(num):
    alist = []


    for i in range(1, num+1):

        alist.append(i)

        if i % 2 == 0:
            alist.insert(i+1, 0)
        
        else:
            continue
        
    return alist
    
# Main program

num = int(input("Please enter length of the list: "))

num_list = linear_list(num)
print(num_list)
