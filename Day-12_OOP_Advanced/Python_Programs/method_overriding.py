# Program 3: Overriding example
class Parent:
    def speak(self):
        print("Parent")

class Child(Parent):
    def speak(self):
        print("Child")

Child().speak()
