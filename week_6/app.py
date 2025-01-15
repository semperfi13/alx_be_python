def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by 0")
    return x / y


result = divide(10, 0)


print(f"{result}")
