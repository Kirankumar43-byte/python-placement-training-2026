# Program 8: Save JSON data
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({'name': 'Asha'}, f)
print('JSON saved')
