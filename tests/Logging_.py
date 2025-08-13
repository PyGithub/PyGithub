############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2018 R1kk3r <R1kk3r@users.noreply.github.com>                      #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jonathan Kliem <jonathan.kliem@gmail.com>                     #
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

import github
from github.Auth import Login

from . import Framework
from .Authentication import CustomAuth


class Logging(Framework.BasicTestCase):
    class MockLogger:
        def __init__(self):
            self.verb = None
            self.url = None
            self.requestHeaders = None
            self.input = None
            self.status = None
            self.responseHeaders = None
            self.output = None

        def isEnabledFor(self, kind):
            return True

        def debug(
            self,
            format_string,
            verb,
            scheme,
            hostname,
            fragment,
            requestHeaders,
            input_,
            status,
            responseHeaders,
            output,
        ):
            self.verb = verb
            self.url = f"{scheme}://{hostname}{fragment}"
            self.requestHeaders = requestHeaders
            self.input = input_
            self.status = status
            self.responseHeaders = responseHeaders
            self.output = output

    def setUp(self):
        super().setUp()
        self.logger = self.MockLogger()
        github.Requester.Requester.injectLogger(self.logger)

    def tearDown(self):
        github.Requester.Requester.resetLogger()
        super().tearDown()

    def assertLogging(self, verb, url, requestHeaders, responseHeaders, output):
        self.assertEqual(self.logger.verb, verb)
        self.assertEqual(self.logger.url, url)
        self.assertEqual(self.logger.requestHeaders, requestHeaders)
        self.assertIsNone(self.logger.input)
        self.assertEqual(self.logger.status, 200)
        self.assertEqual(self.logger.responseHeaders, responseHeaders)
        self.assertEqual(self.logger.output, output)

    def testLoggingWithBasicAuthentication(self):
        self.assertEqual(github.Github(auth=Login("login", "password")).get_user().name, "Vincent Jacques")
        url = "https://api.github.com/user"
        requestHeaders = {
            "Authorization": "Basic (login and password removed)",
            "User-Agent": "PyGithub/Python",
        }
        responseHeaders = {
            "status": "200 OK",
            "content-length": "806",
            "x-github-media-type": "github.beta; format=json",
            "x-content-type-options": "nosniff",
            "x-ratelimit-limit": "5000",
            "vary": "Accept, Authorization, Cookie",
            "x-ratelimit-remaining": "4993",
            "server": "nginx",
            "last-modified": "Fri, 14 Sep 2012 18:47:46 GMT",
            "connection": "keep-alive",
            "etag": '"434dfe5d3f50558fe3cea087cb95c401"',
            "cache-control": "private, s-maxage=60, max-age=60",
            "date": "Mon, 17 Sep 2012 17:12:32 GMT",
            "content-type": "application/json; charset=utf-8",
            "DEBUG_FRAME": 0,
        }
        output = '{"owned_private_repos":3,"disk_usage":18612,"following":28,"type":"User","public_repos":13,"location":"Paris, France","company":"Criteo","avatar_url":"https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png","plan":{"space":614400,"private_repos":5,"name":"micro","collaborators":1},"blog":"http://vincent-jacques.net","login":"jacquev6","public_gists":3,"html_url":"https://github.com/jacquev6","hireable":false,"created_at":"2010-07-09T06:10:06Z","private_gists":5,"followers":13,"name":"Vincent Jacques","email":"vincent@vincent-jacques.net","bio":"","total_private_repos":3,"collaborators":0,"gravatar_id":"b68de5ae38616c296fa345d2b9df2225","id":327146,"url":"https://api.github.com/users/jacquev6"}'
        self.assertLogging("GET", url, requestHeaders, responseHeaders, output)

    def testLoggingWithOAuthAuthentication(self):
        self.assertEqual(github.Github(auth=self.oauth_token).get_user().name, "Vincent Jacques")
        url = "https://api.github.com/user"
        requestHeaders = {
            "Authorization": "token (oauth token removed)",
            "User-Agent": "PyGithub/Python",
        }
        responseHeaders = {
            "status": "200 OK",
            "x-ratelimit-remaining": "4993",
            "x-github-media-type": "github.beta; format=json",
            "x-content-type-options": "nosniff",
            "vary": "Accept, Authorization, Cookie",
            "content-length": "628",
            "server": "nginx",
            "last-modified": "Tue, 25 Sep 2012 07:42:42 GMT",
            "connection": "keep-alive",
            "x-ratelimit-limit": "5000",
            "etag": '"c23ad6b5815fc3d6ec6341c4a47afe85"',
            "cache-control": "private, max-age=60, s-maxage=60",
            "date": "Tue, 25 Sep 2012 20:36:54 GMT",
            "x-oauth-scopes": "",
            "content-type": "application/json; charset=utf-8",
            "x-accepted-oauth-scopes": "user",
            "DEBUG_FRAME": 0,
        }
        output = '{"type":"User","bio":"","html_url":"https://github.com/jacquev6","login":"jacquev6","followers":14,"company":"Criteo","blog":"http://vincent-jacques.net","public_repos":13,"created_at":"2010-07-09T06:10:06Z","avatar_url":"https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png","email":"vincent@vincent-jacques.net","following":29,"name":"Vincent Jacques","gravatar_id":"b68de5ae38616c296fa345d2b9df2225","hireable":false,"id":327146,"public_gists":3,"location":"Paris, France","url":"https://api.github.com/users/jacquev6"}'
        self.assertLogging("GET", url, requestHeaders, responseHeaders, output)

    def testLoggingWithoutAuthentication(self):
        self.assertEqual(github.Github().get_user("jacquev6").name, "Vincent Jacques")
        url = "https://api.github.com/users/jacquev6"
        requestHeaders = {"User-Agent": "PyGithub/Python"}
        responseHeaders = {
            "status": "200 OK",
            "content-length": "628",
            "x-github-media-type": "github.beta; format=json",
            "x-content-type-options": "nosniff",
            "x-ratelimit-limit": "5000",
            "vary": "Accept",
            "x-ratelimit-remaining": "4989",
            "server": "nginx",
            "last-modified": "Tue, 25 Sep 2012 07:42:42 GMT",
            "connection": "keep-alive",
            "etag": '"9bd085221a16b6d2ea95e72634c3c1ac"',
            "cache-control": "public, max-age=60, s-maxage=60",
            "date": "Tue, 25 Sep 2012 20:38:56 GMT",
            "content-type": "application/json; charset=utf-8",
            "DEBUG_FRAME": 0,
        }
        output = '{"type":"User","html_url":"https://github.com/jacquev6","login":"jacquev6","followers":14,"company":"Criteo","created_at":"2010-07-09T06:10:06Z","email":"vincent@vincent-jacques.net","hireable":false,"avatar_url":"https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png","public_gists":3,"bio":"","following":29,"name":"Vincent Jacques","blog":"http://vincent-jacques.net","gravatar_id":"b68de5ae38616c296fa345d2b9df2225","id":327146,"public_repos":13,"location":"Paris, France","url":"https://api.github.com/users/jacquev6"}'
        self.assertLogging("GET", url, requestHeaders, responseHeaders, output)

    def testLoggingWithBaseUrl(self):
        # ReplayData forged, not recorded
        self.assertEqual(
            github.Github(base_url="http://my.enterprise.com/my/prefix").get_user("jacquev6").name,
            "Vincent Jacques",
        )
        url = "http://my.enterprise.com/my/prefix/users/jacquev6"
        requestHeaders = {"User-Agent": "PyGithub/Python"}
        responseHeaders = {
            "status": "200 OK",
            "content-length": "628",
            "x-github-media-type": "github.beta; format=json",
            "x-content-type-options": "nosniff",
            "x-ratelimit-limit": "5000",
            "vary": "Accept",
            "x-ratelimit-remaining": "4989",
            "server": "nginx",
            "last-modified": "Tue, 25 Sep 2012 07:42:42 GMT",
            "connection": "keep-alive",
            "etag": '"9bd085221a16b6d2ea95e72634c3c1ac"',
            "cache-control": "public, max-age=60, s-maxage=60",
            "date": "Tue, 25 Sep 2012 20:38:56 GMT",
            "content-type": "application/json; charset=utf-8",
            "DEBUG_FRAME": 0,
        }
        output = '{"type":"User","html_url":"https://github.com/jacquev6","login":"jacquev6","followers":14,"company":"Criteo","created_at":"2010-07-09T06:10:06Z","email":"vincent@vincent-jacques.net","hireable":false,"avatar_url":"https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png","public_gists":3,"bio":"","following":29,"name":"Vincent Jacques","blog":"http://vincent-jacques.net","gravatar_id":"b68de5ae38616c296fa345d2b9df2225","id":327146,"public_repos":13,"location":"Paris, France","url":"https://api.github.com/users/jacquev6"}'
        self.assertLogging("GET", url, requestHeaders, responseHeaders, output)

    def testLoggingDoesNotModifyRequestHeaders(self):
        # Recorded replay data already sanitizes Authorization headers, so we
        # need to go under the covers
        requestHeaders = {"Authorization": "thisisnotatoken"}
        responseHeaders = {"status": "200 OK"}
        github.Github()._Github__requester._Requester__log(
            "GET",
            "http://example.com",
            requestHeaders,
            None,
            200,
            responseHeaders,
            None,
        )
        self.assertEqual(requestHeaders["Authorization"], "thisisnotatoken")

    def testMaskingOfCustomAuthHeader(self):
        requestHeaders = {"Custom key": "secret"}
        responseHeaders = {"status": "200 OK"}
        github.Github(auth=CustomAuth())._Github__requester._Requester__log(
            "GET",
            "http://example.com",
            requestHeaders,
            None,
            200,
            responseHeaders,
            None,
        )
        self.assertEqual({"Custom key": "Masked custom header"}, self.logger.requestHeaders)
