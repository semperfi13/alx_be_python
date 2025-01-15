from error_class import ValueTooHighError


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError(f"You can't divide {x} by {y} !")
    return x / y


""" try:
    divide(5, 0)
except Exception as e:
    print(e) """


def valueTooHigh(number):
    if number > 100:
        raise ValueTooHighError(number)
    print(f"Your number is {number} and is is lower than 100")


try:
    valueTooHigh(992)
    # divide(5, 0)
except Exception as e:
    print(e)
