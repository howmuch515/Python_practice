for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="")
    print()
