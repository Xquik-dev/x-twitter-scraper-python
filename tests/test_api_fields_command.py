# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
from typing import Dict, List
from pathlib import Path

import pytest

from scripts.check_api_fields import main

ROOT = Path(__file__).parents[1]
SPEC_HELP = "Check network access, or set XQUIK_OPENAPI_SPEC to a local copy of https://xquik.com/openapi.json."
SPEC_FIX = "Fix the spec, or set XQUIK_OPENAPI_SPEC to a valid copy of https://xquik.com/openapi.json."
UNREADABLE_NEXT = (
    "Name the params and response types the SDK defines, or teach scripts/check_api_fields.py the new type."
)
FIX_NEXT = "Fix each field above in the SDK, or list it in accepted-field-differences.json with a reason."
REMOVE_NEXT = "Remove each difference above from accepted-field-differences.json."
INVALID_NEXT = "Fix accepted-field-differences.json in the format CONTRIBUTING.md shows under API fields."

TYPES = """
from __future__ import annotations

from typing import Any, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from pydantic import Field as FieldInfo

from x_twitter_scraper._types import FileTypes, SequenceNotStr
from x_twitter_scraper._utils import PropertyInfo
from x_twitter_scraper._models import BaseModel


class TrendParams(TypedDict, total=False):
    count: int
    legacy_filter: Annotated[str, PropertyInfo(alias="legacyFilter")]
    omit: str
    woeid: int


class Trend(BaseModel):
    name: str
    rank: int
    tweet_volume: Optional[int] = FieldInfo(alias="tweetVolume", default=None)


class TrendList(BaseModel):
    trends: List[Trend]
    woeid: int
    legacy_score: Optional[float] = FieldInfo(alias="legacyScore", default=None)
    meta: Optional[Dict[str, object]] = None
    parent: Optional[TrendList] = None
    paused_reason: Optional[Literal["x_user_not_found"]] = FieldInfo(alias="pausedReason", default=None)


class MonitorParams(TypedDict, total=False):
    event_types: Required[Annotated[List[Literal["tweet.new"]], PropertyInfo(alias="eventTypes")]]
    username: Required[str]


class Monitor(BaseModel):
    id: str
    event_types: List[Literal["tweet.new"]] = FieldInfo(alias="eventTypes")
    name: str


class UploadParams(TypedDict, total=False):
    account: Required[str]
    attachments: SequenceNotStr[FileTypes]
    file: FileTypes
    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Upload(BaseModel):
    created: datetime
    id: str


class ArchiveParams(TypedDict, total=False):
    archive_id: Required[str]
    note: str


class ArchiveItem(BaseModel):
    a: Optional[str] = None
    b: Optional[str] = None


class ArchiveBlob(BaseModel):
    z: Optional[str] = None


class ArchiveOwner(BaseModel):
    id: Optional[str] = None
    nickname: Optional[str] = None


class ArchiveChoice(BaseModel):
    kind: Optional[str] = None
    x: Optional[str] = None
    y: Optional[str] = None


class Archive(BaseModel):
    id: str
    anything: Any = None
    blob: Optional[ArchiveBlob] = None
    choice: Optional[ArchiveChoice] = None
    cleared: Optional[str] = None
    items: Optional[List[ArchiveItem]] = None
    note: Optional[str] = None
    owner: Optional[ArchiveOwner] = None
    owners: Optional[Dict[str, ArchiveOwner]] = None
    ranks: Optional[Dict[str, ArchiveItem]] = None
    tiers: Optional[Dict[str, ArchiveItem]] = None
    labels: Optional[Dict[str, Any]] = None
    size: Optional[int] = None
    state: Optional[Literal["open", "closed"]] = None


class Weird:
    pass


RESPONSES = {"archive": Archive}
"""

RESOURCES = """
from __future__ import annotations

from typing import Any, cast

from {package} import types
from {package}.types import Upload, Monitor, TrendList


class TrendsResource:
    def list(self, woeid, count, legacy_filter):
        return self._get(
            "/trends",
            options=make_request_options(
                query=maybe_transform(
                    {{"woeid": woeid, "count": count, "legacy_filter": legacy_filter}}, types.TrendParams
                )
            ),
            cast_to=TrendList,
        )

    def create_monitor(self, event_types, username):
        return self._post(
            "/monitors",
            body=maybe_transform({{"event_types": event_types, "username": username}}, types.MonitorParams),
            options=make_request_options(),
            cast_to=Monitor,
        )

    def upload(self, account, file):
        body = deepcopy_with_paths({{"account": account, "file": file}}, [["file"]])
        return self._post("/media", body=maybe_transform(body, types.UploadParams), cast_to=cast(Any, Upload))

    def delete(self, id):
        return self._delete(path_template("/tweets/{{id}}", id=id), cast_to=NoneType)

    def legacy(self):
        return self._get("/legacy", options=make_request_options(query={{"since": "1d"}}), cast_to=object)

    def stats(self):
        return self._get("/stats", cast_to=object)

    def archive(self, archive_id, note):
        return self._post(
            path_template("/archive/{{archive_id}}", archive_id=archive_id),
            body=maybe_transform({{"archive_id": archive_id, "note": note}}, types.ArchiveParams),
            cast_to=types.Archive,
        )

    def purge(self):
        return self._delete("/purge", cast_to=NoneType)


class AsyncTrendsResource:
    async def list(self, woeid, count, legacy_filter):
        return await self._get(
            "/trends",
            options=make_request_options(
                query=await async_maybe_transform(
                    {{"woeid": woeid, "count": count, "legacy_filter": legacy_filter}}, types.TrendParams
                )
            ),
            cast_to=TrendList,
        )
"""

SPEC: Dict[str, object] = {
    "openapi": "3.1.0",
    "servers": [{"url": "https://xquik.com/api/v1"}],
    "paths": {
        "/trends": {
            "get": {
                "operationId": "listTrends",
                "parameters": [
                    {"name": "woeid", "in": "query", "schema": {"type": "integer"}},
                    {"name": "count", "in": "query", "required": True, "schema": {"type": "integer"}},
                    {"name": "cursor", "in": "query", "schema": {"type": "string"}},
                    {"$ref": "#/components/parameters/Fields"},
                    {"name": "X-Trace", "in": "header", "schema": {"type": "string"}},
                ],
                "responses": {
                    "200": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/TrendList"}}}},
                    "400": {"content": {"application/json": {"schema": {"type": "object"}}}},
                },
            }
        },
        "/monitors": {
            "post": {
                "parameters": [{"name": "Idempotency-Key", "in": "header", "schema": {"type": "string"}}],
                "requestBody": {"$ref": "#/components/requestBodies/MonitorBody"},
                "responses": {
                    "201": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/Monitor"}}}}
                },
            }
        },
        "/media": {
            "post": {
                "parameters": [{"name": "Idempotency-Key", "in": "header", "schema": {"type": "string"}}],
                "requestBody": {
                    "content": {
                        "multipart/form-data": {
                            "schema": {
                                "type": "object",
                                "required": ["account", "file"],
                                "properties": {
                                    "account": {"type": "string"},
                                    "file": {"type": "string", "format": "binary"},
                                    "is_long_video": {"type": "boolean"},
                                },
                            }
                        },
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "required": ["account", "url"],
                                "properties": {"account": {"type": "string"}, "url": {"type": "string"}},
                            }
                        },
                        "text/plain": {"schema": {"type": "string"}},
                    }
                },
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {"allOf": [{"$ref": "#/components/schemas/UploadBase"}, {"required": ["id"]}]}
                            }
                        }
                    }
                },
            }
        },
        "/tweets/{tweetId}": {
            "parameters": [{"name": "tweetId", "in": "path", "required": True, "schema": {"type": "string"}}],
            "delete": {"responses": {"204": {"description": "Deleted"}}},
        },
        "/ask": {"get": {"servers": [{"url": "https://xquik.com"}], "responses": {"200": {"description": "Answer"}}}},
        "/stats": {
            "get": {
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {"type": "object", "properties": {"total": {"type": "integer"}}}
                            }
                        }
                    }
                }
            }
        },
        "/archive/{archiveId}": {
            "post": {
                "parameters": [{"name": "archiveId", "in": "path", "required": True, "schema": {"type": "string"}}],
                "responses": {
                    "200": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/ArchiveResult"}}}}
                },
            }
        },
        "/purge": {
            "delete": {
                "requestBody": {
                    "content": {
                        "application/json": {"schema": {"type": "object", "properties": {"reason": {"type": "string"}}}}
                    }
                },
                "responses": {"204": {"description": "Purged"}},
            }
        },
    },
    "components": {
        "parameters": {"Fields": {"name": "fields", "in": "query", "schema": {"type": "string"}}},
        "requestBodies": {
            "MonitorBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": ["eventTypes", "username"],
                            "properties": {
                                "eventTypes": {"type": "array", "items": {"$ref": "#/components/schemas/EventType"}},
                                "username": {"type": "string"},
                            },
                        }
                    }
                }
            }
        },
        "schemas": {
            "EventType": {"type": "string", "enum": ["tweet.new", "follower.added"]},
            "Trend": {
                "type": "object",
                "required": ["name"],
                "properties": {
                    "name": {"type": "string"},
                    "rank": {"type": "integer"},
                    "tweetVolume": {"type": ["integer", "null"]},
                },
            },
            "TrendList": {
                "type": "object",
                "required": ["trends", "woeid"],
                "properties": {
                    "trends": {"type": "array", "items": {"$ref": "#/components/schemas/Trend"}},
                    "woeid": {"type": "integer", "const": 1},
                    "pausedReason": {"type": "string", "enum": ["x_user_not_found", "insufficient_credits", None]},
                    "capturedAt": {"type": "string", "format": "date-time"},
                    "meta": {
                        "type": "object",
                        "additionalProperties": True,
                        "properties": {"source": {"type": "string"}},
                    },
                    "parent": {"$ref": "#/components/schemas/TrendList"},
                    "nested": {"oneOf": [{"$ref": "#/components/schemas/Trend"}, {"type": "null"}]},
                },
            },
            "Monitor": {
                "type": "object",
                "required": ["id", "eventTypes", "name"],
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": ["string", "null"]},
                    "eventTypes": {"type": "array", "items": {"$ref": "#/components/schemas/EventType"}},
                },
            },
            "ArchiveBase": {"type": "object", "required": ["id"], "properties": {"id": {"type": "string"}}},
            "State": {"type": "string", "enum": ["open", "closed"]},
            "ArchiveResult": {
                "properties": {"note": {"type": "string"}},
                "allOf": [
                    {"$ref": "#/components/schemas/ArchiveBase"},
                    {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string", "description": "The archive ID."},
                            "anything": {},
                            "items": {
                                "allOf": [
                                    {
                                        "type": "array",
                                        "items": {"type": "object", "properties": {"a": {"type": "string"}}},
                                    },
                                    {
                                        "type": "array",
                                        "items": {"type": "object", "properties": {"b": {"type": "string"}}},
                                    },
                                ]
                            },
                            "state": {"allOf": [{"$ref": "#/components/schemas/State"}]},
                            "gone": {"type": "null"},
                            "cleared": {"anyOf": [{"type": "null"}]},
                            "blob": {"type": "object"},
                            "owner": {
                                "type": "object",
                                "additionalProperties": True,
                                "properties": {"id": {"type": "string"}},
                            },
                            "ranks": {
                                "allOf": [
                                    {
                                        "type": "object",
                                        "additionalProperties": {
                                            "type": "object",
                                            "properties": {"a": {"type": "string"}},
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "additionalProperties": {
                                            "type": "object",
                                            "properties": {"b": {"type": "string"}},
                                        },
                                    },
                                ]
                            },
                            "tiers": {
                                "oneOf": [
                                    {
                                        "type": "object",
                                        "additionalProperties": {
                                            "type": "object",
                                            "properties": {"a": {"type": "string"}},
                                        },
                                    },
                                    {
                                        "type": "object",
                                        "additionalProperties": {
                                            "type": "object",
                                            "properties": {"b": {"type": "string"}},
                                        },
                                    },
                                ]
                            },
                            "labels": {"type": "object", "additionalProperties": {"type": "string"}},
                            "owners": {
                                "type": "object",
                                "additionalProperties": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "string"},
                                        "nickname": {"type": "string"},
                                        "rank": {"type": "integer"},
                                    },
                                },
                            },
                            "choice": {
                                "type": "object",
                                "properties": {"kind": {"type": "string"}},
                                "oneOf": [
                                    {"type": "object", "properties": {"x": {"type": "string"}}},
                                    {"type": "object", "properties": {"y": {"type": "string"}}},
                                ],
                            },
                            "size": {"type": "object", "properties": {"w": {"type": "integer"}}},
                        },
                    },
                ],
            },
            "UploadBase": {
                "type": "object",
                "properties": {"id": {"type": "string"}, "created": {"type": "string", "format": "date-time"}},
            },
        },
    },
}

FOUND = [
    "DELETE /api/v1/purge request missing reason",
    "GET /api/v1/stats response missing (body)",
    "GET /api/v1/trends request extra legacyFilter",
    "GET /api/v1/trends request missing cursor",
    "GET /api/v1/trends request missing fields",
    "GET /api/v1/trends request required count",
    "GET /api/v1/trends response enum pausedReason",
    "GET /api/v1/trends response extra legacyScore",
    "GET /api/v1/trends response missing capturedAt",
    "GET /api/v1/trends response missing nested",
    "GET /api/v1/trends response required trends[].rank",
    "POST /api/v1/archive/{archiveId} request extra note",
    "POST /api/v1/archive/{archiveId} response missing gone",
    "POST /api/v1/archive/{archiveId} response missing owners{}.rank",
    "POST /api/v1/archive/{archiveId} response missing size",
    "POST /api/v1/media request extra attachments",
    "POST /api/v1/media request missing is_long_video",
    "POST /api/v1/media request missing url",
    "POST /api/v1/media response required created",
    "POST /api/v1/monitors request enum eventTypes[]",
    "POST /api/v1/monitors response enum eventTypes[]",
    "POST /api/v1/monitors response nullable name",
]


@pytest.fixture
def sdk_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    package = f"fieldsdk_{tmp_path.name.replace('-', '_')}"
    source = tmp_path / "repo" / "src" / package
    (source / "resources").mkdir(parents=True)
    (source / "__init__.py").write_text("")
    (source / "types.py").write_text(TYPES)
    (source / "resources" / "__init__.py").write_text("")
    (source / "resources" / "trends.py").write_text(RESOURCES.format(package=package))
    monkeypatch.setattr(sys, "path", [str(tmp_path / "repo" / "src"), *sys.path])
    spec_path = tmp_path / "openapi.json"
    spec_path.write_text(json.dumps(SPEC))
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    return tmp_path / "repo"


def run(root: Path, capsys: pytest.CaptureFixture[str], accepted: object) -> tuple[int, List[str], List[str]]:
    (root / "accepted-field-differences.json").write_text(json.dumps(accepted))
    package = next((root / "src").iterdir()).name
    status = main(root, package)
    output = capsys.readouterr()
    return status, output.out.splitlines(), output.err.splitlines()


def test_accepted_differences_pass(sdk_root: Path, capsys: pytest.CaptureFixture[str]) -> None:
    accepted = [
        {"reason": "Kept from earlier versions.", "differences": FOUND[:11]},
        {"reason": "Uploads and monitors differ on purpose.", "differences": FOUND[11:]},
    ]
    assert run(sdk_root, capsys, accepted) == (
        0,
        [
            "The SDK's fields match the API for 7 operations, and accepted-field-differences.json lists 22 accepted differences."
        ],
        [],
    )


def test_each_difference_fails_with_its_line(sdk_root: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert run(sdk_root, capsys, []) == (1, [], [*FOUND, FIX_NEXT])


def test_a_stale_acceptance_fails(sdk_root: Path, capsys: pytest.CaptureFixture[str]) -> None:
    gone = "GET /api/v1/trends response missing gone"
    accepted = [{"reason": "Kept.", "differences": [*FOUND, gone]}]
    assert run(sdk_root, capsys, accepted) == (
        1,
        [],
        [f"accepted-field-differences.json lists {gone}, which the check no longer finds. Remove it.", REMOVE_NEXT],
    )


def test_new_and_stale_differences_show_together(sdk_root: Path, capsys: pytest.CaptureFixture[str]) -> None:
    gone = "POST /api/v1/monitors request missing name"
    accepted = [{"reason": "Kept.", "differences": [*FOUND[1:], gone]}]
    assert run(sdk_root, capsys, accepted) == (
        1,
        [],
        [
            FOUND[0],
            f"accepted-field-differences.json lists {gone}, which the check no longer finds. Remove it.",
            FIX_NEXT,
        ],
    )


INVALID_ACCEPTED: List[tuple[object, str]] = [
    ({"reason": "x", "differences": FOUND}, "It must be a list of groups, each with a reason and differences."),
    ([FOUND[0]], "Group 1 must hold a reason and differences, and nothing else."),
    ([{"reason": "x", "operations": FOUND}], "Group 1 must hold a reason and differences, and nothing else."),
    ([{"reason": "", "differences": FOUND}], "Group 1 needs a non-empty reason."),
    (
        [{"reason": "x", "differences": FOUND}, {"reason": "y", "differences": []}],
        "Group 2 needs at least 1 difference.",
    ),
    (
        [{"reason": "x", "differences": ["GET /api/v1/trends response lost capturedAt"]}],
        'Group 1 lists "GET /api/v1/trends response lost capturedAt". Write a method, a path, request or response, '
        "a kind and a field, such as GET /api/v1/x/tweets/{id}/replies request extra cardName.",
    ),
    ([{"reason": "x", "differences": [*FOUND, FOUND[3]]}], f"{FOUND[3]} appears more than once."),
]


@pytest.mark.parametrize(("accepted", "problem"), INVALID_ACCEPTED)
def test_an_invalid_accepted_file_fails(
    accepted: object, problem: str, sdk_root: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert run(sdk_root, capsys, accepted) == (
        1,
        [],
        [f"accepted-field-differences.json is not valid. {problem}", INVALID_NEXT],
    )


@pytest.mark.parametrize(
    ("content", "problem"),
    [
        (None, "The file cannot be read."),
        (b'[{"reason": "x",\n "differences": [GET]}]', "Line 2 column 18 breaks the JSON syntax."),
        (b"\xff\xfe\x00", "Its bytes are not valid text."),
    ],
)
def test_an_unreadable_accepted_file_fails(
    content: bytes | None, problem: str, sdk_root: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    accepted = sdk_root / "accepted-field-differences.json"
    if content is not None:
        accepted.write_bytes(content)
    assert main(sdk_root, next((sdk_root / "src").iterdir()).name) == 1
    output = capsys.readouterr()
    assert (output.out, output.err.splitlines()) == (
        "",
        [f"accepted-field-differences.json is not valid. {problem}", INVALID_NEXT],
    )


def test_a_missing_spec_fails(
    sdk_root: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec_path = tmp_path / "missing.json"
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    assert run(sdk_root, capsys, []) == (1, [], [f"Could not read the API spec from {spec_path}. {SPEC_HELP}"])


@pytest.mark.parametrize(
    "spec",
    [
        {"paths": {"/trends": {"get": {"parameters": [{"$ref": "#/components/parameters/Missing"}]}}}},
        {"paths": {"/trends": {"get": {"responses": {"200": {"content": {"application/json": {"schema": []}}}}}}}},
        {"paths": {"/trends": {"$ref": "#/components/pathItems/Trends"}}},
    ],
    ids=["dangling-reference", "schema-list", "path-item-reference"],
)
def test_a_spec_with_an_unreadable_part_fails(
    spec: object, sdk_root: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec_path = tmp_path / "broken.json"
    spec_path.write_text(json.dumps(spec))
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    assert run(sdk_root, capsys, []) == (
        1,
        [],
        [f"The API spec from {spec_path} has a part the check cannot read. {SPEC_FIX}"],
    )


@pytest.mark.parametrize(
    ("call", "problem"),
    [
        ('self._get("/weird", cast_to=types.Weird)', "uses the type Weird, which the check cannot read"),
        (
            'self._get("/weird", cast_to=types.RESPONSES["archive"])',
            "names types.RESPONSES['archive'], which the check cannot read",
        ),
        ('self._get("/weird", cast_to=types.Missing)', "names types.Missing, which the check cannot find"),
        ('self._get("/weird", cast_to=types.Archive.__name__)', "uses the type 'Archive', which the check cannot read"),
        ('self._get("/weird", cast_to=pick(types.Archive))', "names pick(types.Archive), which the check cannot read"),
        (
            'self._get("/weird", options=make_request_options(query=build_query()), cast_to=object)',
            "builds request fields with build_query(), which the check cannot read",
        ),
        (
            'self._post("/weird", body=maybe_transform(types.ArchiveParams), cast_to=object)',
            "builds request fields with maybe_transform(types.ArchiveParams), which the check cannot read",
        ),
    ],
    ids=[
        "plain-class",
        "subscript",
        "missing-name",
        "string-name",
        "wrapped-cast",
        "built-query",
        "one-argument-transform",
    ],
)
def test_an_unreadable_type_names_its_file_and_line(
    call: str, problem: str, sdk_root: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    package = next((sdk_root / "src").iterdir()).name
    (sdk_root / "src" / package / "resources" / "weird.py").write_text(
        f"from {package} import types\n\n\nclass Weird:\n    def read(self):\n        return {call}\n"
    )
    assert run(sdk_root, capsys, []) == (
        1,
        [],
        [f"src/{package}/resources/weird.py:6 {problem}.", UNREADABLE_NEXT],
    )


def test_an_unreadable_request_names_its_file_and_line(sdk_root: Path, capsys: pytest.CaptureFixture[str]) -> None:
    package = next((sdk_root / "src").iterdir()).name
    (sdk_root / "src" / package / "resources" / "broken.py").write_text(
        "class Broken:\n    def list(self):\n        return self._get(PATH, cast_to=object)\n"
    )
    assert run(sdk_root, capsys, []) == (
        1,
        [],
        [
            f"src/{package}/resources/broken.py:3 has a request whose path or cast_to cannot be read.",
            "Fix that line. Write each request path as a string or a path_template call, and pass cast_to.",
        ],
    )


REPOSITORY_SPEC: Dict[str, object] = {
    "openapi": "3.1.0",
    "servers": [{"url": "https://xquik.com/api/v1"}],
    "paths": {
        "/x/trends": {
            "get": {
                "parameters": [
                    {"name": name, "in": "query", "schema": {"type": "string"}}
                    for name in ("at", "count", "country", "fields", "location", "omit", "region", "woeid")
                ],
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "additionalProperties": True,
                                    "required": ["capturedAt", "trends"],
                                    "properties": {
                                        "capturedAt": {"type": "string", "format": "date-time"},
                                        "trends": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "additionalProperties": True,
                                                "required": ["name"],
                                                "properties": {"name": {"type": "string"}},
                                            },
                                        },
                                    },
                                }
                            }
                        }
                    }
                },
            }
        },
        "/x/media": {
            "post": {
                "parameters": [
                    {"name": "Idempotency-Key", "in": "header", "required": True, "schema": {"type": "string"}}
                ],
                "requestBody": {
                    "content": {
                        "multipart/form-data": {
                            "schema": {
                                "type": "object",
                                "required": ["account"],
                                "properties": {
                                    "account": {"type": "string"},
                                    "caption": {"type": "string"},
                                    "file": {"type": "string", "format": "binary"},
                                    "is_long_video": {"type": "boolean"},
                                    "url": {"type": "string"},
                                },
                            }
                        }
                    }
                },
                "responses": {"200": {"content": {"application/json": {"schema": {"type": "object"}}}}},
            }
        },
        "/events": {
            "get": {
                "parameters": [
                    {"name": name, "in": "query", "schema": {"type": "string"}}
                    for name in ("cursor", "eventType", "keywordMonitorId", "limit", "monitorId", "postMonitorId")
                ],
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "additionalProperties": True,
                                    "required": ["events"],
                                    "properties": {
                                        "events": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "additionalProperties": True,
                                                "required": ["type"],
                                                "properties": {"type": {"type": "string", "enum": ["tweet.new"]}},
                                            },
                                        }
                                    },
                                }
                            }
                        }
                    }
                },
            }
        },
        "/drafts/{id}": {
            "delete": {
                "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "string"}}],
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {"type": "object", "properties": {"deleted": {"type": "boolean"}}}
                            }
                        }
                    }
                },
            }
        },
    },
}


def test_the_repository_sdk_types_are_compared(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    (root / "src").symlink_to(ROOT / "src", target_is_directory=True)
    (root / "accepted-field-differences.json").write_text("[]")
    spec_path = tmp_path / "openapi.json"
    spec_path.write_text(json.dumps(REPOSITORY_SPEC))
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    assert main(root, "x_twitter_scraper") == 1
    output = capsys.readouterr()
    assert (output.out, output.err.splitlines()) == (
        "",
        [
            "DELETE /api/v1/drafts/{id} response missing (body)",
            "GET /api/v1/events response enum events[].type",
            "GET /api/v1/x/trends request missing region",
            "GET /api/v1/x/trends response required capturedAt",
            "POST /api/v1/x/media request missing caption",
            FIX_NEXT,
        ],
    )
