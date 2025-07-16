#!/usr/bin/env python

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Changyong Um <eum6211@gmail.com>                              #
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
        self.issue = self.repo.get_issue(28)

    def testListSubIssues(self):
        """
        Test listing sub-issues of an issue.
        """
        sub_issues = [self.issue.get_sub_issues()]

        self.assertEqual(_sub_issues[0].number, 30)
        self.assertEqual(_sub_issues[0].title, "Sub-issue title")
        self.assertEqual(len(_sub_issues), 2)

    def testAddSubIssue(self):
        """
        Test adding a sub-issue to an issue.
        """
        sub_issue = self.repo.get_issue(31)
        result = self.issue.add_sub_issue(sub_issue.id)
        self.assertEqual(result.id, sub_issue.id)
        self.assertEqual(result.number, sub_issue.number)
        self.assertEqual(result.title, sub_issue.title)

    def testRemoveSubIssue(self):
        """
        Test removing a sub-issue from an issue.
        """
        sub_issue = self.repo.get_issue(30)
        result = self.issue.remove_sub_issue(sub_issue.id)
        self.assertEqual(result.id, sub_issue.id)
        self.assertEqual(result.number, sub_issue.number)
        self.assertEqual(result.title, sub_issue.title)

    def testReprioritizeSubIssue(self):
        """
        Test changing the priority of a sub-issue.
        """
        sub_issue = self.repo.get_issue(30)
        after_issue = self.repo.get_issue(31)
        result = self.issue.reprioritize_sub_issue(sub_issue.id, after_issue.id)
        self.assertEqual(result.id, sub_issue.id)
        self.assertEqual(result.number, sub_issue.number)
        self.assertEqual(result.title, sub_issue.title)
