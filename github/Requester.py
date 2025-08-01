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
# Copyright 2016 Denis K <f1nal@cgaming.org>                                   #
# Copyright 2016 Jared K. Smith <jaredsmith@jaredsmith.net>                    #
# Copyright 2016 Mathieu Mitchell <mmitchell@iweb.com>                         #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Arda Kuyumcu <kuyumcuarda@gmail.com>                          #
# Copyright 2018 Dylan <djstein@ncsu.edu>                                      #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 R1kk3r <R1kk3r@users.noreply.github.com>                      #
# Copyright 2018 Shubham Singh <41840111+singh811@users.noreply.github.com>    #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Tuuu Nya <yuzesheji@qq.com>                                   #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Isac Souza <isouza@daitan.com>                                #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Jesse Li <jesse.li2002@gmail.com>                             #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Amador Pahim <apahim@redhat.com>                              #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Liuyang Wan <tsfdye@gmail.com>                                #
# Copyright 2023 Denis Blanchette <dblanchette@coveo.com>                      #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Heitor Polidoro <heitor.polidoro@gmail.com>                   #
# Copyright 2023 Hemslo Wang <hemslo.wang@gmail.com>                           #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Phillip Tran <phillip.qtr@gmail.com>                          #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 adosibalo <94008816+adosibalo@users.noreply.github.com>       #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Jonathan Kliem <jonathan.kliem@gmail.com>                     #
# Copyright 2024 Kobbi Gal <85439776+kgal-pan@users.noreply.github.com>        #
# Copyright 2024 Min RK <benjaminrk@gmail.com>                                 #
# Copyright 2025 Alec Ostrander <alec.ostrander@gmail.com>                     #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Jakub Smolar <jakub.smolar@scylladb.com>                      #
# Copyright 2025 Neel Malik <41765022+neel-m@users.noreply.github.com>         #
# Copyright 2025 Timothy Klopotoski <tklopotoski@ebsco.com>                    #
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

import io
import json
import logging
import mimetypes
import os
import re
import threading
import time
import urllib
import urllib.parse
from collections import deque
from datetime import datetime, timezone
from io import IOBase
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Callable,
    Deque,
    Generic,
    ItemsView,
    Iterator,
    TypeVar,
)

import requests
import requests.adapters
from urllib3 import Retry

import github.Consts as Consts
import github.GithubException
import github.GithubException as GithubException
from github.GithubObject import as_rest_api_attributes

if TYPE_CHECKING:
    from .AppAuthentication import AppAuthentication
    from .Auth import Auth
    from .GithubObject import GithubObject
    from .InstallationAuthorization import InstallationAuthorization

T = TypeVar("T")
T_gh = TypeVar("T_gh", bound="GithubObject")

# For App authentication, time remaining before token expiration to request a new one
ACCESS_TOKEN_REFRESH_THRESHOLD_SECONDS = 20


class RequestsResponse:
    # mimic the httplib response object
    def __init__(self, r: requests.Response):
        self.status = r.status_code
        self.headers = r.headers
        self.response = r

    def getheaders(self) -> ItemsView[str, str]:
        return self.headers.items()

    def read(self) -> str:
        return self.response.text

    def iter_content(self, chunk_size: int | None = 1) -> Iterator:
        return self.response.iter_content(chunk_size=chunk_size)

    def raise_for_status(self) -> None:
        self.response.raise_for_status()


class HTTPSRequestsConnectionClass:
    retry: int | Retry

    # mimic the httplib connection object
    def __init__(
        self,
        host: str,
        port: int | None = None,
        strict: bool = False,
        timeout: int | None = None,
        retry: int | Retry | None = None,
        pool_size: int | None = None,
        **kwargs: Any,
    ) -> None:
        self.port = port if port else 443
        self.host = host
        self.protocol = "https"
        self.timeout = timeout
        self.verify = kwargs.get("verify", True)
        self.session = requests.Session()
        # having Session.auth set something other than None disables falling back to .netrc file
        # https://github.com/psf/requests/blob/d63e94f552ebf77ccf45d97e5863ac46500fa2c7/src/requests/sessions.py#L480-L481
        # see https://github.com/PyGithub/PyGithub/pull/2703
        self.session.auth = Requester.noopAuth

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

    def request(
        self,
        verb: str,
        url: str,
        input: str | io.BufferedReader | None,
        headers: dict[str, str],
        stream: bool = False,
    ) -> None:
        self.verb = verb
        self.url = url
        self.input = input
        self.headers = headers
        self.stream = stream

    def getresponse(self) -> RequestsResponse:
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

    def close(self) -> None:
        self.session.close()


class HTTPRequestsConnectionClass:
    # mimic the httplib connection object
    def __init__(
        self,
        host: str,
        port: int | None = None,
        strict: bool = False,
        timeout: int | None = None,
        retry: int | Retry | None = None,
        pool_size: int | None = None,
        **kwargs: Any,
    ):
        self.port = port if port else 80
        self.host = host
        self.protocol = "http"
        self.timeout = timeout
        self.verify = kwargs.get("verify", True)
        self.session = requests.Session()
        # having Session.auth set something other than None disables falling back to .netrc file
        # https://github.com/psf/requests/blob/d63e94f552ebf77ccf45d97e5863ac46500fa2c7/src/requests/sessions.py#L480-L481
        # see https://github.com/PyGithub/PyGithub/pull/2703
        self.session.auth = Requester.noopAuth

        if retry is None:
            self.retry = requests.adapters.DEFAULT_RETRIES
        else:
            self.retry = retry  # type: ignore

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

    def request(self, verb: str, url: str, input: None, headers: dict[str, str], stream: bool = False) -> None:
        self.verb = verb
        self.url = url
        self.input = input
        self.headers = headers
        self.stream = stream

    def getresponse(self) -> RequestsResponse:
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

    def close(self) -> None:
        self.session.close()


class Requester:
    __installation_authorization: InstallationAuthorization | None
    __app_auth: AppAuthentication | None

    __httpConnectionClass = HTTPRequestsConnectionClass
    __httpsConnectionClass = HTTPSRequestsConnectionClass
    __persist = True
    __logger: logging.Logger | None = None

    _frameBuffer: list[Any]

    @staticmethod
    def noopAuth(request: requests.models.PreparedRequest) -> requests.models.PreparedRequest:
        return request

    @classmethod
    def injectConnectionClasses(
        cls,
        httpConnectionClass: type[HTTPRequestsConnectionClass],
        httpsConnectionClass: type[HTTPSRequestsConnectionClass],
    ) -> None:
        cls.__persist = False
        cls.__httpConnectionClass = httpConnectionClass
        cls.__httpsConnectionClass = httpsConnectionClass

    @classmethod
    def resetConnectionClasses(cls) -> None:
        cls.__persist = True
        cls.__httpConnectionClass = HTTPRequestsConnectionClass
        cls.__httpsConnectionClass = HTTPSRequestsConnectionClass

    @classmethod
    def injectLogger(cls, logger: logging.Logger) -> None:
        cls.__logger = logger

    @classmethod
    def resetLogger(cls) -> None:
        cls.__logger = None

    #############################################################
    # For Debug
    @classmethod
    def setDebugFlag(cls, flag: bool) -> None:
        cls.DEBUG_FLAG = flag

    @classmethod
    def setOnCheckMe(cls, onCheckMe: Callable) -> None:
        cls.ON_CHECK_ME = onCheckMe

    DEBUG_FLAG = False

    DEBUG_FRAME_BUFFER_SIZE = 1024

    DEBUG_HEADER_KEY = "DEBUG_FRAME"

    ON_CHECK_ME: Callable | None = None

    def NEW_DEBUG_FRAME(self, requestHeader: dict[str, str]) -> None:
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

    def DEBUG_ON_RESPONSE(self, statusCode: int, responseHeader: dict[str, str | int], data: str) -> None:
        """
        Update current frame with response Current frame index will be attached to responseHeader.
        """
        if self.DEBUG_FLAG:  # pragma no branch (Flag always set in tests)
            self._frameBuffer[self._frameCount][1:4] = [
                statusCode,
                responseHeader,
                data,
            ]
            responseHeader[self.DEBUG_HEADER_KEY] = self._frameCount

    def check_me(self, obj: GithubObject) -> None:
        if self.DEBUG_FLAG and self.ON_CHECK_ME is not None:  # pragma no branch (Flag always set in tests)
            frame = None
            if self.DEBUG_HEADER_KEY in obj._headers:
                frame_index = obj._headers[self.DEBUG_HEADER_KEY]
                frame = self._frameBuffer[frame_index]  # type: ignore
            self.ON_CHECK_ME(obj, frame)

    def _initializeDebugFeature(self) -> None:
        self._frameCount = 0
        self._frameBuffer = []

    #############################################################

    _frameCount: int
    __connectionClass: type[HTTPRequestsConnectionClass] | type[HTTPSRequestsConnectionClass]
    __hostname: str
    __authorizationHeader: str | None
    __seconds_between_requests: float | None
    __seconds_between_writes: float | None

    # keep arguments in-sync with github.MainClass and GithubIntegration
    def __init__(
        self,
        auth: Auth | None,
        base_url: str,
        timeout: int,
        user_agent: str,
        per_page: int,
        verify: bool | str,
        retry: int | Retry | None,
        pool_size: int | None,
        seconds_between_requests: float | None = None,
        seconds_between_writes: float | None = None,
        lazy: bool = False,
    ):
        self._initializeDebugFeature()

        self.__auth = auth
        self.__base_url = base_url

        o = urllib.parse.urlparse(base_url)
        self.__graphql_prefix = self.get_graphql_prefix(o.path)
        self.__graphql_url = urllib.parse.urlunparse(o._replace(path=self.__graphql_prefix))
        self.__hostname = o.hostname  # type: ignore
        self.__port = o.port
        self.__prefix = o.path
        self.__timeout = timeout
        self.__retry = retry  # NOTE: retry can be either int or an urllib3 Retry object
        self.__pool_size = pool_size
        self.__seconds_between_requests = seconds_between_requests
        self.__seconds_between_writes = seconds_between_writes
        self.__last_requests: dict[str, float] = dict()
        self.__scheme = o.scheme
        if o.scheme == "https":
            self.__connectionClass = self.__httpsConnectionClass
        elif o.scheme == "http":
            self.__connectionClass = self.__httpConnectionClass
        else:
            assert False, "Unknown URL scheme"
        self.__connection: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None
        self.__connection_lock = threading.Lock()
        self.__custom_connections: Deque[HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass] = deque()
        self.rate_limiting = (-1, -1)
        self.rate_limiting_resettime = 0
        self.FIX_REPO_GET_GIT_REF = True
        self.per_page = per_page

        self.oauth_scopes = None

        assert user_agent is not None, (
            "github now requires a user-agent. "
            "See https://docs.github.com/en/rest/overview/resources-in-the-rest-api#user-agent-required"
        )
        self.__userAgent = user_agent
        self.__verify = verify
        self.__lazy = lazy

        self.__installation_authorization = None

        # provide auth implementations that require a requester with this requester
        if isinstance(self.__auth, WithRequester):
            self.__auth.withRequester(self)

    def __getstate__(self) -> dict[str, Any]:
        state = self.__dict__.copy()
        # __connection_lock is not picklable
        del state["_Requester__connection_lock"]
        # __connection is not usable on remote, so ignore it
        del state["_Requester__connection"]
        # __custom_connections is not usable on remote, so ignore it
        del state["_Requester__custom_connections"]
        return state

    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__dict__.update(state)
        self.__connection_lock = threading.Lock()
        self.__connection = None
        self.__custom_connections = deque()

    @staticmethod
    # replace with str.removesuffix once support for Python 3.8 is dropped
    def remove_suffix(string: str, suffix: str) -> str:
        if string.endswith(suffix):
            return string[: -len(suffix)]
        return string

    @staticmethod
    def get_graphql_prefix(path: str | None) -> str:
        if path is None or path in ["", "/"]:
            path = ""
        if path.endswith(("/v3", "/v3/")):
            path = Requester.remove_suffix(path, "/")
            path = Requester.remove_suffix(path, "/v3")
        return path + "/graphql"

    @staticmethod
    def get_parameters_of_url(url: str) -> dict[str, list]:
        query = urllib.parse.urlparse(url)[4]
        return urllib.parse.parse_qs(query)

    @staticmethod
    def add_parameters_to_url(
        url: str,
        parameters: dict[str, Any],
    ) -> str:
        scheme, netloc, url, params, query, fragment = urllib.parse.urlparse(url)
        url_params = urllib.parse.parse_qs(query)
        # union parameters in url with given parameters, the latter have precedence
        url_params.update(**{k: v if isinstance(v, list) else [v] for k, v in parameters.items()})
        parameter_list = [(key, value) for key, values in url_params.items() for value in values]
        # remove query from url
        url = urllib.parse.urlunparse((scheme, netloc, url, params, "", fragment))

        if len(parameter_list) == 0:
            return url
        else:
            return f"{url}?{urllib.parse.urlencode(parameter_list)}"

    def close(self) -> None:
        """
        Close the connection to the server.
        """
        with self.__connection_lock:
            if self.__connection is not None:
                self.__connection.close()
                self.__connection = None
        while self.__custom_connections:
            self.__custom_connections.popleft().close()

    @property
    def kwargs(self) -> dict[str, Any]:
        """
        Returns arguments required to recreate this Requester with Requester.__init__, as well as with
        MainClass.__init__ and GithubIntegration.__init__.
        """
        return dict(
            auth=self.__auth,
            base_url=self.__base_url,
            timeout=self.__timeout,
            user_agent=self.__userAgent,
            per_page=self.per_page,
            verify=self.__verify,
            retry=self.__retry,
            pool_size=self.__pool_size,
            seconds_between_requests=self.__seconds_between_requests,
            seconds_between_writes=self.__seconds_between_writes,
            lazy=self.__lazy,
        )

    @property
    def base_url(self) -> str:
        return self.__base_url

    @property
    def graphql_url(self) -> str:
        return self.__graphql_url

    @property
    def scheme(self) -> str:
        return self.__scheme

    @property
    def hostname(self) -> str:
        return self.__hostname

    @property
    def hostname_and_port(self) -> str:
        if self.__port is None:
            return self.hostname
        return f"{self.hostname}:{self.__port}"

    @property
    def auth(self) -> Auth | None:
        return self.__auth

    def withAuth(self, auth: Auth | None) -> Requester:
        """
        Create a new requester instance with identical configuration but the given authentication method.

        :param auth: authentication method
        :return: new Requester instance

        """
        kwargs = self.kwargs
        kwargs.update(auth=auth)
        return Requester(**kwargs)

    @property
    def is_lazy(self) -> bool:
        return self.__lazy

    @property
    def is_not_lazy(self) -> bool:
        return not self.__lazy

    def withLazy(self, lazy: bool) -> Requester:
        """
        Create a new requester instance with identical configuration but the given lazy setting.

        :param lazy: completable objects created from this instance are lazy, as well as completable objects created
            from those, and so on
        :return: new Requester instance

        """
        kwargs = self.kwargs
        kwargs.update(lazy=lazy)
        return Requester(**kwargs)

    def requestJsonAndCheck(
        self,
        verb: str,
        url: str,
        parameters: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        input: Any | None = None,
        follow_302_redirect: bool = False,
    ) -> tuple[dict[str, Any], Any]:
        """
        Send a request with JSON body.

        :param input: request body, serialized to JSON if specified

        :return: ``(headers: dict, JSON Response: Any)``
        :raises: :class:`GithubException` for error status codes

        """
        return self.__check(
            *self.requestJson(
                verb,
                url,
                parameters,
                headers,
                input,
                self.__customConnection(url),
                follow_302_redirect=follow_302_redirect,
            )
        )

    def requestMultipartAndCheck(
        self,
        verb: str,
        url: str,
        parameters: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        input: dict[str, str] | None = None,
    ) -> tuple[dict[str, Any], dict[str, Any] | None]:
        """
        Send a request with multi-part-encoded body.

        :param input: request body, will be multi-part encoded if specified

        :return: ``(headers: dict, JSON Response: Any)``
        :raises: :class:`GithubException` for error status codes

        """
        return self.__check(*self.requestMultipart(verb, url, parameters, headers, input, self.__customConnection(url)))

    def requestBlobAndCheck(
        self,
        verb: str,
        url: str,
        parameters: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        input: str | None = None,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        Send a request with a file for the body.

        :param input: path to a file to use for the request body

        :return: ``(headers: dict, JSON Response: Any)``
        :raises: :class:`GithubException` for error status codes

        """
        return self.__check(*self.requestBlob(verb, url, parameters, headers, input, self.__customConnection(url)))

    def graphql_query(self, query: str, variables: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_
        """
        input_ = {"query": query, "variables": variables}

        response_headers, data = self.requestJsonAndCheck("POST", self.graphql_url, input=input_)
        if "errors" in data:
            if len(data["errors"]) == 1:
                error = data["errors"][0]
                if error.get("type") == "NOT_FOUND":
                    raise github.UnknownObjectException(404, data, response_headers, error.get("message"))
            raise self.createException(400, response_headers, data)
        return response_headers, data

    @classmethod
    def paths_of_dict(cls, d: dict) -> dict:
        return {key: cls.paths_of_dict(val) if isinstance(val, dict) else None for key, val in d.items()}

    def data_as_class(
        self, headers: dict[str, Any], data: dict[str, Any], data_path: list[str], klass: type[T_gh]
    ) -> T_gh:
        for item in data_path:
            if item not in data:
                raise RuntimeError(f"GraphQL path {data_path} not found in data: {self.paths_of_dict(data)}")
            data = data[item]
        if klass.is_rest():
            data = as_rest_api_attributes(data)
        return klass(self, headers, data)

    def graphql_node(self, node_id: str, graphql_schema: str, node_type: str) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_
        """
        if not graphql_schema.startswith("\n"):
            graphql_schema = f" {graphql_schema} "
        query = (
            """
            query Q($id: ID!) {
              node(id: $id) {
                __typename
                ... on """
            + f"{node_type} {{{graphql_schema}}}"
            + """
              }
            }
            """
        )

        headers, data = self.graphql_query(query, {"id": node_id})
        actual_node_type = data.get("data", {}).get("node", {}).get("__typename", node_type)
        if actual_node_type != node_type:
            raise github.GithubException(
                400,
                data,
                message=f"Retrieved {node_type} object is of different type: {actual_node_type}",
            )
        return headers, data

    def graphql_node_class(
        self, node_id: str, graphql_schema: str, klass: type[T_gh], node_type: str | None = None
    ) -> T_gh:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_
        """
        if node_type is None:
            node_type = klass.__name__

        headers, data = self.graphql_node(node_id, graphql_schema, node_type)
        return self.data_as_class(headers, data, ["data", "node"], klass)

    def graphql_query_class(
        self, query: str, variables: dict[str, Any], data_path: list[str], klass: type[T_gh]
    ) -> T_gh:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_
        """
        headers, data = self.graphql_query(query, variables)
        return self.data_as_class(headers, data, ["data"] + data_path, klass)

    def graphql_named_mutation(
        self, mutation_name: str, mutation_input: dict[str, Any], output_schema: str
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        Create a mutation in the format:
            mutation Mutation($input: MutationNameInput!) {
                mutationName(input: $input) { <output_schema> }
            }
        and call the self.graphql_query method.

        Returns the response data according to given output schema.
        """
        mutation_input_name = mutation_name[:1].upper() + mutation_name[1:] + "Input!"
        query = f"mutation Mutation($input: {mutation_input_name}) {{ {mutation_name}(input: $input) {{ {output_schema} }} }}"
        headers, data = self.graphql_query(query, {"input": mutation_input})
        return headers, data.get("data", {}).get(mutation_name, {})

    def graphql_named_mutation_class(
        self, mutation_name: str, mutation_input: dict[str, Any], output_schema: str, item: str, klass: type[T_gh]
    ) -> T_gh:
        """
        Executes a mutation and returns the output object as the given GithubObject.

        See {@link graphql_named_mutation}.

        """
        headers, data = self.graphql_named_mutation(mutation_name, mutation_input, output_schema)
        return self.data_as_class(headers, data, [item], klass)

    def __check(
        self,
        status: int,
        responseHeaders: dict[str, Any],
        output: str,
    ) -> tuple[dict[str, Any], Any]:
        data = self.__structuredFromJson(output)
        if status >= 400:
            raise self.createException(status, responseHeaders, data)
        return responseHeaders, data

    def __customConnection(self, url: str) -> HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None:
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None
        if not url.startswith("/"):
            o = urllib.parse.urlparse(url)
            if (
                o.hostname != self.__hostname
                or (o.port and o.port != self.__port)
                or (o.scheme != self.__scheme and not (o.scheme == "https" and self.__scheme == "http"))
            ):  # issue80
                if o.scheme == "http":
                    cnx = self.__httpConnectionClass(
                        o.hostname,  # type: ignore
                        o.port,
                        retry=self.__retry,
                        pool_size=self.__pool_size,
                    )
                    self.__custom_connections.append(cnx)
                elif o.scheme == "https":
                    cnx = self.__httpsConnectionClass(
                        o.hostname,  # type: ignore
                        o.port,
                        retry=self.__retry,
                        pool_size=self.__pool_size,
                    )
                    self.__custom_connections.append(cnx)
        return cnx

    @classmethod
    def createException(
        cls,
        status: int,
        headers: dict[str, Any],
        output: dict[str, Any],
    ) -> GithubException.GithubException:
        message = output.get("message") if output else None
        lc_message = message.lower() if message else ""

        msg = None
        exc = GithubException.GithubException
        if status == 401 and lc_message == "bad credentials":
            exc = GithubException.BadCredentialsException
        elif status == 401 and Consts.headerOTP in headers and re.match(r".*required.*", headers[Consts.headerOTP]):
            exc = GithubException.TwoFactorException
        elif status == 403 and lc_message.startswith("missing or invalid user agent string"):
            exc = GithubException.BadUserAgentException
        elif status == 403 and cls.isRateLimitError(lc_message):
            exc = GithubException.RateLimitExceededException
        elif status == 404 and ("not found" in lc_message or "no object found" in lc_message):
            exc = GithubException.UnknownObjectException
            if lc_message != "not found":
                msg = message
        else:
            # for general GithubException, provide the actual message
            msg = message

        return exc(status, output, headers, msg)

    @classmethod
    def isRateLimitError(cls, message: str) -> bool:
        return cls.isPrimaryRateLimitError(message) or cls.isSecondaryRateLimitError(message)

    @classmethod
    def isPrimaryRateLimitError(cls, message: str) -> bool:
        if not message:
            return False

        message = message.lower()
        return message.startswith("api rate limit exceeded")

    @classmethod
    def isSecondaryRateLimitError(cls, message: str) -> bool:
        if not message:
            return False

        message = message.lower()
        return (
            message.startswith("you have exceeded a secondary rate limit")
            or message.endswith("please retry your request again later.")
            or message.endswith("please wait a few minutes before you try again.")
        )

    def __structuredFromJson(self, data: str) -> Any:
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

    def getFile(
        self,
        url: str,
        path: str,
        parameters: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None,
        chunk_size: int | None | None = 1,
    ) -> None:
        """
        GET a file from the server and save it to the given path, which includes the filename.
        """
        _, _, stream_chunk_iterator = self.getStream(url, parameters, headers, cnx, chunk_size=chunk_size)
        with open(path, "wb") as f:
            for chunk in stream_chunk_iterator:
                if chunk:
                    f.write(chunk)

    def getStream(
        self,
        url: str,
        parameters: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None,
        chunk_size: int | None | None = 1,
    ) -> tuple[int, dict[str, Any], Iterator]:
        """
        GET a stream from the server.

        :returns:``(status, headers, stream_chunk_iterator)``

        """
        if headers is None:
            headers = {}
        headers["Accept"] = "application/octet-stream"

        def encode(_: Any) -> tuple[str, str]:
            return "", ""

        status, responseHeaders, output = self.__requestEncode(
            cnx, "GET", url, parameters, headers, None, encode, stream=True, follow_302_redirect=True
        )
        if isinstance(output, RequestsResponse) or (
            hasattr(output, "iter_content") and hasattr(output, "raise_for_status")
        ):
            output.raise_for_status()
            return status, responseHeaders, output.iter_content(chunk_size=chunk_size)
        raise TypeError(f"Expected a RequestsResponse object: {type(output)}")

    def requestJson(
        self,
        verb: str,
        url: str,
        parameters: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        input: Any | None = None,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None,
        follow_302_redirect: bool = False,
    ) -> tuple[int, dict[str, Any], str]:
        """
        Send a request with JSON input.

        :param input: request body, will be serialized as JSON
        :returns:``(status, headers, body)``

        """

        def encode(input: Any) -> tuple[str, str]:
            return "application/json", json.dumps(input)

        status, responseHeaders, output = self.__requestEncode(
            cnx, verb, url, parameters, headers, input, encode, follow_302_redirect=follow_302_redirect
        )
        if isinstance(output, str):
            return status, responseHeaders, output
        raise ValueError("requestJson() Expected a str, should never happen")

    def requestMultipart(
        self,
        verb: str,
        url: str,
        parameters: dict[str, Any] | None = None,
        headers: dict[str, Any] | None = None,
        input: dict[str, str] | None = None,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None,
    ) -> tuple[int, dict[str, Any], str]:
        """
        Send a request with multi-part encoding.

        :param input: request body, will be serialized as multipart form data
        :returns:``(status, headers, body)``

        """

        def encode(input: dict[str, Any]) -> tuple[str, str]:
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

        status, responseHeaders, output = self.__requestEncode(cnx, verb, url, parameters, headers, input, encode)
        if isinstance(output, str):
            return status, responseHeaders, output
        raise ValueError("requestMultipart() Expected a str, should never happen")

    def requestBlob(
        self,
        verb: str,
        url: str,
        parameters: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        input: str | None = None,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None,
    ) -> tuple[int, dict[str, Any], str]:
        """
        Send a request with a file as request body.

        :param input: path to a local file to use for request body
        :returns:``(status, headers, body)``

        """
        if headers is None:
            headers = {}

        def encode(local_path: str) -> tuple[str, Any]:
            if "Content-Type" in headers:  # type: ignore
                mime_type = headers["Content-Type"]  # type: ignore
            else:
                guessed_type = mimetypes.guess_type(local_path)
                mime_type = guessed_type[0] if guessed_type[0] is not None else Consts.defaultMediaType
            f = open(local_path, "rb")
            return mime_type, f

        if input:
            headers["Content-Length"] = str(os.path.getsize(input))

        status, responseHeaders, output = self.__requestEncode(cnx, verb, url, parameters, headers, input, encode)
        if isinstance(output, str):
            return status, responseHeaders, output
        raise ValueError("requestBlob() Expected a str, should never happen")

    def requestMemoryBlobAndCheck(
        self,
        verb: str,
        url: str,
        parameters: Any,
        headers: dict[str, Any],
        file_like: BinaryIO,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None = None,
    ) -> tuple[dict[str, Any], Any]:
        """
        Send a request with a binary file-like for the body.

        :param file_like: file-like object to use for the request body
        :return: ``(headers: dict, JSON Response: Any)``
        :raises: :class:`GithubException` for error status codes

        """

        # The expected signature of encode means that the argument is ignored.
        def encode(_: Any) -> tuple[str, Any]:
            return headers["Content-Type"], file_like

        if not cnx:
            cnx = self.__customConnection(url)

        status, responseHeaders, output = self.__requestEncode(cnx, verb, url, parameters, headers, file_like, encode)
        if isinstance(output, str):
            return self.__check(status, responseHeaders, output)
        raise ValueError("requestMemoryBlobAndCheck() Expected a str, should never happen")

    def __requestEncode(
        self,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None,
        verb: str,
        url: str,
        parameters: dict[str, str] | None,
        requestHeaders: dict[str, str] | None,
        input: T | None,
        encode: Callable[[T], tuple[str, Any]],
        stream: bool = False,
        follow_302_redirect: bool = False,
    ) -> tuple[int, dict[str, Any], str | object]:
        assert verb in ["HEAD", "GET", "POST", "PATCH", "PUT", "DELETE"]
        if parameters is None:
            parameters = {}
        if requestHeaders is None:
            requestHeaders = {}

        if self.__auth is not None:
            self.__auth.authentication(requestHeaders)
        requestHeaders["User-Agent"] = self.__userAgent

        url = self.__makeAbsoluteUrl(url)
        url = Requester.add_parameters_to_url(url, parameters)

        encoded_input = None
        if input is not None:
            requestHeaders["Content-Type"], encoded_input = encode(input)

        self.NEW_DEBUG_FRAME(requestHeaders)

        status, responseHeaders, output = self.__requestRaw(
            cnx, verb, url, requestHeaders, encoded_input, stream=stream, follow_302_redirect=follow_302_redirect
        )

        if Consts.headerRateRemaining in responseHeaders and Consts.headerRateLimit in responseHeaders:
            self.rate_limiting = (
                # ints expected but sometimes floats returned: https://github.com/PyGithub/PyGithub/pull/2697
                int(float(responseHeaders[Consts.headerRateRemaining])),
                int(float(responseHeaders[Consts.headerRateLimit])),
            )
        if Consts.headerRateReset in responseHeaders:
            # ints expected but sometimes floats returned: https://github.com/PyGithub/PyGithub/pull/2697
            self.rate_limiting_resettime = int(float(responseHeaders[Consts.headerRateReset]))

        if Consts.headerOAuthScopes in responseHeaders:
            self.oauth_scopes = responseHeaders[Consts.headerOAuthScopes].split(", ")

        self.DEBUG_ON_RESPONSE(status, responseHeaders, output if isinstance(output, str) else "stream")

        return status, responseHeaders, output

    def __requestRaw(
        self,
        cnx: HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass | None,
        verb: str,
        url: str,
        requestHeaders: dict[str, str],
        input: Any | None,
        stream: bool = False,
        follow_302_redirect: bool = False,
    ) -> tuple[int, dict[str, Any], str | object]:
        self.__deferRequest(verb)

        try:
            original_cnx = cnx
            if cnx is None:
                cnx = self.__createConnection()
            cnx.request(verb, url, input, requestHeaders, stream)
            response = cnx.getresponse()
            output = response if stream else response.read()
            status = response.status
            responseHeaders = {k.lower(): v for k, v in response.getheaders()}

            if input:
                if isinstance(input, IOBase):
                    input.close()

            self.__log(verb, url, requestHeaders, input, status, responseHeaders, output)

            if status == 202 and (
                verb == "GET" or verb == "HEAD"
            ):  # only for requests that are considered 'safe' in RFC 2616
                time.sleep(Consts.PROCESSING_202_WAIT_TIME)
                return self.__requestRaw(original_cnx, verb, url, requestHeaders, input, stream=stream)

            if status == 301 and "location" in responseHeaders:
                location = responseHeaders["location"]
                o = urllib.parse.urlparse(location)
                if o.scheme != self.__scheme:
                    raise RuntimeError(
                        f"Github server redirected from {self.__scheme} protocol to {o.scheme}, "
                        f"please correct your Github server URL via base_url: Github(base_url=...)"
                    )
                if o.hostname != self.__hostname:
                    raise RuntimeError(
                        f"Github server redirected from host {self.__hostname} to {o.hostname}, "
                        f"please correct your Github server URL via base_url: Github(base_url=...)"
                    )
                if o.path == url:
                    port = ":" + str(self.__port) if self.__port is not None else ""
                    requested_location = f"{self.__scheme}://{self.__hostname}{port}{url}"
                    raise RuntimeError(
                        f"Requested {requested_location} but server redirected to {location}, "
                        f"you may need to correct your Github server URL "
                        f"via base_url: Github(base_url=...)"
                    )
                if self._logger.isEnabledFor(logging.INFO):
                    self._logger.info(f"Following Github server redirection from {url} to {o.path}")
                return self.__requestRaw(original_cnx, verb, o.path, requestHeaders, input, stream=stream)
            if status == 302 and follow_302_redirect and "location" in responseHeaders:
                location = responseHeaders["location"]
                o = urllib.parse.urlparse(location)
                cnx = self.__customConnection(location)
                path = self.__makeAbsoluteUrl(location)
                if self._logger.isEnabledFor(logging.DEBUG):
                    self._logger.debug(f"Following Github server redirection (302) from {url} to {o.path}")
                # remove auth to not leak authentication to redirection location
                if o.hostname != self.__hostname:
                    requestHeaders = {k: v for k, v in requestHeaders.items() if k != "Authorization"}
                return self.__requestRaw(
                    cnx, verb, path, requestHeaders, input, stream=stream, follow_302_redirect=True
                )
            return status, responseHeaders, output
        finally:
            # we record the time of this request after it finished
            # to defer next request starting from this request's end, not start
            self.__recordRequestTime(verb)

    def __deferRequest(self, verb: str) -> None:
        # Ensures at least self.__seconds_between_requests seconds have passed since any last request
        # and self.__seconds_between_writes seconds have passed since last write request (if verb refers to a write).
        # Uses self.__last_requests.
        requests = self.__last_requests.values()
        writes = [l for v, l in self.__last_requests.items() if v != "GET"]

        last_request = max(requests) if requests else 0
        last_write = max(writes) if writes else 0

        next_request = (last_request + self.__seconds_between_requests) if self.__seconds_between_requests else 0
        next_write = (last_write + self.__seconds_between_writes) if self.__seconds_between_writes else 0

        next = next_request if verb == "GET" else max(next_request, next_write)
        defer = max(next - datetime.now(timezone.utc).timestamp(), 0)
        if defer > 0:
            if self.__logger is None:
                self.__logger = logging.getLogger(__name__)
            self.__logger.debug(f"sleeping {defer}s before next GitHub request")
            time.sleep(defer)

    def __recordRequestTime(self, verb: str) -> None:
        # Updates self.__last_requests with current timestamp for given verb
        self.__last_requests[verb] = datetime.now(timezone.utc).timestamp()

    def __makeAbsoluteUrl(self, url: str) -> str:
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
                "objects.githubusercontent.com",
            ], o.hostname
            assert o.path.startswith((self.__prefix, self.__graphql_prefix, "/api/", "/login/oauth")), o.path
            assert o.port == self.__port, o.port
            url = o.path
            if o.query != "":
                url += f"?{o.query}"
        return url

    def __createConnection(
        self, hostname: str | None = None
    ) -> HTTPRequestsConnectionClass | HTTPSRequestsConnectionClass:
        if self.__persist and self.__connection is not None and hostname is not None and hostname == self.__hostname:
            return self.__connection

        with self.__connection_lock:
            if self.__connection is not None and hostname is not None and hostname == self.__hostname:
                if self.__persist:
                    return self.__connection
            if self.__connection is not None:
                self.__connection.close()
                self.__connection = None
            self.__connection = self.__connectionClass(
                hostname if hostname is not None else self.__hostname,
                self.__port,
                retry=self.__retry,
                pool_size=self.__pool_size,
                timeout=self.__timeout,
                verify=self.__verify,
            )

        return self.__connection

    @property
    def _logger(self) -> logging.Logger:
        if self.__logger is None:
            self.__logger = logging.getLogger(__name__)
        return self.__logger

    def __log(
        self,
        verb: str,
        url: str,
        requestHeaders: dict[str, str],
        input: Any | None,
        status: int | None,
        responseHeaders: dict[str, Any],
        output: str | object | None,
    ) -> None:
        if self._logger.isEnabledFor(logging.DEBUG):
            headersForRequest = requestHeaders.copy()
            if self.__auth:
                self.__auth.mask_authentication(headersForRequest)
            self._logger.debug(
                "%s %s://%s%s %s %s ==> %i %s %s",
                verb,
                self.__scheme,
                self.__hostname,
                url,
                headersForRequest,
                input,
                status,
                responseHeaders,
                output if isinstance(output, str) else "stream",
            )


class WithRequester(Generic[T]):
    """
    Mixin class that allows to set a requester.
    """

    __requester: Requester

    def __init__(self) -> None:
        self.__requester: Requester | None = None  # type: ignore

    @property
    def requester(self) -> Requester:
        return self.__requester

    def withRequester(self, requester: Requester) -> WithRequester[T]:
        assert isinstance(requester, Requester), requester
        self.__requester = requester
        return self
