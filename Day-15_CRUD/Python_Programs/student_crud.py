# Program 1: Student CRUD application
import sqlite3

conn = sqlite3.connect('student_db.sqlite3')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)')
cur.execute("INSERT INTO students (name, marks) VALUES ('Ravi', 88)")
conn.commit()
cur.execute('SELECT * FROM students')
print(cur.fetchall())
conn.close()
