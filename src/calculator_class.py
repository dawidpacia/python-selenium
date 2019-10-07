class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return self.result


calculator = Calculator()
add_result = calculator.add(1, 2)
print(add_result)
