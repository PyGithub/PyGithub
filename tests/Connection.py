############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Liuyang Wan <tsfdye@gmail.com>                                #
# Copyright 2020 Michał Górny <mgorny@gentoo.org>                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Maja Massarini <2678400+majamassarini@users.noreply.github.com>#
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


import itertools

import pytest
from vcr.request import Request

from . import Framework, VcrSerializer

PARAMETERS = itertools.product(
    ["http", "https"],
    [
        '{"body":"BODY TEXT"}',
        '{"body":"BODY\xa0TEXT"}',
        "BODY TEXT",
        "BODY\xa0TEXT",
    ],
)


def _cassette_dict(protocol, response_body):
    uri = f"{protocol}://api.github.com/user"
    return {
        "version": VcrSerializer.CASSETTE_FORMAT_VERSION,
        "interactions": [
            {
                "request": {
                    "method": "GET",
                    "uri": uri,
                    "body": None,
                    "headers": {
                        "Authorization": ["Basic p4ssw0rd"],
                        "User-Agent": ["PyGithub/Python"],
                    },
                },
                "response": {
                    "status": {"code": 200, "message": ""},
                    "headers": {},
                    "body": {"string": response_body.encode("utf-8")},
                },
            },
        ],
    }


@pytest.mark.parametrize(("protocol", "response_body"), list(PARAMETERS))
def testRecordAndReplay(protocol, response_body):
    cassette_dict = _cassette_dict(protocol, response_body)

    # serializing scrubs the Authorization header and writes the expected on-disk record shape
    text = VcrSerializer.serialize(cassette_dict)
    expected = (
        f"{protocol}\n"
        "GET\n"
        "api.github.com\n"
        "None\n"
        "/user\n"
        "{'Authorization': 'Basic login_and_password_removed', 'User-Agent': 'PyGithub/Python'}\n"
        "None\n"
        "200\n"
        "[]\n"
        f"{response_body}\n"
        "\n"
    )
    assert text == expected

    # deserializing that same text reconstructs the original response body byte for byte
    data = VcrSerializer.deserialize(text)
    assert len(data["interactions"]) == 1
    interaction = data["interactions"][0]
    assert interaction["request"]["method"] == "GET"
    assert interaction["request"]["uri"] == f"{protocol}://api.github.com/user"
    assert interaction["request"]["headers"]["Authorization"] == ["Basic login_and_password_removed"]
    assert interaction["response"]["status"]["code"] == 200
    assert interaction["response"]["body"]["string"] == response_body.encode("utf-8")


@pytest.mark.parametrize(
    ("recorded", "sent", "matches"),
    [
        ('{"message": "expected"}', b'{"message": "changed"}', False),
        ('{"message": "expected"}', b"{}", False),
        ('{"message": "expected"}', None, False),
        (None, b'{"message": "unexpected"}', False),
        ('{"a": 1, "b": [2, 3]}', b'{"b":[2,3],"a":1}', True),
        ('{"values": [1, 2]}', b'{"values": [2, 1]}', False),
        ('{"name": "café"}', b'{"name": "caf\\u00e9"}', True),
        ("first body", b"second body", False),
        ("same body", b"same body", True),
        ("first\r\nsecond", b"first\r\nsecond", True),
        (b"\xff\x00", b"\xff\x00", True),
        (b"\xff\x00", b"\xff\x01", False),
        ("<html>first</html>", b"<html>second</html>", False),
        (None, None, True),
        (None, b"", True),
        (None, b"null", False),
    ],
)
def testReplayChecksRequestBody(tmp_path, recorded, sent, matches):
    cassette_dict = _cassette_dict("https", "response body")
    request = cassette_dict["interactions"][0]["request"]
    request.update(method="POST", body=recorded)
    path = tmp_path / "body.txt"
    path.write_text(VcrSerializer.serialize(cassette_dict), encoding="utf-8")

    # Exercise the shared replay configuration, including its serializer.
    with Framework._vcr.use_cassette(str(path)) as cassette:
        actual = Request("POST", request["uri"], sent, {})
        assert cassette.can_play_response_for(actual) is matches
        if matches:
            assert cassette.play_response(actual)["body"]["string"] == b"response body"
        else:
            assert cassette.play_counts[0] == 0


@pytest.mark.parametrize("method", ["GET", "HEAD", "POST"])
def testReplayLegacyNullBody(tmp_path, method):
    cassette_dict = _cassette_dict("https", "response body")
    request = cassette_dict["interactions"][0]["request"]
    request.update(method=method, body="null")
    path = tmp_path / "legacy-null.txt"
    path.write_text(VcrSerializer.serialize(cassette_dict), encoding="utf-8")

    with Framework._vcr.use_cassette(str(path)) as cassette:
        actual = Request(method, request["uri"], None, {})
        assert cassette.can_play_response_for(actual) is (method != "POST")
