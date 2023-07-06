from woocommapitest.src.utilities.requests_utility import RequestsUtility


class ProductsHelper:

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_all_products_by(self, filter):
        products_api_res = self.requests_utility.get(endpoint='products?per_page=100', expected_status_code=200)
        products = [product[filter] for product in products_api_res]
        products.sort()
        return products
