############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2016 humbug <bah>                                                  #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Tuuu Nya <yuzesheji@qq.com>                                   #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

import pickle
from unittest import mock

import github

from . import Framework


class Exceptions(Framework.TestCase):
    def testInvalidInput(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.g.get_user().create_key("Bad key", "xxx")
        self.assertIsInstance(raisedexp.exception, github.GithubException)
        self.assertEqual(raisedexp.exception.message, "Validation Failed")
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "errors": [
                    {
                        "code": "custom",
                        "field": "key",
                        "message": "key is invalid. It must begin with 'ssh-rsa' or 'ssh-dss'. Check that you're copying the public half of the key",
                        "resource": "PublicKey",
                    }
                ],
                "message": "Validation Failed",
            },
        )

    def testNonJsonDataReturnedByGithub(self):
        # Replay data was forged according to https://github.com/jacquev6/PyGithub/pull/182
        with self.assertRaises(github.GithubException) as raisedexp:
            # 503 would be retried, disable retries
            self.get_github(self.authMode, retry=None).get_user("jacquev6")
        self.assertIsInstance(raisedexp.exception, github.GithubException)
        self.assertIsNone(raisedexp.exception.message)
        self.assertEqual(raisedexp.exception.status, 503)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "data": "<html><body><h1>503 Service Unavailable</h1>No server is available to handle this request.</body></html>",
            },
        )

    def testUnknownObject(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.g.get_user().get_repo("Xxx")
        self.assertIsInstance(raisedexp.exception, github.UnknownObjectException)
        self.assertIsNone(raisedexp.exception.message)
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(raisedexp.exception.data, {"message": "Not Found"})
        self.assertEqual(str(raisedexp.exception), '404 {"message": "Not Found"}')

    def testUnknownUser(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.g.get_user("ThisUserShouldReallyNotExist")
        self.assertIsInstance(raisedexp.exception, github.UnknownObjectException)
        self.assertIsNone(raisedexp.exception.message)
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(raisedexp.exception.data, {"message": "Not Found"})
        self.assertEqual(str(raisedexp.exception), '404 {"message": "Not Found"}')

    def testBadAuthentication(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            github.Github(auth=github.Auth.Login("BadUser", "BadPassword")).get_user().login
        self.assertIsInstance(raisedexp.exception, github.BadCredentialsException)
        self.assertIsNone(raisedexp.exception.message)
        self.assertEqual(raisedexp.exception.status, 401)
        self.assertEqual(raisedexp.exception.data, {"message": "Bad credentials"})
        self.assertEqual(str(raisedexp.exception), '401 {"message": "Bad credentials"}')

    def testExceptionPickling(self):
        pickle.loads(pickle.dumps(github.GithubException("foo", "bar", None)))

    def testJSONParseError(self):
        # Replay data was forged to force a JSON error
        with self.assertRaises(ValueError):
            self.g.get_user("jacquev6")


class SpecificExceptions(Framework.TestCase):
    def testBadCredentials(self):
        self.assertRaises(
            github.BadCredentialsException,
            lambda: github.Github(auth=github.Auth.Login("BadUser", "BadPassword")).get_user().login,
        )

    def test2FARequired(self):
        self.assertRaises(
            github.TwoFactorException,
            lambda: github.Github(auth=github.Auth.Login("2fauser", "password")).get_user().login,
        )

    def testUnknownObject(self):
        self.assertRaises(github.UnknownObjectException, lambda: self.g.get_user().get_repo("Xxx"))

    def testBadUserAgent(self):
        self.assertRaises(
            github.BadUserAgentException,
            lambda: github.Github(auth=self.oauth_token, user_agent="").get_user().name,
        )

    def testRateLimitExceeded(self):
        # rate limit errors would be retried if retry is not set None
        g = github.Github(retry=None)

        def exceed():
            for i in range(100):
                g.get_user("jacquev6")

        self.assertRaises(github.RateLimitExceededException, exceed)

    def testAuthenticatedRateLimitExceeded(self):
        def exceed():
            for i in range(100):
                res = self.g.search_code("jacquev6")
                res.get_page(0)

        with self.assertRaises(github.RateLimitExceededException) as raised:
            exceed()
        self.assertEqual(raised.exception.headers.get("retry-after"), "60")

    def testIncompletableObject(self):
        github.UserKey.UserKey.setCheckAfterInitFlag(False)
        obj = github.UserKey.UserKey(mock.MagicMock(), {}, {}, False)
        self.assertRaises(github.IncompletableObject, obj._completeIfNeeded)
