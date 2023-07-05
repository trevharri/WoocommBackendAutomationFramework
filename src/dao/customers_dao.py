from woocommapitest.src.utilities.db_utility import DBUtility


class CustomersDAO:

    def __init__(self):
        self.db_util = DBUtility()

    def get_customer_by_email(self, email):
        sql = f'SELECT * FROM quicksitedb.wp_users WHERE user_email="{email}";'
        rs_sql = self.db_util.execute_select(sql)
        return rs_sql

    def get_all_customer_ids(self):
        sql = 'SELECT ID FROM quicksitedb.wp_users WHERE ID!=1 LIMIT 100;'
        rs_sql = self.db_util.execute_select(sql)
        ids_list = [customer['ID'] for customer in rs_sql]
        return ids_list

    def get_random_customer_email(self, quantity=1):
        sql = f'SELECT user_email FROM quicksitedb.wp_users ORDER BY RAND() LIMIT {quantity};'
        rs_sql = self.db_util.execute_select(sql)
        email = rs_sql[0]['user_email']
        return email
