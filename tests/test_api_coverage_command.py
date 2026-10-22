# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Iterator
from pathlib import Path
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing_extensions import override

import pytest

from scripts.check_api_coverage import main

ROOT = Path(__file__).parents[1]
SPEC_HELP = "Check network access, or set XQUIK_OPENAPI_SPEC to a local copy of https://xquik.com/openapi.json."
ADD_NEXT = "Add each operation above to the SDK, or list it in excluded-operations.json with a reason."
REMOVE_NEXT = "Remove each operation above from excluded-operations.json."
FIX_NEXT = "Fix excluded-operations.json in the format CONTRIBUTING.md shows under API coverage."
READ_NEXT = "Fix that line. Write each request path as a string or a path_template call, and pass cast_to."
COVERED = "The SDK covers 2 of 3 API operations, and excluded-operations.json lists the other 1."

RESOURCES = {
    "trends.py": """
class TrendsResource:
    def list(self):
        return self._get("/trends", cast_to=TrendListResponse)
""",
    "x/tweets.py": """
class TweetsResource:
    def retrieve(self, id):
        return self._get(path_template("/x/tweets/{id}", id=id), cast_to=TweetDetail)

    def delete(self, id):
        return self._delete(path_template("/x/tweets/{id}", id=id), cast_to=TweetDeleteResponse)

    def search(self, query):
        return self.params.get("q", query)
""",
}

EXCLUSIONS = [{"reason": "Searches the docs outside the SDK base URL.", "operations": ["GET /ask"]}]

PUBLIC_PATHS: dict[str, object] = {
    "/api/v1/trends": {"get": {"operationId": "listTrends"}},
    "/api/v1/x/tweets/{tweetId}": {"get": {"operationId": "getTweet"}, "parameters": []},
    "/ask": {"get": {"operationId": "askDocs"}},
}
PUBLIC_SPEC: dict[str, object] = {"openapi": "3.1.0", "servers": [{"url": "https://xquik.com"}], "paths": PUBLIC_PATHS}
SPEC_BODY = json.dumps(PUBLIC_SPEC).encode()


INVALID_EXCLUSIONS: list[tuple[object, str]] = [
    (
        {"reason": "x", "operations": ["GET /ask"]},
        "It must be a list of groups, each with a reason and operations.",
    ),
    (["GET /ask"], "Group 1 must hold a reason and operations, and nothing else."),
    ([{"operations": ["GET /ask"]}], "Group 1 must hold a reason and operations, and nothing else."),
    (
        [{"reason": "x", "operations": ["GET /ask"], "note": "y"}],
        "Group 1 must hold a reason and operations, and nothing else.",
    ),
    ([{"reason": " ", "operations": ["GET /ask"]}], "Group 1 needs a non-empty reason."),
    ([{"reason": 7, "operations": ["GET /ask"]}], "Group 1 needs a non-empty reason."),
    ([*EXCLUSIONS, {"reason": "x", "operations": []}], "Group 2 needs at least 1 operation."),
    ([{"reason": "x", "operations": "GET /ask"}], "Group 1 needs at least 1 operation."),
    (
        [{"reason": "x", "operations": ["get /ask"]}],
        'Group 1 lists "get /ask". Write an upper case method, a space and a path, such as GET /api/v1/x/trends.',
    ),
    (
        [{"reason": "x", "operations": [["GET", "/ask"]]}],
        'Group 1 lists ["GET", "/ask"]. Write an upper case method, a space and a path, such as GET /api/v1/x/trends.',
    ),
    (
        [
            {"reason": "x", "operations": ["GET /ask", "GET /api/v1/x/{id}"]},
            {"reason": "y", "operations": ["GET /api/v1/x/{name}"]},
        ],
        "GET /api/v1/x/{name} appears more than once.",
    ),
]


def write_root(tmp_path: Path, resources: dict[str, str], exclusions: object) -> Path:
    for name, source in resources.items():
        path = tmp_path / "src/x_twitter_scraper/resources" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(source)
    (tmp_path / "excluded-operations.json").write_text(json.dumps(exclusions))
    return tmp_path


def run(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    spec: object,
    *,
    resources: dict[str, str] = RESOURCES,
    exclusions: object = EXCLUSIONS,
) -> tuple[int, list[str], list[str]]:
    spec_path = tmp_path / "openapi.json"
    spec_path.write_text(json.dumps(spec))
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    status = main(write_root(tmp_path / "repo", resources, exclusions))
    output = capsys.readouterr()
    return status, output.out.splitlines(), output.err.splitlines()


def with_paths(**paths: object) -> dict[str, object]:
    return {**PUBLIC_SPEC, "paths": {**PUBLIC_PATHS, **paths}}


def test_covered_spec_passes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    assert run(tmp_path, monkeypatch, capsys, PUBLIC_SPEC) == (0, [COVERED], [])


@pytest.mark.parametrize(
    "spec",
    [
        pytest.param(
            {
                "servers": [{"url": "https://xquik.com/api/v1/"}],
                "paths": {
                    "/trends": {"get": {"operationId": "listTrends"}},
                    "/x/tweets/{tweetId}": {"get": {"operationId": "getTweet"}},
                    "/ask": {"get": {"operationId": "askDocs", "servers": [{"url": "https://xquik.com/"}]}},
                },
            },
            id="operation-servers",
        ),
        pytest.param(
            {
                "servers": [{"url": "/api/v1"}],
                "paths": {
                    "/trends": {"get": {"operationId": "listTrends"}},
                    "/x/tweets/{tweetId}": {"get": {"operationId": "getTweet"}},
                    "/ask": {"servers": [{"url": "https://xquik.com"}], "get": {"operationId": "askDocs"}},
                },
            },
            id="path-item-servers",
        ),
        pytest.param(
            {
                "servers": [{"url": "https://xquik.com/elsewhere"}],
                "paths": {
                    "/trends": {
                        "servers": [{"url": "https://xquik.com/also-elsewhere"}],
                        "get": {"operationId": "listTrends", "servers": [{"url": "https://xquik.com/api/v1"}]},
                    },
                    "/x/tweets/{tweetId}": {
                        "servers": [{"url": "https://xquik.com/api/v1"}],
                        "get": {"operationId": "getTweet", "servers": []},
                    },
                    "/ask": {"get": {"operationId": "askDocs", "servers": [{"url": "https://xquik.com"}]}},
                },
            },
            id="nearest-servers-win",
        ),
    ],
)
def test_operation_servers_win_over_path_and_root_servers(
    spec: object, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    assert run(tmp_path, monkeypatch, capsys, spec) == (0, [COVERED], [])


def test_spec_without_servers_uses_the_path_keys(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec = {key: value for key, value in PUBLIC_SPEC.items() if key != "servers"}
    assert run(tmp_path, monkeypatch, capsys, spec) == (0, [COVERED], [])


def test_missing_operation_fails_with_its_line(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec = with_paths(
        **{
            "/api/v1/x/trends/history": {"get": {"operationId": "getXTrendsHistory"}},
            "/api/v1/x/tweets/{tweetId}": {"get": {"operationId": "getTweet"}, "post": {"summary": "Edit a tweet"}},
        }
    )
    assert run(tmp_path, monkeypatch, capsys, spec) == (
        1,
        [],
        [
            "GET /api/v1/x/trends/history (getXTrendsHistory) is in the API but not in the SDK.",
            "POST /api/v1/x/tweets/{tweetId} is in the API but not in the SDK.",
            ADD_NEXT,
        ],
    )


def test_exclusion_the_api_no_longer_has_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    exclusions = [*EXCLUSIONS, {"reason": "Retired.", "operations": ["GET /api/v1/old"]}]
    assert run(tmp_path, monkeypatch, capsys, PUBLIC_SPEC, exclusions=exclusions) == (
        1,
        [],
        ["excluded-operations.json lists GET /api/v1/old, which the API no longer has. Remove it.", REMOVE_NEXT],
    )


def test_exclusion_the_sdk_implements_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    exclusions = [*EXCLUSIONS, {"reason": "Not ported yet.", "operations": ["GET /api/v1/x/tweets/{id}"]}]
    assert run(tmp_path, monkeypatch, capsys, PUBLIC_SPEC, exclusions=exclusions) == (
        1,
        [],
        [
            "excluded-operations.json lists GET /api/v1/x/tweets/{id}, which the SDK already implements. Remove it.",
            REMOVE_NEXT,
        ],
    )


def test_every_failure_shows_before_the_next_step(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec = with_paths(**{"/api/v1/x/trends/history": {"get": {"operationId": "getXTrendsHistory"}}})
    exclusions = [*EXCLUSIONS, {"reason": "Old.", "operations": ["DELETE /api/v1/old", "GET /api/v1/trends"]}]
    assert run(tmp_path, monkeypatch, capsys, spec, exclusions=exclusions) == (
        1,
        [],
        [
            "GET /api/v1/x/trends/history (getXTrendsHistory) is in the API but not in the SDK.",
            "excluded-operations.json lists DELETE /api/v1/old, which the API no longer has. Remove it.",
            "excluded-operations.json lists GET /api/v1/trends, which the SDK already implements. Remove it.",
            ADD_NEXT,
        ],
    )


@pytest.mark.parametrize(("exclusions", "problem"), INVALID_EXCLUSIONS)
def test_invalid_exclusion_file_fails(
    exclusions: object,
    problem: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert run(tmp_path, monkeypatch, capsys, PUBLIC_SPEC, exclusions=exclusions) == (
        1,
        [],
        [f"excluded-operations.json is not valid. {problem}", FIX_NEXT],
    )


@pytest.mark.parametrize(
    ("content", "problem"),
    [
        (None, "The file cannot be read."),
        (b'[{"reason": "x",\n  "operations": [GET]}]', "Line 2 column 18 breaks the JSON syntax."),
        (b"\xff\xfe\x00", "Its bytes are not valid text."),
    ],
)
def test_unreadable_exclusion_file_fails(
    content: bytes | None,
    problem: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    spec_path = tmp_path / "openapi.json"
    spec_path.write_text(json.dumps(PUBLIC_SPEC))
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    root = write_root(tmp_path / "repo", RESOURCES, EXCLUSIONS)
    exclusions = root / "excluded-operations.json"
    if content is None:
        exclusions.unlink()
    else:
        exclusions.write_bytes(content)
    assert main(root) == 1
    output = capsys.readouterr()
    assert (output.out, output.err.splitlines()) == (
        "",
        [f"excluded-operations.json is not valid. {problem}", FIX_NEXT],
    )


@pytest.mark.parametrize(
    "content",
    [None, "openapi: 3.1.0\npaths: {}\n", b"\xff\xfe\x00"],
    ids=["missing", "yaml", "not-text"],
)
def test_unreadable_spec_file_fails(
    content: str | bytes | None, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec_path = tmp_path / "openapi.json"
    if isinstance(content, bytes):
        spec_path.write_bytes(content)
    elif content is not None:
        spec_path.write_text(content)
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    assert main(write_root(tmp_path / "repo", RESOURCES, EXCLUSIONS)) == 1
    output = capsys.readouterr()
    assert (output.out, output.err.splitlines()) == ("", [f"Could not read the API spec from {spec_path}. {SPEC_HELP}"])


@pytest.mark.parametrize(
    "content",
    [
        "[]",
        '{"openapi": "3.1.0"}',
        '{"paths": []}',
        '{"paths": {"/x": null}}',
        '{"paths": {"/x": {"$ref": "#/components/pathItems/x"}}}',
        '{"paths": {"/x": {"get": "x"}}}',
        '{"servers": {"url": "https://xquik.com"}, "paths": {"/x": {"get": {}}}}',
        '{"servers": [{"description": "Production"}], "paths": {"/x": {"get": {}}}}',
    ],
    ids=[
        "list",
        "no-paths",
        "paths-list",
        "null-path-item",
        "path-item-reference",
        "operation-string",
        "servers-object",
        "server-without-url",
    ],
)
def test_spec_with_an_unreadable_part_fails(
    content: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec_path = tmp_path / "openapi.json"
    spec_path.write_text(content)
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    assert main(write_root(tmp_path / "repo", RESOURCES, EXCLUSIONS)) == 1
    output = capsys.readouterr()
    assert (output.out, output.err.splitlines()) == (
        "",
        [
            f"The API spec from {spec_path} has a part the check cannot read. "
            "Fix the spec, or set XQUIK_OPENAPI_SPEC to a valid copy of https://xquik.com/openapi.json."
        ],
    )


class SpecHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/truncated.json":
            self.send_response(200)
            self.send_header("Content-Length", str(len(SPEC_BODY)))
            self.end_headers()
            self.wfile.write(SPEC_BODY[:10])
            return
        if self.path != "/openapi.json":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(SPEC_BODY)))
        self.end_headers()
        self.wfile.write(SPEC_BODY)

    @override
    def log_message(self, format: str, *args: object) -> None:
        del format, args


@pytest.fixture
def spec_url() -> Iterator[str]:
    server = HTTPServer(("127.0.0.1", 0), SpecHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def test_spec_url_is_read(
    spec_url: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", f"{spec_url}/openapi.json")
    assert main(write_root(tmp_path, RESOURCES, EXCLUSIONS)) == 0
    assert capsys.readouterr().out.splitlines() == [COVERED]


@pytest.mark.parametrize("name", ["missing.json", "truncated.json"])
def test_unreachable_spec_url_fails(
    name: str, spec_url: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", f"{spec_url}/{name}")
    assert main(write_root(tmp_path, RESOURCES, EXCLUSIONS)) == 1
    output = capsys.readouterr()
    assert (output.out, output.err.splitlines()) == (
        "",
        [f"Could not read the API spec from {spec_url}/{name}. {SPEC_HELP}"],
    )


REQUEST_PROBLEM = "has a request whose path or cast_to cannot be read"


@pytest.mark.parametrize(
    ("source", "line", "problem"),
    [
        (
            b"\nclass Broken:\n    def list(self):\n        return self._get(TRENDS_PATH, cast_to=object)\n",
            4,
            REQUEST_PROBLEM,
        ),
        (
            b'\nclass Broken:\n    def list(self):\n        return self._post(f"/trends/{1}", cast_to=object)\n',
            4,
            REQUEST_PROBLEM,
        ),
        (b'\nclass Broken:\n\n    def list(self):\n        return self._get("/trends")\n', 5, REQUEST_PROBLEM),
        (b"\nclass Broken:\n    def list(self):\n        return self._put(cast_to=object)\n", 4, REQUEST_PROBLEM),
        (
            b"\nclass Broken:\n    def list(self):\n        return client._delete(PATH, cast_to=object)\n",
            4,
            REQUEST_PROBLEM,
        ),
        (b"\n\nclass Broken(:\n", 3, "is not valid Python"),
        (b"\xff\xfe", 1, "is not valid Python"),
    ],
    ids=["variable-path", "f-string-path", "no-cast-to", "no-path", "other-receiver", "syntax", "not-utf-8"],
)
def test_unreadable_request_names_its_file_and_line(
    source: bytes,
    line: int,
    problem: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = write_root(tmp_path / "repo", RESOURCES, EXCLUSIONS)
    (root / "src/x_twitter_scraper/resources/x/broken.py").write_bytes(source)
    spec_path = tmp_path / "openapi.json"
    spec_path.write_text(json.dumps(PUBLIC_SPEC))
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    assert main(root) == 1
    output = capsys.readouterr()
    assert (output.out, output.err.splitlines()) == (
        "",
        [f"src/x_twitter_scraper/resources/x/broken.py:{line} {problem}.", READ_NEXT],
    )


def test_repository_sdk_and_exclusions_are_readable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    spec = {
        "servers": [{"url": "https://xquik.com"}],
        "paths": {
            "/ask": {"get": {"operationId": "askXquik"}, "post": {"operationId": "askXquikPost"}},
            "/api/v1/api-keys": {"get": {"operationId": "listApiKeys"}, "post": {"operationId": "createApiKey"}},
            "/api/v1/api-keys/bulk-revoke": {"post": {"operationId": "bulkRevokeApiKeys"}},
            "/api/v1/api-keys/{keyId}": {
                "delete": {"operationId": "revokeApiKey"},
                "patch": {"operationId": "updateApiKey"},
            },
            "/api/v1/credits/quick-topup": {"post": {"operationId": "quickTopupCredits"}},
            "/api/v1/x/trends": {"get": {"operationId": "getXTrends"}},
            "/api/v1/x/tweets/{tweetId}": {"get": {"operationId": "getXTweet"}},
            "/api/v1/credits/topup/redirect": {"get": {"operationId": "redirectTopupCheckout"}},
        },
    }
    spec_path = tmp_path / "openapi.json"
    spec_path.write_text(json.dumps(spec))
    monkeypatch.setenv("XQUIK_OPENAPI_SPEC", str(spec_path))
    assert main(ROOT) == 0
    assert capsys.readouterr().out.splitlines() == [
        "The SDK covers 3 of 11 API operations, and excluded-operations.json lists the other 8."
    ]
