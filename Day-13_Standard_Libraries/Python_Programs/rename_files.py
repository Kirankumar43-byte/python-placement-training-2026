# Program 2: Rename files
import os
for index, file in enumerate(os.listdir('.')):
    if file.endswith('.txt'):
        os.rename(file, f"copy_{index}.txt")
print("Files renamed")
