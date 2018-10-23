# -*- coding: utf-8 -*-

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
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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
import sys
import pickle

import Framework

atMostPython2 = sys.hexversion < 0x03000000


class Exceptions(Framework.TestCase):
    def testInvalidInput(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.g.get_user().create_key("Bad key", "xxx")
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data, {
                "errors": [
                    {
                        "code": "custom",
                        "field": "key",
                        "message": "key is invalid. It must begin with 'ssh-rsa' or 'ssh-dss'. Check that you're copying the public half of the key",
                        "resource": "PublicKey"
                    }
                ],
                "message": "Validation Failed"
            }
        )

    def testNonJsonDataReturnedByGithub(self):
        # Replay data was forged according to https://github.com/jacquev6/PyGithub/pull/182
        with self.assertRaises(github.GithubException) as raisedexp:
            self.g.get_user("jacquev6")
        self.assertEqual(raisedexp.exception.status, 503)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "data": "<html><body><h1>503 Service Unavailable</h1>No server is available to handle this request.</body></html>",
            }
        )

    def testUnknownObject(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.g.get_user().get_repo("Xxx")
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(raisedexp.exception.data, {"message": "Not Found"})
        if atMostPython2:
            self.assertEqual(str(raisedexp.exception), "404 {u'message': u'Not Found'}")
        else:
            self.assertEqual(str(raisedexp.exception), "404 {'message': 'Not Found'}")  # pragma no cover (Covered with Python 3)

    def testUnknownUser(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.g.get_user("ThisUserShouldReallyNotExist")
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(raisedexp.exception.data, {"message": "Not Found"})
        if atMostPython2:
            self.assertEqual(str(raisedexp.exception), "404 {u'message': u'Not Found'}")
        else:
            self.assertEqual(str(raisedexp.exception), "404 {'message': 'Not Found'}")  # pragma no cover (Covered with Python 3)

    def testBadAuthentication(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            github.Github("BadUser", "BadPassword").get_user().login
        self.assertEqual(raisedexp.exception.status, 401)
        self.assertEqual(raisedexp.exception.data, {"message": "Bad credentials"})
        if atMostPython2:
            self.assertEqual(str(raisedexp.exception), "401 {u'message': u'Bad credentials'}")
        else:
            self.assertEqual(str(raisedexp.exception), "401 {'message': 'Bad credentials'}")  # pragma no cover (Covered with Python 3)

    def testExceptionPickling(self):
        pickle.loads(pickle.dumps(github.GithubException('foo', 'bar')))


class SpecificExceptions(Framework.TestCase):
    def testBadCredentials(self):
        self.assertRaises(github.BadCredentialsException, lambda: github.Github("BadUser", "BadPassword").get_user().login)

    def testUnknownObject(self):
        self.assertRaises(github.UnknownObjectException, lambda: self.g.get_user().get_repo("Xxx"))

    def testBadUserAgent(self):
        self.assertRaises(github.BadUserAgentException, lambda: github.Github(self.login, self.password, user_agent="").get_user().name)

    def testRateLimitExceeded(self):
        g = github.Github()

        def exceed():
            for i in range(100):
                g.get_user("jacquev6")

        self.assertRaises(github.RateLimitExceededException, exceed)

    def testAuthenticatedRateLimitExceeded(self):

        def exceed():
            for i in range(100):
                res = self.g.search_code("jacquev6")
                res.get_page(0)

        self.assertRaises(github.RateLimitExceededException, exceed)
