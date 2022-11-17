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


from typing import Optional
from pydantic import BaseModel, StrictStr

class HasOnlyReadOnly(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    bar: Optional[StrictStr] = None
    foo: Optional[StrictStr] = None
    __properties = ["bar", "foo"]

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
    def from_json(cls, json_str: str) -> HasOnlyReadOnly:
        """Create an instance of HasOnlyReadOnly from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HasOnlyReadOnly:
        """Create an instance of HasOnlyReadOnly from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HasOnlyReadOnly.parse_obj(obj)

        _obj = HasOnlyReadOnly.parse_obj({
            "bar": obj.get("bar"),
            "foo": obj.get("foo")
        })
        return _obj

