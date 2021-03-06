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


class ArticleEmbargoUpdater(object):
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
        'is_embargoed': 'bool',
        'embargo_date': 'str',
        'embargo_type': 'str',
        'embargo_reason': 'str'
    }

    attribute_map = {
        'is_embargoed': 'is_embargoed',
        'embargo_date': 'embargo_date',
        'embargo_type': 'embargo_type',
        'embargo_reason': 'embargo_reason'
    }

    def __init__(self, is_embargoed=None, embargo_date=None, embargo_type=None, embargo_reason=None):  # noqa: E501
        """ArticleEmbargoUpdater - a model defined in Swagger"""  # noqa: E501

        self._is_embargoed = None
        self._embargo_date = None
        self._embargo_type = None
        self._embargo_reason = None
        self.discriminator = None

        if is_embargoed is not None:
            self.is_embargoed = is_embargoed
        if embargo_date is not None:
            self.embargo_date = embargo_date
        if embargo_type is not None:
            self.embargo_type = embargo_type
        if embargo_reason is not None:
            self.embargo_reason = embargo_reason

    @property
    def is_embargoed(self):
        """Gets the is_embargoed of this ArticleEmbargoUpdater.  # noqa: E501

        Embargo status  # noqa: E501

        :return: The is_embargoed of this ArticleEmbargoUpdater.  # noqa: E501
        :rtype: bool
        """
        return self._is_embargoed

    @is_embargoed.setter
    def is_embargoed(self, is_embargoed):
        """Sets the is_embargoed of this ArticleEmbargoUpdater.

        Embargo status  # noqa: E501

        :param is_embargoed: The is_embargoed of this ArticleEmbargoUpdater.  # noqa: E501
        :type: bool
        """

        self._is_embargoed = is_embargoed

    @property
    def embargo_date(self):
        """Gets the embargo_date of this ArticleEmbargoUpdater.  # noqa: E501

        Date when the embargo expires and the article gets published  # noqa: E501

        :return: The embargo_date of this ArticleEmbargoUpdater.  # noqa: E501
        :rtype: str
        """
        return self._embargo_date

    @embargo_date.setter
    def embargo_date(self, embargo_date):
        """Sets the embargo_date of this ArticleEmbargoUpdater.

        Date when the embargo expires and the article gets published  # noqa: E501

        :param embargo_date: The embargo_date of this ArticleEmbargoUpdater.  # noqa: E501
        :type: str
        """

        self._embargo_date = embargo_date

    @property
    def embargo_type(self):
        """Gets the embargo_type of this ArticleEmbargoUpdater.  # noqa: E501

        Embargo can be enabled at the article or the file level. Possible values: article, file  # noqa: E501

        :return: The embargo_type of this ArticleEmbargoUpdater.  # noqa: E501
        :rtype: str
        """
        return self._embargo_type

    @embargo_type.setter
    def embargo_type(self, embargo_type):
        """Sets the embargo_type of this ArticleEmbargoUpdater.

        Embargo can be enabled at the article or the file level. Possible values: article, file  # noqa: E501

        :param embargo_type: The embargo_type of this ArticleEmbargoUpdater.  # noqa: E501
        :type: str
        """
        allowed_values = ["article", "file"]  # noqa: E501
        if embargo_type not in allowed_values:
            raise ValueError(
                "Invalid value for `embargo_type` ({0}), must be one of {1}"  # noqa: E501
                .format(embargo_type, allowed_values)
            )

        self._embargo_type = embargo_type

    @property
    def embargo_reason(self):
        """Gets the embargo_reason of this ArticleEmbargoUpdater.  # noqa: E501

        Reason for setting embargo  # noqa: E501

        :return: The embargo_reason of this ArticleEmbargoUpdater.  # noqa: E501
        :rtype: str
        """
        return self._embargo_reason

    @embargo_reason.setter
    def embargo_reason(self, embargo_reason):
        """Sets the embargo_reason of this ArticleEmbargoUpdater.

        Reason for setting embargo  # noqa: E501

        :param embargo_reason: The embargo_reason of this ArticleEmbargoUpdater.  # noqa: E501
        :type: str
        """

        self._embargo_reason = embargo_reason

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
        if issubclass(ArticleEmbargoUpdater, dict):
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
        if not isinstance(other, ArticleEmbargoUpdater):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
