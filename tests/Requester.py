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
# Copyright 2026 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2026 Noethix <ryuga.rago1111@gmail.com>                            #
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

import contextlib
import json
import pickle
from datetime import datetime, timedelta, timezone
from unittest import mock

import github
from github import Consts
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
            api_version="version",
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
                api_version="version",
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
            api_version="version",
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
                api_version="version",
            ),
        )

    def testApiVersion(self):
        def requester(version: str | None) -> gr.Requester:
            return gr.Requester(
                auth=None,
                base_url=Consts.DEFAULT_BASE_URL,
                timeout=Consts.DEFAULT_TIMEOUT,
                user_agent=Consts.DEFAULT_USER_AGENT,
                per_page=Consts.DEFAULT_PER_PAGE,
                verify=True,
                retry=github.GithubRetry(),
                pool_size=None,
                api_version=version,
            )

        for api_version in [None, Consts.API_VERSION_2022_11_28, Consts.API_VERSION_2026_03_10, "version"]:
            r = requester(api_version)
            self.assertEqual(r.api_version, api_version)

            with self.captureRequests() as requests:
                # endpoint /rate_limit should contain the item "rate" for version "2022-11-28", but not for later versions
                # json = r.requestJson("GET", "/rate_limit")
                json = r.requestJson("GET", "/repos/PyGithub/PyGithub")

            self.assertIsNotNone(json)
            status, header, body = json
            self.assertEqual(status, 200)
            # you would expect the endpoint to fail for unknown / unsupported versions
            # and return "x-github-api-version-selected": api_version for supported ones
            # if api_version in [Consts.API_VERSION_2022_11_28, Consts.API_VERSION_2026_03_10]:
            #    self.assertEqual(header.get("x-github-api-version-selected"), api_version)
            # else:
            self.assertEqual(header.get("x-github-api-version-selected"), "2022-11-28")
            self.assertIn('"id":3544490,', body)

            self.assertEqual(len(requests), 1)
            request_headers = requests[0].request_headers
            if api_version is None:
                self.assertNotIn(Consts.headerApiVersion, request_headers)
            else:
                self.assertEqual(request_headers.get(Consts.headerApiVersion), api_version)

    def testWithApiVersion(self):
        r = gr.Requester(
            auth=None,
            base_url=Consts.DEFAULT_BASE_URL,
            timeout=Consts.DEFAULT_TIMEOUT,
            user_agent=Consts.DEFAULT_USER_AGENT,
            per_page=Consts.DEFAULT_PER_PAGE,
            verify=True,
            retry=github.GithubRetry(),
            pool_size=None,
            api_version=None,
        )
        self.assertIsNone(r.api_version)

        r2 = r.withApiVersion(None)
        self.assertIs(r2, r)

        r3 = r2.withApiVersion("version")
        self.assertIsNot(r3, r2)
        self.assertEqual(r3.api_version, "version")

        r4 = r3.withApiVersion("version")
        self.assertIs(r4, r3)

        r5 = r4.withApiVersion("version2")
        self.assertIsNot(r5, r4)
        self.assertEqual(r5.api_version, "version2")

        r6 = r5.withApiVersion(None)
        self.assertIsNot(r6, r5)
        self.assertIsNot(r6, r)
        self.assertIsNone(r6.api_version)

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
            "https://github.com/api?page=2&per_page=10",
            gr.Requester.add_parameters_to_url("https://github.com/api", {"per_page": 10, "page": 2}),
        )
        self.assertEqual(
            "https://github.com/api?page=2&per_page=10",
            gr.Requester.add_parameters_to_url("https://github.com/api?per_page=10", {"page": 2}),
        )
        self.assertEqual(
            "https://github.com/api?page=2&per_page=10",
            gr.Requester.add_parameters_to_url("https://github.com/api?per_page=10&page=1", {"page": 2}),
        )
        self.assertEqual(
            "https://github.com/api?item=3&item=4",
            gr.Requester.add_parameters_to_url("https://github.com/api?item=1&item=2&item=3", {"item": [3, 4]}),
        )
        self.assertEqual(
            "https://github.com/api?all=true&participating=false",
            gr.Requester.add_parameters_to_url("https://github.com/api", {"all": True, "participating": False}),
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
        assert self.g.requester.__hostnameHasDomain("github.com", ["github.com", "githubusercontent.com"])
        assert self.g.requester.__hostnameHasDomain("api.github.com", ["github.com", "githubusercontent.com"])
        assert self.g.requester.__hostnameHasDomain("githubusercontent.com", ["github.com", "githubusercontent.com"])
        assert self.g.requester.__hostnameHasDomain(
            "objects.githubusercontent.com", ["github.com", "githubusercontent.com"]
        )
        assert self.g.requester.__hostnameHasDomain("maliciousgithub.com", "github.com") is False
        assert self.g.requester.__hostnameHasDomain("abc.def", ["github.com", "githubusercontent.com"]) is False

    def testAssertUrlAllowed(self):
        # default github.com requester
        requester = self.g.requester
        self.assertEqual(set(requester.__domains), {"github.com", "githubusercontent.com"})

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
        self.assertEqual(set(requester.__domains), {"prod.ghe.local"})

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

        # custom (Enterprise) requester with api subdomain and prefix
        requester = github.Github(base_url="https://api.prod.ghe.local/github-api/").requester
        self.assertEqual(set(requester.__domains), {"api.prod.ghe.local", "prod.ghe.local"})

        for allowed in [
            "https://api.prod.ghe.local/github-api/request",
            "https://prod.ghe.local/path",
            "https://uploads.prod.ghe.local/path",
            "https://status.prod.ghe.local/path",
        ]:
            requester.__assertUrlAllowed(allowed)

        for not_allowed, arg in [
            ("https://api.prod.ghe.local/path", "/path"),
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
        # default github.com requester (empty prefix)
        requester = self.g.requester
        self.assertEqual("/request", requester.__makeAbsoluteUrl("/request"))
        self.assertEqual("/request?param=value", requester.__makeAbsoluteUrl("/request?param=value"))
        self.assertEqual("/request", requester.__makeAbsoluteUrl("https://github.com/request"))
        self.assertEqual("/request?param=value", requester.__makeAbsoluteUrl("https://github.com/request?param=value"))

        # default base_url with a trailing slash must not produce a doubled slash
        requester = github.Github(base_url="https://api.github.com/").requester
        self.assertEqual("/request", requester.__makeAbsoluteUrl("/request"))
        self.assertEqual("/request?param=value", requester.__makeAbsoluteUrl("/request?param=value"))

        # GHE requester with /api/v3 prefix and a trailing slash
        requester = github.Github(base_url="https://ghe.example.com/api/v3/").requester
        self.assertEqual("/api/v3/request", requester.__makeAbsoluteUrl("/request"))
        self.assertEqual("/api/v3/request?param=value", requester.__makeAbsoluteUrl("/request?param=value"))

        # custom (Enterprise) requester with different prefix and a trailing slash
        requester = github.Github(base_url="https://api.enterprise.ghe.com/github-api/").requester
        self.assertEqual("/github-api/request", requester.__makeAbsoluteUrl("/request"))
        self.assertEqual("/github-api/request?param=value", requester.__makeAbsoluteUrl("/request?param=value"))
        # absolute URLs returned by the server (pagination links) pass through unchanged
        self.assertEqual(
            "/github-api/request",
            requester.__makeAbsoluteUrl("https://api.enterprise.ghe.com/github-api/request"),
        )
        self.assertEqual("/request?param=value", requester.__makeAbsoluteUrl("https://github.com/request?param=value"))

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

    def _requestWithHeaders(self, requester, headers):
        with mock.patch.object(requester, "_Requester__requestRaw", return_value=(200, headers, "{}")):
            requester.requestJsonAndCheck("GET", "/some/path")

    @staticmethod
    def _rateLimitHeaders(resource, limit, remaining, used, reset):
        return {
            "x-ratelimit-limit": limit,
            "x-ratelimit-remaining": remaining,
            "x-ratelimit-used": used,
            "x-ratelimit-reset": reset,
            "x-ratelimit-resource": resource,
        }

    def assertRate(self, rate, limit, remaining, used, reset):
        self.assertEqual(rate.limit, limit)
        self.assertEqual(rate.remaining, remaining)
        self.assertEqual(rate.used, used)
        self.assertEqual(rate.reset, datetime.fromtimestamp(reset, tz=timezone.utc))

    def testCurrentRateLimitWithoutResponses(self):
        overview = self.g.requester.current_rate_limit
        self.assertIsInstance(overview, github.RateLimitOverview.RateLimitOverview)
        self.assertIsNone(overview.rate)
        self.assertIsNone(overview.resources.core)
        self.assertIsNone(overview.resources.search)

    def testCurrentRateLimitKeepsResourcesApart(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        self._requestWithHeaders(requester, self._rateLimitHeaders("search", "30", "29", "1", "1700000060"))

        overview = requester.current_rate_limit
        self.assertRate(overview.rate, 5000, 4999, 1, 1700000000)
        self.assertRate(overview.resources.core, 5000, 4999, 1, 1700000000)
        self.assertRate(overview.resources.search, 30, 29, 1, 1700000060)
        self.assertIsNone(overview.resources.graphql)

    def testCurrentRateLimitProvidesLatestValues(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        earlier = requester.current_rate_limit

        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4998", "2", "1700000000"))
        self.assertRate(requester.current_rate_limit.resources.core, 5000, 4998, 2, 1700000000)

        # an overview earlier provided is a snapshot, it does not change with later responses
        self.assertRate(earlier.resources.core, 5000, 4999, 1, 1700000000)

    def testCurrentRateLimitWithoutCoreResource(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("graphql", "5000", "4900", "100", "1700000000"))

        overview = requester.current_rate_limit
        self.assertIsNone(overview.rate)
        self.assertRate(overview.resources.graphql, 5000, 4900, 100, 1700000000)

    def testCurrentRateLimitWithFloatHeaderValues(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000.0", "4999.0", "1.0", "1700000000.0"))
        self.assertRate(requester.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)

    def testCurrentRateLimitWithoutUsedHeader(self):
        requester = self.g.requester
        headers = self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000")
        del headers["x-ratelimit-used"]
        self._requestWithHeaders(requester, headers)

        core = requester.current_rate_limit.resources.core
        self.assertEqual(core.remaining, 4999)
        self.assertIsNone(core.used)

    def testCurrentRateLimitIgnoresResponsesWithoutResource(self):
        requester = self.g.requester
        headers = self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000")
        del headers["x-ratelimit-resource"]
        self._requestWithHeaders(requester, headers)
        self._requestWithHeaders(requester, {})

        self.assertIsNone(requester.current_rate_limit.resources.core)
        self.assertEqual(requester.rate_limiting, (4999, 5000))

    def testCurrentRateLimitWithUnknownResource(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("new_resource", "10", "9", "1", "1700000000"))

        overview = requester.current_rate_limit
        self.assertIsNone(overview.resources.core)
        self.assertEqual(overview.raw_data["resources"]["new_resource"]["remaining"], 9)

    def testCurrentRateLimitRawDataIsIndependent(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))

        requester.current_rate_limit.raw_data["resources"]["core"]["remaining"] = 0
        self.assertEqual(requester.current_rate_limit.resources.core.remaining, 4999)

    def testCurrentRateLimitAfterPickle(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        restored = pickle.loads(pickle.dumps(requester))
        self.assertRate(restored.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)

    def _getRateLimit(self, requester, body):
        headers = self._rateLimitHeaders("core", "5000", "4990", "10", "1700000000")
        with mock.patch.object(
            requester, "_Requester__requestRaw", return_value=(200, headers, json.dumps(body))
        ) as raw:
            result = requester.get_rate_limit()
        raw.assert_called_once()
        self.assertEqual(raw.call_args.args[1:3], ("GET", "/rate_limit"))
        return result

    RATE_LIMIT_BODY = {
        "resources": {
            "core": {"limit": 5000, "used": 10, "remaining": 4990, "reset": 1700000000},
            "search": {"limit": 30, "used": 2, "remaining": 28, "reset": 1700000060},
        }
    }

    def testCurrentRateLimitSharedWithDerivedRequesters(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))

        for name, derived in [
            ("withLazy", requester.withLazy(not requester.is_lazy)),
            ("withApiVersion", requester.withApiVersion("2026-03-10")),
            ("chained", requester.withLazy(not requester.is_lazy).withApiVersion("2026-03-10")),
        ]:
            with self.subTest(name):
                self.assertIsNot(derived, requester)

                # known values are available to the derived requester
                self.assertRate(derived.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)

                # values seen by the derived requester are available to the original requester, and vice versa
                self._requestWithHeaders(derived, self._rateLimitHeaders("search", "30", "29", "1", "1700000060"))
                self.assertRate(requester.current_rate_limit.resources.search, 30, 29, 1, 1700000060)
                self._requestWithHeaders(requester, self._rateLimitHeaders("search", "30", "28", "2", "1700000060"))
                self.assertRate(derived.current_rate_limit.resources.search, 30, 28, 2, 1700000060)

    def testCurrentRateLimitSharedWithGithubWithLazy(self):
        for lazy in [True, False]:
            with self.subTest(lazy=lazy):
                g = github.Github(auth=github.Auth.Token("token"))
                self._assertCurrentRateLimitShared(g.requester, g.withLazy(lazy).requester)

    def testCurrentRateLimitSharedWithGithubIntegrationWithLazy(self):
        for lazy in [True, False]:
            with self.subTest(lazy=lazy):
                gi = github.GithubIntegration(auth=github.Auth.AppAuth(APP_ID, PRIVATE_KEY))
                self._assertCurrentRateLimitShared(gi.requester, gi.withLazy(lazy).requester)

    def _assertCurrentRateLimitShared(self, requester, derived):
        self.assertIsNot(derived, requester)
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        self.assertRate(derived.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)
        self._requestWithHeaders(derived, self._rateLimitHeaders("search", "30", "29", "1", "1700000060"))
        self.assertRate(requester.current_rate_limit.resources.search, 30, 29, 1, 1700000060)

    def testCurrentRateLimitOfObjectFromGithubWithLazy(self):
        self._requestWithHeaders(self.g.requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        repo = self.g.withLazy(True).get_repo("lazy/repo")
        self.assertRate(repo.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)

    def testUseCurrentRateLimit(self):
        requester = self.g.requester
        other = requester.withAuth(github.Auth.Token("other token"))
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        self._requestWithHeaders(other, self._rateLimitHeaders("search", "30", "29", "1", "1700000060"))

        other.useCurrentRateLimit(requester)

        # the requester drops its own values
        self.assertRate(other.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)
        self.assertIsNone(other.current_rate_limit.resources.search)

    def testCurrentRateLimitOfLazyObject(self):
        requester = self.g.requester
        self.assertFalse(requester.is_lazy)
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))

        user = self.g.get_user("login", lazy=True)
        self.assertIsNot(user.requester, requester)
        self.assertRate(user.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)

    def testCurrentRateLimitOfGithub(self):
        g = github.Github(auth=github.Auth.Token("token"))
        self.assertIsNone(g.current_rate_limit.resources.core)
        self._requestWithHeaders(g.requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        self.assertRate(g.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)

    def testCurrentRateLimitOfGithubIntegration(self):
        gi = github.GithubIntegration(auth=github.Auth.AppAuth(APP_ID, PRIVATE_KEY))
        self.assertIsNone(gi.current_rate_limit.resources.core)
        self._requestWithHeaders(gi.requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        self.assertRate(gi.current_rate_limit.resources.core, 5000, 4999, 1, 1700000000)

    def testCurrentRateLimitSharingByArgument(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))

        for arguments, shared in [
            (dict(auth=github.Auth.Token("other token")), False),
            (dict(auth=None), False),
            (dict(base_url="https://github.example.com/api/v3"), False),
            (dict(auth=github.Auth.Token("other token"), base_url="https://github.example.com/api/v3"), False),
            (dict(timeout=1), True),
            (dict(user_agent="agent"), True),
            (dict(per_page=1), True),
            (dict(verify=False), True),
            (dict(retry=1), True),
            (dict(pool_size=1), True),
            (dict(seconds_between_requests=1.0), True),
            (dict(seconds_between_writes=1.0), True),
            (dict(lazy=True), True),
            (dict(api_version="2026-03-10"), True),
        ]:
            with self.subTest(arguments=sorted(arguments)):
                other = requester._Requester__withArguments(**arguments)
                self.assertIsNot(other, requester)
                core = other.current_rate_limit.resources.core
                if shared:
                    self.assertRate(core, 5000, 4999, 1, 1700000000)
                else:
                    self.assertIsNone(core)

    def testCurrentRateLimitNotSharedAcrossAuthentications(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))

        other = requester.withAuth(github.Auth.Token("other token"))
        self.assertIsNone(other.current_rate_limit.resources.core)

        self._requestWithHeaders(other, self._rateLimitHeaders("search", "30", "29", "1", "1700000060"))
        self.assertIsNone(requester.current_rate_limit.resources.search)

        # a requester derived from another authentication shares with that authentication only
        derived = other.withApiVersion("2026-03-10")
        self.assertRate(derived.current_rate_limit.resources.search, 30, 29, 1, 1700000060)
        self.assertIsNone(derived.current_rate_limit.resources.core)

    def testGetRateLimitUpdatesCurrentRateLimit(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        self._requestWithHeaders(requester, self._rateLimitHeaders("graphql", "5000", "4900", "100", "1700000000"))

        self._getRateLimit(requester, self.RATE_LIMIT_BODY)

        overview = requester.current_rate_limit
        self.assertRate(overview.rate, 5000, 4990, 10, 1700000000)
        self.assertRate(overview.resources.core, 5000, 4990, 10, 1700000000)
        self.assertRate(overview.resources.search, 30, 28, 2, 1700000060)
        # resources not contained in the response keep their values
        self.assertRate(overview.resources.graphql, 5000, 4900, 100, 1700000000)

        # later response headers replace these values
        self._requestWithHeaders(requester, self._rateLimitHeaders("search", "30", "27", "3", "1700000060"))
        self.assertRate(requester.current_rate_limit.resources.search, 30, 27, 3, 1700000060)

    def testGetRateLimitWithoutResources(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("graphql", "5000", "4900", "100", "1700000000"))
        self._getRateLimit(requester, {})
        self.assertRate(requester.current_rate_limit.resources.graphql, 5000, 4900, 100, 1700000000)

    def testGetRateLimitDoesNotShareDataWithCurrentRateLimit(self):
        requester = self.g.requester
        result = self._getRateLimit(requester, self.RATE_LIMIT_BODY)

        result.raw_data["resources"]["search"]["remaining"] = 0
        self.assertEqual(requester.current_rate_limit.resources.search.remaining, 28)

    def testRateLimitOverviewUpdate(self):
        requester = self.g.requester
        self._requestWithHeaders(requester, self._rateLimitHeaders("core", "5000", "4999", "1", "1700000000"))
        self._requestWithHeaders(requester, self._rateLimitHeaders("graphql", "5000", "4900", "100", "1700000000"))
        overview = requester.current_rate_limit

        headers = self._rateLimitHeaders("core", "5000", "4990", "10", "1700000000")
        response = (200, headers, json.dumps(self.RATE_LIMIT_BODY))
        with mock.patch.object(requester, "_Requester__requestRaw", return_value=response) as raw:
            updated = overview.update()

        raw.assert_called_once()
        self.assertEqual(raw.call_args.args[1:3], ("GET", "/rate_limit"))

        # the returned object provides what the response provides, which does not contain rate in later API versions
        self.assertIsNot(updated, overview)
        self.assertIsNone(updated.rate)
        self.assertRate(updated.resources.core, 5000, 4990, 10, 1700000000)
        self.assertRate(updated.resources.search, 30, 28, 2, 1700000060)
        self.assertIsNone(updated.resources.graphql)
        self.assertEqual(updated.raw_data["resources"], self.RATE_LIMIT_BODY["resources"])
        self.assertEqual(updated.raw_headers, headers)

        # the object itself does not change
        self.assertRate(overview.rate, 5000, 4999, 1, 1700000000)
        self.assertRate(overview.resources.core, 5000, 4999, 1, 1700000000)
        self.assertRate(overview.resources.graphql, 5000, 4900, 100, 1700000000)
        self.assertIsNone(overview.resources.search)

        # the requester's values get updated, resources not contained in the response keep their values
        current = requester.current_rate_limit
        self.assertRate(current.resources.core, 5000, 4990, 10, 1700000000)
        self.assertRate(current.resources.search, 30, 28, 2, 1700000060)
        self.assertRate(current.resources.graphql, 5000, 4900, 100, 1700000000)

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
        with (
            mock.patch("github.Requester.time.sleep", side_effect=self.sleep) as sleep_mock,
            mock.patch("github.Requester.datetime") as datetime_mock,
        ):
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
