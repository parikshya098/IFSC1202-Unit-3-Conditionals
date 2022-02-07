a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

small_num = 0

if a < b and a < c:
    small_num = a
elif b < c:
    small_num = b
else:
    small_num = c

print(small_num)