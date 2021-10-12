import json
from os.path import exists

import requests
import openpyxl
from openpyxl.cell import Cell

from api import OptiComParser, Category


def find(categories: list[Category], category_id: int):
    if category_id == 0:
        return None

    for category in categories:
        if category.id == category_id:
            return category


def to_plain(data: dict) -> dict:
    country = data["attributes"].get("Страна производства", "отсутствует")
    brand = data["attributes"].get("Бренд", "отсутствует")

    return {
        "_ID_": data["id"],
        "_MAIN_CATEGORY_": data["category"][-1] if len(data["category"]) else "",
        "_CATEGORY_": "|".join(reversed(data["category"][:-1])),
        "_NAME_": data["title"],
        "_SKU_": data["article"],
        "_MANUFACTURER_": f"{brand} ({country})",
        "_PRICE_": str(round(0.95 * data["price"], 2)).replace(',', "."),
        "_QUANTITY_": data["quantity"],
        "_ATTRIBUTES_": "\n".join([
            f"{i}.|{k}|{v}" for i, (k, v)
            in enumerate(data["attributes"].items(), 1)
            if k != "Страна производства"
        ]),
        "_DESCRIPTION_": f'<p><span style="color: rgb(33, 37, 41); '
                         f'font-family: &quot;PT Sans&quot;, sans-serif; font-size: 17px; '
                         f'background-color: rgb(250, 250, 250);">'
                         f'{" ".join(" ".join(desc).split())}'
                         f'</span><br></p>' if (desc := data.get("description")) else ""
    }


def create_xlsx():
    with open("products.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

    new_data = []
    for product in data:
        plain = to_plain(product)
        if plain is not None:
            new_data.append(plain)

    new_data.sort(key=lambda x: x['_SKU_'])

    for i, e in enumerate(new_data, 1):
        e["_SORT_ORDER_"] = i

    wb = openpyxl.Workbook()
    ws = wb.active

    for e in new_data:
        try:
            ws.append(str(j) for j in e.values())
        except Exception as exc:
            print(exc)

    for row in ws:
        for cell in row:
            cell: Cell
            cell.data_type = "s"

    wb.save("products.xlsx")


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
    if not exists("./tree.json"):
        tree = list(parser.get_categories())
        with open("tree.json", "w", encoding="UTF-8") as file:
            saved_tree = [e.__dict__ for e in tree]
            json.dump(saved_tree, file, ensure_ascii=False, indent=4)
    else:
        with open("tree.json", "r", encoding="UTF-8") as file:
            saved_tree = json.load(file)
            tree = [Category(**e) for e in saved_tree]

    products_data = []
    with open("products.txt", "r", encoding="UTF-8") as file:
        for line in file.readlines():
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
    # session = requests.Session()

    # Выбор региона через cookies
    # session.cookies.update({"regionId": "1"})

    # Инициализация парсера
    # parser = OptiComParser(session=session)

    # Сбор ID всех товаров в "products.txt"
    # dump_all_products(parser)

    # Загрузка данных всех товаров в "products.json"
    # load_all_products(parser)

    create_xlsx()


if __name__ == '__main__':
    main()
