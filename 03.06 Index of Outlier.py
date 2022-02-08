num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 == num2 and num1!=num3):
    print(3)
elif (num1 != num2 and num1==num3):
    print(2)
else:
    print(1)