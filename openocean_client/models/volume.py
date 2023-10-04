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

class Volume(object):
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
        '_1day': 'float',
        '_7day': 'float',
        '_30day': 'float',
        'all_time': 'float'
    }

    attribute_map = {
        '_1day': '1day',
        '_7day': '7day',
        '_30day': '30day',
        'all_time': 'allTime'
    }

    def __init__(self, _1day=None, _7day=None, _30day=None, all_time=None):  # noqa: E501
        """Volume - a model defined in Swagger"""  # noqa: E501
        self.__1day = None
        self.__7day = None
        self.__30day = None
        self._all_time = None
        self.discriminator = None
        self._1day = _1day
        self._7day = _7day
        self._30day = _30day
        self.all_time = all_time

    @property
    def _1day(self):
        """Gets the _1day of this Volume.  # noqa: E501

        1day volume  # noqa: E501

        :return: The _1day of this Volume.  # noqa: E501
        :rtype: float
        """
        return self.__1day

    @_1day.setter
    def _1day(self, _1day):
        """Sets the _1day of this Volume.

        1day volume  # noqa: E501

        :param _1day: The _1day of this Volume.  # noqa: E501
        :type: float
        """
        if _1day is None:
            raise ValueError("Invalid value for `_1day`, must not be `None`")  # noqa: E501

        self.__1day = _1day

    @property
    def _7day(self):
        """Gets the _7day of this Volume.  # noqa: E501

        7day volume  # noqa: E501

        :return: The _7day of this Volume.  # noqa: E501
        :rtype: float
        """
        return self.__7day

    @_7day.setter
    def _7day(self, _7day):
        """Sets the _7day of this Volume.

        7day volume  # noqa: E501

        :param _7day: The _7day of this Volume.  # noqa: E501
        :type: float
        """
        if _7day is None:
            raise ValueError("Invalid value for `_7day`, must not be `None`")  # noqa: E501

        self.__7day = _7day

    @property
    def _30day(self):
        """Gets the _30day of this Volume.  # noqa: E501

        30day volume  # noqa: E501

        :return: The _30day of this Volume.  # noqa: E501
        :rtype: float
        """
        return self.__30day

    @_30day.setter
    def _30day(self, _30day):
        """Sets the _30day of this Volume.

        30day volume  # noqa: E501

        :param _30day: The _30day of this Volume.  # noqa: E501
        :type: float
        """
        if _30day is None:
            raise ValueError("Invalid value for `_30day`, must not be `None`")  # noqa: E501

        self.__30day = _30day

    @property
    def all_time(self):
        """Gets the all_time of this Volume.  # noqa: E501

        allTime volume  # noqa: E501

        :return: The all_time of this Volume.  # noqa: E501
        :rtype: float
        """
        return self._all_time

    @all_time.setter
    def all_time(self, all_time):
        """Sets the all_time of this Volume.

        allTime volume  # noqa: E501

        :param all_time: The all_time of this Volume.  # noqa: E501
        :type: float
        """
        if all_time is None:
            raise ValueError("Invalid value for `all_time`, must not be `None`")  # noqa: E501

        self._all_time = all_time

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
        if issubclass(Volume, dict):
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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
