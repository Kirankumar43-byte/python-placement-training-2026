# Program 15: Hierarchical inheritance
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(Dog.__mro__)
