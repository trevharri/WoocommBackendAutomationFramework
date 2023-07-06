from woocommapitest.src.utilities.db_utility import DBUtility


class ProductsDAO:

    def __init__(self):
        self.db_util = DBUtility()

    def get_all_product_by(self, column):
        sql = f"SELECT {column} FROM quicksitedb.wp_posts WHERE post_type='product';"
        rs_sql = self.db_util.execute_select(sql)
        products = [product[column] for product in rs_sql]
        products.sort()
        return products
