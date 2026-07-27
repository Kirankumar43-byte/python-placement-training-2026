# Program 15: Word frequency dictionary
text = "python python is fun"
words = text.split()
print({word: words.count(word) for word in set(words)})
