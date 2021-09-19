import requests

# from app.api import OptiComParser
from api import OptiComParser


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


def load_all_products(parser: OptiComParser):
    with open("products.txt", "r", encoding="UTF-8") as file:
        for line in file.readlines():
            product_id = int(line.strip())
            product_dict = parser.parse_product(product_id)
            print(product_dict)
            break


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
