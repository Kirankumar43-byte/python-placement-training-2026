with open('notes.txt', 'w') as f:
    f.write('Python file handling demo\n')

with open('notes.txt', 'r') as f:
    print(f.read())

with open('notes.txt', 'a') as f:
    f.write('Appended line\n')
