num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("The largest number between",num1,"and",num2,"is :")

if num1 > num2:
    print(num1,"is a largest number")
elif num2 > num1:
    print(num2,"is a largest number")
else:
    print("Both the numbers are equal.2")