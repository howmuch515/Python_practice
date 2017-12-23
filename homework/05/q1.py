def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print("-----factorial-----")
for i in range(11):
    print("{}: {}".format(i, factorial(i)))

print("-----fibonacci-----")
for i in range(11):
    print("{}: {}".format(i, fibonacci(i)))
