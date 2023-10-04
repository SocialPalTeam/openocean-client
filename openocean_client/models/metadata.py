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

class Metadata(object):
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
        'image_url': 'str',
        'discord_url': 'str',
        'description': 'str',
        'external_url': 'str',
        'banner_image_url': 'str',
        'twitter_username': 'str'
    }

    attribute_map = {
        'image_url': 'imageUrl',
        'discord_url': 'discordUrl',
        'description': 'description',
        'external_url': 'externalUrl',
        'banner_image_url': 'bannerImageUrl',
        'twitter_username': 'twitterUsername'
    }

    def __init__(self, image_url=None, discord_url=None, description=None, external_url=None, banner_image_url=None, twitter_username=None):  # noqa: E501
        """Metadata - a model defined in Swagger"""  # noqa: E501
        self._image_url = None
        self._discord_url = None
        self._description = None
        self._external_url = None
        self._banner_image_url = None
        self._twitter_username = None
        self.discriminator = None
        self.image_url = image_url
        self.discord_url = discord_url
        self.description = description
        self.external_url = external_url
        self.banner_image_url = banner_image_url
        self.twitter_username = twitter_username

    @property
    def image_url(self):
        """Gets the image_url of this Metadata.  # noqa: E501

        nft image  # noqa: E501

        :return: The image_url of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Metadata.

        nft image  # noqa: E501

        :param image_url: The image_url of this Metadata.  # noqa: E501
        :type: str
        """
        if image_url is None:
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501

        self._image_url = image_url

    @property
    def discord_url(self):
        """Gets the discord_url of this Metadata.  # noqa: E501

        discord  # noqa: E501

        :return: The discord_url of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._discord_url

    @discord_url.setter
    def discord_url(self, discord_url):
        """Sets the discord_url of this Metadata.

        discord  # noqa: E501

        :param discord_url: The discord_url of this Metadata.  # noqa: E501
        :type: str
        """
        if discord_url is None:
            raise ValueError("Invalid value for `discord_url`, must not be `None`")  # noqa: E501

        self._discord_url = discord_url

    @property
    def description(self):
        """Gets the description of this Metadata.  # noqa: E501

        description  # noqa: E501

        :return: The description of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Metadata.

        description  # noqa: E501

        :param description: The description of this Metadata.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def external_url(self):
        """Gets the external_url of this Metadata.  # noqa: E501


        :return: The external_url of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """Sets the external_url of this Metadata.


        :param external_url: The external_url of this Metadata.  # noqa: E501
        :type: str
        """
        if external_url is None:
            raise ValueError("Invalid value for `external_url`, must not be `None`")  # noqa: E501

        self._external_url = external_url

    @property
    def banner_image_url(self):
        """Gets the banner_image_url of this Metadata.  # noqa: E501


        :return: The banner_image_url of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._banner_image_url

    @banner_image_url.setter
    def banner_image_url(self, banner_image_url):
        """Sets the banner_image_url of this Metadata.


        :param banner_image_url: The banner_image_url of this Metadata.  # noqa: E501
        :type: str
        """
        if banner_image_url is None:
            raise ValueError("Invalid value for `banner_image_url`, must not be `None`")  # noqa: E501

        self._banner_image_url = banner_image_url

    @property
    def twitter_username(self):
        """Gets the twitter_username of this Metadata.  # noqa: E501

        twitter  # noqa: E501

        :return: The twitter_username of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._twitter_username

    @twitter_username.setter
    def twitter_username(self, twitter_username):
        """Sets the twitter_username of this Metadata.

        twitter  # noqa: E501

        :param twitter_username: The twitter_username of this Metadata.  # noqa: E501
        :type: str
        """
        if twitter_username is None:
            raise ValueError("Invalid value for `twitter_username`, must not be `None`")  # noqa: E501

        self._twitter_username = twitter_username

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
        if issubclass(Metadata, dict):
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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
