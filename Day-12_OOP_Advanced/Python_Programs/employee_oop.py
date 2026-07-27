# Program 6: Employee OOP example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)

Employee("Riya", 45000).show()
