############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Cameron White <cawhite@pdx.edu>                               #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2016 humbug <bah>                                                  #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Liuyang Wan <tsfdye@gmail.com>                                #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

import json
from typing import Any


class GithubException(Exception):
    """
    Error handling in PyGithub is done with exceptions. This class is the base of all exceptions raised by PyGithub
    (but :class:`github.GithubException.BadAttributeException`).

    Some other types of exceptions might be raised by underlying libraries, for example for network-related issues.

    """

    def __init__(
        self,
        status: int,
        data: Any = None,
        headers: dict[str, str] | None = None,
        message: str | None = None,
    ):
        super().__init__()
        self.__status = status
        self.__data = data
        self.__headers = headers
        self.__message = message
        self.args = (status, data, headers, message)

    @property
    def message(self) -> str | None:
        return self.__message

    @property
    def status(self) -> int:
        """
        The status returned by the Github API.
        """
        return self.__status

    @property
    def data(self) -> Any:
        """
        The (decoded) data returned by the Github API.
        """
        return self.__data

    @property
    def headers(self) -> dict[str, str] | None:
        """
        The headers returned by the Github API.
        """
        return self.__headers

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__str__()})"

    def __str__(self) -> str:
        if self.__message:
            msg = f"{self.__message}: {self.status}"
        else:
            msg = f"{self.status}"

        if self.data is not None:
            msg += " " + json.dumps(self.data)

        return msg


class BadCredentialsException(GithubException):
    """
    Exception raised in case of bad credentials (when Github API replies with a 401 or 403 HTML status)
    """


class UnknownObjectException(GithubException):
    """
    Exception raised when a non-existing object is requested (when Github API replies with a 404 HTML status)
    """


class BadUserAgentException(GithubException):
    """
    Exception raised when request is sent with a bad user agent header (when Github API replies with a 403 bad user
    agent HTML status)
    """


class RateLimitExceededException(GithubException):
    """
    Exception raised when the rate limit is exceeded (when Github API replies with a 403 rate limit exceeded HTML
    status)
    """


class BadAttributeException(Exception):
    """
    Exception raised when Github returns an attribute with the wrong type.
    """

    def __init__(
        self,
        actualValue: Any,
        expectedType: (
            dict[tuple[type[str], type[str]], type[dict]]
            | tuple[type[str], type[str]]
            | list[type[dict]]
            | list[tuple[type[str], type[str]]]
        ),
        transformationException: Exception | None,
    ):
        self.__actualValue = actualValue
        self.__expectedType = expectedType
        self.__transformationException = transformationException

    @property
    def actual_value(self) -> Any:
        """
        The value returned by Github.
        """
        return self.__actualValue

    @property
    def expected_type(
        self,
    ) -> (
        list[type[dict]]
        | tuple[type[str], type[str]]
        | dict[tuple[type[str], type[str]], type[dict]]
        | list[tuple[type[str], type[str]]]
    ):
        """
        The type PyGithub expected.
        """
        return self.__expectedType

    @property
    def transformation_exception(self) -> Exception | None:
        """
        The exception raised when PyGithub tried to parse the value.
        """
        return self.__transformationException


class TwoFactorException(GithubException):
    """
    Exception raised when Github requires a onetime password for two-factor authentication.
    """


class IncompletableObject(GithubException):
    """
    Exception raised when we can not request an object from Github because the data returned did not include a URL.
    """
