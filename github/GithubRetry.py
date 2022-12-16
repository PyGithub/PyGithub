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

import datetime
import json
import logging

from requests import Response
from requests.models import CaseInsensitiveDict
from requests.utils import get_encoding_from_headers
from urllib3 import Retry
from urllib3.exceptions import MaxRetryError

from github import GithubException
from github.Requester import Requester


DEFAULT_SECONDARY_RATE_WAIT = 60


class GithubRetry(Retry):
    __logger = None

    def __init__(self, secondaryRateWait=DEFAULT_SECONDARY_RATE_WAIT, **kwargs):
        self.secondaryRateWait = secondaryRateWait
        # 403 is too broad to be retried, but GitHub API signals rate limits via 403
        # we retry 403 and look into the response header via Retry.increment
        # to determine if we really retry that 403
        kwargs['status_forcelist'] = kwargs.get('status_forcelist', list(Retry.RETRY_AFTER_STATUS_CODES)) + [403]
        super().__init__(**kwargs)

    def new(self, **kw):
        kw.update(dict(secondaryRateWait=self.secondaryRateWait))
        return super().new(**kw)

    def increment(self,
                  method=None,
                  url=None,
                  response=None,
                  error=None,
                  _pool=None,
                  _stacktrace=None):
        if response:
            # we retry 403 only when there is a Retry-After header (indicating it is retry-able)
            # or the body message does imply a rate limit error
            if response.status == 403:
                self.__log(logging.INFO, f'Request {method} {url} failed with {response.status}: {response.reason}')
                if 'Retry-After' in response.headers:
                    # Sleeping 'Retry-After' seconds is implemented in urllib3.Retry.sleep() and called by urllib3
                    self.__log(logging.DEBUG, f'Retrying after {response.headers.get("Retry-After")} seconds')
                else:
                    self.__log(logging.DEBUG, f'There is no Retry-After in the response header')
                    content = response.reason

                    # to identify retry-able methods, we inspect the response body
                    try:
                        content = self.get_content(response, url)
                        content = json.loads(content)
                        message = content.get('message')

                        if Requester.isRateLimitError(message):
                            self.__log(logging.DEBUG, f'Response body indicates retry-able rate limit error: {message}')

                            # check early that we are retrying at all
                            retry = super().increment(method, url, response, error, _pool, _stacktrace)

                            if Requester.isSecondaryRateLimitError(message):
                                self.__log(logging.DEBUG, f'Secondary rate limit has backoff of {self.secondaryRateWait}s')

                            # we backoff primary rate limit at least until X-RateLimit-Reset
                            # we backoff secondary rate limit at least for secondaryRateWait seconds,
                            # or X-RateLimit-Reset, whatever comes first
                            backoff = 0
                            if 'X-RateLimit-Reset' in response.headers:
                                value = response.headers.get('X-RateLimit-Reset')
                                if value and value.isdigit():
                                    reset = datetime.datetime.utcfromtimestamp(int(value))
                                    delta = reset - self.__utc_now()
                                    resetBackoff = delta.total_seconds()

                                    if resetBackoff > 0:
                                        self.__log(
                                            logging.DEBUG,
                                            f'Reset occurs in {str(delta)} ({value} / {reset})'
                                        )

                                    # plus 1s as it is not clear when in that second the reset occurs
                                    backoff = resetBackoff + 1

                                    # experience has shown that secondary rate limit clears on primary rate reset
                                    if Requester.isSecondaryRateLimitError(message):
                                        backoff = min(backoff, self.secondaryRateWait)
                            elif Requester.isSecondaryRateLimitError(message):
                                backoff = self.secondaryRateWait

                            # we backoff at least retry's next backoff
                            retry_backoff = retry.get_backoff_time()
                            if retry_backoff > backoff:
                                if backoff >= 0:
                                    self.__log(logging.DEBUG, f'Retry backoff of {retry_backoff}s exceeds '
                                                              f'required rate limit backoff of {backoff}s')
                                backoff = retry.get_backoff_time()

                            def get_backoff_time():
                                return backoff

                            self.__log(logging.DEBUG, f'Setting next backoff to {backoff}s')
                            retry.get_backoff_time = get_backoff_time
                            return retry

                        self.__log(logging.DEBUG, 'Response message does not indicate retry-able error')
                        raise Requester.createException(response.status, response.headers, content)
                    except (MaxRetryError, GithubException):
                        raise
                    except Exception as e:
                        self.__log(logging.WARNING, 'Failed to inspect response message', exc_info=e)

                    raise GithubException(response.status, content, response.headers)

        # retry the request as usual
        return super().increment(method, url, response, error, _pool, _stacktrace)

    @staticmethod
    def get_content(resp, url):
        # logic taken from HTTPAdapter.build_response (requests.adapters)
        response = Response()

        # Fallback to None if there's no status_code, for whatever reason.
        response.status_code = getattr(resp, 'status', None)

        # Make headers case-insensitive.
        response.headers = CaseInsensitiveDict(getattr(resp, 'headers', {}))

        # Set encoding.
        response.encoding = get_encoding_from_headers(response.headers)
        response.raw = resp
        response.reason = response.raw.reason

        response.url = url

        return response.content

    def __utc_now(self):
        """Used to inject time for testing"""
        return datetime.datetime.utcnow()

    def __log(self, level, message, **kwargs):
        if self.__logger is None:
            self.__logger = logging.getLogger(__name__)
        if self.__logger.isEnabledFor(level):
            self.__logger.log(level, message, **kwargs)
