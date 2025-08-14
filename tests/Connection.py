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
from io import StringIO
from unittest.mock import Mock

import pytest
import responses

from . import Framework

PARAMETERS = itertools.product(
    [
        (Framework.ReplayingHttpConnection, "http"),
        (Framework.ReplayingHttpsConnection, "https"),
    ],
    [
        (
            '{"body":"BODY TEXT"}',
            "\nGET\napi.github.com\nNone\n/user\n{'Authorization': 'Basic login_and_password_removed', 'User-Agent': 'PyGithub/Python'}\nNone\n200\n[]\n{\"body\":\"BODY TEXT\"}\n\n",
        ),
        (
            '{"body":"BODY\xa0TEXT"}',
            "\nGET\napi.github.com\nNone\n/user\n{'Authorization': 'Basic login_and_password_removed', 'User-Agent': 'PyGithub/Python'}\nNone\n200\n[]\n{\"body\":\"BODY\xa0TEXT\"}\n\n",
        ),
        (
            "BODY TEXT",
            "\nGET\napi.github.com\nNone\n/user\n{'Authorization': 'Basic login_and_password_removed', 'User-Agent': 'PyGithub/Python'}\nNone\n200\n[]\nBODY TEXT\n\n",
        ),
        (
            "BODY\xa0TEXT",
            "\nGET\napi.github.com\nNone\n/user\n{'Authorization': 'Basic login_and_password_removed', 'User-Agent': 'PyGithub/Python'}\nNone\n200\n[]\nBODY\xa0TEXT\n\n",
        ),
    ],
)


class RecordingMockConnection(Framework.RecordingConnection):
    def __init__(self, protocol, host, port, realConnection):
        self._realConnection = realConnection
        super().__init__(protocol, host, port)


@pytest.mark.parametrize(
    ("replaying_connection_class", "protocol", "response_body", "expected_recording"),
    list(tuple(itertools.chain(*p)) for p in PARAMETERS),
)
@responses.activate
def testRecordAndReplay(replaying_connection_class, protocol, response_body, expected_recording):
    file = StringIO()
    host = "api.github.com"
    verb = "GET"
    url = "/user"
    headers = {"Authorization": "Basic p4ssw0rd", "User-Agent": "PyGithub/Python"}

    response = Mock()
    response.status = 200
    response.getheaders.return_value = {}
    response.read.return_value = response_body

    connection = Mock()
    connection.getresponse.return_value = response

    # write mock response to buffer
    RecordingMockConnection.setOpenFile(lambda slf, mode: file)
    recording_connection = RecordingMockConnection(protocol, host, None, lambda *args, **kwds: connection)
    recording_connection.request(verb, url, None, headers)
    recording_connection.getresponse()
    recording_connection.close()

    # validate contents of buffer
    file_value_lines = file.getvalue().split("\n")
    expected_recording_lines = (protocol + expected_recording).split("\n")
    assert file_value_lines[:5] == expected_recording_lines[:5]
    assert eval(file_value_lines[5]) == eval(expected_recording_lines[5])
    # dict literal, so keys not in guaranteed order
    assert file_value_lines[6:] == expected_recording_lines[6:]

    # rewind buffer and attempt to replay response from it
    file.seek(0)
    replaying_connection_class.setOpenFile(lambda slf, mode: file)
    replaying_connection = replaying_connection_class(host=host, port=None)
    replaying_connection.request(verb, url, None, headers)
    replaying_connection.getresponse()
