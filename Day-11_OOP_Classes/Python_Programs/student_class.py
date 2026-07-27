# Program 1: Student class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(self.name, self.grade)

student = Student("Mina", "A")
student.show()
