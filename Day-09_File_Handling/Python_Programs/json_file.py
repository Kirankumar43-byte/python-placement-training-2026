# Program 15: Store JSON to file
import json
with open("student.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Asha"}, f)
print("JSON saved")
