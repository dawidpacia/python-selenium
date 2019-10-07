def fibonacci(n):
    a1, a2 = 0, 1
    if n == 0:
        return a1
    elif n == 1:
        return a2
    elif n < 0:
        return False
    for i in range(2, n + 1):
        a1, a2 = a2, a1 + a2
    return a1


if __name__ == "__main__":
    print(fibonacci(10))
