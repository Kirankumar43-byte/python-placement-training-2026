# Program 9: Read JSON data
import json
with open('data.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
