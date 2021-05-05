############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Andrew Bettison <andrewb@zip.com.au>                          #
# Copyright 2012 Dima Kukushkin <dima@kukushkin.me>                            #
# Copyright 2012 Michael Woodworth <mwoodworth@upverter.com>                   #
# Copyright 2012 Petteri Muilu <pmuilu@xena.(none)>                            #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Cameron White <cawhite@pdx.edu>                               #
# Copyright 2013 Ed Jackson <ed.jackson@gmail.com>                             #
# Copyright 2013 Jonathan J Hunt <hunt@braincorporation.com>                   #
# Copyright 2013 Mark Roddy <markroddy@gmail.com>                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Jimmy Zelinskie <jimmyzelinskie@gmail.com>                    #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Brian Eugley <Brian.Eugley@capitalone.com>                    #
# Copyright 2015 Daniel Pocock <daniel@pocock.pro>                             #
# Copyright 2015 Jimmy Zelinskie <jimmyzelinskie@gmail.com>                    #
# Copyright 2016 Denis K <f1nal@cgaming.org>                                   #
# Copyright 2016 Jared K. Smith <jaredsmith@jaredsmith.net>                    #
# Copyright 2016 Jimmy Zelinskie <jimmy.zelinskie+git@gmail.com>               #
# Copyright 2016 Mathieu Mitchell <mmitchell@iweb.com>                         #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Dylan <djstein@ncsu.edu>                                      #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 R1kk3r <R1kk3r@users.noreply.github.com>                      #
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

import base64
import json
import logging
import mimetypes
import os
import re
import time
import urllib
from io import IOBase

import requests

from . import Consts, GithubException


class RequestsResponse:
    # mimic the httplib response object
    def __init__(self, r):
        self.status = r.status_code
        self.headers = r.headers
        self.text = r.text

    def getheaders(self):
        return self.headers.items()

    def read(self):
        return self.text


class HTTPSRequestsConnectionClass:
    # mimic the httplib connection object
    def __init__(
        self,
        host,
        port=None,
        strict=False,
        timeout=None,
        retry=None,
        pool_size=None,
        **kwargs,
    ):
        self.port = port if port else 443
        self.host = host
        self.protocol = "https"
        self.timeout = timeout
        self.verify = kwargs.get("verify", True)
        self.session = requests.Session()

        if retry is None:
            self.retry = requests.adapters.DEFAULT_RETRIES
        else:
            self.retry = retry

        if pool_size is None:
            self.pool_size = requests.adapters.DEFAULT_POOLSIZE
        else:
            self.pool_size = pool_size

        self.adapter = requests.adapters.HTTPAdapter(
            max_retries=self.retry,
            pool_connections=self.pool_size,
            pool_maxsize=self.pool_size,
        )
        self.session.mount("https://", self.adapter)

    def request(self, verb, url, input, headers):
        self.verb = verb
        self.url = url
        self.input = input
        self.headers = headers

    def getresponse(self):
        verb = getattr(self.session, self.verb.lower())
        url = f"{self.protocol}://{self.host}:{self.port}{self.url}"
        r = verb(
            url,
            headers=self.headers,
            data=self.input,
            timeout=self.timeout,
            verify=self.verify,
            allow_redirects=False,
        )
        return RequestsResponse(r)

    def close(self):
        return


class HTTPRequestsConnectionClass:
    # mimic the httplib connection object
    def __init__(
        self,
        host,
        port=None,
        strict=False,
        timeout=None,
        retry=None,
        pool_size=None,
        **kwargs,
    ):
        self.port = port if port else 80
        self.host = host
        self.protocol = "http"
        self.timeout = timeout
        self.verify = kwargs.get("verify", True)
        self.session = requests.Session()

        if retry is None:
            self.retry = requests.adapters.DEFAULT_RETRIES
        else:
            self.retry = retry

        if pool_size is None:
            self.pool_size = requests.adapters.DEFAULT_POOLSIZE
        else:
            self.pool_size = pool_size

        self.adapter = requests.adapters.HTTPAdapter(
            max_retries=self.retry,
            pool_connections=self.pool_size,
            pool_maxsize=self.pool_size,
        )
        self.session.mount("http://", self.adapter)

    def request(self, verb, url, input, headers):
        self.verb = verb
        self.url = url
        self.input = input
        self.headers = headers

    def getresponse(self):
        verb = getattr(self.session, self.verb.lower())
        url = f"{self.protocol}://{self.host}:{self.port}{self.url}"
        r = verb(
            url,
            headers=self.headers,
            data=self.input,
            timeout=self.timeout,
            verify=self.verify,
            allow_redirects=False,
        )
        return RequestsResponse(r)

    def close(self):
        return


class Requester:
    __httpConnectionClass = HTTPRequestsConnectionClass
    __httpsConnectionClass = HTTPSRequestsConnectionClass
    __connection = None
    __persist = True
    __logger = None

    @classmethod
    def injectConnectionClasses(cls, httpConnectionClass, httpsConnectionClass):
        cls.__persist = False
        cls.__httpConnectionClass = httpConnectionClass
        cls.__httpsConnectionClass = httpsConnectionClass

    @classmethod
    def resetConnectionClasses(cls):
        cls.__persist = True
        cls.__httpConnectionClass = HTTPRequestsConnectionClass
        cls.__httpsConnectionClass = HTTPSRequestsConnectionClass

    @classmethod
    def injectLogger(cls, logger):
        cls.__logger = logger

    @classmethod
    def resetLogger(cls):
        cls.__logger = None

    #############################################################
    # For Debug
    @classmethod
    def setDebugFlag(cls, flag):
        cls.DEBUG_FLAG = flag

    @classmethod
    def setOnCheckMe(cls, onCheckMe):
        cls.ON_CHECK_ME = onCheckMe

    DEBUG_FLAG = False

    DEBUG_FRAME_BUFFER_SIZE = 1024

    DEBUG_HEADER_KEY = "DEBUG_FRAME"

    ON_CHECK_ME = None

    def NEW_DEBUG_FRAME(self, requestHeader):
        """
        Initialize a debug frame with requestHeader
        Frame count is updated and will be attached to respond header
        The structure of a frame: [requestHeader, statusCode, responseHeader, raw_data]
        Some of them may be None
        """
        if self.DEBUG_FLAG:  # pragma no branch (Flag always set in tests)
            new_frame = [requestHeader, None, None, None]
            if (
                self._frameCount < self.DEBUG_FRAME_BUFFER_SIZE - 1
            ):  # pragma no branch (Should be covered)
                self._frameBuffer.append(new_frame)
            else:
                self._frameBuffer[0] = new_frame  # pragma no cover (Should be covered)

            self._frameCount = len(self._frameBuffer) - 1

    def DEBUG_ON_RESPONSE(self, statusCode, responseHeader, data):
        """
        Update current frame with response
        Current frame index will be attached to responseHeader
        """
        if self.DEBUG_FLAG:  # pragma no branch (Flag always set in tests)
            self._frameBuffer[self._frameCount][1:4] = [
                statusCode,
                responseHeader,
                data,
            ]
            responseHeader[self.DEBUG_HEADER_KEY] = self._frameCount

    def check_me(self, obj):
        if (
            self.DEBUG_FLAG and self.ON_CHECK_ME is not None
        ):  # pragma no branch (Flag always set in tests)
            frame = None
            if self.DEBUG_HEADER_KEY in obj._headers:
                frame_index = obj._headers[self.DEBUG_HEADER_KEY]
                frame = self._frameBuffer[frame_index]
            self.ON_CHECK_ME(obj, frame)

    def _initializeDebugFeature(self):
        self._frameCount = 0
        self._frameBuffer = []

    #############################################################

    def __init__(
        self,
        login_or_token,
        password,
        jwt,
        base_url,
        timeout,
        user_agent,
        per_page,
        verify,
        retry,
        pool_size,
    ):
        self._initializeDebugFeature()

        if password is not None:
            login = login_or_token
            b64 = (
                base64.b64encode((f"{login}:{password}").encode("utf-8"))
                .decode("utf-8")
                .replace("\n", "")
            )
            self.__authorizationHeader = f"Basic {b64}"
        elif login_or_token is not None:
            token = login_or_token
            self.__authorizationHeader = f"token {token}"
        elif jwt is not None:
            self.__authorizationHeader = f"Bearer {jwt}"
        else:
            self.__authorizationHeader = None

        self.__base_url = base_url
        o = urllib.parse.urlparse(base_url)
        self.__hostname = o.hostname
        self.__port = o.port
        self.__prefix = o.path
        self.__timeout = timeout
        self.__retry = retry  # NOTE: retry can be either int or an urllib3 Retry object
        self.__pool_size = pool_size
        self.__scheme = o.scheme
        if o.scheme == "https":
            self.__connectionClass = self.__httpsConnectionClass
        elif o.scheme == "http":
            self.__connectionClass = self.__httpConnectionClass
        else:
            assert False, "Unknown URL scheme"
        self.rate_limiting = (-1, -1)
        self.rate_limiting_resettime = 0
        self.FIX_REPO_GET_GIT_REF = True
        self.per_page = per_page

        self.oauth_scopes = None

        assert user_agent is not None, (
            "github now requires a user-agent. "
            "See http://docs.github.com/en/rest/reference/#user-agent-required"
        )
        self.__userAgent = user_agent
        self.__verify = verify

    def requestJsonAndCheck(self, verb, url, parameters=None, headers=None, input=None):
        return self.__check(
            *self.requestJson(
                verb, url, parameters, headers, input, self.__customConnection(url)
            )
        )

    def requestMultipartAndCheck(
        self, verb, url, parameters=None, headers=None, input=None
    ):
        return self.__check(
            *self.requestMultipart(
                verb, url, parameters, headers, input, self.__customConnection(url)
            )
        )

    def requestBlobAndCheck(self, verb, url, parameters=None, headers=None, input=None):
        return self.__check(
            *self.requestBlob(
                verb, url, parameters, headers, input, self.__customConnection(url)
            )
        )

    def __check(self, status, responseHeaders, output):
        output = self.__structuredFromJson(output)
        if status >= 400:
            raise self.__createException(status, responseHeaders, output)
        return responseHeaders, output

    def __customConnection(self, url):
        cnx = None
        if not url.startswith("/"):
            o = urllib.parse.urlparse(url)
            if (
                o.hostname != self.__hostname
                or (o.port and o.port != self.__port)
                or (
                    o.scheme != self.__scheme
                    and not (o.scheme == "https" and self.__scheme == "http")
                )
            ):  # issue80
                if o.scheme == "http":
                    cnx = self.__httpConnectionClass(
                        o.hostname,
                        o.port,
                        retry=self.__retry,
                        pool_size=self.__pool_size,
                    )
                elif o.scheme == "https":
                    cnx = self.__httpsConnectionClass(
                        o.hostname,
                        o.port,
                        retry=self.__retry,
                        pool_size=self.__pool_size,
                    )
        return cnx

    def __createException(self, status, headers, output):
        if status == 401 and output.get("message") == "Bad credentials":
            cls = GithubException.BadCredentialsException
        elif (
            status == 401
            and Consts.headerOTP in headers
            and re.match(r".*required.*", headers[Consts.headerOTP])
        ):
            cls = GithubException.TwoFactorException
        elif status == 403 and output.get("message").startswith(
            "Missing or invalid User Agent string"
        ):
            cls = GithubException.BadUserAgentException
        elif status == 403 and (
            output.get("message").lower().startswith("api rate limit exceeded")
            or output.get("message")
            .lower()
            .endswith("please wait a few minutes before you try again.")
        ):
            cls = GithubException.RateLimitExceededException
        elif status == 404 and output.get("message") == "Not Found":
            cls = GithubException.UnknownObjectException
        else:
            cls = GithubException.GithubException
        return cls(status, output, headers)

    def __structuredFromJson(self, data):
        if len(data) == 0:
            return None
        else:
            if isinstance(data, bytes):
                data = data.decode("utf-8")
            try:
                return json.loads(data)
            except ValueError:
                if data.startswith("{") or data.startswith("["):
                    raise
                return {"data": data}

    def requestJson(
        self, verb, url, parameters=None, headers=None, input=None, cnx=None
    ):
        def encode(input):
            return "application/json", json.dumps(input)

        return self.__requestEncode(cnx, verb, url, parameters, headers, input, encode)

    def requestMultipart(
        self, verb, url, parameters=None, headers=None, input=None, cnx=None
    ):
        def encode(input):
            boundary = "----------------------------3c3ba8b523b2"
            eol = "\r\n"

            encoded_input = ""
            for name, value in input.items():
                encoded_input += f"--{boundary}{eol}"
                encoded_input += f'Content-Disposition: form-data; name="{name}"{eol}'
                encoded_input += eol
                encoded_input += value + eol
            encoded_input += f"--{boundary}--{eol}"
            return f"multipart/form-data; boundary={boundary}", encoded_input

        return self.__requestEncode(cnx, verb, url, parameters, headers, input, encode)

    def requestBlob(self, verb, url, parameters={}, headers={}, input=None, cnx=None):
        def encode(local_path):
            if "Content-Type" in headers:
                mime_type = headers["Content-Type"]
            else:
                guessed_type = mimetypes.guess_type(input)
                mime_type = (
                    guessed_type[0]
                    if guessed_type[0] is not None
                    else Consts.defaultMediaType
                )
            f = open(local_path, "rb")
            return mime_type, f

        if input:
            headers["Content-Length"] = str(os.path.getsize(input))
        return self.__requestEncode(cnx, verb, url, parameters, headers, input, encode)

    def requestMemoryBlobAndCheck(
        self, verb, url, parameters, headers, file_like, cnx=None
    ):
        # The expected signature of encode means that the argument is ignored.
        def encode(_):
            return headers["Content-Type"], file_like

        if not cnx:
            cnx = self.__customConnection(url)
        return self.__check(
            *self.__requestEncode(
                cnx, verb, url, parameters, headers, file_like, encode
            )
        )

    def __requestEncode(
        self, cnx, verb, url, parameters, requestHeaders, input, encode
    ):
        assert verb in ["HEAD", "GET", "POST", "PATCH", "PUT", "DELETE"]
        if parameters is None:
            parameters = dict()
        if requestHeaders is None:
            requestHeaders = dict()

        self.__authenticate(url, requestHeaders, parameters)
        requestHeaders["User-Agent"] = self.__userAgent

        url = self.__makeAbsoluteUrl(url)
        url = self.__addParametersToUrl(url, parameters)

        encoded_input = None
        if input is not None:
            requestHeaders["Content-Type"], encoded_input = encode(input)

        self.NEW_DEBUG_FRAME(requestHeaders)

        status, responseHeaders, output = self.__requestRaw(
            cnx, verb, url, requestHeaders, encoded_input
        )

        if (
            Consts.headerRateRemaining in responseHeaders
            and Consts.headerRateLimit in responseHeaders
        ):
            self.rate_limiting = (
                int(responseHeaders[Consts.headerRateRemaining]),
                int(responseHeaders[Consts.headerRateLimit]),
            )
        if Consts.headerRateReset in responseHeaders:
            self.rate_limiting_resettime = int(responseHeaders[Consts.headerRateReset])

        if Consts.headerOAuthScopes in responseHeaders:
            self.oauth_scopes = responseHeaders[Consts.headerOAuthScopes].split(", ")

        self.DEBUG_ON_RESPONSE(status, responseHeaders, output)

        return status, responseHeaders, output

    def __requestRaw(self, cnx, verb, url, requestHeaders, input):
        original_cnx = cnx
        if cnx is None:
            cnx = self.__createConnection()
        cnx.request(verb, url, input, requestHeaders)
        response = cnx.getresponse()

        status = response.status
        responseHeaders = {k.lower(): v for k, v in response.getheaders()}
        output = response.read()

        cnx.close()
        if input:
            if isinstance(input, IOBase):
                input.close()

        self.__log(verb, url, requestHeaders, input, status, responseHeaders, output)

        if status == 202 and (
            verb == "GET" or verb == "HEAD"
        ):  # only for requests that are considered 'safe' in RFC 2616
            time.sleep(Consts.PROCESSING_202_WAIT_TIME)
            return self.__requestRaw(original_cnx, verb, url, requestHeaders, input)

        if status == 301 and "location" in responseHeaders:
            o = urllib.parse.urlparse(responseHeaders["location"])
            return self.__requestRaw(original_cnx, verb, o.path, requestHeaders, input)

        return status, responseHeaders, output

    def __authenticate(self, url, requestHeaders, parameters):
        if self.__authorizationHeader is not None:
            requestHeaders["Authorization"] = self.__authorizationHeader

    def __makeAbsoluteUrl(self, url):
        # URLs generated locally will be relative to __base_url
        # URLs returned from the server will start with __base_url
        if url.startswith("/"):
            url = f"{self.__prefix}{url}"
        else:
            o = urllib.parse.urlparse(url)
            assert o.hostname in [
                self.__hostname,
                "uploads.github.com",
                "status.github.com",
                "github.com",
            ], o.hostname
            assert o.path.startswith((self.__prefix, "/api/"))
            assert o.port == self.__port
            url = o.path
            if o.query != "":
                url += f"?{o.query}"
        return url

    def __addParametersToUrl(self, url, parameters):
        if len(parameters) == 0:
            return url
        else:
            return f"{url}?{urllib.parse.urlencode(parameters)}"

    def __createConnection(self):
        kwds = {}
        kwds["timeout"] = self.__timeout
        kwds["verify"] = self.__verify

        if self.__persist and self.__connection is not None:
            return self.__connection

        self.__connection = self.__connectionClass(
            self.__hostname,
            self.__port,
            retry=self.__retry,
            pool_size=self.__pool_size,
            **kwds,
        )

        return self.__connection

    def __log(self, verb, url, requestHeaders, input, status, responseHeaders, output):
        if self.__logger is None:
            self.__logger = logging.getLogger(__name__)
        if self.__logger.isEnabledFor(logging.DEBUG):
            if "Authorization" in requestHeaders:
                if requestHeaders["Authorization"].startswith("Basic"):
                    requestHeaders[
                        "Authorization"
                    ] = "Basic (login and password removed)"
                elif requestHeaders["Authorization"].startswith("token"):
                    requestHeaders["Authorization"] = "token (oauth token removed)"
                elif requestHeaders["Authorization"].startswith("Bearer"):
                    requestHeaders["Authorization"] = "Bearer (jwt removed)"
                else:  # pragma no cover (Cannot happen, but could if we add an authentication method => be prepared)
                    requestHeaders[
                        "Authorization"
                    ] = "(unknown auth removed)"  # pragma no cover (Cannot happen, but could if we add an authentication method => be prepared)
            self.__logger.debug(
                "%s %s://%s%s %s %s ==> %i %s %s",
                verb,
                self.__scheme,
                self.__hostname,
                url,
                requestHeaders,
                input,
                status,
                responseHeaders,
                output,
            )
