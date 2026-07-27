# Program 5: Multi-level inheritance
class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Puppy(Dog):
    pass

Puppy().speak()
