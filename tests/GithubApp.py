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

from datetime import datetime, timezone

from . import Framework


class GithubApp(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.app_slug = "github-actions"

    def testGetPublicApp(self):
        app = self.g.get_app(slug=self.app_slug)
        self.assertEqual(
            app.created_at, datetime(2018, 7, 30, 9, 30, 17, tzinfo=timezone.utc)
        )
        self.assertEqual(
            app.description, "Automate your workflow from idea to production"
        )
        self.assertListEqual(
            app.events,
            [
                "check_run",
                "check_suite",
                "create",
                "delete",
                "deployment",
                "deployment_status",
                "fork",
                "gollum",
                "issues",
                "issue_comment",
                "label",
                "milestone",
                "page_build",
                "project",
                "project_card",
                "project_column",
                "public",
                "pull_request",
                "pull_request_review",
                "pull_request_review_comment",
                "push",
                "registry_package",
                "release",
                "repository",
                "repository_dispatch",
                "status",
                "watch",
                "workflow_dispatch",
                "workflow_run",
            ],
        )
        self.assertEqual(app.external_url, "https://help.github.com/en/actions")
        self.assertEqual(app.html_url, "https://github.com/apps/github-actions")
        self.assertEqual(app.id, 15368)
        self.assertEqual(app.name, "GitHub Actions")
        self.assertEqual(app.owner.login, "github")
        self.assertDictEqual(
            app.permissions,
            {
                "actions": "write",
                "checks": "write",
                "contents": "write",
                "deployments": "write",
                "issues": "write",
                "metadata": "read",
                "packages": "write",
                "pages": "write",
                "pull_requests": "write",
                "repository_hooks": "write",
                "repository_projects": "write",
                "security_events": "write",
                "statuses": "write",
                "vulnerability_alerts": "read",
            },
        )
        self.assertEqual(app.slug, "github-actions")
        self.assertEqual(
            app.updated_at, datetime(2019, 12, 10, 19, 4, 12, tzinfo=timezone.utc)
        )
        self.assertEqual(app.url, "/apps/github-actions")

    def testGetAuthenticatedApp(self):
        # For this to work correctly in record mode, this test must be run with --auth_with_jwt
        app = self.g.get_app()
        # At this point the GithubApp object is not complete.
        # The url should change when the object is completed - after pulling it down
        # from the github API
        self.assertEqual(app.url, "/app")
        self.assertEqual(
            app.created_at, datetime(2020, 8, 1, 17, 23, 46, tzinfo=timezone.utc)
        )
        self.assertEqual(app.description, "Sample App to test PyGithub")
        self.assertListEqual(
            app.events,
            ["check_run", "check_suite", "label", "member", "public"],
        )
        self.assertEqual(app.external_url, "https://pygithub.readthedocs.io")
        self.assertEqual(app.html_url, "https://github.com/apps/pygithubtest")
        self.assertEqual(app.id, 75269)
        self.assertEqual(app.name, "PyGithubTest")
        self.assertEqual(app.owner.login, "wrecker")
        self.assertDictEqual(
            app.permissions,
            {
                "actions": "write",
                "checks": "write",
                "keys": "read",
                "members": "read",
                "metadata": "read",
                "packages": "read",
                "pages": "read",
                "repository_hooks": "write",
                "vulnerability_alerts": "read",
                "workflows": "write",
            },
        )
        self.assertEqual(app.slug, "pygithubtest")
        self.assertEqual(
            app.updated_at, datetime(2020, 8, 1, 17, 44, 31, tzinfo=timezone.utc)
        )
        self.assertEqual(app.url, "/apps/pygithubtest")
