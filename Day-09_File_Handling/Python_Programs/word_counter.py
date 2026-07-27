# Program 7: Count words in a file
with open("demo.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(len(text.split()))
