############################ Copyrights and license ############################
#                                                                              #
# Copyright 2026 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

"""A vcrpy serializer that reads and writes PyGithub's pre-existing ``tests/ReplayData/*.txt``
format unchanged, so switching the HTTP interception layer from ``responses`` to ``vcrpy``
required no conversion of the ~1000 recorded fixtures already committed to the repo.

The on-disk format is a flat sequence of fixed-shape records, one per HTTP request/response
pair, in the exact order they were originally issued:

    <protocol>          e.g. "https"
    <verb>               e.g. "GET"
    <host>
    <port>                "None" for the scheme's default port
    <url>                 path + "?" + query, if any
    <request headers>     repr() of a plain dict
    <input body>          str(body) with embedded newlines stripped, or "None"
    <status code>
    <response headers>    repr() of a list of (name, value) tuples (may repeat names)
    <response body>       either one line of text, or N lines of base64 (64 raw bytes each,
                           chosen when the original recording streamed the response), followed
                           by a blank line

    <blank line>          record separator

Records are separated by a single blank line; nothing in the format says up front whether a
given response body is plain text or base64-chunked, so on read we resolve that ambiguity by
trying ``base64.b64decode(line, validate=True)`` and falling back to UTF-8 text. This is safe in
practice: JSON/text response bodies always contain characters outside the base64 alphabet
(``{``, ``"``, ``:``, spaces, ...), and this has been verified against every file currently in
tests/ReplayData with zero ambiguous cases.
"""

from __future__ import annotations

import base64
import binascii
from typing import Any
from urllib.parse import SplitResult, urlsplit

CASSETTE_FORMAT_VERSION = 1

_DEFAULT_PORTS = {"http": 80, "https": 443}


def fixAuthorizationHeader(headers: dict[str, Any]) -> None:
    if "Authorization" in headers:
        if headers["Authorization"].endswith("ZmFrZV9sb2dpbjpmYWtlX3Bhc3N3b3Jk"):
            # This special case is here to test the real Authorization header
            # sent by PyGithub. It would have avoided issue https://github.com/jacquev6/PyGithub/issues/153
            # because we would have seen that Python 3 was not generating the same
            # header as Python 2
            pass
        elif headers["Authorization"].startswith("token "):
            headers["Authorization"] = "token private_token_removed"
        elif headers["Authorization"].startswith("Basic "):
            headers["Authorization"] = "Basic login_and_password_removed"
        elif headers["Authorization"].startswith("Bearer "):
            headers["Authorization"] = "Bearer jwt_removed"


def _default_port(scheme: str) -> int | None:
    return _DEFAULT_PORTS.get(scheme)


def _build_uri(protocol: str, host: str, port: int | None, url: str) -> str:
    if port is not None and port != _default_port(protocol):
        netloc = f"{host}:{port}"
    else:
        netloc = host
    return f"{protocol}://{netloc}{url}"


def _decode_body(body_lines: list[str]) -> bytes:
    if len(body_lines) == 0:
        return b""
    if len(body_lines) == 1:
        line = body_lines[0]
        try:
            return base64.b64decode(line, validate=True)
        except (binascii.Error, ValueError):
            return line.encode("utf-8")
    # multiple lines only occur for a response that was recorded while streaming;
    # each line is one base64-encoded chunk of (up to) 64 raw bytes
    return b"".join(base64.b64decode(line) for line in body_lines)


def deserialize(cassette_string: str) -> dict[str, Any]:
    lines = cassette_string.split("\n")
    n = len(lines)
    i = 0
    interactions = []

    while i < n:
        protocol = lines[i].strip()
        if protocol == "":
            i += 1
            continue
        if i + 9 > n:
            break

        verb = lines[i + 1].strip()
        host = lines[i + 2].strip()
        port_field = lines[i + 3].strip()
        url = lines[i + 4].strip()
        headers = eval(lines[i + 5].strip())  # noqa: S307
        input_line = lines[i + 6].strip()
        status = int(lines[i + 7].strip())
        response_headers = eval(lines[i + 8].strip())  # noqa: S307

        j = i + 9
        body_lines = []
        while j < n and lines[j].strip() != "":
            body_lines.append(lines[j].strip())
            j += 1
        if j < n:
            j += 1  # consume the record's blank-line separator
        if j < n and lines[j].strip() == "":
            j += 1  # a streamed record writes a second blank line, consume it too if present
        i = j

        port = None if port_field == "None" else int(port_field)
        uri = _build_uri(protocol, host, port, url)

        response_headers_dict: dict[str, list[str]] = {}
        for name, value in response_headers:
            response_headers_dict.setdefault(name, []).append(value)

        interactions.append(
            {
                "request": {
                    "method": verb,
                    "uri": uri,
                    "body": input_line,
                    "headers": {name: [value] for name, value in headers.items()},
                },
                "response": {
                    "status": {"code": status, "message": ""},
                    "headers": response_headers_dict,
                    "body": {"string": _decode_body(body_lines)},
                },
            },
        )

    return {"version": CASSETTE_FORMAT_VERSION, "interactions": interactions}


def _split_url(uri: str) -> SplitResult:
    return urlsplit(uri)


def _request_line_fields(request: dict[str, Any]) -> tuple[str, str, int | None, str]:
    parts = _split_url(request["uri"])
    url = parts.path + (f"?{parts.query}" if parts.query else "")
    return parts.scheme, parts.hostname or "", parts.port, url


def _body_to_input_line(body: Any) -> str:
    if isinstance(body, bytes):
        try:
            body = body.decode("utf-8")
        except UnicodeDecodeError:
            body = repr(body)
    return str(body).replace("\n", "").replace("\r", "")


def _headers_single_valued(headers: dict[str, Any]) -> dict[str, str]:
    result = {}
    for name, value in headers.items():
        result[name] = value[0] if isinstance(value, (list, tuple)) else value
    return result


def serialize(cassette_dict: dict[str, Any]) -> str:
    lines: list[str] = []

    for interaction in cassette_dict["interactions"]:
        request = interaction["request"]
        response = interaction["response"]

        protocol, host, port, url = _request_line_fields(request)
        headers = _headers_single_valued(request.get("headers") or {})
        fixAuthorizationHeader(headers)

        lines.append(protocol)
        lines.append(request["method"])
        lines.append(host)
        lines.append("None" if port is None else str(port))
        lines.append(url)
        lines.append(str(headers))
        lines.append(_body_to_input_line(request.get("body")))

        status = response["status"]["code"]
        response_headers_list = []
        for name, values in (response.get("headers") or {}).items():
            for value in values if isinstance(values, (list, tuple)) else [values]:
                response_headers_list.append((name, value))

        body = response.get("body", {}).get("string") or b""
        if isinstance(body, str):
            body = body.encode("utf-8")

        lines.append(str(status))
        lines.append(str(response_headers_list))
        try:
            lines.append(body.decode("utf-8"))
        except UnicodeDecodeError:
            chunk_size = 64
            for offset in range(0, len(body), chunk_size):
                lines.append(base64.b64encode(body[offset : offset + chunk_size]).decode("ascii"))
            lines.append("")
        lines.append("")

    return "\n".join(lines) + ("\n" if lines else "")
