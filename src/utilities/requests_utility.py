import requests
from requests_oauthlib import OAuth1
import os
import json
import logging as logger

from woocommapitest.src.configs.hosts_config import API_HOSTS
from woocommapitest.src.utilities.credentials_utility import CredentialsUtility


class RequestsUtility:

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.wc_creds = CredentialsUtility.get_wc_api_keys()
        self.auth = OAuth1(*self.wc_creds)

    def assert_status_code(self):
        assert self.rs_status_code == self.expected_status_code, \
            f"Expected status code: {self.expected_status_code}, but actual: {self.rs_status_code}" \
            f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)

        self.rs_status_code = rs_api.status_code
        self.expected_status_code = int(expected_status_code)
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"POST API response: {rs_api.json()}")

        return self.rs_json

    def get(self, endpoint, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint

        rs_api = requests.get(url=self.url, headers=headers, auth=self.auth)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = int(expected_status_code)
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {rs_api.json()}")

        return self.rs_json
