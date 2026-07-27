# Program 10: Simple calculator using conditions
op = input("Enter operator (+, -, *, /): ")
a = 8
b = 4
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid")
