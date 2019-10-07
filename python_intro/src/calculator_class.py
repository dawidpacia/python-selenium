class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        try:
            return a + b
        except (TypeError, NameError) as e:
            print(e)
            return False

    def sub(self, a, b):
        try:
            return a - b
        except (TypeError, NameError) as e:
            print(e)
            return False

    def mul(self, a, b):
        try:
            return a * b
        except (TypeError, NameError) as e:
            print(e)
            return False

    def div(self, a, b):
        try:
            return a / b
        except (TypeError, NameError, ZeroDivisionError) as e:
            print(e)
            return False


if __name__ == "__main__":
    calculator = Calculator()
    calculator.add("1", 2)

