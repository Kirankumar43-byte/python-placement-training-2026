# Library management SQLite example
import sqlite3

conn = sqlite3.connect('sample_database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT)')
cur.execute("INSERT INTO books (title, author) VALUES ('Python Basics', 'Guido')")
conn.commit()
cur.execute('SELECT * FROM books')
print(cur.fetchall())
conn.close()
