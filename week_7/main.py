class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This animal {self.name} eat")

    def sleep(self):
        print(f"This animal {self.name} eat")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"This dog {self.name} bark")


animal = Animal("POUPPETTE")

dog = Dog(animal.name)

dog.sleep()
dog.eat()
dog.bark()
