# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import logging
import httplib
import base64
import urllib
import urlparse
import sys

atLeastPython26 = sys.hexversion >= 0x02060000

if atLeastPython26:
    import json
else:  # pragma no cover
    import simplejson as json  # pragma no cover

import GithubException


class Requester:
    __httpConnectionClass = httplib.HTTPConnection
    __httpsConnectionClass = httplib.HTTPSConnection

    @classmethod
    def injectConnectionClasses(cls, httpConnectionClass, httpsConnectionClass):
        cls.__httpConnectionClass = httpConnectionClass
        cls.__httpsConnectionClass = httpsConnectionClass

    def __init__(self, login_or_token, password, base_url, timeout, client_id, client_secret, user_agent):
        if password is not None:
            login = login_or_token
            self.__authorizationHeader = "Basic " + base64.b64encode(login + ":" + password).replace('\n', '')
        elif login_or_token is not None:
            token = login_or_token
            self.__authorizationHeader = "token " + token
        else:
            self.__authorizationHeader = None

        self.__base_url = base_url
        o = urlparse.urlparse(base_url)
        self.__hostname = o.hostname
        self.__port = o.port
        self.__prefix = o.path
        self.__timeout = timeout
        self.__scheme = o.scheme
        if o.scheme == "https":
            self.__connectionClass = self.__httpsConnectionClass
        elif o.scheme == "http":
            self.__connectionClass = self.__httpConnectionClass
        else:
            assert False, "Unknown URL scheme"  # pragma no cover
        self.rate_limiting = (5000, 5000)
        self.FIX_REPO_GET_GIT_REF = True

        self.__clientId = client_id
        self.__clientSecret = client_secret
        self.__userAgent = user_agent

    def requestAndCheck(self, verb, url, parameters, input):
        status, headers, output = self.requestRaw(verb, url, parameters, input)
        output = self.__structuredFromJson(output)
        if status >= 400:
            raise GithubException.GithubException(status, output)
        return headers, output

    def __structuredFromJson(self, data):
        if len(data) == 0:
            return None
        else:
            return json.loads(data)

    def requestRaw(self, verb, url, parameters, input):
        assert verb in ["HEAD", "GET", "POST", "PATCH", "PUT", "DELETE"]
        if parameters is None:
            parameters = dict()

        requestHeaders = dict()
        self.__authenticate(requestHeaders, parameters)
        if self.__userAgent is not None:
            requestHeaders["User-Agent"] = self.__userAgent

        url = self.__makeAbsoluteUrl(url)
        url = self.__addParametersToUrl(url, parameters)

        if input is not None:
            requestHeaders["Content-Type"] = "application/json"

        cnx = self.__createConnection()
        cnx.request(
            verb,
            url,
            json.dumps(input),
            requestHeaders
        )
        response = cnx.getresponse()

        status = response.status
        responseHeaders = dict(response.getheaders())
        output = response.read()

        cnx.close()

        if "x-ratelimit-remaining" in responseHeaders and "x-ratelimit-limit" in responseHeaders:
            self.rate_limiting = (int(responseHeaders["x-ratelimit-remaining"]), int(responseHeaders["x-ratelimit-limit"]))

        self.__log(verb, url, requestHeaders, input, status, responseHeaders, output)

        return status, responseHeaders, output

    def __authenticate(self, requestHeaders, parameters):
        if self.__clientId and self.__clientSecret:
            parameters["client_id"] = self.__clientId
            parameters["client_secret"] = self.__clientSecret
        if self.__authorizationHeader is not None:
            requestHeaders["Authorization"] = self.__authorizationHeader

    def __makeAbsoluteUrl(self, url):
        # URLs generated locally will be relative to __base_url
        # URLs returned from the server will start with __base_url
        if url.startswith("/"):
            url = self.__prefix + url
        else:
            o = urlparse.urlparse(url)
            assert o.scheme == self.__scheme or o.scheme == "https" and self.__scheme == "http"  # Issue #80
            assert o.hostname == self.__hostname
            assert o.path.startswith(self.__prefix)
            assert o.port == self.__port
            url = o.path
            if o.query != "":
                url += "?" + o.query
        return url

    def __addParametersToUrl(self, url, parameters):
        if len(parameters) == 0:
            return url
        else:
            return url + "?" + urllib.urlencode(parameters)

    def __createConnection(self):
        if atLeastPython26:
            return self.__connectionClass(host=self.__hostname, port=self.__port, strict=True, timeout=self.__timeout)
        else:  # pragma no cover
            return self.__connectionClass(host=self.__hostname, port=self.__port, strict=True)  # pragma no cover

    def __log(self, verb, url, requestHeaders, input, status, responseHeaders, output):
        logger = logging.getLogger(__name__)
        if logger.isEnabledFor(logging.DEBUG):
            if "Authorization" in requestHeaders:
                if requestHeaders["Authorization"].startswith("Basic"):
                    requestHeaders["Authorization"] = "Basic (login and password removed)"
                elif requestHeaders["Authorization"].startswith("token"):
                    requestHeaders["Authorization"] = "token (oauth token removed)"
                else:  # pragma no cover
                    requestHeaders["Authorization"] = "Unknown authorization removed"
            logger.debug("%s %s://%s%s %s %s ==> %i %s %s", str(verb), self.__scheme, self.__hostname, str(url), str(requestHeaders), str(input), status, str(responseHeaders), str(output))
