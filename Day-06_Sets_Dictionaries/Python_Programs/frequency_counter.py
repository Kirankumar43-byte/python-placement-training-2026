# Program 13: Frequency count
items = ["a", "b", "a"]
print({item: items.count(item) for item in set(items)})
