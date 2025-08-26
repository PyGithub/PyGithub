############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Benjamin K <53038537+treee111@users.noreply.github.com>       #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from __future__ import annotations

from . import Framework


class RequiredPullRequestReviews(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.required_pull_request_reviews = (
            self.g.get_user().get_repo("PyGithub").get_branch("integrations").get_required_pull_request_reviews()
        )

    def testAttributes(self):
        self.assertIsNone(self.required_pull_request_reviews.bypass_pull_request_allowances)
        self.assertTrue(self.required_pull_request_reviews.dismiss_stale_reviews)
        self.assertIsNone(self.required_pull_request_reviews.dismissal_restrictions)
        self.assertTrue(self.required_pull_request_reviews.require_code_owner_reviews)
        self.assertIsNone(self.required_pull_request_reviews.require_last_push_approval)
        self.assertEqual(self.required_pull_request_reviews.required_approving_review_count, 3)
        self.assertEqual(
            self.required_pull_request_reviews.url,
            "https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_pull_request_reviews",
        )
        self.assertIs(self.required_pull_request_reviews.dismissal_users, None)
        self.assertIs(self.required_pull_request_reviews.dismissal_teams, None)
        self.assertEqual(
            self.required_pull_request_reviews.__repr__(),
            'RequiredPullRequestReviews(url="https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_pull_request_reviews", require_last_push_approval=None, require_code_owner_reviews=True, dismiss_stale_reviews=True)',
        )

    def testOrganizationOwnedTeam(self):
        required_pull_request_reviews = (
            self.g.get_repo("PyGithub/PyGithub", lazy=True)
            .get_branch("integrations")
            .get_required_pull_request_reviews()
        )
        self.assertIsNone(required_pull_request_reviews.bypass_pull_request_allowances.apps)
        self.assertListKeyEqual(
            required_pull_request_reviews.bypass_pull_request_allowances.users,
            lambda u: u.login,
            ["jacquev6"],
        )
        self.assertListKeyEqual(
            required_pull_request_reviews.bypass_pull_request_allowances.teams,
            lambda t: t.slug,
            ["pygithub-owners"],
        )

        self.assertIsNone(required_pull_request_reviews.dismissal_restrictions.apps)
        self.assertListKeyEqual(
            required_pull_request_reviews.dismissal_restrictions.users,
            lambda u: u.login,
            ["jacquev6"],
        )
        self.assertListKeyEqual(
            required_pull_request_reviews.dismissal_restrictions.teams,
            lambda t: t.slug,
            ["pygithub-owners"],
        )
        self.assertEqual(
            required_pull_request_reviews.dismissal_restrictions.users_url,
            "https://api.github.com/repos/PyGithub/PyGithub/branches/integrations/protection/dismissal_restrictions/users",
        )
        self.assertEqual(
            required_pull_request_reviews.dismissal_restrictions.teams_url,
            "https://api.github.com/repos/PyGithub/PyGithub/branches/integrations/protection/dismissal_restrictions/teams",
        )

        self.assertListKeyEqual(
            required_pull_request_reviews.dismissal_users,
            lambda u: u.login,
            ["jacquev6"],
        )
        self.assertListKeyEqual(
            required_pull_request_reviews.dismissal_teams,
            lambda t: t.slug,
            ["pygithub-owners"],
        )
