def fibonacci(n_element):
    """
    Calculating fibbonacci value
    :param n_element: number of fibbonacci sequence
    :return:
    """
    a_1, a_2 = 0, 1
    try:
        if n_element == 1:
            return a_1
        if n_element == 2:
            return a_2
        if n_element <= 0:
            return False
        for _ in range(2, n_element + 1):
            a_1, a_2 = a_2, a_1 + a_2
        return a_1
    except (TypeError, MemoryError) as err:
        print(err)
        return False


if __name__ == "__main__":
    print(fibonacci(10))
