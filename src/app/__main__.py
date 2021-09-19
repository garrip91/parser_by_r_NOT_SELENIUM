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
    data = []
    with open("products.txt", "r", encoding="UTF-8") as file:
        for line in file.readlines():
            product_id = int(line.strip())
            product_dict = parser.parse_product(product_id)
            data.append(product_dict)

            print(
                product_dict["id"], product_dict["title"],
                product_dict["price"], product_dict["quantity"]
            )

            with open("products.json", "w", encoding="UTF-8") as output:
                json.dump(data, output, ensure_ascii=False, indent=4)


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
