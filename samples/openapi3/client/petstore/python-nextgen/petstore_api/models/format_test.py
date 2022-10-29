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
from typing import Optional
from pydantic import BaseModel, Field, StrictBytes, StrictInt, StrictStr, confloat, conint, constr


class FormatTest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    integer: Optional[conint(strict=True, le=100, ge=10)] = None
    int32: Optional[conint(strict=True, le=200, ge=20)] = None
    int64: Optional[StrictInt] = None
    number: confloat(strict=True, le=543.2, ge=32.1) = ...
    float: Optional[confloat(strict=True, le=987.6, ge=54.3)] = None
    double: Optional[confloat(strict=True, le=123.4, ge=67.8)] = None
    string: Optional[constr(strict=True, regex=r'/[a-z]/i')] = None
    byte: StrictBytes = ...
    binary: Optional[StrictBytes] = None
    _date: date = Field(..., alias="date")
    date_time: Optional[datetime] = Field(None, alias="dateTime")
    uuid: Optional[StrictStr] = None
    password: constr(strict=True, max_length=64, min_length=10) = ...
    pattern_with_digits: Optional[constr(strict=True, regex=r'/^\d{10}$/')] = Field(None, description="A string that is a 10 digit number. Can have leading zeros.")
    pattern_with_digits_and_delimiter: Optional[constr(strict=True, regex=r'/^image_\d{1,3}$/i')] = Field(None, description="A string starting with 'image_' (case insensitive) and one to three digits following i.e. Image_01.")

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
    def from_json(cls, json_str: str) -> FormatTest:
        """Create an instance of FormatTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FormatTest:
        """Create an instance of FormatTest from a dict"""
        return FormatTest.parse_obj(obj)


