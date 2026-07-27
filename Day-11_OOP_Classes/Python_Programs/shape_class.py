# Program 9: Shape class
class Shape:
    def area(self):
        print("Area unknown")

class Circle(Shape):
    def area(self):
        print("Circle area")

Circle().area()
