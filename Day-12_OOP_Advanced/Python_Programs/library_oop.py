# Program 7: Library OOP example
class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(self.title)

Book("Django").display()
