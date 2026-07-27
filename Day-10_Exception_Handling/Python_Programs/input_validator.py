# Program 10: Input validator
while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Try again")
print("Age entered:", age)
