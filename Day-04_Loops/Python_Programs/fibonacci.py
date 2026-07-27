# Program 8: Fibonacci sequence
n = 7
first, second = 0, 1
for _ in range(n):
    print(first)
    first, second = second, first + second
