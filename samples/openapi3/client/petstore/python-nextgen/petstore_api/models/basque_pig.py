# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six



from pydantic import BaseModel, Field, StrictStr

class BasquePig(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    class_name: StrictStr = Field(..., alias="className")
    color: StrictStr = ...

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.to_dict())

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.json(by_alias=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> BasquePig:
        """Create an instance of BasquePig from a JSON string"""
        return BasquePig.parse_raw(json_str)

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        return self.dict(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, dict: dict) -> BasquePig:
        """Create an instance of BasquePig from a dict"""
        return BasquePig.parse_obj(dict)

