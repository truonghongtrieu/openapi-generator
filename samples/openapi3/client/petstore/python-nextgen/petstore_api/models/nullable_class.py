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
from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class NullableClass(object):
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
        'integer_prop': 'int',
        'number_prop': 'float',
        'boolean_prop': 'bool',
        'string_prop': 'str',
        'date_prop': 'date',
        'datetime_prop': 'datetime',
        'array_nullable_prop': 'list[object]',
        'array_and_items_nullable_prop': 'list[object]',
        'array_items_nullable': 'list[object]',
        'object_nullable_prop': 'dict(str, object)',
        'object_and_items_nullable_prop': 'dict(str, object)',
        'object_items_nullable': 'dict(str, object)'
    }

    attribute_map = {
        'integer_prop': 'integer_prop',
        'number_prop': 'number_prop',
        'boolean_prop': 'boolean_prop',
        'string_prop': 'string_prop',
        'date_prop': 'date_prop',
        'datetime_prop': 'datetime_prop',
        'array_nullable_prop': 'array_nullable_prop',
        'array_and_items_nullable_prop': 'array_and_items_nullable_prop',
        'array_items_nullable': 'array_items_nullable',
        'object_nullable_prop': 'object_nullable_prop',
        'object_and_items_nullable_prop': 'object_and_items_nullable_prop',
        'object_items_nullable': 'object_items_nullable'
    }

    def __init__(self, integer_prop=None, number_prop=None, boolean_prop=None, string_prop=None, date_prop=None, datetime_prop=None, array_nullable_prop=None, array_and_items_nullable_prop=None, array_items_nullable=None, object_nullable_prop=None, object_and_items_nullable_prop=None, object_items_nullable=None):  # noqa: E501
        """NullableClass - a model defined in OpenAPI"""  # noqa: E501

        self._integer_prop = None
        self._number_prop = None
        self._boolean_prop = None
        self._string_prop = None
        self._date_prop = None
        self._datetime_prop = None
        self._array_nullable_prop = None
        self._array_and_items_nullable_prop = None
        self._array_items_nullable = None
        self._object_nullable_prop = None
        self._object_and_items_nullable_prop = None
        self._object_items_nullable = None
        self.discriminator = None

        self.integer_prop = integer_prop
        self.number_prop = number_prop
        self.boolean_prop = boolean_prop
        self.string_prop = string_prop
        self.date_prop = date_prop
        self.datetime_prop = datetime_prop
        self.array_nullable_prop = array_nullable_prop
        self.array_and_items_nullable_prop = array_and_items_nullable_prop
        if array_items_nullable is not None:
            self.array_items_nullable = array_items_nullable
        self.object_nullable_prop = object_nullable_prop
        self.object_and_items_nullable_prop = object_and_items_nullable_prop
        if object_items_nullable is not None:
            self.object_items_nullable = object_items_nullable

    @property
    def integer_prop(self):
        """Gets the integer_prop of this NullableClass.  # noqa: E501


        :return: The integer_prop of this NullableClass.  # noqa: E501
        :rtype: int
        """
        return self._integer_prop

    @integer_prop.setter
    def integer_prop(self, integer_prop):
        """Sets the integer_prop of this NullableClass.


        :param integer_prop: The integer_prop of this NullableClass.  # noqa: E501
        :type integer_prop: int
        """

        self._integer_prop = integer_prop

    @property
    def number_prop(self):
        """Gets the number_prop of this NullableClass.  # noqa: E501


        :return: The number_prop of this NullableClass.  # noqa: E501
        :rtype: float
        """
        return self._number_prop

    @number_prop.setter
    def number_prop(self, number_prop):
        """Sets the number_prop of this NullableClass.


        :param number_prop: The number_prop of this NullableClass.  # noqa: E501
        :type number_prop: float
        """

        self._number_prop = number_prop

    @property
    def boolean_prop(self):
        """Gets the boolean_prop of this NullableClass.  # noqa: E501


        :return: The boolean_prop of this NullableClass.  # noqa: E501
        :rtype: bool
        """
        return self._boolean_prop

    @boolean_prop.setter
    def boolean_prop(self, boolean_prop):
        """Sets the boolean_prop of this NullableClass.


        :param boolean_prop: The boolean_prop of this NullableClass.  # noqa: E501
        :type boolean_prop: bool
        """

        self._boolean_prop = boolean_prop

    @property
    def string_prop(self):
        """Gets the string_prop of this NullableClass.  # noqa: E501


        :return: The string_prop of this NullableClass.  # noqa: E501
        :rtype: str
        """
        return self._string_prop

    @string_prop.setter
    def string_prop(self, string_prop):
        """Sets the string_prop of this NullableClass.


        :param string_prop: The string_prop of this NullableClass.  # noqa: E501
        :type string_prop: str
        """

        self._string_prop = string_prop

    @property
    def date_prop(self):
        """Gets the date_prop of this NullableClass.  # noqa: E501


        :return: The date_prop of this NullableClass.  # noqa: E501
        :rtype: date
        """
        return self._date_prop

    @date_prop.setter
    def date_prop(self, date_prop):
        """Sets the date_prop of this NullableClass.


        :param date_prop: The date_prop of this NullableClass.  # noqa: E501
        :type date_prop: date
        """

        self._date_prop = date_prop

    @property
    def datetime_prop(self):
        """Gets the datetime_prop of this NullableClass.  # noqa: E501


        :return: The datetime_prop of this NullableClass.  # noqa: E501
        :rtype: datetime
        """
        return self._datetime_prop

    @datetime_prop.setter
    def datetime_prop(self, datetime_prop):
        """Sets the datetime_prop of this NullableClass.


        :param datetime_prop: The datetime_prop of this NullableClass.  # noqa: E501
        :type datetime_prop: datetime
        """

        self._datetime_prop = datetime_prop

    @property
    def array_nullable_prop(self):
        """Gets the array_nullable_prop of this NullableClass.  # noqa: E501


        :return: The array_nullable_prop of this NullableClass.  # noqa: E501
        :rtype: list[object]
        """
        return self._array_nullable_prop

    @array_nullable_prop.setter
    def array_nullable_prop(self, array_nullable_prop):
        """Sets the array_nullable_prop of this NullableClass.


        :param array_nullable_prop: The array_nullable_prop of this NullableClass.  # noqa: E501
        :type array_nullable_prop: list[object]
        """

        self._array_nullable_prop = array_nullable_prop

    @property
    def array_and_items_nullable_prop(self):
        """Gets the array_and_items_nullable_prop of this NullableClass.  # noqa: E501


        :return: The array_and_items_nullable_prop of this NullableClass.  # noqa: E501
        :rtype: list[object]
        """
        return self._array_and_items_nullable_prop

    @array_and_items_nullable_prop.setter
    def array_and_items_nullable_prop(self, array_and_items_nullable_prop):
        """Sets the array_and_items_nullable_prop of this NullableClass.


        :param array_and_items_nullable_prop: The array_and_items_nullable_prop of this NullableClass.  # noqa: E501
        :type array_and_items_nullable_prop: list[object]
        """

        self._array_and_items_nullable_prop = array_and_items_nullable_prop

    @property
    def array_items_nullable(self):
        """Gets the array_items_nullable of this NullableClass.  # noqa: E501


        :return: The array_items_nullable of this NullableClass.  # noqa: E501
        :rtype: list[object]
        """
        return self._array_items_nullable

    @array_items_nullable.setter
    def array_items_nullable(self, array_items_nullable):
        """Sets the array_items_nullable of this NullableClass.


        :param array_items_nullable: The array_items_nullable of this NullableClass.  # noqa: E501
        :type array_items_nullable: list[object]
        """

        self._array_items_nullable = array_items_nullable

    @property
    def object_nullable_prop(self):
        """Gets the object_nullable_prop of this NullableClass.  # noqa: E501


        :return: The object_nullable_prop of this NullableClass.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._object_nullable_prop

    @object_nullable_prop.setter
    def object_nullable_prop(self, object_nullable_prop):
        """Sets the object_nullable_prop of this NullableClass.


        :param object_nullable_prop: The object_nullable_prop of this NullableClass.  # noqa: E501
        :type object_nullable_prop: dict(str, object)
        """

        self._object_nullable_prop = object_nullable_prop

    @property
    def object_and_items_nullable_prop(self):
        """Gets the object_and_items_nullable_prop of this NullableClass.  # noqa: E501


        :return: The object_and_items_nullable_prop of this NullableClass.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._object_and_items_nullable_prop

    @object_and_items_nullable_prop.setter
    def object_and_items_nullable_prop(self, object_and_items_nullable_prop):
        """Sets the object_and_items_nullable_prop of this NullableClass.


        :param object_and_items_nullable_prop: The object_and_items_nullable_prop of this NullableClass.  # noqa: E501
        :type object_and_items_nullable_prop: dict(str, object)
        """

        self._object_and_items_nullable_prop = object_and_items_nullable_prop

    @property
    def object_items_nullable(self):
        """Gets the object_items_nullable of this NullableClass.  # noqa: E501


        :return: The object_items_nullable of this NullableClass.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._object_items_nullable

    @object_items_nullable.setter
    def object_items_nullable(self, object_items_nullable):
        """Sets the object_items_nullable of this NullableClass.


        :param object_items_nullable: The object_items_nullable of this NullableClass.  # noqa: E501
        :type object_items_nullable: dict(str, object)
        """

        self._object_items_nullable = object_items_nullable

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
        if not isinstance(other, NullableClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NullableClass):
            return True

        return self.to_dict() != other.to_dict()

#class NullableClassPydanic(BaseModel):
    integer_prop: Optional[StrictInt] = None
    number_prop: Optional[StrictInt] = None
    boolean_prop: Optional[StrictBool] = None
    string_prop: Optional[StrictStr] = None
    date_prop: Optional[date] = None
    datetime_prop: Optional[datetime] = None
    array_nullable_prop: Optional[List[Dict[str, Any]]] = None
    array_and_items_nullable_prop: Optional[List[Dict[str, Any]]] = None
    array_items_nullable: Optional[List[Dict[str, Any]]] = None
    object_nullable_prop: Optional[Dict[str, Dict[str, Any]]] = None
    object_and_items_nullable_prop: Optional[Dict[str, Dict[str, Any]]] = None
    object_items_nullable: Optional[Dict[str, Dict[str, Any]]] = None


