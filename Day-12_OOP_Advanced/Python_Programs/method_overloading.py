# Program 4: Overloading style using default args
class Demo:
    def add(self, a, b=0):
        return a + b

print(Demo().add(3))
print(Demo().add(2, 5))
