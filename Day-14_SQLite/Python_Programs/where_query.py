# Program 7: WHERE query
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('SELECT * FROM students WHERE id = 1')
print(cur.fetchall())
conn.close()
