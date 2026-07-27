# Program 12: Bank transaction example
balance = 100
try:
    withdraw = int(input("Enter amount to withdraw: "))
    if withdraw > balance:
        raise ValueError("Insufficient balance")
    print("Balance left:", balance - withdraw)
except ValueError as exc:
    print(exc)
