import json


with open('products.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
    for k, v in data[0].items():
        print(v["Страна производства"])