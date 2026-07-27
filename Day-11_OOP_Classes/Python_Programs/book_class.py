# Program 3: Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(self.title, self.author)

Book("Python", "Guido").info()
