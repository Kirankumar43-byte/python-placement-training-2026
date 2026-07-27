# Program 10: Student manager using class
class StudentManager:
    def __init__(self):
        self.students = []

    def add(self, name):
        self.students.append(name)

manager = StudentManager()
manager.add("Ravi")
print(manager.students)
