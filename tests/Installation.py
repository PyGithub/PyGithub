############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
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

import datetime

from . import Framework


class Installation(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.installation = self.g.get_installation_by_id(12482183)

    def testAttributes(self):
        installation = self.installation
        self.assertEqual(
            installation.access_tokens_url,
            "https://api.github.com/app/installations/12482183/access_tokens",
        )
        self.assertEqual(installation.account.login, "dhruvmanila")
        self.assertEqual(installation.app_id, 85429)
        self.assertEqual(installation.app_slug, "test-pygithub")
        self.assertEqual(
            installation.created_at, datetime.datetime(2020, 10, 19, 16, 30, 7)
        )
        self.assertListEqual(
            installation.events,
            [
                "check_run",
                "check_suite",
                "issues",
                "issue_comment",
                "pull_request",
                "pull_request_review",
                "pull_request_review_comment",
                "push",
                "workflow_run",
            ],
        )
        self.assertFalse(installation.has_multiple_single_files)
        self.assertEqual(
            installation.html_url, "https://github.com/settings/installations/12482183"
        )
        self.assertEqual(installation.id, 12482183)
        self.assertDictEqual(
            installation.permissions,
            {
                "checks": "write",
                "issues": "write",
                "actions": "write",
                "contents": "write",
                "metadata": "read",
                "workflows": "write",
                "pull_requests": "write",
            },
        )
        self.assertEqual(
            installation.repositories_url,
            "https://api.github.com/installation/repositories",
        )
        self.assertEqual(installation.repository_selection, "selected")
        self.assertIsNone(installation.single_file_name)
        self.assertListEqual(installation.single_file_paths, [])
        self.assertEqual(installation.target_id, 67177269)
        self.assertEqual(installation.target_type, "User")
        self.assertEqual(
            installation.updated_at, datetime.datetime(2020, 12, 18, 2, 25, 54)
        )
        self.assertEqual(repr(installation), "Installation(id=12482183)")
