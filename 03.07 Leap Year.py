year = int(input("Enter Year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("LEAP YEAR")
elif (year % 4 ==0) and (year % 100 != 0):
    print("LEAP YEAR")
else:
    print("COMMON YEAR")