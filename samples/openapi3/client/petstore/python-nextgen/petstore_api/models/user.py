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
from pydantic import BaseModel, Field, StrictInt, StrictStr

from pydantic import ValidationError

class User(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[StrictInt] = None
    username: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    email: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    user_status: Optional[StrictInt] = Field(None, alias="userStatus", description="User Status")

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
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if type(obj) is not dict:
            return User.parse_obj(obj)

        return User.parse_obj({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "email": obj.get("email"),
            "password": obj.get("password"),
            "phone": obj.get("phone"),
            "user_status": obj.get("userStatus")
        })


