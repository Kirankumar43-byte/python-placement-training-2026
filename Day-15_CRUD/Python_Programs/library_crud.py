# Program 3: Library CRUD application
import sqlite3

conn = sqlite3.connect('library_db.sqlite3')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)')
cur.execute("INSERT INTO books (title, author) VALUES ('Python Basics', 'Guido')")
conn.commit()
cur.execute('SELECT * FROM books')
print(cur.fetchall())
conn.close()
