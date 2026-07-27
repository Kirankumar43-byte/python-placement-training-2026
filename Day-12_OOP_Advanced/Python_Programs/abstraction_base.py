# Program 2: Abstract base class style
class Vehicle:
    def start(self):
        raise NotImplementedError

class Car(Vehicle):
    def start(self):
        print("Car started")

Car().start()
