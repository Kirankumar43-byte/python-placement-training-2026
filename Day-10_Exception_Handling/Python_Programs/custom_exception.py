# Program 4: Custom exception
class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Age must be 18 or above")
    print("Adult")
except AgeError as exc:
    print(exc)
