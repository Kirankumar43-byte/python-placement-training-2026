# Program 8: Safe division
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print(numerator / denominator)
except Exception as exc:
    print("An error occurred:", exc)
