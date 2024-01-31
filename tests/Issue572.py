############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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


class Issue572(Framework.TestCase):
    def setUp(self):
        super().setUp()
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
