from functools import reduce
import math
import random

nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(reduce(lambda a, b: a + b, nums))
print(math.sqrt(16))
print(random.randint(1, 10))
