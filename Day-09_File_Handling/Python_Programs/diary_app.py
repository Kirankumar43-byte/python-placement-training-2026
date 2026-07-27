# Program 13: Mini diary app
entry = input("Enter your diary entry: ")
with open("diary.txt", "a", encoding="utf-8") as f:
    f.write(entry + "
")
print("Entry saved")
