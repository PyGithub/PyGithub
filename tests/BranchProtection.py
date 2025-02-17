############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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


class BranchProtection(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.branch_protection = self.g.get_repo("curvewise-forks/PyGithub").get_branch("master").get_protection()

    def testAttributes(self):
        self.assertEqual(self.branch_protection.allow_deletions, False)
        self.assertEqual(self.branch_protection.allow_force_pushes, False)
        self.assertEqual(self.branch_protection.allow_fork_syncing, False)
        self.assertEqual(self.branch_protection.block_creations, False)
        self.assertIsNone(self.branch_protection.enabled)
        self.assertEqual(self.branch_protection.enforce_admins, True)
        self.assertEqual(self.branch_protection.lock_branch, False)
        self.assertIsNone(self.branch_protection.name)
        self.assertIsNone(self.branch_protection.protection_url)
        self.assertEqual(self.branch_protection.required_conversation_resolution, False)
        self.assertEqual(self.branch_protection.required_linear_history, True)
        self.assertEqual(
            self.branch_protection.required_pull_request_reviews.url,
            "https://api.github.com/repos/curvewise-forks/PyGithub/branches/master/protection/required_pull_request_reviews",
        )
        self.assertEqual(self.branch_protection.required_signatures, False)
        self.assertTrue(self.branch_protection.required_status_checks.strict)
        self.assertEqual(self.branch_protection.required_status_checks.contexts, ["build (3.10)"])
        self.assertTrue(self.branch_protection.required_linear_history)
        self.assertIsNone(self.branch_protection.restrictions)
        self.assertEqual(
            self.branch_protection.url,
            "https://api.github.com/repos/curvewise-forks/PyGithub/branches/master/protection",
        )
        self.assertEqual(
            self.branch_protection.__repr__(),
            'BranchProtection(url="https://api.github.com/repos/curvewise-forks/PyGithub/branches/master/protection")',
        )
        self.assertFalse(self.branch_protection.allow_force_pushes)
        self.assertFalse(self.branch_protection.allow_deletions)
        self.assertFalse(self.branch_protection.required_conversation_resolution)
        self.assertFalse(self.branch_protection.lock_branch)
        self.assertFalse(self.branch_protection.allow_fork_syncing)
