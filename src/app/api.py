from typing import Generator

import requests

MAX_LIMIT = 1499


class OptiComParser:
    def __init__(self, session: requests.Session):
        self._session = session

    def parse_tree(self) -> Generator[int, None, None]:
        tree = self._session.get("https://api.opti-com.ru/v1.1/catalog/tree").json()["tree"]

        for big_category in tree:
            yield big_category['id']

    def count_products(self, category_id: int):
        url = "https://api.opti-com.ru/v1.1/catalog/products?limit=1&offset=0&catalog[]={}"
        return self._session.get(url.format(category_id)).json()["totalproductcount"]

    def parse_products(self, category_id: int):
        products_len = self.count_products(category_id)
        for i in range((products_len + MAX_LIMIT - 1) // MAX_LIMIT):
            url = f"https://api.opti-com.ru/v1.1/catalog/products?" \
                  f"catalog[]={category_id}&limit={MAX_LIMIT}&offset={i * MAX_LIMIT}"
            response = self._session.get(url).json()
            yield from (product["id"] for product in response["products"])

    def parse_product(self, product_id: int):
        url = f"https://api.opti-com.ru/v1.1/catalog/product/{product_id}"
        product_data = self._session.get(url).json()

        product_dict = {
            "attributes": {attr['title']: attr['value'] for attr in product_data["attributes"]},
            "certificates": [certificate["path"] for certificate in product_data["certificates"]],
            "about": product_data["product"]["about"],
            "article": product_data["product"]["article"],
            "description": [desc["content"] for desc in product_data["product"]["full"]],
            "id": product_id,
            "images": [image["image"] for image in product_data["product"]["images"]],
            "available": product_data["product"]["isavailable"],
            "buyable": product_data["product"]["isbuyable"],
            "price": product_data["product"]["price"],
            "quantity": product_data["product"]["quantity"],
            "title": product_data["product"]["title"],
        }

        return product_dict
