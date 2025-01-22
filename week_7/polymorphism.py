class Animal:
    def make_sound(self):
        # print("THis animal make sound")
        return "This animal make sound"


""" Animal """


class Dog:
    def make_sound(self):
        return "This dog make sound"
        # print("This dog make sound")


""" animals = [Dog(), Animal()]

for animal in animals:
    animal.make_sound() """


# Polymorphic function
def make_sound(obj):
    return obj.make_sound()


animal = Animal()
dog = Dog()


print(make_sound(animal))
print(make_sound(dog))
