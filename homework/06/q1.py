def isPrime(n):
    i = 2
    while i <= (n ** (1 / 2)):
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(2, 21):
    if isPrime(i):
        print("prime")
    else:
        print(i)
