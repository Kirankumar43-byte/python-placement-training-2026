# Program 2: Bank account class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(account.balance)
