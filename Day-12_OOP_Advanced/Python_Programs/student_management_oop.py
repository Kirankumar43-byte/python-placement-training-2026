# Program 8: Student management OOP
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

sm = StudentManager()
sm.add_student("Kavya")
print(sm.students)
