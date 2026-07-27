# Program 16: Method overriding
class Parent:
    def greet(self):
        print("Parent")

class Child(Parent):
    def greet(self):
        print("Child")

Child().greet()
