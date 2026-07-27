# Program 6: Multiple exceptions
try:
    value = int(input("Enter number: "))
    print(100 / value)
except ZeroDivisionError:
    print("Zero division")
except ValueError:
    print("Invalid number")
