# Program 10: Backup database
import shutil
shutil.copy('students.db', 'students_backup.db')
print('Backup created')
