from woocommapitest.src.helpers.products_helper import ProductsHelper
from woocommapitest.src.utilities.requests_utility import RequestsUtility
from woocommapitest.src.dao.products_dao import ProductsDAO


def test_create_1_simple_product():
    product_helper = ProductsHelper()
    req_util = RequestsUtility()
    product_dao = ProductsDAO()

    payload = product_helper.generate_simple_product_data()
    products_api_res = req_util.post(endpoint='products', payload=payload, expected_status_code=201)
    assert products_api_res, f"Create product api response is empty. Payload: {payload}"

    product_api_name = products_api_res['name']
    product_api_desc = products_api_res['description']
    product_api_price = float(products_api_res['regular_price'])
    assert payload['name'] == product_api_name
    assert payload['description'] == product_api_desc
    assert float(payload['regular_price']) == product_api_price

    product_id = products_api_res['id']
    product_db_data = product_dao.get_product_by_id(product_id)
    product_db_name = product_db_data['post_title']
    product_db_desc = product_db_data['post_content']
    product_db_price = float(product_db_data['meta_value'])
    assert product_db_name == product_api_name
    assert product_db_desc == product_api_desc
    assert product_db_price == product_api_price
