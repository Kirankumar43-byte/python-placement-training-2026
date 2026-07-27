# Program 11: Library system class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

lib = Library()
lib.add_book("Python Basics")
print(lib.books)
