class Dog:

    def make_sound(self):
        print("This dog make sound")


class Cat:

    def make_sound(self):
        print("This cat make sound")


class Bird:

    def make_sound(self):
        print("This bird make sound")


def let_them_speak(list_objs):
    for obj in list_objs:
        obj.make_sound()


animals = [Dog(), Cat(), Bird()]
let_them_speak(animals)
