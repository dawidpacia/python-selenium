def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    else:
        return False




if __name__ == "__main__":
    print(factorial(5))
