# -*- coding: utf-8 -*-

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
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Laurent Mazuel <lmazuel@microsoft.com>                        #
# Copyright 2018 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import json
import os
import sys
import traceback
import unittest
import httpretty
from requests.structures import CaseInsensitiveDict
from urllib3.util import Url

import github

python2 = sys.hexversion < 0x03000000
atLeastPython3 = sys.hexversion >= 0x03000000


def readLine(file):
    if atLeastPython3:
        return file.readline().decode("utf-8").strip()
    else:
        return file.readline().strip()


class FakeHttpResponse:
    def __init__(self, status, headers, output):
        self.status = status
        self.__headers = headers
        self.__output = output

    def getheaders(self):
        return self.__headers

    def read(self):
        return self.__output


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


class RecordingConnection:  # pragma no cover (Class useful only when recording new tests, not used during automated tests)
    def __init__(self, file, protocol, host, port, *args, **kwds):
        self.__file = file
        self.__protocol = protocol
        self.__host = host
        self.__port = str(port)
        self.__cnx = self._realConnection(host, port, *args, **kwds)

    def request(self, verb, url, input, headers):
        print verb, url, input, headers,
        self.__cnx.request(verb, url, input, headers)
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
        self.__writeLine(str(anonymous_headers))
        self.__writeLine(str(input).replace('\n', '').replace('\r', ''))

    def getresponse(self):
        res = self.__cnx.getresponse()

        status = res.status
        print "=>", status
        headers = res.getheaders()
        output = res.read()

        self.__writeLine(str(status))
        self.__writeLine(str(list(headers)))
        if atLeastPython3:  # In Py3, return from "read" is bytes
            self.__writeLine(output)
        else:
            self.__writeLine(output.encode("utf-8"))

        return FakeHttpResponse(status, headers, output)

    def close(self):
        self.__writeLine("")
        return self.__cnx.close()

    def __writeLine(self, line):
        if atLeastPython3:
            try:  # Detect str/bytes
                self.__file.write(line + b"\n")
            except TypeError:
                self.__file.write((line + "\n").encode('utf-8'))
        else:
            self.__file.write(line + "\n")


class RecordingHttpConnection(RecordingConnection):  # pragma no cover (Class useful only when recording new tests, not used during automated tests)
    _realConnection = github.Requester.HTTPRequestsConnectionClass

    def __init__(self, file, *args, **kwds):
        RecordingConnection.__init__(self, file, "http", *args, **kwds)


class RecordingHttpsConnection(RecordingConnection):  # pragma no cover (Class useful only when recording new tests, not used during automated tests)
    _realConnection = github.Requester.HTTPSRequestsConnectionClass

    def __init__(self, file, *args, **kwds):
        RecordingConnection.__init__(self, file, "https", *args, **kwds)


class ReplayingConnection:
    def __init__(self, testCase, file, protocol, host, port, *args, **kwds):
        self.__testCase = testCase
        self.__file = file
        self.__protocol = protocol
        self.__host = host
        self.__port = port
        self.response_headers = CaseInsensitiveDict()

        self.__cnx = self._realConnection(host, port, *args, **kwds)

    def request(self, verb, url, input, headers):
        full_url = Url(scheme=self.__protocol, host=self.__host, port=self.__port, path=url)

        httpretty.register_uri(
            verb,
            full_url.url,
            body=self.__request_callback
        )

        self.__cnx.request(verb, url, input, headers)

    def __readNextRequest(self, verb, url, input, headers):
        fixAuthorizationHeader(headers)
        self.__testCase.assertEqual(self.__protocol, readLine(self.__file))
        self.__testCase.assertEqual(verb, readLine(self.__file))
        self.__testCase.assertEqual(self.__host, readLine(self.__file))
        self.__testCase.assertEqual(str(self.__port), readLine(self.__file))
        self.__testCase.assertEqual(self.__splitUrl(url), self.__splitUrl(readLine(self.__file)))
        self.__testCase.assertEqual(headers, eval(readLine(self.__file)))
        expectedInput = readLine(self.__file)
        if isinstance(input, (str, unicode)):
            if input.startswith("{"):
                self.__testCase.assertEqual(json.loads(input.replace('\n', '').replace('\r', '')), json.loads(expectedInput))
            elif python2:  # @todo Test in all cases, including Python 3.4+
                # In Python 3.4+, dicts are not output in the same order as in Python 2.7.
                # So, form-data encoding is not deterministic and is difficult to test.
                self.__testCase.assertEqual(input.replace('\n', '').replace('\r', ''), expectedInput)
        else:
            # for non-string input (e.g. upload asset), let it pass.
            pass

    def __splitUrl(self, url):
        splitedUrl = url.split("?")
        if len(splitedUrl) == 1:
            return splitedUrl
        self.__testCase.assertEqual(len(splitedUrl), 2)
        base, qs = splitedUrl
        return (base, sorted(qs.split("&")))

    def __request_callback(self, request, uri, response_headers):
        self.__readNextRequest(self.__cnx.verb, self.__cnx.url, self.__cnx.input, self.__cnx.headers)

        status = int(readLine(self.__file))
        self.response_headers = CaseInsensitiveDict(eval(readLine(self.__file)))
        output = readLine(self.__file)
        readLine(self.__file)

        if atLeastPython3:
            output = bytes(output, 'utf-8')

        # make a copy of the headers and remove the ones that interfere with the response handling
        adding_headers = CaseInsensitiveDict(self.response_headers)
        adding_headers.pop('content-length', None)
        adding_headers.pop('transfer-encoding', None)
        adding_headers.pop('content-encoding', None)

        response_headers.update(adding_headers)
        return [status, response_headers, output]

    def getresponse(self):
        # call original connection, this will go all the way down to the python socket and will be intercepted by httpretty
        response = self.__cnx.getresponse()

        # restore original headers to the response
        response.headers = self.response_headers

        return response

    def close(self):
        self.__cnx.close()


class ReplayingHttpConnection(ReplayingConnection):
    _realConnection = github.Requester.HTTPRequestsConnectionClass

    def __init__(self, testCase, file, *args, **kwds):
        ReplayingConnection.__init__(self, testCase, file, "http", *args, **kwds)


class ReplayingHttpsConnection(ReplayingConnection):
    _realConnection = github.Requester.HTTPSRequestsConnectionClass

    def __init__(self, testCase, file, *args, **kwds):
        ReplayingConnection.__init__(self, testCase, file, "https", *args, **kwds)


class BasicTestCase(unittest.TestCase):
    recordMode = False
    tokenAuthMode = False
    jwtAuthMode = False
    retry = None
    replayDataFolder = os.path.join(os.path.dirname(__file__), "ReplayData")

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__fileName = ""
        self.__file = None
        if self.recordMode:  # pragma no cover (Branch useful only when recording new tests, not used during automated tests)
            github.Requester.Requester.injectConnectionClasses(
                lambda ignored, *args, **kwds: RecordingHttpConnection(self.__openFile("wb"), *args, **kwds),
                lambda ignored, *args, **kwds: RecordingHttpsConnection(self.__openFile("wb"), *args, **kwds)
            )
            import GithubCredentials
            self.login = GithubCredentials.login
            self.password = GithubCredentials.password
            self.oauth_token = GithubCredentials.oauth_token
            self.jwt = GithubCredentials.jwt
            # @todo Remove client_id and client_secret from ReplayData (as we already remove login, password and oauth_token)
            # self.client_id = GithubCredentials.client_id
            # self.client_secret = GithubCredentials.client_secret
        else:
            github.Requester.Requester.injectConnectionClasses(
                lambda ignored, *args, **kwds: ReplayingHttpConnection(self, self.__openFile("rb"), *args, **kwds),
                lambda ignored, *args, **kwds: ReplayingHttpsConnection(self, self.__openFile("rb"), *args, **kwds)
            )
            self.login = "login"
            self.password = "password"
            self.oauth_token = "oauth_token"
            self.client_id = "client_id"
            self.client_secret = "client_secret"
            self.jwt = "jwt"

            httpretty.enable(allow_net_connect=False)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        httpretty.disable()
        httpretty.reset()
        self.__closeReplayFileIfNeeded()
        github.Requester.Requester.resetConnectionClasses()

    def __openFile(self, mode):
        for (_, _, functionName, _) in traceback.extract_stack():
            if functionName.startswith("test") or functionName == "setUp" or functionName == "tearDown":
                if functionName != "test":  # because in class Hook(Framework.TestCase), method testTest calls Hook.test
                    fileName = os.path.join(self.replayDataFolder, self.__class__.__name__ + "." + functionName + ".txt")
        if fileName != self.__fileName:
            self.__closeReplayFileIfNeeded()
            self.__fileName = fileName
            self.__file = open(self.__fileName, mode)
        return self.__file

    def __closeReplayFileIfNeeded(self):
        if self.__file is not None:
            if not self.recordMode:  # pragma no branch (Branch useful only when recording new tests, not used during automated tests)
                self.assertEqual(readLine(self.__file), "")
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
        BasicTestCase.setUp(self)

        # Set up frame debugging
        github.GithubObject.GithubObject.setCheckAfterInitFlag(True)
        github.Requester.Requester.setDebugFlag(True)
        github.Requester.Requester.setOnCheckMe(self.getFrameChecker())

        if self.tokenAuthMode:
            self.g = github.Github(self.oauth_token, retry=self.retry)
        elif self.jwtAuthMode:
            self.g = github.Github(jwt=self.jwt, retry=self.retry)
        else:
            self.g = github.Github(self.login, self.password, retry=self.retry)


def activateRecordMode():  # pragma no cover (Function useful only when recording new tests, not used during automated tests)
    BasicTestCase.recordMode = True


def activateTokenAuthMode():  # pragma no cover (Function useful only when recording new tests, not used during automated tests)
    BasicTestCase.tokenAuthMode = True


def activateJWTAuthMode():  # pragma no cover (Function useful only when recording new tests, not used during automated tests)
    BasicTestCase.jwtAuthMode = True


def enableRetry(retry):
    BasicTestCase.retry = retry
