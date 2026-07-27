# Program 11: Exception summary
try:
    numbers = [1, 2]
    print(numbers[3])
except IndexError:
    print("Index out of range")
