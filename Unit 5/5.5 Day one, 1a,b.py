# Name: Fady Elsayed
# Date: Apr 20, 2021
# File Name: 5.5 Day one, 1a,b.py

import statistics

print("Please enter your marks. Type -1 to quit.")

def get_marks():
    marks = []
    while True:
        try:
            mark = int(input("Please enter a mark: "))                    
            if mark >= 1 and mark <= 100:
                marks.append(mark)
            elif mark == -1:
                break
            else:
                print("Invalid mark.")
        except:
            print("Invalid input.")
    print(marks)
    return marks

    
def mean(marks):
    mean = (sum(marks) / len(marks))
    print("Your average mark is:", mean)
    return mean


def median(marks):
    median = statistics.median(marks)
    print("The median of your marks is:", median)
    return median


def mode(freq_lisst):
    mode = max(freq_list)
    mode_list = []
    for i in range(1, len(freq_list)):
        if freq_list[i] == mode:
            mode_list.append(i)


def freq(marks):
    global freq_list
    freq_list = []
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    j = 0
    k = 0
    l = 0
    for i in marks:  
        if i == 0:
            a += 1
        elif i == 1:
            b += 1
        elif i == 2:
            c += 1
        elif i == 3:
            d += 1
        elif i == 4:
            e += 1
        elif i == 5:
            f += 1
        elif i == 6:
            g += 1
        elif i == 7:
            h += 1
        elif i == 8:
            j += 1
        elif i == 9:
            k += 1
        elif i == 10:
            l += 1
    freq_list.append(a)
    freq_list.append(b)
    freq_list.append(c)
    freq_list.append(d)
    freq_list.append(e)
    freq_list.append(f)
    freq_list.append(g)
    freq_list.append(h)
    freq_list.append(j)
    freq_list.append(k)
    freq_list.append(l)
    print("Your frequency of your marks is: ", freq_list)
    return freq_list


            
def choice():
    choice = 0
    while choice != -5:
        try:
            choice = int(input("Please enter your choice: "))            
            if choice < 1 or choice > 4:
                raise Exception
            elif choice >= 1 and choice <= 4:
                break
            while choice < 1 or choice > 4:         
                choice = int(input("Please enter your choice: "))
                if choice >= 1 and choice <= 4:
                    break        
        except Exception:
            print("Invalid Input!")
    if choice == 1:
            mean(marks)
    elif choice == 2:
            median(marks)
    elif choice == 3:
            mode(freq_list)
    elif choice == 4:
            freq(marks)

    
marks = get_marks()
print("what would you like to do?") 
print("1 - Calculate The Mean") 
print("2 - Calculate The Median") 
print("3 - Calculate The Mode") 
print("4 - Calculate The Frequency") 
print("5 - Quit")
choice()
