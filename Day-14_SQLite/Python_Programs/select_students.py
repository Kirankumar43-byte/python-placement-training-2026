# Program 6: Select all records
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
conn.close()
