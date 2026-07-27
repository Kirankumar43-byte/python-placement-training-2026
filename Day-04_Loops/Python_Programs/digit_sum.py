# Program 14: Sum of digits
num = 1234
s = 0
while num > 0:
    s += num % 10
    num //= 10
print(s)
