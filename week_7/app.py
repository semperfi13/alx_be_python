class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("CLEAR")


person = Person("ALX BACKEND DEV", 12)
del person
