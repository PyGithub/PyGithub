# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import unittest
import httplib
import traceback

import github


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
        if headers["Authorization"].startswith("token "):
            headers["Authorization"] = "token private_token_removed"
        elif headers["Authorization"].startswith("Basic "):
            headers["Authorization"] = "Basic login_and_password_removed"
        else:
            assert False


class RecordingConnection:
    def __init__(self, file, protocol, host, port, *args, **kwds):
        self.__file = file
        self.__protocol = protocol
        self.__host = host
        self.__port = str(port)
        self.__cnx = self._realConnection(host, port, *args, **kwds)

    def request(self, verb, url, input, headers):
        print verb, url, input, headers,
        self.__cnx.request(verb, url, input, headers)
        fixAuthorizationHeader(headers)
        self.__file.write(self.__protocol + " " + verb + " " + self.__host + " " + self.__port + " " + url + " " + str(headers) + " " + input + "\n")

    def getresponse(self):
        res = self.__cnx.getresponse()

        status = res.status
        print "=>", status
        headers = res.getheaders()
        output = res.read()

        self.__file.write(str(status) + "\n")
        self.__file.write(str(headers) + "\n")
        self.__file.write(str(output) + "\n")

        return FakeHttpResponse(status, headers, output)

    def close(self):
        self.__file.write("\n")
        return self.__cnx.close()


class RecordingHttpConnection(RecordingConnection):
    _realConnection = httplib.HTTPConnection

    def __init__(self, file, *args, **kwds):
        RecordingConnection.__init__(self, file, "http", *args, **kwds)


class RecordingHttpsConnection(RecordingConnection):
    _realConnection = httplib.HTTPSConnection

    def __init__(self, file, *args, **kwds):
        print args, kwds
        RecordingConnection.__init__(self, file, "https", *args, **kwds)


class ReplayingConnection:
    def __init__(self, testCase, file, protocol, host, port, *args, **kwds):
        self.__testCase = testCase
        self.__file = file
        self.__protocol = protocol
        self.__host = host
        self.__port = str(port)

    def request(self, verb, url, input, headers):
        fixAuthorizationHeader(headers)
        expectation = self.__file.readline().strip()
        self.__testCase.assertEqual(self.__protocol + " " + verb + " " + self.__host + " " + self.__port + " " + url + " " + str(headers) + " " + input, expectation)

    def getresponse(self):
        status = int(self.__file.readline().strip())
        headers = eval(self.__file.readline().strip())
        output = self.__file.readline().strip()

        return FakeHttpResponse(status, headers, output)

    def close(self):
        self.__file.readline()


def ReplayingHttpConnection(testCase, file, *args, **kwds):
    return ReplayingConnection(testCase, file, "http", *args, **kwds)


def ReplayingHttpsConnection(testCase, file, *args, **kwds):
    return ReplayingConnection(testCase, file, "https", *args, **kwds)


class BasicTestCase(unittest.TestCase):
    recordMode = False

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__fileName = ""
        self.__file = None
        if self.recordMode:
            github.Requester.Requester.injectConnectionClasses(
                lambda ignored, *args, **kwds: RecordingHttpConnection(self.__openFile("wb"), *args, **kwds),
                lambda ignored, *args, **kwds: RecordingHttpsConnection(self.__openFile("wb"), *args, **kwds)
            )
            import GithubCredentials
            self.login = GithubCredentials.login
            self.password = GithubCredentials.password
            self.oauth_token = GithubCredentials.oauth_token
        else:
            github.Requester.Requester.injectConnectionClasses(
                lambda ignored, *args, **kwds: ReplayingHttpConnection(self, self.__openFile("r"), *args, **kwds),
                lambda ignored, *args, **kwds: ReplayingHttpsConnection(self, self.__openFile("r"), *args, **kwds)
            )
            self.login = "login"
            self.password = "password"
            self.oauth_token = "oauth_token"

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.__closeReplayFileIfNeeded()

    def __openFile(self, mode):
        for (_, _, functionName, _) in traceback.extract_stack():
            if functionName.startswith("test") or functionName == "setUp" or functionName == "tearDown":
                if functionName != "test":  # because in class Hook(Framework.TestCase), method testTest calls Hook.test
                    fileName = os.path.join(os.path.dirname(__file__), "ReplayData", self.__class__.__name__ + "." + functionName + ".txt")
        if fileName != self.__fileName:
            self.__closeReplayFileIfNeeded()
            self.__fileName = fileName
            self.__file = open(self.__fileName, mode)
        return self.__file

    def __closeReplayFileIfNeeded(self):
        if self.__file is not None:
            if not self.recordMode:
                self.assertEqual(self.__file.readline(), "")
            self.__file.close()

    def assertListKeyEqual(self, elements, key, expectedKeys):
        realKeys = [key(element) for element in elements]
        self.assertEqual(realKeys, expectedKeys)

    def assertListKeyBegin(self, elements, key, expectedKeys):
        realKeys = [key(element) for element in elements[: len(expectedKeys)]]
        self.assertEqual(realKeys, expectedKeys)


class TestCase(BasicTestCase):
    def setUp(self):
        BasicTestCase.setUp(self)
        self.g = github.Github(self.login, self.password)


def activateRecordMode():
    BasicTestCase.recordMode = True
