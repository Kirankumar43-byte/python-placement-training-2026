# Program 4: Folder cleaner
import os
for file in os.listdir('.'):
    if file.endswith('.tmp'):
        os.remove(file)
print("Cleanup complete")
