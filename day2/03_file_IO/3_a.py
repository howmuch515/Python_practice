txt = input("input> ")

f = open("readme.txt", "w")
f.write(txt)
f.flush()
f.close()
