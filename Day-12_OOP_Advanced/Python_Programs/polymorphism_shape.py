# Program 5: Shape polymorphism
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5

class Circle(Shape):
    def area(self):
        return 3.14 * 3 * 3

for shape in [Rectangle(), Circle()]:
    print(shape.area())
