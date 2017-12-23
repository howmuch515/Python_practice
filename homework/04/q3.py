from random import randint
FILENAME = 'random.txt'

# (1)
with open(FILENAME, 'w') as f:
    for i in range(100):
        n = randint(1, 1000)
        f.write(str(n) + '\n')

# (2)
with open(FILENAME, 'r') as f:
    num_list = f.readlines()
    for i in num_list:
        n = int(i)
        if n % 2 == 0:
            print("{}: odd".format(n))
        else:
            print("{}: even".format(n))
