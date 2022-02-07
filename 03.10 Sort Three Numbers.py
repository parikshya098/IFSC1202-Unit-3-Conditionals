a = int(input("Enter first number: "))
b = int(input("Enter second: "))
c = int(input("Enter third number: "))
if a > c:
    a = a + c
    c = a - c
    a = a - c  
if a > b:
    a = a + b
    b = a - b
    a = a - b
if b > c:
    b = b + c
    c = b - c
    b = b - c
print (a, b, c)