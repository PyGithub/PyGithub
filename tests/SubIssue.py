#!/usr/bin/env python
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Changyong Um <e7217@naver.com>                                #
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

from . import Framework


class SubIssue(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
        self.issue = self.repo.get_issue(5)

    def testListSubIssues(self):
        """
        Test listing sub-issues of an issue.
        """
        self.assertListKeyEqual(self.issue.get_sub_issues(), lambda s: s.number, [34, 35])

    def testAddSubIssue(self):
        """
        Test adding a sub-issue to an issue.
        """
        initial_sub_issues = list(self.issue.get_sub_issues())
        self.assertListKeyEqual(initial_sub_issues, lambda s: s.number, [34, 35, 38])

        sub_issue = self.repo.get_issue(39)
        self.issue.add_sub_issue(sub_issue)

        updated_sub_issues = list(self.issue.get_sub_issues())
        self.assertListKeyEqual(updated_sub_issues, lambda s: s.number, [34, 35, 38, 39])

    def testRemoveSubIssue(self):
        """
        Test removing a sub-issue from an issue.
        """
        initial_sub_issues = list(self.issue.get_sub_issues())
        self.assertListKeyEqual(initial_sub_issues, lambda s: s.number, [34, 35, 38, 39])

        sub_issue = self.repo.get_issue(39)
        self.issue.remove_sub_issue(sub_issue)

        updated_sub_issues = list(self.issue.get_sub_issues())
        self.assertListKeyEqual(updated_sub_issues, lambda s: s.number, [34, 35, 38])

    def testPrioritizeSubIssue(self):
        """
        Test changing the priority of a sub-issue.
        """
        initial_sub_issues = list(self.issue.get_sub_issues())
        self.assertListKeyEqual(initial_sub_issues, lambda s: s.number, [34, 35, 38])

        sub_issue = self.repo.get_issue(35)
        after_issue = self.repo.get_issue(38)
        self.issue.prioritize_sub_issue(sub_issue, after_issue)

        updated_sub_issues = list(self.issue.get_sub_issues())
        self.assertListKeyEqual(updated_sub_issues, lambda s: s.number, [34, 38, 35])
