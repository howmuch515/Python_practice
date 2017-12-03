from random import randint

while True:
    ran_num = randint(0, 256)
    print(ran_num)

    if ran_num % 13 == 0:
        print("end")
        break
