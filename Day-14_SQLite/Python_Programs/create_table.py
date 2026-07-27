# Program 2: Create a table
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()
conn.close()
print('Table created')
