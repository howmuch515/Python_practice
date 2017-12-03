string = input("input> ")

if not string.isdigit():
    raise Exception("invalid input")

year = int(string)

if year % 400 == 0:
    print(str(year) + " is a leap year")
elif year % 100 == 0:
    print(str(year) + " is a normal year")
elif year % 4 == 0:
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is a normal year")
