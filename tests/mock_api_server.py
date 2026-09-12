# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from http import HTTPStatus
from typing import Mapping, ClassVar, cast
from threading import Thread
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlsplit
from typing_extensions import override

from tests.mock_api_routes import ROUTES, Route, ResponseKind, ResponseType
from tests.mock_api_schema import model_payloads

RESPONSES: dict[ResponseType, tuple[HTTPStatus, bytes, str]] = {
    response_type: (HTTPStatus.OK, payload, "application/json")
    for response_type, payload in model_payloads(
        {route.response_type for route in ROUTES if isinstance(route.response_type, type)}
    ).items()
}
RESPONSES.update(
    {
        ResponseKind.EMPTY: (HTTPStatus.NO_CONTENT, b"", "application/json"),
        ResponseKind.BINARY: (HTTPStatus.OK, b'{"foo":"bar"}', "application/octet-stream"),
        ResponseKind.JSON_OBJECT: (HTTPStatus.OK, b"{}", "application/json"),
    }
)


class MockAPIRequestHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    routes: ClassVar[tuple[Route, ...]] = ROUTES
    route_responses: ClassVar[Mapping[ResponseType, tuple[HTTPStatus, bytes, str]]] = RESPONSES

    def do_GET(self) -> None:
        content_length = self.headers.get("Content-Length")
        if content_length is not None:
            self.rfile.read(int(content_length))

        path = urlsplit(self.path).path
        route = next(
            (
                candidate
                for candidate in self.routes
                if candidate.method == self.command and candidate.pattern.fullmatch(path)
            ),
            None,
        )
        if route is None:
            self._write_response(
                HTTPStatus.NOT_FOUND,
                b'{"error":"unregistered mock route"}',
                "application/json",
            )
            return
        self._write_response(*self.route_responses[route.response_type])

    do_POST = do_GET
    do_PUT = do_GET
    do_PATCH = do_GET
    do_DELETE = do_GET

    def _write_response(self, status: HTTPStatus, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    @override
    def log_message(self, format: str, *args: object) -> None:
        del format, args


class MockAPIServer:
    def __init__(self) -> None:
        self._server = ThreadingHTTPServer(("127.0.0.1", 0), MockAPIRequestHandler)
        self._server.daemon_threads = True
        host, port = cast(tuple[str, int], self._server.server_address)
        self.base_url = f"http://{host}:{port}"
        self._thread = Thread(target=self._server.serve_forever, name="mock-api-server", daemon=True)
        self._closed = False
        self._thread.start()

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._server.shutdown()
        self._server.server_close()
        self._thread.join(timeout=5)
        if self._thread.is_alive():
            raise RuntimeError("Mock API server did not stop")
