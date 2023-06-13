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

from unittest import mock

import github

from . import Framework


class Requester(Framework.TestCase):
    logger = None

    def setUp(self):
        super().setUp()
        self.logger = mock.MagicMock()
        github.Requester.Requester.injectLogger(self.logger)

    def tearDown(self):
        github.Requester.Requester.resetLogger()
        super().tearDown()

    def testLoggingRedirection(self):
        self.assertEqual(self.g.get_repo("EnricoMi/test").name, "test-renamed")
        self.logger.info.assert_called_once_with(
            "Following Github server redirection from /repos/EnricoMi/test to /repositories/638123443"
        )

    def testBaseUrlSchemeRedirection(self):
        gh = github.Github(base_url="http://api.github.com")
        with self.assertRaises(RuntimeError) as exc:
            gh.get_repo("PyGithub/PyGithub")
        self.assertEqual(
            exc.exception.args,
            (
                "Github server redirected from http protocol to https, please correct your "
                "Github server URL via base_url: Github(base_url=...)",
            ),
        )

    def testBaseUrlHostRedirection(self):
        gh = github.Github(base_url="https://www.github.com")
        with self.assertRaises(RuntimeError) as exc:
            gh.get_repo("PyGithub/PyGithub")
        self.assertEqual(
            exc.exception.args,
            (
                "Github server redirected from host www.github.com to github.com, "
                "please correct your Github server URL via base_url: Github(base_url=...)",
            ),
        )

    def testBaseUrlPortRedirection(self):
        # replay data forged
        gh = github.Github(base_url="https://api.github.com")
        with self.assertRaises(RuntimeError) as exc:
            gh.get_repo("PyGithub/PyGithub")
        self.assertEqual(
            exc.exception.args,
            (
                "Requested https://api.github.com/repos/PyGithub/PyGithub but server "
                "redirected to https://api.github.com:443/repos/PyGithub/PyGithub, "
                "you may need to correct your Github server URL "
                "via base_url: Github(base_url=...)",
            ),
        )

    def testBaseUrlPrefixRedirection(self):
        # replay data forged
        gh = github.Github(base_url="https://api.github.com/api/v3")
        self.assertEqual(gh.get_repo("PyGithub/PyGithub").name, "PyGithub")
        self.logger.info.assert_called_once_with(
            "Following Github server redirection from /api/v3/repos/PyGithub/PyGithub to /repos/PyGithub/PyGithub"
        )

    def assertException(self, exception, exception_type, status, data, headers, string):
        self.assertIsInstance(exception, exception_type)
        self.assertEqual(exception.status, status)
        if data is None:
            self.assertIsNone(exception.data)
        else:
            self.assertEqual(exception.data, data)
        self.assertEqual(exception.headers, headers)
        self.assertEqual(str(exception), string)

    def testShouldCreateBadCredentialsException(self):
        exc = self.g._Github__requester.__createException(
            401, {"header": "value"}, {"message": "Bad credentials"}
        )
        self.assertException(
            exc,
            github.BadCredentialsException,
            401,
            {"message": "Bad credentials"},
            {"header": "value"},
            '401 {"message": "Bad credentials"}',
        )

    def testShouldCreateTwoFactorException(self):
        exc = self.g._Github__requester.__createException(
            401,
            {"x-github-otp": "required; app"},
            {
                "message": "Must specify two-factor authentication OTP code.",
                "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication",
            },
        )
        self.assertException(
            exc,
            github.TwoFactorException,
            401,
            {
                "message": "Must specify two-factor authentication OTP code.",
                "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication",
            },
            {"x-github-otp": "required; app"},
            '401 {"message": "Must specify two-factor authentication OTP code.", "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication"}',
        )

    def testShouldCreateBadUserAgentException(self):
        exc = self.g._Github__requester.__createException(
            403,
            {"header": "value"},
            {"message": "Missing or invalid User Agent string"},
        )
        self.assertException(
            exc,
            github.BadUserAgentException,
            403,
            {"message": "Missing or invalid User Agent string"},
            {"header": "value"},
            '403 {"message": "Missing or invalid User Agent string"}',
        )

    def testShouldCreateRateLimitExceededException(self):
        for message in [
            "API Rate Limit Exceeded for 92.104.200.119",
            "You have triggered an abuse detection mechanism. Please wait a few minutes before you try again.",
            "You have exceeded a secondary rate limit. Please wait a few minutes before you try again.",
        ]:
            with self.subTest(message=message):
                exc = self.g._Github__requester.__createException(
                    403, {"header": "value"}, {"message": message}
                )
                self.assertException(
                    exc,
                    github.RateLimitExceededException,
                    403,
                    {"message": message},
                    {"header": "value"},
                    f'403 {{"message": "{message}"}}',
                )

    def testShouldCreateUnknownObjectException(self):
        exc = self.g._Github__requester.__createException(
            404, {"header": "value"}, {"message": "Not Found"}
        )
        self.assertException(
            exc,
            github.UnknownObjectException,
            404,
            {"message": "Not Found"},
            {"header": "value"},
            '404 {"message": "Not Found"}',
        )

    def testShouldCreateGithubException(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.__createException(
                    status, {"header": "value"}, {"message": "Something unknown"}
                )
                self.assertException(
                    exc,
                    github.GithubException,
                    status,
                    {"message": "Something unknown"},
                    {"header": "value"},
                    f'{status} {{"message": "Something unknown"}}',
                )

    def testShouldCreateExceptionWithoutMessage(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.__createException(status, {}, {})
                self.assertException(
                    exc, github.GithubException, status, {}, {}, f"{status} {{}}"
                )

    def testShouldCreateExceptionWithoutOutput(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.__createException(status, {}, None)
                self.assertException(
                    exc, github.GithubException, status, None, {}, f"{status} null"
                )
