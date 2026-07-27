# Program 8: ORDER BY query
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('SELECT * FROM students ORDER BY name')
print(cur.fetchall())
conn.close()
