# Program 10: Inheritance and composition
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()

print(Car().engine)
