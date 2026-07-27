# Program 16: Count vowels
word = "beautiful"
count = 0
for ch in word:
    if ch in "aeiou":
        count += 1
print(count)
