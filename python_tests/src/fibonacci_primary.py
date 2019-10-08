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

        num_of_element = 0
        while True:
            if if_primary(a_2):
                num_of_element += 1
            a_1, a_2 = a_2, a_1 + a_2
            if num_of_element == n_element:
                return a_1
    except (TypeError, MemoryError) as err:
        print(err)
        return False


def if_primary(value):
    if value >= 2:
        for i in range(2, value//2):
            if value % i == 0:
                return False
        return True
    return False


if __name__ == "__main__":
    print(fibonacci(10))
    print(if_primary(21))
