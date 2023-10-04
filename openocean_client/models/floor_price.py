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

class FloorPrice(object):
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
        'symbol': 'str',
        'icon': 'str',
        'value': 'float'
    }

    attribute_map = {
        'symbol': 'symbol',
        'icon': 'icon',
        'value': 'value'
    }

    def __init__(self, symbol=None, icon=None, value=None):  # noqa: E501
        """FloorPrice - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._icon = None
        self._value = None
        self.discriminator = None
        self.symbol = symbol
        self.icon = icon
        self.value = value

    @property
    def symbol(self):
        """Gets the symbol of this FloorPrice.  # noqa: E501

        token symbol  # noqa: E501

        :return: The symbol of this FloorPrice.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this FloorPrice.

        token symbol  # noqa: E501

        :param symbol: The symbol of this FloorPrice.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def icon(self):
        """Gets the icon of this FloorPrice.  # noqa: E501

        token icon  # noqa: E501

        :return: The icon of this FloorPrice.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this FloorPrice.

        token icon  # noqa: E501

        :param icon: The icon of this FloorPrice.  # noqa: E501
        :type: str
        """
        if icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def value(self):
        """Gets the value of this FloorPrice.  # noqa: E501

        price  # noqa: E501

        :return: The value of this FloorPrice.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FloorPrice.

        price  # noqa: E501

        :param value: The value of this FloorPrice.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(FloorPrice, dict):
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
        if not isinstance(other, FloorPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
