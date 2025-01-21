class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title} \nAuthor: {self.author} \nPages: {self.pages}"

    def __repr__(self):
        return f"Title: {self.title} \nAuthor: {self.author} \nPages: {self.pages}"


book = Book("ALX", "BACKEND DEV", 123)
print(book)
