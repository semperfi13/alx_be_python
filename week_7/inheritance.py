# single inheritance test


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"This animal '{self.name}' make sound")


class Mammal(Animal):
    def paws_number(self):
        print(f"This mammal '{self.name}' has 04 paws")


class Dog(Mammal):
    def sound(self):
        print(f"This dog {self.name} make sound")


lassie = Dog("LASSIE")
lassie.make_sound()
lassie.sound()
lassie.paws_number()
