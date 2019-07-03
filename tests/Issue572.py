# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
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

import Framework

import github


class Issue572(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testIssueAsPullRequest(self):
        issue = self.repo.get_issue(2)
        pull = issue.as_pull_request()
        self.assertEqual(issue.html_url, pull.html_url)
        self.assertTrue(isinstance(pull, github.PullRequest.PullRequest))

    def testPullReqeustAsIssue(self):
        pull = self.repo.get_pull(2)
        issue = pull.as_issue()
        self.assertEqual(pull.html_url, issue.html_url)
        self.assertTrue(isinstance(issue, github.Issue.Issue))
