# Program 9: Bank account OOP
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

Account().deposit(50)
print(Account().balance)
