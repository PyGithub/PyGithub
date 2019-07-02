# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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


class RequiredPullRequestReviews(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.required_pull_request_reviews = self.g.get_user().get_repo("PyGithub").get_branch("integrations").get_required_pull_request_reviews()

    def testAttributes(self):
        self.assertTrue(self.required_pull_request_reviews.dismiss_stale_reviews)
        self.assertTrue(self.required_pull_request_reviews.require_code_owner_reviews)
        self.assertEqual(self.required_pull_request_reviews.required_approving_review_count, 3)
        self.assertEqual(self.required_pull_request_reviews.url, "https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_pull_request_reviews")
        self.assertIs(self.required_pull_request_reviews.dismissal_users, None)
        self.assertIs(self.required_pull_request_reviews.dismissal_teams, None)
        self.assertEqual(self.required_pull_request_reviews.__repr__(), 'RequiredPullRequestReviews(url="https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_pull_request_reviews", require_code_owner_reviews=True, dismiss_stale_reviews=True)')

    def testOrganizationOwnedTeam(self):
        required_pull_request_reviews = self.g.get_repo("PyGithub/PyGithub", lazy=True).get_branch("integrations").get_required_pull_request_reviews()
        self.assertListKeyEqual(required_pull_request_reviews.dismissal_users, lambda u: u.login, ["jacquev6"])
        self.assertListKeyEqual(required_pull_request_reviews.dismissal_teams, lambda t: t.slug, ["pygithub-owners"])
