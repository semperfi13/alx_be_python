class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_check_out = True


class Library:
    _books = []

    def __init__(self):
        pass

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        try:
            for book in self._books:
                if book.title == title:
                    book._is_check_out = False
        except ValueError as e:
            print(e)

    def return_book(self, title):
        try:
            for book in self._books:
                if book.title == title:
                    book._is_check_out = True
        except ValueError as e:
            print(e)

    def list_available_books(self):
        for book in self._books:
            if book._is_check_out == True:
                print(f"{book.title} by {book.author}")
