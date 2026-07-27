# Program 4: Inheritance example
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

teacher = Teacher("Mr. Rao")
print(teacher.name)
