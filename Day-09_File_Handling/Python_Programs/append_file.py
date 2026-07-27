# Program 3: Append to a file
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("
Appended line")
