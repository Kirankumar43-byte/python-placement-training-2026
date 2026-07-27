# Program 7: Raise a custom exception
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age below minimum")
print("Welcome")
