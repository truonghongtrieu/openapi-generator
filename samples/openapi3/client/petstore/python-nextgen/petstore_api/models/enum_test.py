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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator
from petstore_api.models.outer_enum import OuterEnum
from petstore_api.models.outer_enum_default_value import OuterEnumDefaultValue
from petstore_api.models.outer_enum_integer import OuterEnumInteger
from petstore_api.models.outer_enum_integer_default_value import OuterEnumIntegerDefaultValue

class EnumTest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    enum_string: Optional[StrictStr] = None
    enum_string_required: StrictStr = ...
    enum_integer: Optional[StrictInt] = None
    enum_number: Optional[StrictFloat] = None
    outer_enum: Optional[OuterEnum] = Field(None, alias="outerEnum")
    outer_enum_integer: Optional[OuterEnumInteger] = Field(None, alias="outerEnumInteger")
    outer_enum_default_value: Optional[OuterEnumDefaultValue] = Field(None, alias="outerEnumDefaultValue")
    outer_enum_integer_default_value: Optional[OuterEnumIntegerDefaultValue] = Field(None, alias="outerEnumIntegerDefaultValue")
    additional_properties: Dict[str, Any] = {}
    __properties = ["enum_string", "enum_string_required", "enum_integer", "enum_number", "outerEnum", "outerEnumInteger", "outerEnumDefaultValue", "outerEnumIntegerDefaultValue"]

    @validator('enum_string')
    def enum_string_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('UPPER', 'lower', ''):
            raise ValueError("must validate the enum values ('UPPER', 'lower', '')")
        return v

    @validator('enum_string_required')
    def enum_string_required_validate_enum(cls, v):
        if v not in ('UPPER', 'lower', ''):
            raise ValueError("must validate the enum values ('UPPER', 'lower', '')")
        return v

    @validator('enum_integer')
    def enum_integer_validate_enum(cls, v):
        if v is None:
            return v

        if v not in (1, -1):
            raise ValueError("must validate the enum values (1, -1)")
        return v

    @validator('enum_number')
    def enum_number_validate_enum(cls, v):
        if v is None:
            return v

        if v not in (1.1, -1.2):
            raise ValueError("must validate the enum values (1.1, -1.2)")
        return v

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
        _dict = self.dict(by_alias=True,
                          exclude={"additional_properties"},
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnumTest:
        """Create an instance of EnumTest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EnumTest.parse_obj(obj)

        _obj = EnumTest.parse_obj({
            "enum_string": obj.get("enum_string"),
            "enum_string_required": obj.get("enum_string_required"),
            "enum_integer": obj.get("enum_integer"),
            "enum_number": obj.get("enum_number"),
            "outer_enum": obj.get("outerEnum"),
            "outer_enum_integer": obj.get("outerEnumInteger"),
            "outer_enum_default_value": obj.get("outerEnumDefaultValue"),
            "outer_enum_integer_default_value": obj.get("outerEnumIntegerDefaultValue")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

