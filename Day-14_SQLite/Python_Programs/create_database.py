# Program 1: Create SQLite database
import sqlite3

conn = sqlite3.connect('students.db')
conn.close()
print('Database created')
