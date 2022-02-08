a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

same_number=0

if (a==b==c):
    same_number = 3
elif (a==b and a!=c or b==c and b!=a or a==c and a!=b ):
    same_number = 2
elif (a!=b and b!= c and a!=c):
    same_number = 0

print(same_number)