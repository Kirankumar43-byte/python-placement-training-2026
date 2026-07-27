# Program 2: Handle invalid input
try:
    x = int(input("Enter an integer: "))
    print(x)
except ValueError:
    print("Please enter a valid integer")
