# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr


class Model200Response(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'int',
        '_class': 'str'
    }

    attribute_map = {
        'name': 'name',
        '_class': 'class'
    }

    def __init__(self, name=None, _class=None):  # noqa: E501
        """Model200Response - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self.__class = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if _class is not None:
            self._class = _class

    @property
    def name(self):
        """Gets the name of this Model200Response.  # noqa: E501


        :return: The name of this Model200Response.  # noqa: E501
        :rtype: int
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model200Response.


        :param name: The name of this Model200Response.  # noqa: E501
        :type name: int
        """

        self._name = name

    @property
    def _class(self):
        """Gets the _class of this Model200Response.  # noqa: E501


        :return: The _class of this Model200Response.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Model200Response.


        :param _class: The _class of this Model200Response.  # noqa: E501
        :type _class: str
        """

        self.__class = _class

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Model200Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Model200Response):
            return True

        return self.to_dict() != other.to_dict()

#class Model200ResponsePydanic(BaseModel):
    name: Optional[StrictInt] = None
    _class: Optional[StrictStr] = Field(None, alias="class")


