# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import logging

import github

import Framework


class Logging(Framework.TestCase):
    class MockHandler:
        def __init__(self):
            self.level = logging.DEBUG
            self.handled = None

        def handle(self, record):
            self.handled = record.getMessage()

    def testLogging(self):
        self.maxDiff = None
        logger = github.get_logger()
        logger.setLevel(logging.DEBUG)
        handler = self.MockHandler()
        logger.addHandler(handler)

        self.assertEqual(self.g.get_user().name, "Vincent Jacques")
        self.assertEqual(handler.handled, u'GET https://api.github.com/user None None ==> 200 {\'status\': \'200 OK\', \'content-length\': \'806\', \'x-github-media-type\': \'github.beta; format=json\', \'x-content-type-options\': \'nosniff\', \'vary\': \'Accept, Authorization, Cookie\', \'x-ratelimit-remaining\': \'4993\', \'server\': \'nginx\', \'last-modified\': \'Fri, 14 Sep 2012 18:47:46 GMT\', \'connection\': \'keep-alive\', \'x-ratelimit-limit\': \'5000\', \'etag\': \'"434dfe5d3f50558fe3cea087cb95c401"\', \'cache-control\': \'private, s-maxage=60, max-age=60\', \'date\': \'Mon, 17 Sep 2012 17:12:32 GMT\', \'content-type\': \'application/json; charset=utf-8\'} {"owned_private_repos":3,"disk_usage":18612,"following":28,"type":"User","public_repos":13,"location":"Paris, France","company":"Criteo","avatar_url":"https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png","plan":{"space":614400,"private_repos":5,"name":"micro","collaborators":1},"blog":"http://vincent-jacques.net","login":"jacquev6","public_gists":3,"html_url":"https://github.com/jacquev6","hireable":false,"created_at":"2010-07-09T06:10:06Z","private_gists":5,"followers":13,"name":"Vincent Jacques","email":"vincent@vincent-jacques.net","bio":"","total_private_repos":3,"collaborators":0,"gravatar_id":"b68de5ae38616c296fa345d2b9df2225","id":327146,"url":"https://api.github.com/users/jacquev6"}')
