import json


#with open('products.json', 'r', encoding='UTF-8') as f:
with open('products_test.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
    for line in data:
        for k, v in line.items():
            if k == "attributes":
                for attrs_k, attrs_v in v.items():
                    if attrs_k == "Страна производства":
                        print(attrs_v)
                    else:
                        continue