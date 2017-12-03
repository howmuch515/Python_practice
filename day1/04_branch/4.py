from random import randint

ran_num = randint(-10, 10)
print(ran_num)

if ran_num == 0:
    print("ZERO")
elif ran_num < 0:
    print("NEGATIVE")
else:
    print("POSITIVE")
