# Program 12: Search files by extension
import os
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(file)
