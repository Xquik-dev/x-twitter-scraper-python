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

from tests.mock_api_routes import ROUTES, Route, ResponseKind
from tests.mock_api_schema import model_payload
from x_twitter_scraper._models import BaseModel

MODEL_PAYLOADS = {
    response_type: model_payload(response_type)
    for response_type in {route.response_type for route in ROUTES}
    if isinstance(response_type, type)
}


class MockAPIRequestHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    routes: ClassVar[tuple[Route, ...]] = ROUTES
    model_payloads: ClassVar[Mapping[type[BaseModel], bytes]] = MODEL_PAYLOADS

    def do_GET(self) -> None:
        self._handle()

    def do_POST(self) -> None:
        self._handle()

    def do_PUT(self) -> None:
        self._handle()

    def do_PATCH(self) -> None:
        self._handle()

    def do_DELETE(self) -> None:
        self._handle()

    def _handle(self) -> None:
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
        if route.response_type is ResponseKind.EMPTY:
            self._write_response(HTTPStatus.NO_CONTENT, b"", "application/json")
            return
        if route.response_type is ResponseKind.BINARY:
            self._write_response(HTTPStatus.OK, b"fixture", "application/octet-stream")
            return
        self._write_response(
            HTTPStatus.OK,
            self.model_payloads[route.response_type],
            "application/json",
        )

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
