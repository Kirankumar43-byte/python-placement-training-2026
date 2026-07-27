import os
import json
import random
from datetime import datetime

print(os.getcwd())
print(datetime.now())

password = ''.join(random.choice('abc123') for _ in range(8))
print(password)

student = {'name': 'Asha', 'age': 21}
print(json.dumps(student))
