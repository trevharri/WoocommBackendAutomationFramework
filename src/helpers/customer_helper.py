from woocommapitest.src.utilities.generic_utilities import generate_random_email_and_password
from woocommapitest.src.utilities.requests_utility import RequestsUtility


class CustomerHelper:

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, expected_status_code=201, password="Password1", **kwargs):
        if not email:
            email = generate_random_email_and_password()["email"]

        payload = dict()
        payload["email"] = email
        payload["password"] = password
        payload.update(kwargs)

        create_user_json = self.requests_utility.post('customers', payload=payload,
                                                      expected_status_code=expected_status_code)

        return create_user_json

    def get_all_customer_ids(self):
        all_customers = self.requests_utility.get('customers?per_page=100')
        all_customer_ids = [int(customer['id']) for customer in all_customers]
        all_customer_ids.sort()

        return all_customer_ids
