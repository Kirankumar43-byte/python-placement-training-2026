# Program 6: Read CSV
import csv
with open("students.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)
