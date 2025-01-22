class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total book created: {cls.total_books}")


book_1 = Book()
book_2 = Book()
book_2 = Book()

Book.display_total_books()
