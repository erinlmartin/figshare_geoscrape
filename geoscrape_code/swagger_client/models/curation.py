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


class Curation(object):
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
        'id': 'int',
        'group_id': 'int',
        'account_id': 'int',
        'assigned_to': 'int',
        'article_id': 'int',
        'version': 'int',
        'comments_count': 'int',
        'status': 'str',
        'created_date': 'str',
        'modified_date': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'group_id',
        'account_id': 'account_id',
        'assigned_to': 'assigned_to',
        'article_id': 'article_id',
        'version': 'version',
        'comments_count': 'comments_count',
        'status': 'status',
        'created_date': 'created_date',
        'modified_date': 'modified_date'
    }

    def __init__(self, id=None, group_id=None, account_id=None, assigned_to=None, article_id=None, version=None, comments_count=None, status=None, created_date=None, modified_date=None):  # noqa: E501
        """Curation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._group_id = None
        self._account_id = None
        self._assigned_to = None
        self._article_id = None
        self._version = None
        self._comments_count = None
        self._status = None
        self._created_date = None
        self._modified_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if account_id is not None:
            self.account_id = account_id
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if article_id is not None:
            self.article_id = article_id
        if version is not None:
            self.version = version
        if comments_count is not None:
            self.comments_count = comments_count
        if status is not None:
            self.status = status
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date

    @property
    def id(self):
        """Gets the id of this Curation.  # noqa: E501

        The review id  # noqa: E501

        :return: The id of this Curation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Curation.

        The review id  # noqa: E501

        :param id: The id of this Curation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this Curation.  # noqa: E501

        The group in which the article is present.  # noqa: E501

        :return: The group_id of this Curation.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Curation.

        The group in which the article is present.  # noqa: E501

        :param group_id: The group_id of this Curation.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def account_id(self):
        """Gets the account_id of this Curation.  # noqa: E501

        The ID of the account of the owner of the article of this review.  # noqa: E501

        :return: The account_id of this Curation.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Curation.

        The ID of the account of the owner of the article of this review.  # noqa: E501

        :param account_id: The account_id of this Curation.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def assigned_to(self):
        """Gets the assigned_to of this Curation.  # noqa: E501

        The ID of the account to which this review is assigned.  # noqa: E501

        :return: The assigned_to of this Curation.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this Curation.

        The ID of the account to which this review is assigned.  # noqa: E501

        :param assigned_to: The assigned_to of this Curation.  # noqa: E501
        :type: int
        """

        self._assigned_to = assigned_to

    @property
    def article_id(self):
        """Gets the article_id of this Curation.  # noqa: E501

        The ID of the article of this review.  # noqa: E501

        :return: The article_id of this Curation.  # noqa: E501
        :rtype: int
        """
        return self._article_id

    @article_id.setter
    def article_id(self, article_id):
        """Sets the article_id of this Curation.

        The ID of the article of this review.  # noqa: E501

        :param article_id: The article_id of this Curation.  # noqa: E501
        :type: int
        """

        self._article_id = article_id

    @property
    def version(self):
        """Gets the version of this Curation.  # noqa: E501

        The Version number of the article in review.  # noqa: E501

        :return: The version of this Curation.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Curation.

        The Version number of the article in review.  # noqa: E501

        :param version: The version of this Curation.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def comments_count(self):
        """Gets the comments_count of this Curation.  # noqa: E501

        The number of comments in the review.  # noqa: E501

        :return: The comments_count of this Curation.  # noqa: E501
        :rtype: int
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this Curation.

        The number of comments in the review.  # noqa: E501

        :param comments_count: The comments_count of this Curation.  # noqa: E501
        :type: int
        """

        self._comments_count = comments_count

    @property
    def status(self):
        """Gets the status of this Curation.  # noqa: E501

        The status of the review.  # noqa: E501

        :return: The status of this Curation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Curation.

        The status of the review.  # noqa: E501

        :param status: The status of this Curation.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "approved", "rejected", "closed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_date(self):
        """Gets the created_date of this Curation.  # noqa: E501

        The creation date of the review.  # noqa: E501

        :return: The created_date of this Curation.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Curation.

        The creation date of the review.  # noqa: E501

        :param created_date: The created_date of this Curation.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """Gets the modified_date of this Curation.  # noqa: E501

        The date the review has been modified.  # noqa: E501

        :return: The modified_date of this Curation.  # noqa: E501
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this Curation.

        The date the review has been modified.  # noqa: E501

        :param modified_date: The modified_date of this Curation.  # noqa: E501
        :type: str
        """

        self._modified_date = modified_date

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
        if issubclass(Curation, dict):
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
        if not isinstance(other, Curation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other