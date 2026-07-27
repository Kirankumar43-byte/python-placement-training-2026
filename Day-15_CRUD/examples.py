import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')
cur.execute('INSERT INTO students (name, marks) VALUES ('Ravi', 88)')
conn.commit()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
cur.execute('UPDATE students SET marks = 92 WHERE name = 'Ravi'')
conn.commit()
cur.execute('DELETE FROM students WHERE name = 'Ravi'')
conn.commit()
conn.close()
