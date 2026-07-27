# Program 4: Update record
import sqlite3
conn = sqlite3.connect('students.db')
cur = conn.cursor()
cur.execute("UPDATE students SET name = 'Asha Kumar' WHERE name = 'Asha'")
conn.commit()
conn.close()
print('Student updated')
