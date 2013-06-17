# -*- coding: utf-8 -*-

# Copyright 2012 Andrew Bettison andrewb@zip.com.au
# Copyright 2012 Dima Kukushkin dima@kukushkin.me
# Copyright 2012 Michael Woodworth mwoodworth@upverter.com
# Copyright 2012 Petteri Muilu pmuilu@xena.(none)
# Copyright 2012 Steve English steve.english@navetas.com
# Copyright 2012 Vincent Jacques vincent@vincent-jacques.net
# Copyright 2012 Zearin zearin@gonk.net
# Copyright 2013 Vincent Jacques vincent@vincent-jacques.net
# Copyright 2013 Jonathan J Hunt hunt@braincorporation.com

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

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
atLeastPython3 = sys.hexversion >= 0x03000000

if atLeastPython26:
    import json
else:  # pragma no cover (Covered by all tests with Python 2.5)
    import simplejson as json  # pragma no cover (Covered by all tests with Python 2.5)

import GithubException


class Requester:
    __httpConnectionClass = httplib.HTTPConnection
    __httpsConnectionClass = httplib.HTTPSConnection

    @classmethod
    def injectConnectionClasses(cls, httpConnectionClass, httpsConnectionClass):
        cls.__httpConnectionClass = httpConnectionClass
        cls.__httpsConnectionClass = httpsConnectionClass

    @classmethod
    def resetConnectionClasses(cls):
        cls.__httpConnectionClass = httplib.HTTPConnection
        cls.__httpsConnectionClass = httplib.HTTPSConnection

    def __init__(self, login_or_token, password, base_url, timeout, client_id, client_secret, user_agent, per_page):
        if password is not None:
            login = login_or_token
            if atLeastPython3:
                self.__authorizationHeader = "Basic " + base64.b64encode((login + ":" + password).encode("utf-8")).decode("utf-8").replace('\n', '')  # pragma no cover (Covered by Authentication.testAuthorizationHeaderWithXxx with Python 3)
            else:
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
            assert False, "Unknown URL scheme"
        self.rate_limiting = (5000, 5000)
        self.FIX_REPO_GET_GIT_REF = True
        self.per_page = per_page

        self.oauth_scopes = None

        self.__clientId = client_id
        self.__clientSecret = client_secret

        assert user_agent is not None, 'github now requires a user-agent. ' \
            'See http://developer.github.com/v3/#user-agent-required'
        self.__userAgent = user_agent

    def requestJsonAndCheck(self, verb, url, parameters, input):
        return self.__check(*self.requestJson(verb, url, parameters, input))

    def requestMultipartAndCheck(self, verb, url, parameters, input):
        return self.__check(*self.requestMultipart(verb, url, parameters, input))

    def __check(self, status, responseHeaders, output):
        output = self.__structuredFromJson(output)
        if status >= 400:
            raise self.__createException(status, output)
        return responseHeaders, output

    def __createException(self, status, output):
        if status == 401 and output["message"] == "Bad credentials":
            cls = GithubException.BadCredentialsException
        elif status == 403 and output["message"].startswith("Missing or invalid User Agent string"):
            cls = GithubException.BadUserAgentException
        elif status == 403 and output["message"].startswith("API Rate Limit Exceeded"):
            cls = GithubException.RateLimitExceededException
        elif status == 404 and output["message"] == "Not Found":
            cls = GithubException.UnknownObjectException
        else:
            cls = GithubException.GithubException
        return cls(status, output)

    def __structuredFromJson(self, data):
        if len(data) == 0:
            return None
        else:
            if atLeastPython3 and isinstance(data, bytes):  # pragma no branch (Covered by Issue142.testDecodeJson with Python 3)
                data = data.decode("utf-8")  # pragma no cover (Covered by Issue142.testDecodeJson with Python 3)
            return json.loads(data)

    def requestJson(self, verb, url, parameters, input):
        def encode(input):
            return "application/json", json.dumps(input)

        return self.__requestEncode(verb, url, parameters, input, encode)

    def requestMultipart(self, verb, url, parameters, input):
        def encode(input):
            boundary = "----------------------------3c3ba8b523b2"
            eol = "\r\n"

            encoded_input = ""
            for name, value in input.iteritems():
                encoded_input += "--" + boundary + eol
                encoded_input += "Content-Disposition: form-data; name=\"" + name + "\"" + eol
                encoded_input += eol
                encoded_input += value + eol
            encoded_input += "--" + boundary + "--" + eol
            return "multipart/form-data; boundary=" + boundary, encoded_input

        return self.__requestEncode(verb, url, parameters, input, encode)

    def __requestEncode(self, verb, url, parameters, input, encode):
        assert verb in ["HEAD", "GET", "POST", "PATCH", "PUT", "DELETE"]
        if parameters is None:
            parameters = dict()

        requestHeaders = dict()
        self.__authenticate(url, requestHeaders, parameters)
        requestHeaders["User-Agent"] = self.__userAgent

        url = self.__makeAbsoluteUrl(url)
        url = self.__addParametersToUrl(url, parameters)

        encoded_input = "null"
        if input is not None:
            requestHeaders["Content-Type"], encoded_input = encode(input)

        status, responseHeaders, output = self.__requestRaw(verb, url, requestHeaders, encoded_input)

        if "x-ratelimit-remaining" in responseHeaders and "x-ratelimit-limit" in responseHeaders:
            self.rate_limiting = (int(responseHeaders["x-ratelimit-remaining"]), int(responseHeaders["x-ratelimit-limit"]))

        if "x-oauth-scopes" in responseHeaders:
            self.oauth_scopes = responseHeaders["x-oauth-scopes"].split(", ")

        return status, responseHeaders, output

    def __requestRaw(self, verb, url, requestHeaders, input):
        cnx = self.__createConnection()
        cnx.request(
            verb,
            url,
            input,
            requestHeaders
        )
        response = cnx.getresponse()

        status = response.status
        responseHeaders = dict(response.getheaders())
        output = response.read()

        cnx.close()

        self.__log(verb, url, requestHeaders, input, status, responseHeaders, output)

        return status, responseHeaders, output

    def __authenticate(self, url, requestHeaders, parameters):
        if self.__clientId and self.__clientSecret and "client_id=" not in url:
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
        kwds = {}
        if not atLeastPython3:  # pragma no branch (Branch useful only with Python 3)
            kwds["strict"] = True  # Useless in Python3, would generate a deprecation warning
        if atLeastPython26:  # pragma no branch (Branch useful only with Python 2.5)
            kwds["timeout"] = self.__timeout  # Did not exist before Python2.6
        return self.__connectionClass(host=self.__hostname, port=self.__port, **kwds)

    def __log(self, verb, url, requestHeaders, input, status, responseHeaders, output):
        logger = logging.getLogger(__name__)
        if logger.isEnabledFor(logging.DEBUG):
            if "Authorization" in requestHeaders:
                if requestHeaders["Authorization"].startswith("Basic"):
                    requestHeaders["Authorization"] = "Basic (login and password removed)"
                elif requestHeaders["Authorization"].startswith("token"):
                    requestHeaders["Authorization"] = "token (oauth token removed)"
            logger.debug("%s %s://%s%s %s %s ==> %i %s %s", str(verb), self.__scheme, self.__hostname, str(url), str(requestHeaders), str(input), status, str(responseHeaders), str(output))
