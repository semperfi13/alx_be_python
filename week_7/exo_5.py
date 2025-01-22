class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


result_add = Calculator.add(2.234, 12.1)
result_multiply = Calculator.multiply(2, 12.1)


print(f"Addition result is {result_add}")
print(f"Multiplication result is {result_multiply}")
