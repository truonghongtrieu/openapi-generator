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


from typing import Literal, Optional
from pydantic import BaseModel, Field
from petstore_api.models import OuterEnum, OuterEnumDefaultValue, OuterEnumInteger, OuterEnumIntegerDefaultValue

class EnumTest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    enum_string: Optional[Literal['UPPER', 'lower', '']] = None
    enum_string_required: Literal['UPPER', 'lower', ''] = ...
    enum_integer: Optional[Literal[1, -1]] = None
    enum_number: Optional[Literal[1.1, -1.2]] = None
    outer_enum: Optional[OuterEnum] = Field(None, alias="outerEnum")
    outer_enum_integer: Optional[OuterEnumInteger] = Field(None, alias="outerEnumInteger")
    outer_enum_default_value: Optional[OuterEnumDefaultValue] = Field(None, alias="outerEnumDefaultValue")
    outer_enum_integer_default_value: Optional[OuterEnumIntegerDefaultValue] = Field(None, alias="outerEnumIntegerDefaultValue")

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
    def from_json(cls, json_str: str) -> EnumTest:
        """Create an instance of EnumTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of outer_enum
        if self.outer_enum:
            _dict['outerEnum'] = self.outer_enum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outer_enum_integer
        if self.outer_enum_integer:
            _dict['outerEnumInteger'] = self.outer_enum_integer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outer_enum_default_value
        if self.outer_enum_default_value:
            _dict['outerEnumDefaultValue'] = self.outer_enum_default_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outer_enum_integer_default_value
        if self.outer_enum_integer_default_value:
            _dict['outerEnumIntegerDefaultValue'] = self.outer_enum_integer_default_value.to_dict()

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnumTest:
        """Create an instance of EnumTest from a dict"""
        return EnumTest.parse_obj(obj)


