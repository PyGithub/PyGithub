# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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
# ##############################################################################

import Framework

import datetime


class PullRequestReview(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
#        self.pullreview = self.g.get_user().get_repo("PyGithub").get_pull(538).get_review(1):
        self.pullreview = self.g.get_user().get_repo("PyGithub").get_pull(538).get_reviews(self)
        for ireview in self.pullreview.get_reviews():
            iuser     = xstr(ireview.user.login) + " (" + xstr(ireview.user.name) + ")"
            istate    = xstr(ireview.state)
            print("* Review #{0} was {1} by User: {2}; For Commit {3}: Comment = {4}".format(ireview.id, istate, iuser, ireview.commit_id, ireview.body))
            print("*   HTML_URL = {0}".format(ireview.html_url))
            print("*   Pull Request URL = {0}".format(ireview.pull_request_url))

    def testAttributes(self):
        self.assertEqual(self.pullreview.body, "Comment created by PyGithub")
        self.assertEqual(self.pullreview.commit_id, "8a4f306d4b223682dd19410d4a9150636ebe4206")
        self.assertEqual(self.pullreview.id, 886298)
        self.assertEqual(self.pullreview.state, "src/github/Issue.py")
        self.assertEqual(self.pullreview.user.login, "jacquev6")
        self.assertEqual(self.pullreview.html_url, "https://github.com/jacquev6/PyGithub/pull/170#issuecomment-18637907")
        self.assertEqual(self.pullreview.pull_request_url, "https://github.com/jacquev6/PyGithub/pull/170#issuecomment-18637907")

        # test __repr__() based on this attributes
        self.assertEqual(self.comment.__repr__(), 'PullRequestReview(id=886298, user=NamedUser(login="jacquev6"))')
