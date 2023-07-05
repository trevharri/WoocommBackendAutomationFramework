import os


class CredentialsUtility:

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get('WC_KEY', 'ck_e11d32d3e0634953456ef5785e21992c9cef8d7a')
        wc_secret = os.environ.get('WC_SECRET', 'cs_2f4189fb70b77450ea2c67f062850ca47ed9fb0e')

        # if not wc_key or wc_secret:
        #     raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be in env variables.")
        # else:
        return (wc_key, wc_secret)

    @staticmethod
    def get_db_creds():
        db_user = os.environ.get('DB_USER', 'root')
        db_password = os.environ.get('DB_PASSWORD', 'root')

        # if not db_user or db_password:
        #     raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in env variables.")
        # else:
        return {"db_user": db_user, "db_password": db_password}
