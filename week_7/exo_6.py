class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    @classmethod
    def create_child(cls, name):
        child = Person(name, 0)
        return child


child = Person.create_child("Semperfi")
print(child.name)
print(child.age)
