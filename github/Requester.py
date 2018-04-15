# -*- coding: utf-8 -*-

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
import requests
import sys
import urllib
import urlparse
from io import IOBase

import Consts
import GithubException

atLeastPython3 = sys.hexversion >= 0x03000000


class RequestsResponse:
    # mimic the httplib response object
    def __init__(self, r):
        self.status = r.status_code
        self.headers = r.headers
        self.text = r.text

    def getheaders(self):
        if atLeastPython3:
            return self.headers.items()
        else:
            return self.headers.iteritems()

    def read(self):
        return self.text

class HTTPSRequestsConnectionClass(object):
    # mimic the httplib connection object
    def __init__(self, host, port=None, strict=False, timeout=None, **kwargs):
        self.port = port if port else 443
        self.host = host
        self.protocol = "https"
        self.timeout = timeout
        self.session = requests.Session()

    def request(self, verb, url, input, headers):
        self.verb = verb
        self.url = url
        self.input = input
        self.headers = headers

    def getresponse(self):
        verb = getattr(self.session, self.verb.lower())
        url = "%s://%s:%s%s" % (self.protocol, self.host, self.port, self.url)
        r = verb(url, headers=self.headers, data=self.input, timeout=self.timeout)
        return RequestsResponse(r)

    def close(self):
        return


class HTTPRequestsConnectionClass(object):
    # mimic the httplib connection object
    def __init__(self, host, port=None, strict=False, timeout=None, **kwargs):
        self.port = port if port else 80
        self.host = host
        self.protocol = "http"
        self.timeout = timeout
        self.session = requests.Session()

    def request(self, verb, url, input, headers):
        self.verb = verb
        self.url = url
        self.input = input
        self.headers = headers

    def getresponse(self):
        verb = getattr(self.session, self.verb.lower())
        url = "%s://%s:%s%s" % (self.protocol, self.host, self.port, self.url)
        r = verb(url, headers=self.headers, data=self.input, timeout=self.timeout)
        return RequestsResponse(r)

    def close(self):
        return


class Requester:
    __httpConnectionClass = HTTPRequestsConnectionClass
    __httpsConnectionClass = HTTPSRequestsConnectionClass
    __connection = None
    __persist = True

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
            if self._frameCount < self.DEBUG_FRAME_BUFFER_SIZE - 1:  # pragma no branch (Should be covered)
                self._frameBuffer.append(new_frame)
            else:
                self._frameBuffer[0] = new_frame  # pragma no cover (Should be covered)

            self._frameCount = len(self._frameBuffer) - 1

    def DEBUG_ON_RESPONSE(self, statusCode, responseHeader, data):
        '''
        Update current frame with response
        Current frame index will be attached to responseHeader
        '''
        if self.DEBUG_FLAG:  # pragma no branch (Flag always set in tests)
            self._frameBuffer[self._frameCount][1:4] = [statusCode, responseHeader, data]
            responseHeader[self.DEBUG_HEADER_KEY] = self._frameCount

    def check_me(self, obj):
        if self.DEBUG_FLAG and self.ON_CHECK_ME is not None:  # pragma no branch (Flag always set in tests)
            frame = None
            if self.DEBUG_HEADER_KEY in obj._headers:
                frame_index = obj._headers[self.DEBUG_HEADER_KEY]
                frame = self._frameBuffer[frame_index]
            self.ON_CHECK_ME(obj, frame)

    def _initializeDebugFeature(self):
        self._frameCount = 0
        self._frameBuffer = []

    #############################################################

    def __init__(self, login_or_token, password, base_url, timeout, client_id, client_secret, user_agent, per_page, api_preview):
        self._initializeDebugFeature()

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
        self.rate_limiting = (-1, -1)
        self.rate_limiting_resettime = 0
        self.FIX_REPO_GET_GIT_REF = True
        self.per_page = per_page

        self.oauth_scopes = None

        self.__clientId = client_id
        self.__clientSecret = client_secret

        assert user_agent is not None, 'github now requires a user-agent. ' \
            'See http://developer.github.com/v3/#user-agent-required'
        self.__userAgent = user_agent
        self.__apiPreview = api_preview

    def requestJsonAndCheck(self, verb, url, parameters=None, headers=None, input=None, cnx=None):
        return self.__check(*self.requestJson(verb, url, parameters, headers, input, cnx))

    def requestMultipartAndCheck(self, verb, url, parameters=None, headers=None, input=None):
        return self.__check(*self.requestMultipart(verb, url, parameters, headers, input))

    def requestBlobAndCheck(self, verb, url, parameters=None, headers=None, input=None):
        o = urlparse.urlparse(url)
        self.__hostname = o.hostname
        return self.__check(*self.requestBlob(verb, url, parameters, headers, input))

    def __check(self, status, responseHeaders, output):
        output = self.__structuredFromJson(output)
        if status >= 400:
            raise self.__createException(status, responseHeaders, output)
        return responseHeaders, output

    def __createException(self, status, headers, output):
        if status == 401 and output.get("message") == "Bad credentials":
            cls = GithubException.BadCredentialsException
        elif status == 401 and 'x-github-otp' in headers and re.match(r'.*required.*', headers['x-github-otp']):
            cls = GithubException.TwoFactorException  # pragma no cover (Should be covered)
        elif status == 403 and output.get("message").startswith("Missing or invalid User Agent string"):
            cls = GithubException.BadUserAgentException
        elif status == 403 and output.get("message").lower().startswith("api rate limit exceeded"):
            cls = GithubException.RateLimitExceededException
        elif status == 404 and output.get("message") == "Not Found":
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
            try:
                return json.loads(data)
            except ValueError, e:
                return {'data': data}

    def requestJson(self, verb, url, parameters=None, headers=None, input=None, cnx=None):
        def encode(input):
            return "application/json", json.dumps(input)

        return self.__requestEncode(cnx, verb, url, parameters, headers, input, encode)

    def requestMultipart(self, verb, url, parameters=None, headers=None, input=None):
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

        return self.__requestEncode(None, verb, url, parameters, headers, input, encode)

    def requestBlob(self, verb, url, parameters={}, headers={}, input=None):
        def encode(local_path):
            if "Content-Type" in headers:
                mime_type = headers["Content-Type"]
            else:
                guessed_type = mimetypes.guess_type(input)
                mime_type = guessed_type[0] if guessed_type[0] is not None else "application/octet-stream"
            f = open(local_path, 'rb')
            return mime_type, f

        if input:
            headers["Content-Length"] = os.path.getsize(input)
        return self.__requestEncode(None, verb, url, parameters, headers, input, encode)

    def __requestEncode(self, cnx, verb, url, parameters, requestHeaders, input, encode):
        assert verb in ["HEAD", "GET", "POST", "PATCH", "PUT", "DELETE"]
        if parameters is None:
            parameters = dict()
        if requestHeaders is None:
            requestHeaders = dict()

        self.__authenticate(url, requestHeaders, parameters)
        requestHeaders["User-Agent"] = self.__userAgent
        if self.__apiPreview:
            requestHeaders["Accept"] = "application/vnd.github.moondragon+json"

        url = self.__makeAbsoluteUrl(url)
        url = self.__addParametersToUrl(url, parameters)

        encoded_input = None
        if input is not None:
            requestHeaders["Content-Type"], encoded_input = encode(input)

        self.NEW_DEBUG_FRAME(requestHeaders)

        status, responseHeaders, output = self.__requestRaw(cnx, verb, url, requestHeaders, encoded_input)

        if "x-ratelimit-remaining" in responseHeaders and "x-ratelimit-limit" in responseHeaders:
            self.rate_limiting = (int(responseHeaders["x-ratelimit-remaining"]), int(responseHeaders["x-ratelimit-limit"]))
        if "x-ratelimit-reset" in responseHeaders:
            self.rate_limiting_resettime = int(responseHeaders["x-ratelimit-reset"])

        if "x-oauth-scopes" in responseHeaders:
            self.oauth_scopes = responseHeaders["x-oauth-scopes"].split(", ")

        self.DEBUG_ON_RESPONSE(status, responseHeaders, output)

        return status, responseHeaders, output

    def __requestRaw(self, cnx, verb, url, requestHeaders, input):
        original_cnx = cnx
        if cnx is None:
            cnx = self.__createConnection()
        else:
            assert cnx == "status"
            cnx = self.__httpsConnectionClass("status.github.com", 443)
        cnx.request(
            verb,
            url,
            input,
            requestHeaders
        )
        response = cnx.getresponse()

        status = response.status
        responseHeaders = dict((k.lower(), v) for k, v in response.getheaders())
        output = response.read()

        cnx.close()
        if input:
            if isinstance(input, IOBase):
                input.close()

        self.__log(verb, url, requestHeaders, input, status, responseHeaders, output)

        if status == 301 and 'location' in responseHeaders:
            return self.__requestRaw(original_cnx, verb, responseHeaders['location'], requestHeaders, input)

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
            assert o.hostname in [self.__hostname, "uploads.github.com"], o.hostname
            assert o.path.startswith((self.__prefix, "/api/uploads"))
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
        kwds["timeout"] = self.__timeout

        if self.__persist and self.__connection is not None:
            return self.__connection

        self.__connection = self.__connectionClass(self.__hostname, self.__port, **kwds)

        return self.__connection

    def __log(self, verb, url, requestHeaders, input, status, responseHeaders, output):
        logger = logging.getLogger(__name__)
        if logger.isEnabledFor(logging.DEBUG):
            if "Authorization" in requestHeaders:
                if requestHeaders["Authorization"].startswith("Basic"):
                    requestHeaders["Authorization"] = "Basic (login and password removed)"
                elif requestHeaders["Authorization"].startswith("token"):
                    requestHeaders["Authorization"] = "token (oauth token removed)"
                else:  # pragma no cover (Cannot happen, but could if we add an authentication method => be prepared)
                    requestHeaders["Authorization"] = "(unknown auth removed)"  # pragma no cover (Cannot happen, but could if we add an authentication method => be prepared)
            logger.debug("%s %s://%s%s %s %s ==> %i %s %s", str(verb), self.__scheme, self.__hostname, str(url), str(requestHeaders), str(input), status, str(responseHeaders), str(output))
