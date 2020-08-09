# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Raju Subramanian <coder@mahesh.net>                           #
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
from datetime import datetime


class CheckSuite(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.check_suite_id = 1004503837
        self.repo = self.g.get_repo("wrecker/PySample")
        self.check_suite = self.repo.get_check_suite(self.check_suite_id)
        self.check_suite_ref = "fd09d934bcce792176d6b79d6d0387e938b62b7a"
        self.commit = self.repo.get_commit("fd09d934bcce792176d6b79d6d0387e938b62b7a")

    def testAttributes(self):
        cs = self.check_suite
        self.assertEqual(cs.after, "fd09d934bcce792176d6b79d6d0387e938b62b7a")
        self.assertEqual(cs.app.slug, "github-actions")
        self.assertEqual(cs.before, "9ee0caba8648aa0b8b5fc68ebc37c3c1162aa283")
        self.assertEqual(
            cs.check_runs_url,
            "https://api.github.com/repos/wrecker/PySample/check-suites/1004503837/check-runs",
        )
        self.assertEqual(cs.conclusion, "success")
        self.assertEqual(cs.created_at, datetime(2020, 8, 4, 5, 6, 54))
        self.assertEqual(cs.head_branch, "wrecker-patch-1")
        self.assertEqual(cs.head_commit.sha, "fd09d934bcce792176d6b79d6d0387e938b62b7a")
        self.assertEqual(cs.head_sha, "fd09d934bcce792176d6b79d6d0387e938b62b7a")
        self.assertEqual(cs.id, self.check_suite_id)
        self.assertEqual(cs.latest_check_runs_count, 2)
        self.assertEqual(cs.id, self.check_suite_id)
        self.assertEqual(len(cs.pull_requests), 1)
        self.assertEqual(cs.pull_requests[0].id, 462527907)
        self.assertEqual(
            cs.repository.url, "https://api.github.com/repos/wrecker/PySample"
        )
        self.assertEqual(cs.status, "completed")
        self.assertEqual(cs.updated_at, datetime(2020, 8, 4, 5, 7, 40))
        self.assertEqual(
            cs.url,
            "https://api.github.com/repos/wrecker/PySample/check-suites/1004503837",
        )

    def testGetCheckSuitesForRef(self):
        check_suites = self.commit.get_check_suites()
        self.assertEqual(check_suites.totalCount, 6)
        self.assertListEqual(
            [cs.id for cs in check_suites],
            [1004503392, 1004503393, 1004503395, 1004503397, 1004503837, 1004503857],
        )

    def testGetCheckSuitesForRefFilterByAppId(self):
        check_suites = self.commit.get_check_suites(app_id=29110)
        self.assertEqual(check_suites.totalCount, 1)
        self.assertListEqual([cs.id for cs in check_suites], [1004503392])

    def testGetCheckSuitesForRefFilterByCheckName(self):
        check_suites = self.commit.get_check_suites(check_name="Alex")
        self.assertEqual(check_suites.totalCount, 1)
        self.assertListEqual([cs.id for cs in check_suites], [1004503395])

    def testCheckSuiteRerequest(self):
        cs = self.repo.get_check_suite(1004503395)
        status = cs.rerequest()
        self.assertTrue(status)
