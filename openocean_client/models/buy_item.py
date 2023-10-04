# coding: utf-8

"""
    OpenOcean-Api

    OpenOcean Swagger API Spec  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BuyItem(object):
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
        'market': 'str',
        'token_type': 'str',
        'collection': 'str',
        'token_id': 'float',
        'code': 'str',
        'amount': 'float',
        'price': 'float'
    }

    attribute_map = {
        'market': 'market',
        'token_type': 'tokenType',
        'collection': 'collection',
        'token_id': 'tokenId',
        'code': 'code',
        'amount': 'amount',
        'price': 'price'
    }

    def __init__(self, market=None, token_type=None, collection=None, token_id=None, code=None, amount=None, price=None):  # noqa: E501
        """BuyItem - a model defined in Swagger"""  # noqa: E501
        self._market = None
        self._token_type = None
        self._collection = None
        self._token_id = None
        self._code = None
        self._amount = None
        self._price = None
        self.discriminator = None
        self.market = market
        self.token_type = token_type
        self.collection = collection
        self.token_id = token_id
        self.code = code
        self.amount = amount
        self.price = price

    @property
    def market(self):
        """Gets the market of this BuyItem.  # noqa: E501

        market  # noqa: E501

        :return: The market of this BuyItem.  # noqa: E501
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this BuyItem.

        market  # noqa: E501

        :param market: The market of this BuyItem.  # noqa: E501
        :type: str
        """
        if market is None:
            raise ValueError("Invalid value for `market`, must not be `None`")  # noqa: E501
        allowed_values = ["opensea", "lookrare", "x2y2", "sudoswap"]  # noqa: E501
        if market not in allowed_values:
            raise ValueError(
                "Invalid value for `market` ({0}), must be one of {1}"  # noqa: E501
                .format(market, allowed_values)
            )

        self._market = market

    @property
    def token_type(self):
        """Gets the token_type of this BuyItem.  # noqa: E501

        nft type  # noqa: E501

        :return: The token_type of this BuyItem.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this BuyItem.

        nft type  # noqa: E501

        :param token_type: The token_type of this BuyItem.  # noqa: E501
        :type: str
        """
        if token_type is None:
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ERC721", "ERC1155"]  # noqa: E501
        if token_type not in allowed_values:
            raise ValueError(
                "Invalid value for `token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(token_type, allowed_values)
            )

        self._token_type = token_type

    @property
    def collection(self):
        """Gets the collection of this BuyItem.  # noqa: E501

        nft collection  # noqa: E501

        :return: The collection of this BuyItem.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this BuyItem.

        nft collection  # noqa: E501

        :param collection: The collection of this BuyItem.  # noqa: E501
        :type: str
        """
        if collection is None:
            raise ValueError("Invalid value for `collection`, must not be `None`")  # noqa: E501

        self._collection = collection

    @property
    def token_id(self):
        """Gets the token_id of this BuyItem.  # noqa: E501

        nft id  # noqa: E501

        :return: The token_id of this BuyItem.  # noqa: E501
        :rtype: float
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this BuyItem.

        nft id  # noqa: E501

        :param token_id: The token_id of this BuyItem.  # noqa: E501
        :type: float
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def code(self):
        """Gets the code of this BuyItem.  # noqa: E501

        orders reponse code  # noqa: E501

        :return: The code of this BuyItem.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BuyItem.

        orders reponse code  # noqa: E501

        :param code: The code of this BuyItem.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def amount(self):
        """Gets the amount of this BuyItem.  # noqa: E501

        buy quantity  # noqa: E501

        :return: The amount of this BuyItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BuyItem.

        buy quantity  # noqa: E501

        :param amount: The amount of this BuyItem.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this BuyItem.  # noqa: E501

        unit price(decimals)  # noqa: E501

        :return: The price of this BuyItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BuyItem.

        unit price(decimals)  # noqa: E501

        :param price: The price of this BuyItem.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

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
        if issubclass(BuyItem, dict):
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
        if not isinstance(other, BuyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
