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


from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from petstore_api.models import ReadOnlyFirst

class ArrayTest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    array_of_string: Optional[List[StrictStr]] = None
    array_array_of_integer: Optional[List[List[StrictInt]]] = None
    array_array_of_model: Optional[List[List[ReadOnlyFirst]]] = None

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
    def from_json(cls, json_str: str) -> ArrayTest:
        """Create an instance of ArrayTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in array_array_of_model (list)
        _items = []
        if self.array_array_of_model:
            for _item in self.array_array_of_model:
                if _item:
                    _items.append(_item.to_dict())
            _dict['array_array_of_model'] = _items

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ArrayTest:
        """Create an instance of ArrayTest from a dict"""
        return ArrayTest.parse_obj(obj)


