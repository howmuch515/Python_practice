txt = input("input> ")

with open("readme.txt", "w") as f:
    f.write(txt)

with open("readme.txt", "r") as f:
    print(f.read())
