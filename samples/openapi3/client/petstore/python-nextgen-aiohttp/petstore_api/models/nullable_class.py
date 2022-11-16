# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr

class NullableClass(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    required_integer_prop: Optional[StrictInt] = ...
    integer_prop: Optional[StrictInt] = None
    number_prop: Optional[StrictFloat] = None
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
    __properties = ["required_integer_prop", "integer_prop", "number_prop", "boolean_prop", "string_prop", "date_prop", "datetime_prop", "array_nullable_prop", "array_and_items_nullable_prop", "array_items_nullable", "object_nullable_prop", "object_and_items_nullable_prop", "object_items_nullable"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.to_dict())

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NullableClass:
        """Create an instance of NullableClass from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NullableClass:
        """Create an instance of NullableClass from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NullableClass.parse_obj(obj)

        _obj = NullableClass.parse_obj({
            "required_integer_prop": obj.get("required_integer_prop"),
            "integer_prop": obj.get("integer_prop"),
            "number_prop": obj.get("number_prop"),
            "boolean_prop": obj.get("boolean_prop"),
            "string_prop": obj.get("string_prop"),
            "date_prop": obj.get("date_prop"),
            "datetime_prop": obj.get("datetime_prop"),
            "array_nullable_prop": obj.get("array_nullable_prop"),
            "array_and_items_nullable_prop": obj.get("array_and_items_nullable_prop"),
            "array_items_nullable": obj.get("array_items_nullable"),
            "object_nullable_prop": obj.get("object_nullable_prop"),
            "object_and_items_nullable_prop": obj.get("object_and_items_nullable_prop"),
            "object_items_nullable": obj.get("object_items_nullable")
        })
        return _obj

