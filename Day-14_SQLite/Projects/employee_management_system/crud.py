# CRUD operations for the project
import sqlite3
from pathlib import Path

DB_NAME = 'project.db'


def create_record(name, details):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('INSERT INTO records (name, details) VALUES (?, ?)', (name, details))
    conn.commit()
    conn.close()


def read_records():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('SELECT * FROM records')
    rows = cur.fetchall()
    conn.close()
    return rows


try:
    create_record('Sample', 'Demo record')
    print(read_records())
except sqlite3.Error as exc:
    print('Database error:', exc)
