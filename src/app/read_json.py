import json


with open('products.json', 'r', encoding='utf-8') as content:
    print(len(json.load(content)))