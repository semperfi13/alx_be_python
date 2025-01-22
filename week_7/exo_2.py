class Bird:
    def fly(self):
        return "This bird can fly"


class Mammal:
    def run(self):
        return "This mamal can fly"


class Bat(Bird, Mammal):
    pass


bat = Bat()
print(bat.fly())
print(bat.run())
