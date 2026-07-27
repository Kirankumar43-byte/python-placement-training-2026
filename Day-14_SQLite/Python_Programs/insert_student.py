# Program 3: Insert student record
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute("INSERT INTO students (name) VALUES ('Asha')")
conn.commit()
conn.close()
print('Student inserted')
