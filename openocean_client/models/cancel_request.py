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

class CancelRequest(object):
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
        'sender': 'str',
        'address': 'str',
        'token_id': 'float',
        'market': 'str',
        'signature': 'str',
        'code': 'str'
    }

    attribute_map = {
        'sender': 'sender',
        'address': 'address',
        'token_id': 'tokenId',
        'market': 'market',
        'signature': 'signature',
        'code': 'code'
    }

    def __init__(self, sender=None, address=None, token_id=None, market=None, signature=None, code=None):  # noqa: E501
        """CancelRequest - a model defined in Swagger"""  # noqa: E501
        self._sender = None
        self._address = None
        self._token_id = None
        self._market = None
        self._signature = None
        self._code = None
        self.discriminator = None
        self.sender = sender
        self.address = address
        self.token_id = token_id
        self.market = market
        self.signature = signature
        self.code = code

    @property
    def sender(self):
        """Gets the sender of this CancelRequest.  # noqa: E501

        canceler  # noqa: E501

        :return: The sender of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this CancelRequest.

        canceler  # noqa: E501

        :param sender: The sender of this CancelRequest.  # noqa: E501
        :type: str
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def address(self):
        """Gets the address of this CancelRequest.  # noqa: E501

        collection address  # noqa: E501

        :return: The address of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CancelRequest.

        collection address  # noqa: E501

        :param address: The address of this CancelRequest.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def token_id(self):
        """Gets the token_id of this CancelRequest.  # noqa: E501

        nft id  # noqa: E501

        :return: The token_id of this CancelRequest.  # noqa: E501
        :rtype: float
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this CancelRequest.

        nft id  # noqa: E501

        :param token_id: The token_id of this CancelRequest.  # noqa: E501
        :type: float
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def market(self):
        """Gets the market of this CancelRequest.  # noqa: E501

        market  # noqa: E501

        :return: The market of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this CancelRequest.

        market  # noqa: E501

        :param market: The market of this CancelRequest.  # noqa: E501
        :type: str
        """
        if market is None:
            raise ValueError("Invalid value for `market`, must not be `None`")  # noqa: E501
        allowed_values = ["opensea", "lookrare", "x2y2"]  # noqa: E501
        if market not in allowed_values:
            raise ValueError(
                "Invalid value for `market` ({0}), must be one of {1}"  # noqa: E501
                .format(market, allowed_values)
            )

        self._market = market

    @property
    def signature(self):
        """Gets the signature of this CancelRequest.  # noqa: E501

        signature data only x2y2  # noqa: E501

        :return: The signature of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this CancelRequest.

        signature data only x2y2  # noqa: E501

        :param signature: The signature of this CancelRequest.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def code(self):
        """Gets the code of this CancelRequest.  # noqa: E501

        listings or offers reponse code  # noqa: E501

        :return: The code of this CancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CancelRequest.

        listings or offers reponse code  # noqa: E501

        :param code: The code of this CancelRequest.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

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
        if issubclass(CancelRequest, dict):
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
        if not isinstance(other, CancelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
