# coding: utf-8

"""
    OpenOcean-Api

    OpenOcean Swagger API Spec  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from openocean_api.configuration import Configuration


class Nfts(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'contract_address': 'str',
        'collection_slug': 'str',
        'collection_name': 'str',
        'name': 'str',
        'token_id': 'float',
        'token_amount': 'float',
        'on_sale': 'bool',
        'schema_name': 'str',
        'floor_price': 'float',
        'image_url': 'str',
        'code': 'str',
        'payment_asset': 'OrderPaymentAsset'
    }

    attribute_map = {
        'contract_address': 'contract_address',
        'collection_slug': 'collection_slug',
        'collection_name': 'collection_name',
        'name': 'name',
        'token_id': 'token_id',
        'token_amount': 'tokenAmount',
        'on_sale': 'on_sale',
        'schema_name': 'schema_name',
        'floor_price': 'floorPrice',
        'image_url': 'image_url',
        'code': 'code',
        'payment_asset': 'paymentAsset'
    }

    def __init__(self, contract_address=None, collection_slug=None, collection_name=None, name=None, token_id=None, token_amount=None, on_sale=None, schema_name=None, floor_price=None, image_url=None, code=None, payment_asset=None, _configuration=None):  # noqa: E501
        """Nfts - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._contract_address = None
        self._collection_slug = None
        self._collection_name = None
        self._name = None
        self._token_id = None
        self._token_amount = None
        self._on_sale = None
        self._schema_name = None
        self._floor_price = None
        self._image_url = None
        self._code = None
        self._payment_asset = None
        self.discriminator = None

        self.contract_address = contract_address
        self.collection_slug = collection_slug
        self.collection_name = collection_name
        self.name = name
        self.token_id = token_id
        self.token_amount = token_amount
        self.on_sale = on_sale
        self.schema_name = schema_name
        self.floor_price = floor_price
        self.image_url = image_url
        self.code = code
        self.payment_asset = payment_asset

    @property
    def contract_address(self):
        """Gets the contract_address of this Nfts.  # noqa: E501

        collection address  # noqa: E501

        :return: The contract_address of this Nfts.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this Nfts.

        collection address  # noqa: E501

        :param contract_address: The contract_address of this Nfts.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contract_address is None:
            raise ValueError("Invalid value for `contract_address`, must not be `None`")  # noqa: E501

        self._contract_address = contract_address

    @property
    def collection_slug(self):
        """Gets the collection_slug of this Nfts.  # noqa: E501

        collection slug  # noqa: E501

        :return: The collection_slug of this Nfts.  # noqa: E501
        :rtype: str
        """
        return self._collection_slug

    @collection_slug.setter
    def collection_slug(self, collection_slug):
        """Sets the collection_slug of this Nfts.

        collection slug  # noqa: E501

        :param collection_slug: The collection_slug of this Nfts.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection_slug is None:
            raise ValueError("Invalid value for `collection_slug`, must not be `None`")  # noqa: E501

        self._collection_slug = collection_slug

    @property
    def collection_name(self):
        """Gets the collection_name of this Nfts.  # noqa: E501

        collection name  # noqa: E501

        :return: The collection_name of this Nfts.  # noqa: E501
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        """Sets the collection_name of this Nfts.

        collection name  # noqa: E501

        :param collection_name: The collection_name of this Nfts.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection_name is None:
            raise ValueError("Invalid value for `collection_name`, must not be `None`")  # noqa: E501

        self._collection_name = collection_name

    @property
    def name(self):
        """Gets the name of this Nfts.  # noqa: E501

        nft name  # noqa: E501

        :return: The name of this Nfts.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Nfts.

        nft name  # noqa: E501

        :param name: The name of this Nfts.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def token_id(self):
        """Gets the token_id of this Nfts.  # noqa: E501

        nft id  # noqa: E501

        :return: The token_id of this Nfts.  # noqa: E501
        :rtype: float
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this Nfts.

        nft id  # noqa: E501

        :param token_id: The token_id of this Nfts.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def token_amount(self):
        """Gets the token_amount of this Nfts.  # noqa: E501

        nft count  # noqa: E501

        :return: The token_amount of this Nfts.  # noqa: E501
        :rtype: float
        """
        return self._token_amount

    @token_amount.setter
    def token_amount(self, token_amount):
        """Sets the token_amount of this Nfts.

        nft count  # noqa: E501

        :param token_amount: The token_amount of this Nfts.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and token_amount is None:
            raise ValueError("Invalid value for `token_amount`, must not be `None`")  # noqa: E501

        self._token_amount = token_amount

    @property
    def on_sale(self):
        """Gets the on_sale of this Nfts.  # noqa: E501

        is on sale  # noqa: E501

        :return: The on_sale of this Nfts.  # noqa: E501
        :rtype: bool
        """
        return self._on_sale

    @on_sale.setter
    def on_sale(self, on_sale):
        """Sets the on_sale of this Nfts.

        is on sale  # noqa: E501

        :param on_sale: The on_sale of this Nfts.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and on_sale is None:
            raise ValueError("Invalid value for `on_sale`, must not be `None`")  # noqa: E501

        self._on_sale = on_sale

    @property
    def schema_name(self):
        """Gets the schema_name of this Nfts.  # noqa: E501

        nft type  # noqa: E501

        :return: The schema_name of this Nfts.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this Nfts.

        nft type  # noqa: E501

        :param schema_name: The schema_name of this Nfts.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and schema_name is None:
            raise ValueError("Invalid value for `schema_name`, must not be `None`")  # noqa: E501

        self._schema_name = schema_name

    @property
    def floor_price(self):
        """Gets the floor_price of this Nfts.  # noqa: E501

        unit price(decimals)  # noqa: E501

        :return: The floor_price of this Nfts.  # noqa: E501
        :rtype: float
        """
        return self._floor_price

    @floor_price.setter
    def floor_price(self, floor_price):
        """Sets the floor_price of this Nfts.

        unit price(decimals)  # noqa: E501

        :param floor_price: The floor_price of this Nfts.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and floor_price is None:
            raise ValueError("Invalid value for `floor_price`, must not be `None`")  # noqa: E501

        self._floor_price = floor_price

    @property
    def image_url(self):
        """Gets the image_url of this Nfts.  # noqa: E501

        nft owner  # noqa: E501

        :return: The image_url of this Nfts.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Nfts.

        nft owner  # noqa: E501

        :param image_url: The image_url of this Nfts.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and image_url is None:
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501

        self._image_url = image_url

    @property
    def code(self):
        """Gets the code of this Nfts.  # noqa: E501

        code  # noqa: E501

        :return: The code of this Nfts.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Nfts.

        code  # noqa: E501

        :param code: The code of this Nfts.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def payment_asset(self):
        """Gets the payment_asset of this Nfts.  # noqa: E501

        pay token info  # noqa: E501

        :return: The payment_asset of this Nfts.  # noqa: E501
        :rtype: OrderPaymentAsset
        """
        return self._payment_asset

    @payment_asset.setter
    def payment_asset(self, payment_asset):
        """Sets the payment_asset of this Nfts.

        pay token info  # noqa: E501

        :param payment_asset: The payment_asset of this Nfts.  # noqa: E501
        :type: OrderPaymentAsset
        """
        if self._configuration.client_side_validation and payment_asset is None:
            raise ValueError("Invalid value for `payment_asset`, must not be `None`")  # noqa: E501

        self._payment_asset = payment_asset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Nfts, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Nfts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Nfts):
            return True

        return self.to_dict() != other.to_dict()
