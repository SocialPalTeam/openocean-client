# coding: utf-8

"""
    OpenOcean-Api

    OpenOcean Swagger API Spec  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import openocean_client
from openocean_client.api.wallet_api import WalletApi  # noqa: E501
from openocean_client.rest import ApiException


class TestWalletApi(unittest.TestCase):
    """WalletApi unit test stubs"""

    def setUp(self):
        self.api = WalletApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_controller_wallet_create_wallet(self):
        """Test case for controller_wallet_create_wallet

        create wallet   # noqa: E501
        """
        pass

    def test_controller_wallet_get_balance(self):
        """Test case for controller_wallet_get_balance

        get balance   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()