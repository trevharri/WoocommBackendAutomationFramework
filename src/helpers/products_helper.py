import string

from woocommapitest.src.utilities.requests_utility import RequestsUtility
import random

class ProductsHelper:
    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_all_products_by(self, key):
        products_api_res = self.requests_utility.get(endpoint='products?per_page=100')
        products = [product[key] for product in products_api_res]
        products.sort()
        return products

    def get_product_by_id(self, id):
        products_api_res = self.requests_utility.get(endpoint=f'products/{id}')
        return products_api_res

    def generate_simple_product_data(self):
        product_tag = ''.join(random.choices(string.ascii_letters, k=10))
        product_name = f'Test Product - {product_tag}'
        product_desc = f"This is a product description for product with name: {product_name}"
        product_price = str(round(random.random()*200, 2))

        product_data = {
            "name": product_name,
            "type": "simple",
            "regular_price": product_price,
            "description": product_desc,
        }
        return product_data





