# Program 9: Nested error handling
try:
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print("Inner exception handled")
except Exception:
    print("Outer exception handled")
