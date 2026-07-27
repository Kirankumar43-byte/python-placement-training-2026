# Employee management SQLite example
import sqlite3

conn = sqlite3.connect('sample_database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, salary REAL)')
cur.execute("INSERT INTO employees (name, salary) VALUES ('Neha', 50000)")
conn.commit()
cur.execute('SELECT * FROM employees')
print(cur.fetchall())
conn.close()
