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

import github

from . import Framework


class Requester(Framework.TestCase):
    def testShouldCreateBadCredentialsException(self):
        exc = self.g._Github__requester.__createException(
            401, {"header": "value"}, {"message": "Bad credentials"}
        )
        self.assertIsInstance(exc, github.BadCredentialsException)
        self.assertEqual(exc.status, 401)
        self.assertEqual(exc.data, {"message": "Bad credentials"})
        self.assertEqual(exc.headers, {"header": "value"})
        self.assertEqual(str(exc), '401 {"message": "Bad credentials"}')

    def testShouldCreateTwoFactorException(self):
        exc = self.g._Github__requester.__createException(
            401,
            {"x-github-otp": "required; app"},
            {
                "message": "Must specify two-factor authentication OTP code.",
                "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication",
            },
        )
        self.assertIsInstance(exc, github.TwoFactorException)
        self.assertEqual(exc.status, 401)
        self.assertEqual(
            exc.data,
            {
                "message": "Must specify two-factor authentication OTP code.",
                "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication",
            },
        )
        self.assertEqual(exc.headers, {"x-github-otp": "required; app"})
        self.assertEqual(
            str(exc),
            '401 {"message": "Must specify two-factor authentication OTP code.", "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication"}',
        )

    def testShouldCreateBadUserAgentException(self):
        exc = self.g._Github__requester.__createException(
            403,
            {"header": "value"},
            {"message": "Missing or invalid User Agent string"},
        )
        self.assertIsInstance(exc, github.BadUserAgentException)
        self.assertEqual(exc.status, 403)
        self.assertEqual(exc.data, {"message": "Missing or invalid User Agent string"})
        self.assertEqual(exc.headers, {"header": "value"})
        self.assertEqual(
            str(exc), '403 {"message": "Missing or invalid User Agent string"}'
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
                self.assertIsInstance(exc, github.RateLimitExceededException)
                self.assertEqual(exc.status, 403)
                self.assertEqual(exc.data, {"message": message})
                self.assertEqual(exc.headers, {"header": "value"})
                self.assertEqual(str(exc), f'403 {{"message": "{message}"}}')

    def testShouldCreateUnknownObjectException(self):
        exc = self.g._Github__requester.__createException(
            404, {"header": "value"}, {"message": "Not Found"}
        )
        self.assertIsInstance(exc, github.UnknownObjectException)
        self.assertEqual(exc.status, 404)
        self.assertEqual(exc.data, {"message": "Not Found"})
        self.assertEqual(exc.headers, {"header": "value"})
        self.assertEqual(str(exc), '404 {"message": "Not Found"}')

    def testShouldCreateGithubException(self):
        exc = self.g._Github__requester.__createException(
            405, {"header": "value"}, {"message": "Something unknown"}
        )
        self.assertIsInstance(exc, github.GithubException)
        self.assertEqual(exc.status, 405)
        self.assertEqual(exc.data, {"message": "Something unknown"})
        self.assertEqual(exc.headers, {"header": "value"})
        self.assertEqual(str(exc), '405 {"message": "Something unknown"}')

    def testShouldCreateExceptionWithoutMessage(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.__createException(status, {}, {})
                self.assertIsInstance(exc, github.GithubException)
                self.assertEqual(exc.status, status)
                self.assertEqual(exc.data, {})
                self.assertEqual(exc.headers, {})
                self.assertEqual(str(exc), f"{status} {{}}")

    def testShouldCreateExceptionWithoutOutput(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.__createException(status, {}, None)
                self.assertIsInstance(exc, github.GithubException)
                self.assertEqual(exc.status, status)
                self.assertIsNone(exc.data)
                self.assertEqual(exc.headers, {})
                self.assertEqual(str(exc), f"{status} null")
