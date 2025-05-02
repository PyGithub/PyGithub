############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Patryk Szulczyk <therealsoulcheck@gmail.com>                  #
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

import contextlib
import logging
import sys
import unittest
from datetime import datetime
from io import BytesIO
from unittest import mock

import urllib3.response
from urllib3 import Retry

import github
from github.GithubRetry import DEFAULT_SECONDARY_RATE_WAIT

from . import Requester

PrimaryRateLimitMessage = Requester.Requester.PrimaryRateLimitErrors[0]
PrimaryRateLimitJson = (
    '{"message":"'
    + PrimaryRateLimitMessage
    + '","documentation_url":"https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"}'
)

SecondaryRateLimitMessage = Requester.Requester.SecondaryRateLimitErrors[0]
SecondaryRateLimitJson = (
    '{"message":"'
    + SecondaryRateLimitMessage
    + '","documentation_url": "https://docs.github.com/en/free-pro-team@latest/rest/overview/resources-in-the-rest-api#secondary-rate-limits"}'
)


class GithubRetry(unittest.TestCase):
    def get_test_increment_func(self, expected_rate_limit_error):
        is_primary = expected_rate_limit_error == PrimaryRateLimitMessage

        def test_increment(
            retry,
            response,
            expected_total=None,
            expected_backoff=None,
            expected_retry_backoff=None,
            expect_retry_error=False,
            has_reset=False,
        ):
            # fmt: off
            self.assertTrue(
                expected_total is not None and expected_backoff is not None and not expect_retry_error or  # noqa: W504
                expected_total is None and expected_backoff is None and expect_retry_error
            )
            # fmt: on

            orig_retry = retry
            with mock.patch.object(retry, "_GithubRetry__log") as log:
                if expect_retry_error:
                    with self.assertRaises(urllib3.exceptions.MaxRetryError):
                        retry.increment("TEST", "URL", response)
                    retry = None
                else:
                    retry = retry.increment("TEST", "URL", response)

                    self.assertEqual(expected_total, retry.total)
                    self.assertEqual(
                        expected_backoff if expected_retry_backoff is None else expected_retry_backoff,
                        retry.get_backoff_time(),
                    )
                    self.assertEqual(orig_retry.secondary_rate_wait, retry.secondary_rate_wait)

                # fmt: off
                log.assert_has_calls(
                    [
                        mock.call(20, "Request TEST URL failed with 403: None"),
                        mock.call(10, f"Response body indicates retry-able {'primary' if is_primary else 'secondary'} rate limit error: {expected_rate_limit_error}"),
                    ] + ([
                        mock.call(10, "Reset occurs in 0:00:12 (1644768012 / 2022-02-13 16:00:12+00:00)")
                    ] if has_reset else []) + ([
                        mock.call(10, f"Retry backoff of {expected_retry_backoff}s exceeds required rate limit backoff of {expected_backoff}s")
                    ] if expected_retry_backoff and expected_backoff > 0 else []) + ([
                        mock.call(20, f"Setting next backoff to {expected_backoff if expected_retry_backoff is None else expected_retry_backoff}s")
                    ] if not expect_retry_error else []),
                    any_order=False,
                )
                # fmt: on
            return retry

        return test_increment

    @staticmethod
    def response_func(content, reset=None):
        def response():
            stream = BytesIO(content.encode("utf8"))
            return urllib3.response.HTTPResponse(
                body=stream,
                preload_content=False,
                headers={"X-RateLimit-Reset": f"{reset}"} if reset else {},
                status=403,
            )

        return response

    @contextlib.contextmanager
    def mock_retry_now(self, now):
        if sys.version_info[0] > 3 or sys.version_info[0] == 3 and sys.version_info[1] >= 11:
            attr = "github.GithubRetry.GithubRetry._GithubRetry__datetime"
        else:
            attr = "github.GithubRetry._GithubRetry__datetime"
        with mock.patch(attr) as dt:
            dt.now = lambda tz=None: datetime.fromtimestamp(now, tz=tz)
            dt.fromtimestamp = datetime.fromtimestamp
            yield

    def test_primary_rate_error_with_reset(self):
        retry = github.GithubRetry(total=3)
        response = self.response_func(PrimaryRateLimitJson, 1644768012)
        test_increment = self.get_test_increment_func(PrimaryRateLimitMessage)

        # test 12 seconds before reset, note backoff will be 12+1 second
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=2,
                expected_backoff=12 + 1,
                has_reset=True,
            )
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=1,
                expected_backoff=12 + 1,
                has_reset=True,
            )

        # test 2 seconds after reset, no backoff expected
        with self.mock_retry_now(1644768014):
            retry = test_increment(retry, response(), expected_total=0, expected_backoff=0)
            test_increment(retry, response(), expect_retry_error=True)

    def test_primary_rate_error_with_reset_and_exponential_backoff(self):
        retry = github.GithubRetry(total=3, backoff_factor=10)
        response = self.response_func(PrimaryRateLimitJson, 1644768012)
        test_increment = self.get_test_increment_func(PrimaryRateLimitMessage)

        # test 12 seconds before reset, note backoff will be 12+1 second
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=2,
                expected_backoff=12 + 1,
                has_reset=True,
            )
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=1,
                expected_backoff=12 + 1,
                expected_retry_backoff=20,
                has_reset=True,
            )

        # test 2 seconds after reset, no backoff expected
        with self.mock_retry_now(1644768014):
            retry = test_increment(
                retry,
                response(),
                expected_total=0,
                expected_backoff=-2,
                expected_retry_backoff=40,
            )
            test_increment(retry, response(), expect_retry_error=True)

    def test_primary_rate_error_without_reset(self):
        retry = github.GithubRetry(total=3)
        response = self.response_func(PrimaryRateLimitJson, reset=None)
        test_increment = self.get_test_increment_func(PrimaryRateLimitMessage)

        # test without reset
        retry = test_increment(retry, response(), expected_total=2, expected_backoff=0)
        retry = test_increment(retry, response(), expected_total=1, expected_backoff=0)
        retry = test_increment(retry, response(), expected_total=0, expected_backoff=0)
        test_increment(retry, response(), expect_retry_error=True)

    def test_primary_rate_error_without_reset_with_exponential_backoff(self):
        retry = github.GithubRetry(total=3, backoff_factor=10)
        response = self.response_func(PrimaryRateLimitJson, reset=None)
        test_increment = self.get_test_increment_func(PrimaryRateLimitMessage)

        # test without reset
        retry = test_increment(
            retry,
            response(),
            expected_total=2,
            expected_backoff=0,
            expected_retry_backoff=0,
        )
        retry = test_increment(
            retry,
            response(),
            expected_total=1,
            expected_backoff=0,
            expected_retry_backoff=20,
        )
        retry = test_increment(
            retry,
            response(),
            expected_total=0,
            expected_backoff=0,
            expected_retry_backoff=40,
        )
        test_increment(retry, response(), expect_retry_error=True)

    def test_secondary_rate_error_with_reset(self):
        retry = github.GithubRetry(total=3)
        response = self.response_func(SecondaryRateLimitJson, 1644768012)
        test_increment = self.get_test_increment_func(SecondaryRateLimitMessage)

        # test 12 seconds before reset, expect secondary wait seconds of 60
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=2,
                expected_backoff=60,
                has_reset=False,
            )
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=1,
                expected_backoff=60,
                has_reset=False,
            )

        # test 2 seconds after reset, still expect secondary wait seconds of 60
        with self.mock_retry_now(1644768014):
            retry = test_increment(retry, response(), expected_total=0, expected_backoff=60)
            test_increment(retry, response(), expect_retry_error=True)

    def test_secondary_rate_error_with_reset_and_exponential_backoff(self):
        retry = github.GithubRetry(total=3, backoff_factor=10, secondary_rate_wait=15)
        response = self.response_func(SecondaryRateLimitJson, 1644768012)
        test_increment = self.get_test_increment_func(SecondaryRateLimitMessage)

        # test 12 seconds before reset, expect secondary wait seconds of 15
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=2,
                expected_backoff=15,
                has_reset=False,
            )
        with self.mock_retry_now(1644768000):
            retry = test_increment(
                retry,
                response(),
                expected_total=1,
                expected_backoff=15,
                expected_retry_backoff=20,
                has_reset=False,
            )

        # test 2 seconds after reset, exponential backoff exceeds secondary wait seconds of 15
        with self.mock_retry_now(1644768014):
            retry = test_increment(
                retry,
                response(),
                expected_total=0,
                expected_backoff=15,
                expected_retry_backoff=40,
            )
            test_increment(retry, response(), expect_retry_error=True)

    def test_secondary_rate_error_without_reset(self):
        retry = github.GithubRetry(total=3)
        response = self.response_func(SecondaryRateLimitJson, reset=None)
        test_increment = self.get_test_increment_func(SecondaryRateLimitMessage)

        retry = test_increment(
            retry,
            response(),
            expected_total=2,
            expected_backoff=DEFAULT_SECONDARY_RATE_WAIT,
        )
        retry = test_increment(
            retry,
            response(),
            expected_total=1,
            expected_backoff=DEFAULT_SECONDARY_RATE_WAIT,
        )
        retry = test_increment(
            retry,
            response(),
            expected_total=0,
            expected_backoff=DEFAULT_SECONDARY_RATE_WAIT,
        )
        test_increment(retry, response(), expect_retry_error=True)

    def test_secondary_rate_error_without_reset_with_exponential_backoff(self):
        retry = github.GithubRetry(total=3, backoff_factor=10, secondary_rate_wait=5)
        response = self.response_func(SecondaryRateLimitJson, reset=None)
        test_increment = self.get_test_increment_func(SecondaryRateLimitMessage)

        retry = test_increment(retry, response(), expected_total=2, expected_backoff=5)
        retry = test_increment(
            retry,
            response(),
            expected_total=1,
            expected_backoff=5,
            expected_retry_backoff=20,
        )
        retry = test_increment(
            retry,
            response(),
            expected_total=0,
            expected_backoff=5,
            expected_retry_backoff=40,
        )
        test_increment(retry, response(), expect_retry_error=True)

    def do_test_default_behaviour(self, retry, response):
        expected = Retry(total=retry.total, backoff_factor=retry.backoff_factor)
        self.assertTrue(retry.total > 0)
        for _ in range(retry.total):
            retry = retry.increment("TEST", "URL", response)
            expected = expected.increment("TEST", "URL", response)
            self.assertEqual(expected.total, retry.total)
            self.assertEqual(expected.get_backoff_time(), retry.get_backoff_time())

        with self.assertRaises(urllib3.exceptions.MaxRetryError):
            retry.increment("TEST", "URL", response)
        with self.assertRaises(urllib3.exceptions.MaxRetryError):
            expected.increment("TEST", "URL", response)

    def test_403_with_retry_after(self):
        retry = github.GithubRetry(total=3)
        response = urllib3.response.HTTPResponse(status=403, headers={"Retry-After": "123"})
        self.do_test_default_behaviour(retry, response)

    def test_403_with_non_retryable_error(self):
        retry = github.GithubRetry(total=3)
        with self.assertRaises(github.BadUserAgentException):
            retry.increment(
                "TEST",
                "URL",
                self.response_func('{"message":"Missing or invalid User Agent string."}')(),
            )

    def test_misc_response(self):
        retry = github.GithubRetry(total=3)
        response = urllib3.response.HTTPResponse()
        self.do_test_default_behaviour(retry, response)

    def test_misc_response_exponential_backoff(self):
        retry = github.GithubRetry(total=3, backoff_factor=10)
        response = urllib3.response.HTTPResponse()
        self.do_test_default_behaviour(retry, response)

    def test_error_in_get_content(self):
        retry = github.GithubRetry(total=3)
        response = urllib3.response.HTTPResponse(status=403, reason="NOT GOOD")

        with mock.patch.object(retry, "_GithubRetry__log") as log:
            with self.assertRaises(github.GithubException) as exp:
                retry.increment("TEST", "URL", response)
            self.assertIsNone(exp.exception.message)
            self.assertEqual(403, exp.exception.status)
            self.assertEqual("NOT GOOD", exp.exception.data)
            self.assertEqual({}, exp.exception.headers)

            self.assertIsInstance(exp.exception.__cause__, RuntimeError)
            self.assertEqual(("Failed to inspect response message",), exp.exception.__cause__.args)

            self.assertIsInstance(exp.exception.__cause__.__cause__, ValueError)
            self.assertEqual(
                ("Unable to determine whether fp is closed.",),
                exp.exception.__cause__.__cause__.args,
            )

        log.assert_called_once_with(logging.INFO, "Request TEST URL failed with 403: NOT GOOD")
