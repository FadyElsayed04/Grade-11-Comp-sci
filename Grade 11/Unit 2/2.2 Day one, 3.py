num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))

if num1 > num2:
    print(num1,"is larger.")
elif num1 < num2:
    print(num2,"is larger.")
else:
    print(num1, "and,", num2, "are the same number.")
