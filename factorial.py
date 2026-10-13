print("Please enter any number so that we can find the factorial of that number")
num = int(input("Enter any number: "))
f=1
for i in range(1, num+1):
    f = f*i
    print(f)