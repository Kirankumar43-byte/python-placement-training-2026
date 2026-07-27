import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')
cur.execute('INSERT INTO students (name, marks) VALUES ('Asha', 90)')
conn.commit()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
conn.close()
