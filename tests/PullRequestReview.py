# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Aaron Levine <allevin@sandia.gov>                             #
# Copyright 2017 Mike Miller <github@mikeage.net>                              #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Gilad Shefer <gshefer@redhat.com>                             #
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

import Framework

import datetime


class PullRequestReview(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
        self.pull = self.repo.get_pull(538)

        # Test ability to create a review
        self.created_pullreview = self.pull.create_review(
            self.repo.get_commit('2f0e4e55fe87e38d26efc9aa1346f56abfbd6c52'),
            'Some review created by PyGithub'
        )

        # Test ability to get all reviews
        self.pullreviews = self.pull.get_reviews()

        # Test ability to get a single review
        self.pullreview = self.pull.get_review(28482091)

    def testDismiss(self):
        self.pullreview.dismiss("with prejudice")
        pr = self.pull.get_review(28482091)
        self.assertEqual(pr.state, "DISMISSED")

    def testAttributes(self):
        self.assertEqual(self.pullreview.id, 28482091)
        self.assertEqual(self.pullreview.user.login, "jzelinskie")
        self.assertEqual(self.pullreview.body, "")
        self.assertEqual(self.pullreview.commit_id, "7a0fcb27b7cd6c346fc3f76216ccb6e0f4ca3bcc")
        self.assertEqual(self.pullreview.state, "APPROVED")
        self.assertEqual(self.pullreview.html_url, "https://github.com/PyGithub/PyGithub/pull/538#pullrequestreview-28482091")
        self.assertEqual(self.pullreview.pull_request_url, "https://api.github.com/repos/PyGithub/PyGithub/pulls/538")
        self.assertEqual(self.pullreview.submitted_at, datetime.datetime(2017, 3, 22, 19, 6, 59))
        self.assertIn(self.created_pullreview, self.pullreviews)

        # test __repr__() based on this attributes
        self.assertEqual(self.pullreview.__repr__(), 'PullRequestReview(user=NamedUser(login="jzelinskie"), id=28482091)')
