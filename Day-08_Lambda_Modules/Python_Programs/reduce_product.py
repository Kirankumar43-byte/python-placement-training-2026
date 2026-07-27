# Program 13: Product using reduce
from functools import reduce
nums = [2, 3, 4]
print(reduce(lambda a, b: a * b, nums))
