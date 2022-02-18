# Name: Fady Elsayed
# Date: Apr 9, 2021
# File Name: 5.3 Day one, 1a.py

def user_list():
    alist = []
    while True:
        try:
            n = int(input("Please nter a positive integer, enter -1 when \
done: "))
            while n > 0:
                alist.append(n)
                n = int(input("Please nter a positive integer, enter -1 when \
done: "))
            if n < 0 and n != -1:
                print("Invalid Input!")
                
            elif n == -1:
                break
        except:
            print("Invalid Input!")
            

    return alist

def linear(my_list, item):
    pos = 0
   
    x = 0
    while pos < len(my_list):
        if my_list[pos] == item:
            
            x += 1
            pos = pos+1
        else:
            pos = pos+1
    return x

# Main Program
alist = user_list()
item3 = linear(alist, 3)
print("The amount of 3s in the list is:", item3)
