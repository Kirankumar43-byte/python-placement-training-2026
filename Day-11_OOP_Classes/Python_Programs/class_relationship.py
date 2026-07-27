# Program 20: Class relationship
class Course:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, course):
        self.course = course

course = Course("Python")
student = Student(course)
print(student.course.name)
