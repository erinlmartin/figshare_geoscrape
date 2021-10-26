# coding: utf-8

"""
    Figshare API

    Figshare apiv2. Using Swagger 2.0  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PrivateLinkCreator(object):
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
        'expires_date': 'str'
    }

    attribute_map = {
        'expires_date': 'expires_date'
    }

    def __init__(self, expires_date=None):  # noqa: E501
        """PrivateLinkCreator - a model defined in Swagger"""  # noqa: E501

        self._expires_date = None
        self.discriminator = None

        if expires_date is not None:
            self.expires_date = expires_date

    @property
    def expires_date(self):
        """Gets the expires_date of this PrivateLinkCreator.  # noqa: E501

        Date when this private link should expire - optional. By default private links expire in 365 days.  # noqa: E501

        :return: The expires_date of this PrivateLinkCreator.  # noqa: E501
        :rtype: str
        """
        return self._expires_date

    @expires_date.setter
    def expires_date(self, expires_date):
        """Sets the expires_date of this PrivateLinkCreator.

        Date when this private link should expire - optional. By default private links expire in 365 days.  # noqa: E501

        :param expires_date: The expires_date of this PrivateLinkCreator.  # noqa: E501
        :type: str
        """

        self._expires_date = expires_date

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
        if issubclass(PrivateLinkCreator, dict):
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
        if not isinstance(other, PrivateLinkCreator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other