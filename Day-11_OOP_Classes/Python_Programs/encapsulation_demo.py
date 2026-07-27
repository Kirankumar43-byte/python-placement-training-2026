# Program 17: Encapsulation
class Account:
    def __init__(self):
        self.__balance = 100

    def balance(self):
        return self.__balance

print(Account().balance())
