def greet(name):
    return f'Hello {name}'

print(greet('Neha'))

def add(a, b=5):
    return a + b

print(add(3))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
