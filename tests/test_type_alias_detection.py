# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import sys
import typing
from typing_extensions import TypeAliasType

from x_twitter_scraper._utils._typing import is_type_alias_type

Text = TypeAliasType("Text", str)
if sys.version_info >= (3, 12):
    NativeText = typing.TypeAliasType("NativeText", str)


def test_type_alias_detection_preserves_native_and_backported_aliases() -> None:
    assert is_type_alias_type(Text)
    assert not is_type_alias_type(str)
    assert not is_type_alias_type("Text")
    assert not is_type_alias_type(None)
    if sys.version_info >= (3, 12):
        assert is_type_alias_type(NativeText)
