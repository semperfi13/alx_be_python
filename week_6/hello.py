class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Bird(Animal):
    pass


class Hawk(Animal):
    pass


class Fish(Animal):
    def swing(self):
        print("Can swin")


fish = Fish()
fish.sleep()
fish.swing()
