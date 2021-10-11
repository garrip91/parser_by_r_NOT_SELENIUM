import json

with open('tree.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
        print(len(data))