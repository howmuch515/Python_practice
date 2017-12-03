try:
    f = open("readme.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("not found")
