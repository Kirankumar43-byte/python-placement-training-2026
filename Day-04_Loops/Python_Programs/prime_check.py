# Program 7: Prime number check
n = 29
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)
