# Program 13: Safe calculator
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a + b)
except ValueError:
    print("Enter valid numbers")
