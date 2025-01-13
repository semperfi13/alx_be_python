# Fundamentals of OOP in Python

""" Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. Include a method to display student information. """


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_student_info(self):
        student_infos = f"The student name is {self.name} and he is {self.age} year old"
        return student_infos


new_student = Student("SEMPERFI", "20")
print(new_student.get_student_info())

""" Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock. """


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        total = self.quantity * self.price
        return f"The total value of products in stock is {total}CFA"


new_product = Product("Bananas", 125, 23)
print(new_product.calculate_total())
