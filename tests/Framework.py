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
# Copyright 2026 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2026 Hugo van Kemenade <1324225+hugovk@users.noreply.github.com>   #
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

import contextlib
import functools
import os
import traceback
import unittest
import warnings
from collections.abc import Generator
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlsplit

import vcr
import vcr.cassette
from niquests.packages.urllib3.util import Url
from requests.structures import CaseInsensitiveDict
from vcr.matchers import requests_match

import github
from github import Consts

from . import VcrSerializer

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


@dataclass
class Request:
    protocol: str
    verb: str
    host: str
    port: int | None
    url: str
    request_headers: dict[str, Any]
    input: Any

    def with_response(self, status: int, response_headers: dict[str, Any], output: bytes) -> RequestResponse:
        return RequestResponse(
            self.protocol,
            self.verb,
            self.host,
            self.port,
            self.url,
            self.request_headers,
            self.input,
            status,
            response_headers,
            output,
        )


@dataclass
class RequestResponse(Request):
    protocol: str
    verb: str
    host: str
    port: int | None
    url: str
    request_headers: dict[str, Any]
    input: Any
    status: int
    response_headers: dict[str, Any]
    output: bytes


class OrderedCassette(vcr.cassette.Cassette):
    """
    Same as vcrpy's ``Cassette``, but only ever considers the next not-yet-played interaction as a candidate match,
    instead of searching the whole cassette for any not-yet-played interaction that matches.

    vcrpy's default behavior replays same-shaped requests in recording order (since
    it always returns the earliest unplayed match), but happily serves requests out of order
    relative to *other*, differently-shaped requests -- e.g. cassette [A, B, C] replays fine as
    [B, A, C] as long as each of A, B, C individually matches something unplayed. That would let a
    refactor that accidentally reorders API calls pass silently. Requiring an exact match against
    the next interaction turns that into a hard ``CannotOverwriteExistingCassetteException``.

    """

    def _responses(self, request):
        request = self._before_record_request(request)
        for index, (stored_request, response) in enumerate(self.data):
            if self.play_counts[index] == 0:
                if requests_match(request, stored_request, self._match_on):
                    yield index, response
                return


class OrderedVCR(vcr.VCR):
    def _use_cassette(self, with_current_defaults=False, **kwargs):
        if with_current_defaults:
            config = self.get_merged_config(**kwargs)
            return OrderedCassette.use(**config)
        args_getter = functools.partial(self.get_merged_config, **kwargs)
        return OrderedCassette.use_arg_getter(args_getter)


# A single VCR instance, shared across all tests: it patches http.client/urllib3 generically
# enough that it transparently intercepts both "requests" and "niquests" traffic (see
# https://niquests.readthedocs.io/en/latest/community/extensions.html), unlike "responses",
# which required fooling it into believing niquests IS requests via sys.modules aliasing.
# OrderedVCR additionally enforces that requests are replayed in exactly the order they were
# recorded (see OrderedCassette above).
_vcr = OrderedVCR(serializer="pygithub-replaydata", record_mode="none")
_vcr.register_serializer("pygithub-replaydata", VcrSerializer)
_vcr.register_persister(VcrSerializer.Utf8FilesystemPersister)


class CassetteConnection:
    """
    Base for the classes injected via ``Requester.injectConnectionClasses``.

    All the actual HTTP interception (matching, recording, replaying) is done by ``vcrpy``,
    patched in transparently underneath ``self._realConnection`` (an unmodified
    ``HTTP[S]RequestsConnectionClass``, i.e. the real ``requests``/``niquests`` ``Session``).
    The only thing this class does is make sure the *correct* cassette -- matching the
    currently running setUp/test/tearDown method, or a ``replayData()`` override -- is active
    before the connection is used, mirroring how many real requests happen to reuse a
    single connection per test (``Requester.__persist`` is disabled while testing, so a new
    connection is created for every single HTTP request).

    """

    def __init__(self, host, port, *args, **kwds):
        BasicTestCase.ensureCassette()
        self.__cnx = self._realConnection(host, port, *args, **kwds)

    @property
    def host(self):
        return self.__cnx.host

    def request(self, verb, url, input, headers, stream=False):
        self.__cnx.request(verb, url, input, headers, stream=stream)

    def getresponse(self):
        return self.__cnx.getresponse()

    def close(self):
        return self.__cnx.close()


class CassetteHttpConnection(CassetteConnection):
    _realConnection = github.Requester.HTTPRequestsConnectionClass


class CassetteHttpsConnection(CassetteConnection):
    _realConnection = github.Requester.HTTPSRequestsConnectionClass


class BasicTestCase(unittest.TestCase):
    recordMode = False
    replayDataFolder = os.path.join(os.path.dirname(__file__), "ReplayData")

    # The test currently running, i.e. the one whose stack `ensureCassette()` should inspect
    # to resolve the active replay file. `CassetteConnection.__init__` cannot reach this any
    # other way, since `Requester.injectConnectionClasses` only takes classes, not instances.
    __activeInstance: BasicTestCase | None = None

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
        self.__cassettePath: str | None = None
        self.__cassetteCm = None
        self.__cassette = None
        self.__capturedRequests: list[RequestResponse] | None = None
        BasicTestCase.__activeInstance = self

        github.Requester.Requester.injectConnectionClasses(
            CassetteHttpConnection,
            CassetteHttpsConnection,
        )
        if (
            self.recordMode
        ):  # pragma no cover (Branch useful only when recording new tests, not used during automated tests)
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
            self.oauth_token = github.Auth.Token("oauth_token")
            self.jwt = github.Auth.AppAuthToken("jwt")
            self.app_auth = github.Auth.AppAuth(123456, APP_PRIVATE_KEY)

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
        self.__closeCassetteIfNeeded(silent=self.thisTestFailed)
        github.Requester.Requester.resetConnectionClasses()
        BasicTestCase.__activeInstance = None

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

    @contextlib.contextmanager
    def captureRequests(self) -> Generator[list[RequestResponse]]:
        requests: list[RequestResponse] = []
        previous = self.__capturedRequests
        self.__capturedRequests = requests
        try:
            yield requests
        finally:
            self.__capturedRequests = previous

    @classmethod
    def ensureCassette(cls) -> None:
        """
        Called once per HTTP connection (i.e. once per request, connection reuse is disabled while testing) to make
        sure the vcrpy cassette matching the currently running setUp/test/tearDown method -- or a ``replayData()``
        override -- is the active one.
        """
        self = cls.__activeInstance
        if self is not None:
            self.__ensureCassette()

    def __resolveFileName(self) -> str | None:
        if self.__customFilename:
            return self.__customFilename
        fileName = None
        for _, _, functionName, _ in traceback.extract_stack():
            if functionName.startswith("test") or functionName == "setUp" or functionName == "tearDown":
                # because in class Hook(Framework.TestCase), method testTest calls Hook.test
                if functionName != "test":
                    fileName = f"{self.__class__.__name__}.{functionName}.txt"
        return fileName

    def __ensureCassette(self) -> None:
        fileName = self.__resolveFileName()
        path = os.path.join(self.replayDataFolder, fileName) if fileName else None
        if path == self.__cassettePath:
            return
        self.__closeCassetteIfNeeded()
        self.__cassettePath = path
        if path is None:
            return
        record_mode = "all" if self.recordMode else "none"
        if self.recordMode and os.path.exists(path):
            # vcrpy's "all" record mode never plays back existing interactions, but it still
            # loads them from disk and keeps them in Cassette.data -- so without this, recording
            # over an existing replay file would append the freshly recorded interactions after
            # the stale ones instead of replacing them.
            os.remove(path)
        cassetteCm = _vcr.use_cassette(path, record_mode=record_mode)
        self.__cassette = cassetteCm.__enter__()
        self.__cassetteCm = cassetteCm
        # wired unconditionally (not just while captureRequests() is active) and exactly once per
        # cassette: __recordInteraction() itself checks __capturedRequests, so this single wiring
        # transparently reflects whatever captureRequests() call is active by the time each
        # request actually happens, without ever double-wrapping play_response/append.
        self.__wireCaptureHook(self.__cassette)

    def __closeCassetteIfNeeded(self, silent=False):
        if self.__cassetteCm is not None:
            if (
                not self.recordMode and not silent
            ):  # pragma no branch (Branch useful only when recording new tests, not used during automated tests)
                self.assertTrue(
                    self.__cassette.all_played,
                    f"Not all replay data was used in {self.__cassettePath}",
                )
            self.__cassetteCm.__exit__(None, None, None)
            self.__cassetteCm = None
            self.__cassette = None

    def __wireCaptureHook(self, cassette) -> None:
        originalPlayResponse = cassette.play_response
        originalAppend = cassette.append

        def play_response(request):
            response = originalPlayResponse(request)
            self.__recordInteraction(request, response)
            return response

        def append(request, response):
            originalAppend(request, response)
            self.__recordInteraction(request, response)

        cassette.play_response = play_response
        cassette.append = append

    def __recordInteraction(self, request, response) -> None:
        if self.__capturedRequests is None:
            return
        parts = urlsplit(request.uri)
        url = parts.path + (f"?{parts.query}" if parts.query else "")
        response_headers = CaseInsensitiveDict(
            {name: values[0] if isinstance(values, list) else values for name, values in response["headers"].items()},
        )
        self.__capturedRequests.append(
            RequestResponse(
                parts.scheme,
                request.method,
                parts.hostname,
                parts.port,
                url,
                dict(request.headers),
                request.body,
                response["status"]["code"],
                {k: v for k, v in response_headers.lower_items()},
                response["body"]["string"],
            ),
        )

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
