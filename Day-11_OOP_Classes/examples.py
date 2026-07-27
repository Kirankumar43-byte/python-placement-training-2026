class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(self.name, self.grade)

obj = Student('Mina', 'A')
obj.show()
