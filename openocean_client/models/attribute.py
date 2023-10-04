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

class Attribute(object):
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
        'key': 'str',
        'attribute_count': 'float',
        'kind': 'float',
        'values': 'list[AttributeValue]'
    }

    attribute_map = {
        'key': 'key',
        'attribute_count': 'attributeCount',
        'kind': 'kind',
        'values': 'values'
    }

    def __init__(self, key=None, attribute_count=None, kind=None, values=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._attribute_count = None
        self._kind = None
        self._values = None
        self.discriminator = None
        self.key = key
        self.attribute_count = attribute_count
        self.kind = kind
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this Attribute.  # noqa: E501

        attribute key  # noqa: E501

        :return: The key of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Attribute.

        attribute key  # noqa: E501

        :param key: The key of this Attribute.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def attribute_count(self):
        """Gets the attribute_count of this Attribute.  # noqa: E501

        number of nft of this attribute  # noqa: E501

        :return: The attribute_count of this Attribute.  # noqa: E501
        :rtype: float
        """
        return self._attribute_count

    @attribute_count.setter
    def attribute_count(self, attribute_count):
        """Sets the attribute_count of this Attribute.

        number of nft of this attribute  # noqa: E501

        :param attribute_count: The attribute_count of this Attribute.  # noqa: E501
        :type: float
        """
        if attribute_count is None:
            raise ValueError("Invalid value for `attribute_count`, must not be `None`")  # noqa: E501

        self._attribute_count = attribute_count

    @property
    def kind(self):
        """Gets the kind of this Attribute.  # noqa: E501

        value type  # noqa: E501

        :return: The kind of this Attribute.  # noqa: E501
        :rtype: float
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Attribute.

        value type  # noqa: E501

        :param kind: The kind of this Attribute.  # noqa: E501
        :type: float
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def values(self):
        """Gets the values of this Attribute.  # noqa: E501

        value list  # noqa: E501

        :return: The values of this Attribute.  # noqa: E501
        :rtype: list[AttributeValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Attribute.

        value list  # noqa: E501

        :param values: The values of this Attribute.  # noqa: E501
        :type: list[AttributeValue]
        """

        self._values = values

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
