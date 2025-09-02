############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Hemslo Wang <hemslo.wang@gmail.com>                           #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Jakub Smolar <jakub.smolar@scylladb.com>                      #
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

import contextlib
from datetime import datetime, timedelta, timezone
from unittest import mock

import github
from github import Requester as gr

from . import Framework
from .GithubIntegration import APP_ID, PRIVATE_KEY

REPO_NAME = "PyGithub/PyGithub"


class Requester(Framework.TestCase):
    logger = None

    def setUp(self):
        super().setUp()
        self.logger = mock.MagicMock()
        github.Requester.Requester.injectLogger(self.logger)

    def tearDown(self):
        github.Requester.Requester.resetLogger()
        super().tearDown()

    def testRecreation(self):
        class TestAuth(github.Auth.AppAuth):
            pass

        # create a Requester with non-default arguments
        auth = TestAuth(123, "key")
        requester = github.Requester.Requester(
            auth=auth,
            base_url="https://base.url",
            timeout=1,
            user_agent="user agent",
            per_page=123,
            verify=False,
            retry=3,
            pool_size=5,
            seconds_between_requests=1.2,
            seconds_between_writes=3.4,
            # v3: this should not be the default value, so if this has been changed in v3,
            # change it here is well
            lazy=True,
        )
        kwargs = requester.kwargs

        # assert kwargs consists of ALL constructor arguments
        self.assertEqual(kwargs.keys(), github.Requester.Requester.__init__.__annotations__.keys())
        self.assertEqual(
            kwargs,
            dict(
                auth=auth,
                base_url="https://base.url",
                timeout=1,
                user_agent="user agent",
                per_page=123,
                verify=False,
                retry=3,
                pool_size=5,
                seconds_between_requests=1.2,
                seconds_between_writes=3.4,
                lazy=True,
            ),
        )

        # create a copy Requester, assert identity via kwargs
        copy = github.Requester.Requester(**kwargs)
        self.assertEqual(copy.kwargs, kwargs)

        # create Github instance, assert identity requester
        gh = github.Github(**kwargs)
        self.assertEqual(gh._Github__requester.kwargs, kwargs)

        # create GithubIntegration instance, assert identity requester
        gi = github.GithubIntegration(**kwargs)
        self.assertEqual(gi._GithubIntegration__requester.kwargs, kwargs)

    def testWithAuth(self):
        class TestAuth(github.Auth.AppAuth):
            pass

        # create a Requester with non-default arguments
        auth = TestAuth(123, "key")
        requester = github.Requester.Requester(
            auth=auth,
            base_url="https://base.url",
            timeout=1,
            user_agent="user agent",
            per_page=123,
            verify=False,
            retry=3,
            pool_size=5,
            seconds_between_requests=1.2,
            seconds_between_writes=3.4,
            # v3: this should not be the default value, so if this has been changed in v3,
            # change it here is well
            lazy=True,
        )

        # create a copy with different auth
        auth2 = TestAuth(456, "key2")
        copy = requester.withAuth(auth2)

        # assert kwargs of copy
        self.assertEqual(
            copy.kwargs,
            dict(
                auth=auth2,
                base_url="https://base.url",
                timeout=1,
                user_agent="user agent",
                per_page=123,
                verify=False,
                retry=3,
                pool_size=5,
                seconds_between_requests=1.2,
                seconds_between_writes=3.4,
                lazy=True,
            ),
        )

    def testGetParametersOfUrl(self):
        self.assertEqual({}, gr.Requester.get_parameters_of_url("https://github.com/api"))
        self.assertEqual({"per_page": ["10"]}, gr.Requester.get_parameters_of_url("https://github.com/api?per_page=10"))
        self.assertEqual(
            {"per_page": ["10"], "page": ["2"]},
            gr.Requester.get_parameters_of_url("https://github.com/api?per_page=10&page=2"),
        )
        self.assertEqual(
            {"item": ["1", "2", "3"]}, gr.Requester.get_parameters_of_url("https://github.com/api?item=1&item=2&item=3")
        )

    def testAddParametersToUrl(self):
        self.assertEqual("https://github.com/api", gr.Requester.add_parameters_to_url("https://github.com/api", {}))
        self.assertEqual(
            "https://github.com/api?per_page=10",
            gr.Requester.add_parameters_to_url("https://github.com/api", {"per_page": 10}),
        )
        self.assertEqual(
            "https://github.com/api?per_page=10&page=2",
            gr.Requester.add_parameters_to_url("https://github.com/api", {"per_page": 10, "page": 2}),
        )
        self.assertEqual(
            "https://github.com/api?per_page=10&page=2",
            gr.Requester.add_parameters_to_url("https://github.com/api?per_page=10", {"page": 2}),
        )
        self.assertEqual(
            "https://github.com/api?per_page=10&page=2",
            gr.Requester.add_parameters_to_url("https://github.com/api?per_page=10&page=1", {"page": 2}),
        )
        self.assertEqual(
            "https://github.com/api?item=3&item=4",
            gr.Requester.add_parameters_to_url("https://github.com/api?item=1&item=2&item=3", {"item": [3, 4]}),
        )

    def testCloseGithub(self):
        mocked_connection = mock.MagicMock()
        mocked_custom_connection = mock.MagicMock()

        with github.Github() as gh:
            requester = gh._Github__requester
            requester._Requester__connection = mocked_connection
            requester._Requester__custom_connections.append(mocked_custom_connection)

        mocked_connection.close.assert_called_once_with()
        mocked_custom_connection.close.assert_called_once_with()
        self.assertIsNone(requester._Requester__connection)

    def testCloseGithubIntegration(self):
        mocked_connection = mock.MagicMock()
        mocked_custom_connection = mock.MagicMock()

        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        with github.GithubIntegration(auth=auth) as gi:
            requester = gi._GithubIntegration__requester
            requester._Requester__connection = mocked_connection
            requester._Requester__custom_connections.append(mocked_custom_connection)

        mocked_connection.close.assert_called_once_with()
        mocked_custom_connection.close.assert_called_once_with()
        self.assertIsNone(requester._Requester__connection)

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

    def testHostnameHasDomain(self):
        assert self.g.requester.__hostnameHasDomain("github.com", "github.com")
        assert self.g.requester.__hostnameHasDomain("api.github.com", "github.com")
        assert self.g.requester.__hostnameHasDomain("api.github.com", "github.com")
        assert self.g.requester.__hostnameHasDomain("ghe.local", "ghe.local")
        assert self.g.requester.__hostnameHasDomain("api.ghe.local", "ghe.local")
        assert self.g.requester.__hostnameHasDomain("api.prod.ghe.local", "prod.ghe.local")
        assert self.g.requester.__hostnameHasDomain("github.com", ("github.com", "githubusercontent.com"))
        assert self.g.requester.__hostnameHasDomain("api.github.com", ("github.com", "githubusercontent.com"))
        assert self.g.requester.__hostnameHasDomain("githubusercontent.com", ("github.com", "githubusercontent.com"))
        assert self.g.requester.__hostnameHasDomain(
            "objects.githubusercontent.com", ("github.com", "githubusercontent.com")
        )
        assert self.g.requester.__hostnameHasDomain("maliciousgithub.com", "github.com") is False
        assert self.g.requester.__hostnameHasDomain("abc.def", ("github.com", "githubusercontent.com")) is False

    def testAssertUrlAllowed(self):
        # default github.com requester
        requester = self.g.requester

        for allowed in [
            "https://api.github.com/request",
            "https://github.com/path",
            "https://uploads.github.com/path",
            "https://status.github.com/path",
            "https://githubusercontent.com/path",
            "https://objects.githubusercontent.com/path",
            "https://release-assets.githubusercontent.com/path",
        ]:
            requester.__assertUrlAllowed(allowed)

        for not_allowed, arg in [
            ("https://prod.ghe.local/github-api/request", "prod.ghe.local"),
            ("https://api.prod.ghe.local/github-api/request", "api.prod.ghe.local"),
            ("https://uploads.prod.ghe.local/github-api/path", "uploads.prod.ghe.local"),
            ("https://status.prod.ghe.local/github-api/path", "status.prod.ghe.local"),
            ("https://example.com/", "example.com"),
        ]:
            with self.assertRaises(AssertionError) as exc:
                requester.__assertUrlAllowed(not_allowed)
            self.assertEqual(exc.exception.args, (arg,))

        # custom (Enterprise) requester with prefix
        requester = github.Github(base_url="https://prod.ghe.local/github-api/").requester

        for allowed in [
            "https://prod.ghe.local/github-api/request",
            "https://uploads.prod.ghe.local/path",
            "https://status.prod.ghe.local/path",
        ]:
            requester.__assertUrlAllowed(allowed)

        for not_allowed, arg in [
            ("https://prod.ghe.local/path", "/path"),
            ("https://ghe.local/path", "ghe.local"),
            ("https://api.github.com/request", "api.github.com"),
            ("https://github.com/path", "github.com"),
            ("https://uploads.github.com/path", "uploads.github.com"),
            ("https://status.github.com/path", "status.github.com"),
            ("https://githubusercontent.com/path", "githubusercontent.com"),
            ("https://objects.githubusercontent.com/path", "objects.githubusercontent.com"),
            (
                "https://release-assets.githubusercontent.com/path",
                "release-assets.githubusercontent.com",
            ),
            ("https://example.com/", "example.com"),
        ]:
            with self.assertRaises(AssertionError) as exc:
                requester.__assertUrlAllowed(not_allowed)
            self.assertEqual(exc.exception.args, (arg,))

    def testMakeAbsoluteUrl(self):
        # default github.com requester
        requester = self.g.requester
        assert "/api/v3/request", requester.__makeAbsoluteUrl("/request")
        assert "/api/v3/request", requester.__makeAbsoluteUrl("/request?param=value")
        assert "/api/v3/request", requester.__makeAbsoluteUrl("https://github.com/api/v3/request")
        assert "/api/v3/request", requester.__makeAbsoluteUrl("https://github.com/api/v3/request?param=value")
        assert "/request", requester.__makeAbsoluteUrl("https://github.com/request?param=value")

        # custom (Enterprise) requester with different prefix
        requester = github.Github(base_url="https://api.enterprise.ghe.com/github-api/").requester
        assert "/github-api/request", requester.__makeAbsoluteUrl("/request")
        assert "/github-api/request", requester.__makeAbsoluteUrl("/request?param=value")
        assert "/github-api/request", requester.__makeAbsoluteUrl("https://api.enterprise.ghe.com/github-api/request")
        assert "/github-api/request", requester.__makeAbsoluteUrl(
            "https://api.enterprise.ghe.com/github-api/request?param=value"
        )
        assert "/request", requester.__makeAbsoluteUrl("https://github.com/request?param=value")

    PrimaryRateLimitErrors = [
        "API rate limit exceeded for x.x.x.x. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
    ]
    SecondaryRateLimitErrors = [
        "You have triggered an abuse detection mechanism. Please wait a few minutes before you try again.",
        "You have triggered an abuse detection mechanism and have been temporarily blocked from content creation. Please retry your request again later."
        "You have exceeded a secondary rate limit and have been temporarily blocked from content creation. Please retry your request again later.",
        "You have exceeded a secondary rate limit. Please wait a few minutes before you try again.",
        "Something else here. Please wait a few minutes before you try again.",
    ]
    OtherErrors = ["User does not exist or is not a member of the organization"]

    def testIsRateLimitError(self):
        for message in self.PrimaryRateLimitErrors + self.SecondaryRateLimitErrors:
            self.assertTrue(github.Requester.Requester.isRateLimitError(message), message)
        for message in self.OtherErrors:
            self.assertFalse(github.Requester.Requester.isRateLimitError(message), message)

    def testIsPrimaryRateLimitError(self):
        for message in self.PrimaryRateLimitErrors:
            self.assertTrue(github.Requester.Requester.isPrimaryRateLimitError(message), message)
        for message in self.OtherErrors + self.SecondaryRateLimitErrors:
            self.assertFalse(github.Requester.Requester.isPrimaryRateLimitError(message), message)

    def testIsSecondaryRateLimitError(self):
        for message in self.SecondaryRateLimitErrors:
            self.assertTrue(github.Requester.Requester.isSecondaryRateLimitError(message), message)
        for message in self.OtherErrors + self.PrimaryRateLimitErrors:
            self.assertFalse(github.Requester.Requester.isSecondaryRateLimitError(message), message)

    def assertException(self, exception, exception_type, message, status, data, headers, string):
        self.assertIsInstance(exception, exception_type)
        if message is None:
            self.assertIsNone(exception.message)
        else:
            self.assertEqual(exception.message, message)
        self.assertEqual(exception.status, status)
        if data is None:
            self.assertIsNone(exception.data)
        else:
            self.assertEqual(exception.data, data)
        self.assertEqual(exception.headers, headers)
        self.assertEqual(str(exception), string)

    def testShouldCreateBadCredentialsException(self):
        exc = self.g._Github__requester.createException(401, {"header": "value"}, {"message": "Bad credentials"})
        self.assertException(
            exc,
            github.BadCredentialsException,
            None,
            401,
            {"message": "Bad credentials"},
            {"header": "value"},
            '401 {"message": "Bad credentials"}',
        )

    def testShouldCreateTwoFactorException(self):
        exc = self.g._Github__requester.createException(
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
            None,
            401,
            {
                "message": "Must specify two-factor authentication OTP code.",
                "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication",
            },
            {"x-github-otp": "required; app"},
            '401 {"message": "Must specify two-factor authentication OTP code.", "documentation_url": "https://developer.github.com/v3/auth#working-with-two-factor-authentication"}',
        )

    def testShouldCreateBadUserAgentException(self):
        exc = self.g._Github__requester.createException(
            403,
            {"header": "value"},
            {"message": "Missing or invalid User Agent string"},
        )
        self.assertException(
            exc,
            github.BadUserAgentException,
            None,
            403,
            {"message": "Missing or invalid User Agent string"},
            {"header": "value"},
            '403 {"message": "Missing or invalid User Agent string"}',
        )

    def testShouldCreateRateLimitExceededException(self):
        for message in self.PrimaryRateLimitErrors + self.SecondaryRateLimitErrors:
            with self.subTest(message=message):
                exc = self.g._Github__requester.createException(403, {"header": "value"}, {"message": message})
                self.assertException(
                    exc,
                    github.RateLimitExceededException,
                    None,
                    403,
                    {"message": message},
                    {"header": "value"},
                    f'403 {{"message": "{message}"}}',
                )

    def testShouldCreateUnknownObjectException(self):
        exc = self.g._Github__requester.createException(404, {"header": "value"}, {"message": "Not Found"})
        self.assertException(
            exc,
            github.UnknownObjectException,
            None,
            404,
            {"message": "Not Found"},
            {"header": "value"},
            '404 {"message": "Not Found"}',
        )

    def testShouldCreateUnknownObjectException2(self):
        exc = self.g._Github__requester.createException(
            404, {"header": "value"}, {"message": "No object found for the path some-nonexistent-file"}
        )
        self.assertException(
            exc,
            github.UnknownObjectException,
            "No object found for the path some-nonexistent-file",
            404,
            {"message": "No object found for the path some-nonexistent-file"},
            {"header": "value"},
            'No object found for the path some-nonexistent-file: 404 {"message": "No object found for the path some-nonexistent-file"}',
        )

    def testShouldCreateUnknownObjectException3(self):
        exc = self.g._Github__requester.createException(404, {"header": "value"}, {"message": "Branch Not Found"})
        self.assertException(
            exc,
            github.UnknownObjectException,
            "Branch Not Found",
            404,
            {"message": "Branch Not Found"},
            {"header": "value"},
            'Branch Not Found: 404 {"message": "Branch Not Found"}',
        )

    def testShouldCreateGithubException(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.createException(
                    status, {"header": "value"}, {"message": "Something unknown"}
                )
                self.assertException(
                    exc,
                    github.GithubException,
                    "Something unknown",
                    status,
                    {"message": "Something unknown"},
                    {"header": "value"},
                    f'Something unknown: {status} {{"message": "Something unknown"}}',
                )

    def testShouldCreateExceptionWithoutMessage(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.createException(status, {}, {})
                self.assertException(exc, github.GithubException, None, status, {}, {}, f"{status} {{}}")

    def testShouldCreateExceptionWithoutOutput(self):
        for status in range(400, 600):
            with self.subTest(status=status):
                exc = self.g._Github__requester.createException(status, {}, None)
                self.assertException(exc, github.GithubException, None, status, None, {}, f"{status}")


class RequesterThrottleTestCase(Framework.TestCase):
    def setUp(self):
        self.setPerPage(10)
        super().setUp()

    mock_time = [datetime.now(timezone.utc)]

    def sleep(self, seconds):
        self.mock_time[0] = self.mock_time[0] + timedelta(seconds=seconds)

    def now(self, tz=None):
        return self.mock_time[0]

    @contextlib.contextmanager
    def mock_sleep(self):
        with mock.patch("github.Requester.time.sleep", side_effect=self.sleep) as sleep_mock, mock.patch(
            "github.Requester.datetime"
        ) as datetime_mock:
            datetime_mock.now = self.now
            yield sleep_mock


class RequesterUnThrottled(RequesterThrottleTestCase):
    def testShouldNotDeferRequests(self):
        with self.mock_sleep() as sleep_mock:
            # same test setup as in RequesterThrottled.testShouldDeferRequests
            with self.replayData("RequesterThrottleTestCase.testDeferRequests.txt"):
                repository = self.g.get_repo(REPO_NAME)
                releases = list(repository.get_releases())
                self.assertEqual(len(releases), 30)

        sleep_mock.assert_not_called()


class RequesterThrottled(RequesterThrottleTestCase):
    def setUp(self):
        self.setSecondsBetweenRequests(1.0)
        self.setSecondsBetweenWrites(3.0)
        super().setUp()

    def testShouldDeferRequests(self):
        with self.mock_sleep() as sleep_mock:
            with self.replayData("RequesterThrottleTestCase.testDeferRequests.txt"):
                # same test setup as in RequesterUnThrottled.testShouldNotDeferRequests
                repository = self.g.get_repo(REPO_NAME)
                releases = [release for release in repository.get_releases()]
                self.assertEqual(len(releases), 30)

        self.assertEqual(sleep_mock.call_args_list, [mock.call(1), mock.call(1), mock.call(1)])

    def testShouldDeferWrites(self):
        with self.mock_sleep() as sleep_mock:
            # same test setup as in AuthenticatedUser.testEmail
            user = self.g.get_user()
            emails = user.get_emails()
            self.assertEqual(
                [item.email for item in emails],
                ["vincent@vincent-jacques.net", "github.com@vincent-jacques.net"],
            )
            self.assertTrue(emails[0].primary)
            self.assertTrue(emails[0].verified)
            self.assertEqual(emails[0].visibility, "private")
            user.add_to_emails("1@foobar.com", "2@foobar.com")
            self.assertEqual(
                [item.email for item in user.get_emails()],
                [
                    "vincent@vincent-jacques.net",
                    "1@foobar.com",
                    "2@foobar.com",
                    "github.com@vincent-jacques.net",
                ],
            )
            user.remove_from_emails("1@foobar.com", "2@foobar.com")
            self.assertEqual(
                [item.email for item in user.get_emails()],
                ["vincent@vincent-jacques.net", "github.com@vincent-jacques.net"],
            )

        self.assertEqual(
            sleep_mock.call_args_list,
            [
                # g.get_user() does not call into GitHub API
                # user.get_emails() is the first request so no waiting needed
                # user.add_to_emails is a write request, this is the first write request
                mock.call(1),
                # user.get_emails() is a read request
                mock.call(1),
                # user.remove_from_emails is a write request, it has to be 3 seconds after the last write
                mock.call(2),
                # user.get_emails() is a read request
                mock.call(1),
            ],
        )
