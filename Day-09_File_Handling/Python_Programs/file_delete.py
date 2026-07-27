# Program 11: Delete a file
from pathlib import Path
Path("renamed_demo.txt").unlink(missing_ok=True)
print("File removed")
