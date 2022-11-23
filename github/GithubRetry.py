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


class GithubRetry(Retry):
    __logger = None

    def __init__(self, **kwargs):
        # 403 is too broad to be retried, but GitHub API signals rate limits via 403
        # we retry 403 and look into the response header via Retry.increment
        kwargs['status_forcelist'] = kwargs.get('status_forcelist', list(Retry.RETRY_AFTER_STATUS_CODES)) + [403]
        super().__init__(**kwargs)

    def increment(self,
                  method=None,
                  url=None,
                  response=None,
                  error=None,
                  _pool=None,
                  _stacktrace=None):
        if response:
            self.__log(logging.DEBUG, f'Request {method} {url} failed with {response.status} {response.reason}')

            # we do not retry 403 when there is no Retry-After header (indicating it is retry-able)
            # and the body message does not imply a rate limit error
            if response.status == 403:
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
                            self.__log(logging.DEBUG, f'Response body indicates retry-able error: {message}')

                            # backoff until X-RateLimit-Reset
                            if 'X-RateLimit-Reset' in response.headers:
                                value = response.headers.get('X-RateLimit-Reset')
                                if value and value.isdigit():
                                    reset = datetime.datetime.utcfromtimestamp(int(value))
                                    delta = reset - self.__utc_now()
                                    retry = super().increment(method, url, response, error, _pool, _stacktrace)
                                    backoff = retry.get_backoff_time()

                                    if delta.total_seconds() > 0:
                                        self.__log(
                                            logging.DEBUG,
                                            f'Reset occurs in {str(delta)} ({value} / {reset}), '
                                            f'setting next backoff to {delta.total_seconds()}s'
                                        )

                                        def get_backoff_time():
                                            # plus 1s as it is not clear when in that second the reset occurs
                                            return max(delta.total_seconds() + 1, backoff)

                                        retry.get_backoff_time = get_backoff_time

                                    return retry

                            return super().increment(method, url, response, error, _pool, _stacktrace)

                        self.__log(logging.DEBUG, 'Response message does not indicate retry-able error')
                        raise Requester.createException(response.status, response.headers, {"message": content})
                    except MaxRetryError:
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
