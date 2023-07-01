############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Enrico Minack <github@enrico.minack.dev>                      #
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
import logging
from datetime import datetime, timezone
from logging import Logger
from typing import Optional

from requests import Response
from requests.models import CaseInsensitiveDict
from requests.utils import get_encoding_from_headers
from urllib3 import HTTPResponse, Retry
from urllib3.exceptions import MaxRetryError

from github.GithubException import GithubException
from github.Requester import Requester

DEFAULT_SECONDARY_RATE_WAIT: int = 60


class GithubRetry(Retry):
    """
    A Github-specific implementation of `urllib3.Retry`

    This retries 403 responses if they are retry-able. Github requests are retry-able when
    the response provides a `"Retry-After"` header, or the content indicates a rate limit error.

    By default, response codes 403, and 500 up to 599 are retried. This can be configured
    via the `status_forcelist` argument.

    By default, all methods defined in `Retry.DEFAULT_ALLOWED_METHODS` are retried, plus GET and POST.
    This can be configured via the `allowed_methods` argument.
    """

    __logger: Optional[Logger] = None

    # used to mock datetime, mock.patch("github.GithubRetry.date") does not work as this
    # references the class, not the module (due to re-exporting in github/__init__.py)
    __datetime = datetime

    def __init__(
        self, secondary_rate_wait: float = DEFAULT_SECONDARY_RATE_WAIT, **kwargs
    ):
        """
        :param secondary_rate_wait: seconds to wait before retrying secondary rate limit errors
        :param kwargs: see urllib3.Retry for more arguments
        """
        self.secondary_rate_wait = secondary_rate_wait
        # 403 is too broad to be retried, but GitHub API signals rate limits via 403
        # we retry 403 and look into the response header via Retry.increment
        # to determine if we really retry that 403
        kwargs["status_forcelist"] = kwargs.get(
            "status_forcelist", list(range(500, 600))
        ) + [403]
        kwargs["allowed_methods"] = kwargs.get(
            "allowed_methods", Retry.DEFAULT_ALLOWED_METHODS.union({"GET", "POST"})
        )
        super().__init__(**kwargs)

    def new(self, **kw):
        kw.update(dict(secondary_rate_wait=self.secondary_rate_wait))
        return super().new(**kw)

    def increment(
        self,
        method=None,
        url=None,
        response=None,
        error=None,
        _pool=None,
        _stacktrace=None,
    ) -> Retry:
        if response:
            # we retry 403 only when there is a Retry-After header (indicating it is retry-able)
            # or the body message does imply a rate limit error
            if response.status == 403:
                self.__log(
                    logging.INFO,
                    f"Request {method} {url} failed with {response.status}: {response.reason}",
                )
                if "Retry-After" in response.headers:
                    # Sleeping 'Retry-After' seconds is implemented in urllib3.Retry.sleep() and called by urllib3
                    self.__log(
                        logging.INFO,
                        f'Retrying after {response.headers.get("Retry-After")} seconds',
                    )
                else:
                    content = response.reason

                    # to identify retry-able methods, we inspect the response body
                    try:
                        content = self.get_content(response, url)
                        content = json.loads(content)
                        message = content.get("message")

                        if Requester.isRateLimitError(message):
                            rate_type = (
                                "primary"
                                if Requester.isPrimaryRateLimitError(message)
                                else "secondary"
                            )
                            self.__log(
                                logging.DEBUG,
                                f"Response body indicates retry-able {rate_type} rate limit error: {message}",
                            )

                            # check early that we are retrying at all
                            retry = super().increment(
                                method, url, response, error, _pool, _stacktrace
                            )

                            # we backoff primary rate limit at least until X-RateLimit-Reset,
                            # we backoff secondary rate limit at for secondary_rate_wait seconds
                            backoff = 0.0

                            if Requester.isPrimaryRateLimitError(message):
                                if "X-RateLimit-Reset" in response.headers:
                                    value = response.headers.get("X-RateLimit-Reset")
                                    if value and value.isdigit():
                                        reset = self.__datetime.utcfromtimestamp(
                                            int(value)
                                        )
                                        delta = reset - self.__datetime.now(
                                            timezone.utc
                                        )
                                        resetBackoff = delta.total_seconds()

                                        if resetBackoff > 0:
                                            self.__log(
                                                logging.DEBUG,
                                                f"Reset occurs in {str(delta)} ({value} / {reset})",
                                            )

                                        # plus 1s as it is not clear when in that second the reset occurs
                                        backoff = resetBackoff + 1
                            else:
                                backoff = self.secondary_rate_wait

                            # we backoff at least retry's next backoff
                            retry_backoff = retry.get_backoff_time()
                            if retry_backoff > backoff:
                                if backoff > 0:
                                    self.__log(
                                        logging.DEBUG,
                                        f"Retry backoff of {retry_backoff}s exceeds "
                                        f"required rate limit backoff of {backoff}s".replace(
                                            ".0s", "s"
                                        ),
                                    )
                                backoff = retry_backoff

                            def get_backoff_time():
                                return backoff

                            self.__log(
                                logging.INFO,
                                f"Setting next backoff to {backoff}s".replace(
                                    ".0s", "s"
                                ),
                            )
                            retry.get_backoff_time = get_backoff_time  # type: ignore
                            return retry

                        self.__log(
                            logging.DEBUG,
                            "Response message does not indicate retry-able error",
                        )
                        raise Requester.createException(
                            response.status, response.headers, content
                        )
                    except (MaxRetryError, GithubException):
                        raise
                    except Exception as e:
                        self.__log(
                            logging.WARNING,
                            "Failed to inspect response message",
                            exc_info=e,
                        )

                    raise GithubException(response.status, content, response.headers)

        # retry the request as usual
        return super().increment(method, url, response, error, _pool, _stacktrace)

    @staticmethod
    def get_content(resp: HTTPResponse, url: str) -> bytes:
        # logic taken from HTTPAdapter.build_response (requests.adapters)
        response = Response()

        # Fallback to None if there's no status_code, for whatever reason.
        response.status_code = getattr(resp, "status", None)  # type: ignore

        # Make headers case-insensitive.
        response.headers = CaseInsensitiveDict(getattr(resp, "headers", {}))

        # Set encoding.
        response.encoding = get_encoding_from_headers(response.headers)
        response.raw = resp
        response.reason = response.raw.reason  # type: ignore

        response.url = url

        return response.content

    def __log(self, level: int, message: str, **kwargs) -> None:
        if self.__logger is None:
            self.__logger = logging.getLogger(__name__)
        if self.__logger.isEnabledFor(level):
            self.__logger.log(level, message, **kwargs)
