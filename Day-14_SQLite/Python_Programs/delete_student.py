# Program 5: Delete record
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute("DELETE FROM students WHERE name = 'Asha Kumar'")
conn.commit()
conn.close()
print('Student deleted')
