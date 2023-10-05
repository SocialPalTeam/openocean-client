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


class Orders(object):
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
        'id': 'str',
        'contract_address': 'str',
        'collection': 'Collection',
        'token_id': 'float',
        'name': 'str',
        'schema_name': 'str',
        'market': 'str',
        'price': 'float',
        'owner': 'str',
        'status': 'str',
        'image_url': 'str',
        'traits': 'list[str]',
        'code': 'str',
        'payment_asset': 'OrderPaymentAsset',
        'is_flagged': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'contract_address': 'contract_address',
        'collection': 'collection',
        'token_id': 'token_id',
        'name': 'name',
        'schema_name': 'schema_name',
        'market': 'market',
        'price': 'price',
        'owner': 'owner',
        'status': 'status',
        'image_url': 'image_url',
        'traits': 'traits',
        'code': 'code',
        'payment_asset': 'paymentAsset',
        'is_flagged': 'isFlagged'
    }

    def __init__(self, id=None, contract_address=None, collection=None, token_id=None, name=None, schema_name=None, market=None, price=None, owner=None, status=None, image_url=None, traits=None, code=None, payment_asset=None, is_flagged=None, _configuration=None):  # noqa: E501
        """Orders - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._contract_address = None
        self._collection = None
        self._token_id = None
        self._name = None
        self._schema_name = None
        self._market = None
        self._price = None
        self._owner = None
        self._status = None
        self._image_url = None
        self._traits = None
        self._code = None
        self._payment_asset = None
        self._is_flagged = None
        self.discriminator = None

        self.id = id
        self.contract_address = contract_address
        self.collection = collection
        self.token_id = token_id
        self.name = name
        self.schema_name = schema_name
        self.market = market
        self.price = price
        self.owner = owner
        self.status = status
        self.image_url = image_url
        self.traits = traits
        self.code = code
        self.payment_asset = payment_asset
        self.is_flagged = is_flagged

    @property
    def id(self):
        """Gets the id of this Orders.  # noqa: E501

        id  # noqa: E501

        :return: The id of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Orders.

        id  # noqa: E501

        :param id: The id of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def contract_address(self):
        """Gets the contract_address of this Orders.  # noqa: E501

        contract address  # noqa: E501

        :return: The contract_address of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this Orders.

        contract address  # noqa: E501

        :param contract_address: The contract_address of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contract_address is None:
            raise ValueError("Invalid value for `contract_address`, must not be `None`")  # noqa: E501

        self._contract_address = contract_address

    @property
    def collection(self):
        """Gets the collection of this Orders.  # noqa: E501

        collection info  # noqa: E501

        :return: The collection of this Orders.  # noqa: E501
        :rtype: Collection
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this Orders.

        collection info  # noqa: E501

        :param collection: The collection of this Orders.  # noqa: E501
        :type: Collection
        """
        if self._configuration.client_side_validation and collection is None:
            raise ValueError("Invalid value for `collection`, must not be `None`")  # noqa: E501

        self._collection = collection

    @property
    def token_id(self):
        """Gets the token_id of this Orders.  # noqa: E501

        nft id  # noqa: E501

        :return: The token_id of this Orders.  # noqa: E501
        :rtype: float
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this Orders.

        nft id  # noqa: E501

        :param token_id: The token_id of this Orders.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def name(self):
        """Gets the name of this Orders.  # noqa: E501

        nft name  # noqa: E501

        :return: The name of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Orders.

        nft name  # noqa: E501

        :param name: The name of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def schema_name(self):
        """Gets the schema_name of this Orders.  # noqa: E501

        nft type  # noqa: E501

        :return: The schema_name of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this Orders.

        nft type  # noqa: E501

        :param schema_name: The schema_name of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and schema_name is None:
            raise ValueError("Invalid value for `schema_name`, must not be `None`")  # noqa: E501

        self._schema_name = schema_name

    @property
    def market(self):
        """Gets the market of this Orders.  # noqa: E501

        market  # noqa: E501

        :return: The market of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this Orders.

        market  # noqa: E501

        :param market: The market of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and market is None:
            raise ValueError("Invalid value for `market`, must not be `None`")  # noqa: E501

        self._market = market

    @property
    def price(self):
        """Gets the price of this Orders.  # noqa: E501

        unit price  # noqa: E501

        :return: The price of this Orders.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Orders.

        unit price  # noqa: E501

        :param price: The price of this Orders.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def owner(self):
        """Gets the owner of this Orders.  # noqa: E501

        nft owner  # noqa: E501

        :return: The owner of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Orders.

        nft owner  # noqa: E501

        :param owner: The owner of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def status(self):
        """Gets the status of this Orders.  # noqa: E501

        status  # noqa: E501

        :return: The status of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Orders.

        status  # noqa: E501

        :param status: The status of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def image_url(self):
        """Gets the image_url of this Orders.  # noqa: E501

        nft image  # noqa: E501

        :return: The image_url of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Orders.

        nft image  # noqa: E501

        :param image_url: The image_url of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and image_url is None:
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501

        self._image_url = image_url

    @property
    def traits(self):
        """Gets the traits of this Orders.  # noqa: E501

        nft traites  # noqa: E501

        :return: The traits of this Orders.  # noqa: E501
        :rtype: list[str]
        """
        return self._traits

    @traits.setter
    def traits(self, traits):
        """Sets the traits of this Orders.

        nft traites  # noqa: E501

        :param traits: The traits of this Orders.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and traits is None:
            raise ValueError("Invalid value for `traits`, must not be `None`")  # noqa: E501

        self._traits = traits

    @property
    def code(self):
        """Gets the code of this Orders.  # noqa: E501

        code  # noqa: E501

        :return: The code of this Orders.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Orders.

        code  # noqa: E501

        :param code: The code of this Orders.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def payment_asset(self):
        """Gets the payment_asset of this Orders.  # noqa: E501

        pay token info  # noqa: E501

        :return: The payment_asset of this Orders.  # noqa: E501
        :rtype: OrderPaymentAsset
        """
        return self._payment_asset

    @payment_asset.setter
    def payment_asset(self, payment_asset):
        """Sets the payment_asset of this Orders.

        pay token info  # noqa: E501

        :param payment_asset: The payment_asset of this Orders.  # noqa: E501
        :type: OrderPaymentAsset
        """
        if self._configuration.client_side_validation and payment_asset is None:
            raise ValueError("Invalid value for `payment_asset`, must not be `None`")  # noqa: E501

        self._payment_asset = payment_asset

    @property
    def is_flagged(self):
        """Gets the is_flagged of this Orders.  # noqa: E501

        is flagged  # noqa: E501

        :return: The is_flagged of this Orders.  # noqa: E501
        :rtype: bool
        """
        return self._is_flagged

    @is_flagged.setter
    def is_flagged(self, is_flagged):
        """Sets the is_flagged of this Orders.

        is flagged  # noqa: E501

        :param is_flagged: The is_flagged of this Orders.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_flagged is None:
            raise ValueError("Invalid value for `is_flagged`, must not be `None`")  # noqa: E501

        self._is_flagged = is_flagged

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
        if issubclass(Orders, dict):
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
        if not isinstance(other, Orders):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Orders):
            return True

        return self.to_dict() != other.to_dict()
