# Program 5: Folder size summary
import os
print(sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)))
