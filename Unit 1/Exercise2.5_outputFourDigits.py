import math


a = int(input("Please enter a positive, 4-digit number (1000 to 9999): "))
c = a // 1000
print ("The first digit is:" , c)

d = a % 1000
e = d // 100
print ("The second digit is:" , e)

f = d % 100
g = f // 10
print ("The third digit is:" , g)


h = f % 10
i = h // 1
print ("The forth digit is:" , i)


