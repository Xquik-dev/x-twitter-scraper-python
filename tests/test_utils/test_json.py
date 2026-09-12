# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
from typing import Any, Union

import pytest
import pydantic

from x_twitter_scraper import _compat
from x_twitter_scraper._utils._json import openapi_dumps


class TestOpenapiDumps:
    def test_basic(self) -> None:
        assert openapi_dumps({"key": "value", "number": 42}) == b'{"key":"value","number":42}'

    def test_datetime_serialization(self) -> None:
        assert (
            openapi_dumps({"datetime": datetime.datetime(2023, 1, 1, 12, 0, 0)})
            == b'{"datetime":"2023-01-01T12:00:00"}'
        )

    def test_pydantic_model_serialization(self) -> None:
        class User(pydantic.BaseModel):
            first_name: str
            last_name: str
            age: int

        model_instance = User(first_name="John", last_name="Kramer", age=83)
        assert (
            openapi_dumps({"model": model_instance}) == b'{"model":{"first_name":"John","last_name":"Kramer","age":83}}'
        )

    @pytest.mark.parametrize(
        "values, expected",
        [
            ({"name": "Alice"}, b'{"model":{"name":"Alice"}}'),
            (
                {"name": "Bob", "role": "admin", "active": False},
                b'{"model":{"name":"Bob","role":"admin","active":false}}',
            ),
        ],
        ids=["defaults omitted", "explicit overrides retained"],
    )
    def test_pydantic_model_with_default_values(self, values: dict[str, Any], expected: bytes) -> None:
        class User(pydantic.BaseModel):
            name: str
            role: str = "user"
            active: bool = True
            score: int = 0

        assert openapi_dumps({"model": User(**values)}) == expected

    def test_pydantic_model_with_alias(self) -> None:
        class User(pydantic.BaseModel):
            first_name: str = pydantic.Field(alias="firstName")
            last_name: str = pydantic.Field(alias="lastName")

        model_instance = User(firstName="John", lastName="Doe")
        assert openapi_dumps({"model": model_instance}) == b'{"model":{"firstName":"John","lastName":"Doe"}}'

    def test_pydantic_model_with_alias_and_default(self) -> None:
        class User(pydantic.BaseModel):
            user_name: str = pydantic.Field(alias="userName")
            user_role: str = pydantic.Field(default="member", alias="userRole")
            is_active: bool = pydantic.Field(default=True, alias="isActive")

        model_instance = User(userName="charlie")
        assert openapi_dumps({"model": model_instance}) == b'{"model":{"userName":"charlie"}}'

        model_with_overrides = User(userName="diana", userRole="admin", isActive=False)
        assert (
            openapi_dumps({"model": model_with_overrides})
            == b'{"model":{"userName":"diana","userRole":"admin","isActive":false}}'
        )

    def test_pydantic_model_with_nested_models_and_defaults(self) -> None:
        class Address(pydantic.BaseModel):
            street: str
            city: str = "Unknown"

        class User(pydantic.BaseModel):
            name: str
            address: Address
            verified: bool = False

        if _compat.PYDANTIC_V1:
            # to handle forward references in Pydantic v1
            User.update_forward_refs(**locals())  # type: ignore[reportDeprecated]

        address = Address(street="123 Main St")
        user = User(name="Diana", address=address)
        assert openapi_dumps({"user": user}) == b'{"user":{"name":"Diana","address":{"street":"123 Main St"}}}'

        address_with_city = Address(street="456 Oak Ave", city="Boston")
        user_verified = User(name="Eve", address=address_with_city, verified=True)
        assert (
            openapi_dumps({"user": user_verified})
            == b'{"user":{"name":"Eve","address":{"street":"456 Oak Ave","city":"Boston"},"verified":true}}'
        )

    def test_pydantic_model_with_optional_fields(self) -> None:
        class User(pydantic.BaseModel):
            name: str
            email: Union[str, None]
            phone: Union[str, None]

        model_with_none = User(name="Eve", email=None, phone=None)
        assert openapi_dumps({"model": model_with_none}) == b'{"model":{"name":"Eve","email":null,"phone":null}}'

        model_with_values = User(name="Frank", email="frank@example.com", phone=None)
        assert (
            openapi_dumps({"model": model_with_values})
            == b'{"model":{"name":"Frank","email":"frank@example.com","phone":null}}'
        )

    def test_rejects_unsupported_objects(self) -> None:
        with pytest.raises(TypeError, match="is not JSON serializable"):
            openapi_dumps(object())
