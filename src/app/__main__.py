import json
import requests
from api import OptiComParser


# Функция для сбора ID всех товаров
def dump_all_products(parser: OptiComParser):
    # Множество для отслеживания уникальных значений
    processed = set()

    # Открытие файла для записи id товаров
    with open("products.txt", "w", encoding="UTF-8") as file:
        for category_id in parser.parse_tree():
            for product in parser.parse_products(category_id):
                if product not in processed:
                    file.write(f"{product}\n")
                    processed.add(product)


# Функция загрузки всех товаров в JSON
def load_all_products(parser: OptiComParser):
    
    s = 0
    with open("products.txt", "r", encoding="UTF-8") as f:
        for line in f.readlines():
            if line == "\n":
                continue
            else:
                s += 1
    
    c = 0
    data = []
    with open("products.txt", "r", encoding="UTF-8") as file:
        for line in file.readlines():
            if line == "\n":
                continue
            else:
                product_id = int(line.strip())
                product_dict = parser.parse_product(product_id)
                if not product_dict['price']:
                    continue
                else:
                    data.append(product_dict)
                    c += 1
            
            console_line = " || ".join(
                [
                    str(product_dict['id']), # id
                    product_dict['title'], # название
                    product_dict['article'], # артикул
                    str(product_dict['price']), # цена
                    str(product_dict['quantity']), # количество
                ]
            )
            
            print(F'***[[ Товар № {c} из {s} товаров: ]]***')
            print(console_line)
            with open('data.txt', 'a', encoding='UTF-8') as output:
                output.write(console_line + "\n")

            with open("products.json", "w", encoding="UTF-8") as output:
                json.dump(data, output, ensure_ascii=False, indent=4)
                
        print(F'***[[ У ВАС ВСЕГО {s} ТОВАРОВ! ]]***')


def main():
    session = requests.Session()

    # Выбор региона через cookies
    session.cookies.update({"regionId": "1"})

    # Инициализация парсера
    parser = OptiComParser(session=session)

    dump_all_products(parser)
    load_all_products(parser)


if __name__ == '__main__':
    main()
