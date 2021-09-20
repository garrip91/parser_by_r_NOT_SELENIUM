from typing import Generator

import requests

MAX_LIMIT = 1499


class OptiComParser:
    def __init__(self, session: requests.Session):
        self._session = session

    def parse_tree(self) -> Generator[int, None, None]:
        tree = self.load("https://api.opti-com.ru/v1.1/catalog/tree")["tree"]

        for big_category in tree:
            yield big_category['id']

    def count_products(self, category_id: int):
        url = "https://api.opti-com.ru/v1.1/catalog/products?limit=1&offset=0&catalog[]={}"
        return self.load(url.format(category_id))["totalproductcount"]

    def parse_products(self, category_id: int):
        products_len = self.count_products(category_id)
        for i in range((products_len + MAX_LIMIT - 1) // MAX_LIMIT):
            url = f"https://api.opti-com.ru/v1.1/catalog/products?" \
                  f"catalog[]={category_id}&limit={MAX_LIMIT}&offset={i * MAX_LIMIT}"
            response = self.load(url)
            yield from (product["id"] for product in response["products"])

    def parse_product(self, product_id: int):
        url = f"https://api.opti-com.ru/v1.1/catalog/product/{product_id}"
        product_data = self.load(url)

        product_dict = {
            "id": product_id,
            "title": product_data["product"].get("title"), # Заголовок товара
            "price": product_data["product"].get("price"), # Цена товара
            "article": product_data["product"].get("article"), # Артикул
            "quantity": product_data["product"].get("quantity"), # Количество товара на складе
            "available": product_data["product"].get("isavailable"), # Доступность товара (можно ли заказать товар (в наличии или нет))
            "attributes": {attr['title']: attr['value'] for attr in product_data.get("attributes", [])}, # Характеристики товара
            "about": product_data["product"].get("about"), # "О товаре"
            "certificates": [certificate["path"] for certificate in product_data.get("certificates", [])], # Типа техпаспорта товара
            "images": [image["image"] for image in product_data["product"].get("images", [])], # Фотоальбом товара
        }

        if product_data["product"].get("full"):
            product_dict["description"] = [desc["content"] for desc in product_data["product"]["full"]] # Описание товара

        return product_dict

    def load(self, url: str):
        while True:
            try:
                data = self._session.get(url, timeout=10).json()
                return data
            except Exception as e:
                print(e)
