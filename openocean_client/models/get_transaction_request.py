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

class GetTransactionRequest(object):
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
        'chain': 'str',
        'hash': 'str'
    }

    attribute_map = {
        'chain': 'chain',
        'hash': 'hash'
    }

    def __init__(self, chain=None, hash=None):  # noqa: E501
        """GetTransactionRequest - a model defined in Swagger"""  # noqa: E501
        self._chain = None
        self._hash = None
        self.discriminator = None
        self.chain = chain
        self.hash = hash

    @property
    def chain(self):
        """Gets the chain of this GetTransactionRequest.  # noqa: E501

        chain code  # noqa: E501

        :return: The chain of this GetTransactionRequest.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this GetTransactionRequest.

        chain code  # noqa: E501

        :param chain: The chain of this GetTransactionRequest.  # noqa: E501
        :type: str
        """
        if chain is None:
            raise ValueError("Invalid value for `chain`, must not be `None`")  # noqa: E501
        allowed_values = ["eth", "bsc", "polygon", "avax", "fantom", "optimism", "arbitrum", "okex", "xdai", "heco", "boba", "aurora", "cronos", "harmony", "kava", "solana", "ont", "aptos", "near", "tron"]  # noqa: E501
        if chain not in allowed_values:
            raise ValueError(
                "Invalid value for `chain` ({0}), must be one of {1}"  # noqa: E501
                .format(chain, allowed_values)
            )

        self._chain = chain

    @property
    def hash(self):
        """Gets the hash of this GetTransactionRequest.  # noqa: E501


        :return: The hash of this GetTransactionRequest.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this GetTransactionRequest.


        :param hash: The hash of this GetTransactionRequest.  # noqa: E501
        :type: str
        """
        if hash is None:
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

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
        if issubclass(GetTransactionRequest, dict):
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
        if not isinstance(other, GetTransactionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other