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

    ### Possible Causes

    This exception is raised possibly because of:
    1. Insufficient scope of token
    2. An expired token. In an application with **cache** mechanism, the cached PyGithub-like objects might
    contain an expired token unexpectedly. ATTENTION: The PyGithub-like objects can not update the token
    automatically.
    3. A leaked token. Committing a token into your repo and pushing to github automatically invalidates the token.

    ### Expose the token in the logs

    Attention: This is for debugging purposes only, as this leaks the token into log files, which is a security risk.

    The best way to investigate the root cause is to show the actual token used to authenticate in the logs.
    Usually, the token is obfuscated for security reasons. Here we deliberately write the plain token to the logs,
    so that we can compare it with the expected token.
    
    1. Identify the location of the github source code installed via pip or virtual env:
    
    ```bash
    python -c "from github import Requester; print(Requester.__file__)"
    ```

    2. Edit this `github/Requester.py` file and replace in `def __log`:
    
    ```python
        elif requestHeaders["Authorization"].startswith("token"):
        headersForRequest["Authorization"] = "token (oauth token removed)"
    ```
    
    with
    
    ```python
        elif requestHeaders["Authorization"].startswith("token"):
            import hashlib
            token = requestHeaders["Authorization"][5:]
            token = hashlib.md5(token.encode('utf-8')).hexdigest()
            headersForRequest["Authorization"] = f"token ({token})"
    ```

    2. Insert `github.enable_console_debug_logging()` at the start of your program. You will see the token
    used for each call of the GitHub REST API. The output format as follows: 
    
    ```
    GET https://api.github.com/repos/totycro/stacs/branches/main {'Authorization': 'token (xxxx)', 'User-Agent': ...
    ```

    **CHECK whether the output token is expected**.

    ### Ways to fix

    If you find the token is unexpected, you can choose to
    1) Recreate the Github instance with a new token: `g = Github(auth=Auth.Token("access_token"))`
        and fetch the PyGithub objects again. (recommended)
    2) Renew the token in PyGithub objects by replacing the token with the newer one.
        For `Issue` and `Repository` got through github token,
        use `o._requester.auth._token = <new token str>` to renew objects.  (not recommended)

    See https://github.com/PyGithub/PyGithub/issues/1753 for more details.
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
