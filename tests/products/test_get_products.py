import pytest

from woocommapitest.src.helpers.products_helper import ProductsHelper
from woocommapitest.src.dao.products_dao import ProductsDAO


@pytest.mark.tcid24
def test_get_all_products():
    # test wont work if there are more than 100 products
    # would be better if the ids were mapped to the names to ensure correct name is associated
    # each id
    product_dao = ProductsDAO()
    product_db_ids = product_dao.get_all_product_by('ID')
    product_db_names = product_dao.get_all_product_by('post_title')
    product_helper = ProductsHelper()
    product_api_ids = product_helper.get_all_products_by('id')
    product_api_names = product_helper.get_all_products_by('name')
    assert product_db_ids == product_api_ids, "Products ids in API response do not match product IDs found in DB."
    assert product_api_names == product_db_names, "Product names in API response do not match post_titles found in DB."

