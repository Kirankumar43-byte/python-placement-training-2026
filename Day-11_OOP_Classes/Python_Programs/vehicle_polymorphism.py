# Program 6: Polymorphism
class Vehicle:
    def move(self):
        print("Vehicle moving")

class Car(Vehicle):
    def move(self):
        print("Car moving")

for obj in [Vehicle(), Car()]:
    obj.move()
