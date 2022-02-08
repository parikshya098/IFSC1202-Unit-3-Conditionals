num1 = int(input("Enter point A: "))
num2 = int(input("Enter point B: "))
num3 = int(input("Enter point C: "))

distance_a_to_b = abs(num2 - num1)
distance_a_to_c = abs(num3 - num1)

if (distance_a_to_b > distance_a_to_c):
    print(distance_a_to_c)
else:
    print(distance_a_to_b)