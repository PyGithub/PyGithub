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

from github import GithubException, Requester
from requests import Response
from requests.models import CaseInsensitiveDict
from requests.utils import get_encoding_from_headers
from urllib3 import Retry, HTTPResponse
from urllib3.exceptions import MaxRetryError, ResponseError

from publish.github_action import GithubAction


class GitHubRetry(Retry):
    def __init__(self, **kwargs):
        # 403 is too broad to be retried, but GitHub API signals rate limits via 403
        # we retry 403 and look into the response header via Retry.increment
        kwargs['status_forcelist'] = kwargs.get('status_forcelist', Retry.RETRY_AFTER_STATUS_CODES) + [403]
        super().__init__(**kwargs)

    def increment(self,
                  method=None,
                  url=None,
                  response=None,
                  error=None,
                  _pool=None,
                  _stacktrace=None):
        # we do not retry 403 when there is no Retry-After header (indicating it is retry-able)
        # and the body message does not imply a rate limit error
        if response and response.status == 403 and 'Retry-After' not in response.headers:
            try:
                content = get_content(response, url)
                content = json.loads(content)
                message = content.get('message')

                if not Requester.isRateLimitError(message):
                    raise Requester.createException(response.status, response.headers, {"message": content})
            except GithubException:
                raise
            except Exception as e:
                logger.warning('failed to inspect response message', exc_info=e)
                raise GithubException(response.status, response.reason, response.headers)

        # retry the request as usual
        return super().increment(method, url, response, error, _pool, _stacktrace)


def get_content(resp: HTTPResponse, url: str):
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
