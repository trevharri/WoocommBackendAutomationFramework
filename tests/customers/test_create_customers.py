import logging as logger
import pytest

from woocommapitest.src.utilities.generic_utilities import generate_random_email_and_password
from woocommapitest.src.helpers.customer_helper import CustomerHelper
from woocommapitest.src.dao.customers_dao import CustomersDAO


@pytest.mark.smoke
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    random_info = generate_random_email_and_password()
    email = random_info['email']

    customer_obj = CustomerHelper()
    customer_api_res = customer_obj.create_customer(email=email)
    email_in_api_res = customer_api_res['email']
    f_name_in_api_res = customer_api_res['first_name']
    username_in_api_res = customer_api_res['username']
    expected_username = email.split('@')[0].lower()

    assert email_in_api_res == email, f"Expected email to be: {email}" \
                                      f"Actual email is: {email_in_api_res}"
    assert f_name_in_api_res == '', "Create customer API returned value for first_name but it should be empty"
    assert username_in_api_res == expected_username

    customer_dao = CustomersDAO()
    customer_db_info = customer_dao.get_customer_by_email(email)
    id_in_api = customer_api_res['id']
    id_in_db = customer_db_info[0]['ID']

    assert id_in_db == id_in_api, f'Customer ID in DB does not match ID is API response.\n' \
                                  f'Database ID: {id_in_db}, API ID: {id_in_api}\n' \
                                  f'Email: {email}'


@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    customer_dao = CustomersDAO()
    email_in_db = customer_dao.get_random_customer_email()

    customer_obj = CustomerHelper()
    customer_obj.create_customer(email=email_in_db, expected_status_code=400)

