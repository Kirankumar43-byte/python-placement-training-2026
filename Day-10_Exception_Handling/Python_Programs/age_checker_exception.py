# Program 15: Age check with exception
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("Child")
    print("Adult")
except Exception as exc:
    print(exc)
