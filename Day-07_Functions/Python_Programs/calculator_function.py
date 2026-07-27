# Program 14: Calculator function
def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    return None

print(calc(5, 3, '+'))
