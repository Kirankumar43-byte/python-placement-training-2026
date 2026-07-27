# Program 8: Count lines
with open("demo.txt", "r", encoding="utf-8") as f:
    print(len(f.readlines()))
