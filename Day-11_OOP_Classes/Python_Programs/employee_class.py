# Program 7: Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

Employee("Asha", 50000).display()
