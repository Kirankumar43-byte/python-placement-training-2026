# Program 18: Abstract idea
class Shape:
    def draw(self):
        raise NotImplementedError

try:
    Shape().draw()
except NotImplementedError:
    print("Implemented later")
