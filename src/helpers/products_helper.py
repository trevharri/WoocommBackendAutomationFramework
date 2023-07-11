from woocommapitest.src.utilities.requests_utility import RequestsUtility


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
