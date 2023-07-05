import pymysql
import logging as logger
from woocommapitest.src.utilities.credentials_utility import CredentialsUtility

class DBUtility:

    def __init__(self):
        creds_util = CredentialsUtility()
        self.creds = creds_util.get_db_creds()
        self.host = 'localhost'
        self.port = 8889

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=self.port)
        return connection

    def execute_select(self, sql):
        connection = self.create_connection()

        try:
            logger.debug(f'Executing: {sql}')
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            rs_dict = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f"Failed to run sql: {sql} \nError: {str(e)}")
        finally:
            connection.close()

        return rs_dict

    def execute_sql(self, sql):
        pass