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

class ActivityByAddressResponse(object):
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
        'code': 'float',
        'message': 'str',
        'data': 'list[ActivityByAddress]',
        'next': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data',
        'next': 'next'
    }

    def __init__(self, code=None, message=None, data=None, next=None):  # noqa: E501
        """ActivityByAddressResponse - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._data = None
        self._next = None
        self.discriminator = None
        self.code = code
        self.message = message
        if data is not None:
            self.data = data
        if next is not None:
            self.next = next

    @property
    def code(self):
        """Gets the code of this ActivityByAddressResponse.  # noqa: E501

        response code, 0-success, -1-fail, 201-invalid params, 500-server error  # noqa: E501

        :return: The code of this ActivityByAddressResponse.  # noqa: E501
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ActivityByAddressResponse.

        response code, 0-success, -1-fail, 201-invalid params, 500-server error  # noqa: E501

        :param code: The code of this ActivityByAddressResponse.  # noqa: E501
        :type: float
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this ActivityByAddressResponse.  # noqa: E501

        response message  # noqa: E501

        :return: The message of this ActivityByAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ActivityByAddressResponse.

        response message  # noqa: E501

        :param message: The message of this ActivityByAddressResponse.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def data(self):
        """Gets the data of this ActivityByAddressResponse.  # noqa: E501


        :return: The data of this ActivityByAddressResponse.  # noqa: E501
        :rtype: list[ActivityByAddress]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ActivityByAddressResponse.


        :param data: The data of this ActivityByAddressResponse.  # noqa: E501
        :type: list[ActivityByAddress]
        """

        self._data = data

    @property
    def next(self):
        """Gets the next of this ActivityByAddressResponse.  # noqa: E501


        :return: The next of this ActivityByAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this ActivityByAddressResponse.


        :param next: The next of this ActivityByAddressResponse.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if issubclass(ActivityByAddressResponse, dict):
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
        if not isinstance(other, ActivityByAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
