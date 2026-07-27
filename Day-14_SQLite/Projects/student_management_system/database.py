# Database helper for the project
import sqlite3

DB_NAME = 'project.db'


def connect():
    conn = sqlite3.connect(DB_NAME)
    return conn


conn = connect()
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, details TEXT)')
conn.commit()
conn.close()
print('Database ready')
