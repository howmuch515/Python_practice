string = input("input> ")

try:
    num = int(string)
    print(num ** 5)
except:
    print("invalid num")
