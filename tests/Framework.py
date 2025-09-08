############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Uriel Corfa <uriel@corfa.fr>                                  #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Arda Kuyumcu <kuyumcuarda@gmail.com>                          #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Laurent Mazuel <lmazuel@microsoft.com>                        #
# Copyright 2018 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Filipe Laíns <filipe.lains@gmail.com>                         #
# Copyright 2019 Isac Souza <isouza@daitan.com>                                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2020 Michał Górny <mgorny@gentoo.org>                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Amador Pahim <apahim@redhat.com>                              #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Denis Blanchette <dblanchette@coveo.com>                      #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 chantra <chantra@users.noreply.github.com>                    #
# Copyright 2025 Alex Olieman <alex@olieman.net>                               #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Maja Massarini <2678400+majamassarini@users.noreply.github.com>#
# Copyright 2025 Matej Focko <mfocko@users.noreply.github.com>                 #
# Copyright 2025 Neel Malik <41765022+neel-m@users.noreply.github.com>         #
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

from __future__ import annotations

import base64
import contextlib
import io
import json
import os
import traceback
import unittest
import warnings
from io import BytesIO

import responses
from requests.structures import CaseInsensitiveDict
from urllib3.util import Url

import github
from github import Consts

APP_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC+5ePolLv6VcWLp2f17g6r6vHl+eoLuodOOfUl8JK+MVmvXbPa
xDy0SS0pQhwTOMtB0VdSt++elklDCadeokhEoGDQp411o+kiOhzLxfakp/kewf4U
HJnu4M/A2nHmxXVe2lzYnZvZHX5BM4SJo5PGdr0Ue2JtSXoAtYr6qE9maQIDAQAB
AoGAFhOJ7sy8jG+837Clcihso+8QuHLVYTPaD+7d7dxLbBlS8NfaQ9Nr3cGUqm/N
xV9NCjiGa7d/y4w/vrPwGh6UUsA+CvndwDgBd0S3WgIdWvAvHM8wKgNh/GBLLzhT
Bg9BouRUzcT1MjAnkGkWqqCAgN7WrCSUMLt57TNleNWfX90CQQDjvVKTT3pOiavD
3YcLxwkyeGd0VMvKiS4nV0XXJ97cGXs2GpOGXldstDTnF5AnB6PbukdFLHpsx4sW
Hft3LRWnAkEA1pY15ke08wX6DZVXy7zuQ2izTrWSGySn7B41pn55dlKpttjHeutA
3BEQKTFvMhBCphr8qST7Wf1SR9FgO0tFbwJAEhHji2yy96hUyKW7IWQZhrem/cP8
p4Va9CQolnnDZRNgg1p4eiDiLu3dhLiJ547joXuWTBbLX/Y1Qvv+B+a74QJBAMCW
O3WbMZlS6eK6//rIa4ZwN00SxDg8I8FUM45jwBsjgVGrKQz2ilV3sutlhIiH82kk
m1Iq8LMJGYl/LkDJA10CQBV1C+Xu3ukknr7C4A/4lDCa6Xb27cr1HanY7i89A+Ab
eatdM6f/XVqWp8uPT9RggUV9TjppJobYGT2WrWJMkYw=
-----END RSA PRIVATE KEY-----
"""


def readLine(file_):
    line = file_.readline()
    if isinstance(line, bytes):
        line = line.decode("utf-8")
    return line.strip()


class FakeHttpResponse:
    def __init__(self, status, headers, output):
        self.status = status
        self.__headers = headers
        self.__output = output

    def getheaders(self):
        return self.__headers

    def read(self):
        return self.__output

    def iter_content(self, chunk_size=1):
        return iter([self.__output[i : i + chunk_size] for i in range(0, len(self.__output), chunk_size)])

    def raise_for_status(self):
        pass


def fixAuthorizationHeader(headers):
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


class RecordingConnection:
    __openFile = None

    @staticmethod
    def setOpenFile(func):
        RecordingConnection.__openFile = func

    def __init__(self, protocol, host, port, *args, **kwds):
        self.__file = self.__openFile("w")
        # write operations make the assumption that the file is not in binary mode
        assert isinstance(self.__file, io.TextIOBase)
        self.__protocol = protocol
        self.__host = host
        self.__port = port
        self.__cnx = self._realConnection(host, port, *args, **kwds)
        self.__stream = False

    @property
    def host(self):
        return self.__host

    def request(self, verb, url, input, headers, stream=False):
        self.__cnx.request(verb, url, input, headers)
        self.__stream = stream
        # fixAuthorizationHeader changes the parameter directly to remove Authorization token.
        # however, this is the real dictionary that *will be sent* by "requests",
        # since we are writing here *before* doing the actual request.
        # So we must avoid changing the real "headers" or this create this:
        # https://github.com/PyGithub/PyGithub/pull/664#issuecomment-389964369
        # https://github.com/PyGithub/PyGithub/issues/822
        # Since it's dict[str, str], a simple copy is enough.
        anonymous_headers = headers.copy()
        fixAuthorizationHeader(anonymous_headers)
        self.__writeLine(self.__protocol)
        self.__writeLine(verb)
        self.__writeLine(self.__host)
        self.__writeLine(self.__port)
        self.__writeLine(url)
        self.__writeLine(anonymous_headers)
        self.__writeLine(str(input).replace("\n", "").replace("\r", ""))

    def getresponse(self):
        res = self.__cnx.getresponse()

        status = res.status
        headers = res.getheaders()
        output = res if self.__stream else res.read()

        self.__writeLine(status)
        self.__writeLine(list(headers))
        if self.__stream:
            chunks = [chunk for chunk in output.iter_content(chunk_size=64)]
            output = b"".join(chunks)
            for chunk in chunks:
                self.__writeLine(base64.b64encode(chunk).decode("ascii"))
            self.__writeLine("")
        else:
            self.__writeLine(output)
        self.__writeLine("")

        return FakeHttpResponse(status, headers, output)

    def close(self):
        return self.__cnx.close()

    def __writeLine(self, line):
        self.__file.write(str(line) + "\n")


class RecordingHttpConnection(RecordingConnection):
    _realConnection = github.Requester.HTTPRequestsConnectionClass

    def __init__(self, *args, **kwds):
        super().__init__("http", *args, **kwds)


class RecordingHttpsConnection(RecordingConnection):
    _realConnection = github.Requester.HTTPSRequestsConnectionClass

    def __init__(self, *args, **kwds):
        super().__init__("https", *args, **kwds)


class ReplayingConnection:
    __openFile = None

    @staticmethod
    def setOpenFile(func):
        ReplayingConnection.__openFile = func

    def __init__(self, protocol, host, port, *args, **kwds):
        self.__file = self.__openFile("r")
        self.__protocol = protocol
        self.__host = host
        self.__port = port
        self.__stream = False
        self.response_headers = CaseInsensitiveDict()

        self.__cnx = self._realConnection(host, port, *args, **kwds)

    @property
    def host(self):
        return self.__host

    def request(
        self,
        verb,
        url,
        input,
        headers,
        stream: bool = False,
    ):
        port = self.__port if self.__port else 443 if self.__protocol == "https" else 80
        full_url = Url(scheme=self.__protocol, host=self.__host, port=port, path=url)

        response_headers = self.response_headers.copy()
        responses.add_callback(
            method=verb,
            url=full_url.url,
            callback=lambda request: self.__request_callback(verb, full_url.url, response_headers),
        )

        self.__stream = stream
        self.__cnx.request(verb, url, input, headers, stream=stream)

    def __readNextRequest(self, verb, url, input, headers):
        fixAuthorizationHeader(headers)
        assert self.__protocol == readLine(self.__file)
        assert verb == readLine(self.__file)
        assert self.__host == readLine(self.__file)
        assert str(self.__port) == readLine(self.__file)
        assert self.__splitUrl(url) == self.__splitUrl(readLine(self.__file))
        assert headers == eval(readLine(self.__file))
        expectedInput = readLine(self.__file)
        if isinstance(input, str):
            trInput = input.replace("\n", "").replace("\r", "")
            if input.startswith("{"):
                assert expectedInput.startswith("{"), expectedInput
                assert json.loads(trInput) == json.loads(expectedInput)
            else:
                assert trInput == expectedInput
        else:
            # for non-string input (e.g. upload asset), let it pass.
            pass

    def __splitUrl(self, url):
        splitedUrl = url.split("?")
        if len(splitedUrl) == 1:
            return splitedUrl
        assert len(splitedUrl) == 2
        base, qs = splitedUrl
        return (base, sorted(qs.split("&")))

    def __request_callback(self, request, uri, response_headers):
        self.__readNextRequest(self.__cnx.verb, self.__cnx.url, self.__cnx.input, self.__cnx.headers)

        status = int(readLine(self.__file))
        self.response_headers = CaseInsensitiveDict(eval(readLine(self.__file)))
        if self.__stream:
            output = BytesIO()
            while True:
                line = readLine(self.__file)
                if not line:
                    break
                output.write(base64.b64decode(line))
            output = output.getvalue()
        else:
            output = bytearray(readLine(self.__file), "utf-8")
        readLine(self.__file)

        # make a copy of the headers and remove the ones that interfere with the response handling
        adding_headers = CaseInsensitiveDict(self.response_headers)
        adding_headers.pop("content-length", None)
        adding_headers.pop("transfer-encoding", None)
        adding_headers.pop("content-encoding", None)

        response_headers.update(adding_headers)

        return [status, response_headers, output]

    def getresponse(self):
        response = self.__cnx.getresponse()

        # restore original headers to the response
        response.headers = self.response_headers

        return response

    def close(self):
        self.__cnx.close()


class ReplayingHttpConnection(ReplayingConnection):
    _realConnection = github.Requester.HTTPRequestsConnectionClass

    def __init__(self, *args, **kwds):
        super().__init__("http", *args, **kwds)


class ReplayingHttpsConnection(ReplayingConnection):
    _realConnection = github.Requester.HTTPSRequestsConnectionClass

    def __init__(self, *args, **kwds):
        super().__init__("https", *args, **kwds)


class BasicTestCase(unittest.TestCase):
    recordMode = False
    replayDataFolder = os.path.join(os.path.dirname(__file__), "ReplayData")

    def __init__(self, methodName="runTest") -> None:
        super().__init__(methodName)
        self.authMode = "token"
        self.per_page = Consts.DEFAULT_PER_PAGE
        self.retry = None
        self.pool_size = None
        self.seconds_between_requests: float | None = None
        self.seconds_between_writes: float | None = None

    def setUp(self):
        super().setUp()
        self.__customFilename: str | None = None
        self.__fileName = ""
        self.__file = None
        if (
            self.recordMode
        ):  # pragma no cover (Branch useful only when recording new tests, not used during automated tests)
            RecordingConnection.setOpenFile(self.__openFile)
            github.Requester.Requester.injectConnectionClasses(
                RecordingHttpConnection,
                RecordingHttpsConnection,
            )
            import GithubCredentials  # type: ignore

            self.oauth_token = (
                github.Auth.Token(GithubCredentials.oauth_token) if GithubCredentials.oauth_token else None
            )
            self.jwt = github.Auth.AppAuthToken(GithubCredentials.jwt) if GithubCredentials.jwt else None
            self.app_auth = (
                github.Auth.AppAuth(GithubCredentials.app_id, GithubCredentials.app_private_key)
                if GithubCredentials.app_id and GithubCredentials.app_private_key
                else None
            )
        else:
            ReplayingConnection.setOpenFile(self.__openFile)
            github.Requester.Requester.injectConnectionClasses(
                ReplayingHttpConnection,
                ReplayingHttpsConnection,
            )
            self.oauth_token = github.Auth.Token("oauth_token")
            self.jwt = github.Auth.AppAuthToken("jwt")
            self.app_auth = github.Auth.AppAuth(123456, APP_PRIVATE_KEY)

            responses.start()

    def setPerPage(self, per_page):
        self.per_page = per_page

    def setRetry(self, retry):
        self.retry = retry

    def setPoolSize(self, pool_size):
        self.pool_size = pool_size

    def setSecondsBetweenRequests(self, seconds_between_requests):
        self.seconds_between_requests = seconds_between_requests

    def setSecondsBetweenWrites(self, seconds_between_writes):
        self.seconds_between_writes = seconds_between_writes

    @property
    def thisTestFailed(self) -> bool:
        if hasattr(self._outcome, "errors"):  # type: ignore
            # Python 3.4 - 3.10
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)  # type: ignore
            ok = all(test != self for test, text in result.errors + result.failures)
            return not ok
        else:
            # Python 3.11+
            return self._outcome.result._excinfo is not None and self._outcome.result._excinfo  # type: ignore

    def tearDown(self):
        super().tearDown()
        responses.stop()
        responses.reset()
        self.__closeReplayFileIfNeeded(silent=self.thisTestFailed)
        github.Requester.Requester.resetConnectionClasses()

    def assertWarning(self, warning, expected):
        self.assertWarnings(warning, expected)

    def assertWarnings(self, warning, *expecteds):
        actual = [(type(message), type(message.message), message.message.args) for message in warning.warnings]
        expected = [(warnings.WarningMessage, DeprecationWarning, (expected,)) for expected in expecteds]
        self.assertSequenceEqual(actual, expected)

    @contextlib.contextmanager
    def ignoreWarning(self, category=Warning, module=""):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=category, module=module)
            yield

    @contextlib.contextmanager
    def replayData(self, filename: str):
        previous = self.__customFilename
        self.__customFilename = filename
        try:
            yield
        finally:
            self.__customFilename = previous

    def __openFile(self, mode):
        fileName = None
        if self.__customFilename:
            fileName = self.__customFilename
        else:
            for _, _, functionName, _ in traceback.extract_stack():
                if functionName.startswith("test") or functionName == "setUp" or functionName == "tearDown":
                    # because in class Hook(Framework.TestCase), method testTest calls Hook.test
                    if functionName != "test":
                        fileName = f"{self.__class__.__name__}.{functionName}.txt"
        fileName = os.path.join(self.replayDataFolder, fileName) if fileName else None
        if fileName != self.__fileName:
            self.__closeReplayFileIfNeeded()
            self.__fileName = fileName
            self.__file = open(self.__fileName, mode, encoding="utf-8")
        return self.__file

    def __closeReplayFileIfNeeded(self, silent=False):
        if self.__file is not None:
            if (
                not self.recordMode and not silent
            ):  # pragma no branch (Branch useful only when recording new tests, not used during automated tests)
                self.assertEqual(readLine(self.__file), "", self.__fileName)
            self.__file.close()

    def assertListKeyEqual(self, elements, key, expectedKeys):
        realKeys = [key(element) for element in elements]
        self.assertEqual(realKeys, expectedKeys)

    def assertListKeyBegin(self, elements, key, expectedKeys):
        realKeys = [key(element) for element in elements[: len(expectedKeys)]]
        self.assertEqual(realKeys, expectedKeys)


class TestCase(BasicTestCase):
    def doCheckFrame(self, obj, frame):
        if obj._headers == {} and frame is None:
            return
        if obj._headers is None and frame == {}:
            return
        self.assertEqual(obj._headers, frame[2])

    def getFrameChecker(self):
        return lambda requester, obj, frame: self.doCheckFrame(obj, frame)

    def setUp(self):
        super().setUp()

        # Set up frame debugging
        github.GithubObject.GithubObject.setCheckAfterInitFlag(True)
        github.Requester.Requester.setDebugFlag(True)
        github.Requester.Requester.setOnCheckMe(self.getFrameChecker())

        self.g = self.get_github(self.authMode, self.retry, self.pool_size)

    def get_github(self, authMode, retry=None, pool_size=None):
        if authMode == "token":
            auth = self.oauth_token
        elif authMode == "jwt":
            auth = self.jwt
        elif authMode == "app":
            auth = self.app_auth
        elif self.authMode == "none":
            auth = None
        else:
            raise ValueError(f"Unsupported test auth mode: {authMode}")

        return github.Github(
            auth=auth,
            per_page=self.per_page,
            retry=retry,
            pool_size=pool_size,
            seconds_between_requests=self.seconds_between_requests,
            seconds_between_writes=self.seconds_between_writes,
        )


def activateRecordMode():  # pragma no cover (Function useful only when recording new tests, not used during automated tests)
    BasicTestCase.recordMode = True
