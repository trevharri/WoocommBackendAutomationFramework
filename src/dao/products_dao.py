from woocommapitest.src.utilities.db_utility import DBUtility


class ProductsDAO:

    def __init__(self):
        self.db_util = DBUtility()

    def get_all_products_from_db(self, column="*"):
        sql = f"SELECT {column} FROM quicksitedb.wp_posts WHERE post_type='product';"
        rs_sql = self.db_util.execute_select(sql)
        products = [product[column] for product in rs_sql]
        products.sort()
        return products

    def get_rand_product(self, limit=1):
        sql = f"SELECT ID, post_title,post_content FROM quicksitedb.wp_posts WHERE post_type='product' ORDER BY rand() " \
              f"LIMIT {limit};"
        rs_sql = self.db_util.execute_select(sql)
        return rs_sql

    def get_product_by_id(self, product_id):
        sql = f'SELECT prod.ID, prod.post_title, prod.post_content, price.meta_value FROM quicksitedb.wp_posts prod ' \
              f'LEFT JOIN quicksitedb.wp_postmeta price ON prod.ID = price.post_id WHERE ID={product_id} AND ' \
              f'meta_key="_regular_price";'
        rs_sql = self.db_util.execute_select(sql)
        return rs_sql[0]

