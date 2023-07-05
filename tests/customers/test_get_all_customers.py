import pytest
from woocommapitest.src.dao.customers_dao import CustomersDAO
from woocommapitest.src.helpers.customer_helper import CustomerHelper


@pytest.mark.tcid30
def test_get_all_customers():
    customer_helper = CustomerHelper()
    all_api_customer_ids = customer_helper.get_all_customer_ids()

    customers_dao = CustomersDAO()
    all_db_customer_ids = customers_dao.get_all_customer_ids()

    assert all_api_customer_ids == all_db_customer_ids, "List of customer IDs found in API response does not match " \
                                                        "the list found in the DB."
