import json
import requests
from api import OptiComParser, Category


def find(categories: list[Category], category_id: int):
    if category_id == 0:
        return None

    for category in categories:
        if category.id == category_id:
            return category


def to_plain(data: dict) -> None:
    to_remove = []
    to_update = []

    for key, value in data.items():
        if isinstance(value, list):
            data[key] = "^".join(value)
        elif isinstance(value, dict):
            to_update.append(value)
            to_remove.append(key)
        elif isinstance(value, str):
            data[key] = value.replace("\n", "\\n")

    for e in to_remove:
        del data[e]

    for e in to_update:
        data.update(e)


def create_csv():
    with open("products.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

    keys_set = set()
    for d in data:
        to_plain(d)
        keys_set.update(d.keys())

    keys = list(keys_set)

    with open("csv_result.csv", "w", encoding="UTF-8") as file:
        line = "||".join(str(key) for key in keys)
        file.write(line + "\n")

        for plain_dict in data:
            line = "||".join(str(plain_dict.get(key)).replace("\n", "\\n") for key in keys)
            file.write(line + "\n")


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
    tree = list(parser.get_categories())

    products_data = []
    with open("products.txt", "r", encoding="UTF-8") as file:
        for line in file.readlines():
            if line == "\n":
                continue
            else:
                product_id = int(line.strip())
                product_dict = parser.parse_product(product_id)

                if not product_dict.get('price'):
                    continue

                categories = []
                category_id = product_dict["subcategory"]

                print(f"https://api.opti-com.ru/v1.1/catalog/product/{product_dict['id']}")

                while subcategory := find(tree, category_id):
                    categories.append(subcategory.name)
                    category_id = subcategory.parent_id

                product_dict["category"] = categories
                products_data.append(product_dict)

            with open("products.json", "w", encoding="UTF-8") as output:
                json.dump(products_data, output, ensure_ascii=False, indent=4)


def main():
    # Создание сессии для совершения запросов
    session = requests.Session()

    # Выбор региона через cookies
    session.cookies.update({"regionId": "1"})

    # Инициализация парсера
    parser = OptiComParser(session=session)

    # Сбор ID всех товаров в "products.txt"
    dump_all_products(parser)

    # Загрузка данных всех товаров в "products.json"
    load_all_products(parser)

    create_csv()


if __name__ == '__main__':
    main()
