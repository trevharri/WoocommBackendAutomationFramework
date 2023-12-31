import pytest

from woocommapitest.src.helpers.products_helper import ProductsHelper
from woocommapitest.src.dao.products_dao import ProductsDAO


@pytest.mark.tcid24
def test_get_all_products():
    # test wont work if there are more than 100 products
    # would be better if the ids were mapped to the names to ensure correct name is associated
    # each id
    product_dao = ProductsDAO()
    product_helper = ProductsHelper()
    product_db_ids = product_dao.get_all_products_from_db('ID')
    product_db_names = product_dao.get_all_products_from_db('post_title')
    product_api_ids = product_helper.get_all_products_by('id')
    product_api_names = product_helper.get_all_products_by('name')
    assert product_db_ids == product_api_ids, "Products ids in API response do not match product IDs found in DB."
    assert product_api_names == product_db_names, "Product names in API response do not match post_titles found in DB."


@pytest.mark.tcid26
def test_get_product_by_id():
    product_dao = ProductsDAO()
    product_helper = ProductsHelper()
    db_product = product_dao.get_rand_product()[0]
    product_id = db_product['ID']
    db_product_desc = db_product['post_content']
    db_product_name = db_product['post_title']
    api_product = product_helper.get_product_by_id(product_id)
    assert db_product_name == api_product['name'], f'Get product by ID:{product_id} returned wrong product' \
                                                   f'Expected product: {db_product_name}, Returned product: {api_product["name"]}'
    assert db_product_desc in api_product['description'], "Product description in API response doesnt match" \
                                                          "description in DB"
