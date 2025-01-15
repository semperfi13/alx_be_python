class ErroClass(Exception):
    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock"


class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Sorry guys! your number {self.number} is higher thant 100"
