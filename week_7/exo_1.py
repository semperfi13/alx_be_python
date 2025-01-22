class Shape:

    def calculate_area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def calculate_area(self):
        return self.largeur * self.longueur


rectangle = Rectangle(12, 12)
print(rectangle.calculate_area())
