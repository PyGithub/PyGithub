############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Mahesh Raju <coder@mahesh.net>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 chantra <chantra@users.noreply.github.com>                    #
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

from datetime import datetime, timezone

import github
import github.Organization

from . import Framework
from .GithubIntegration import APP_ID, PRIVATE_KEY


class GithubApp(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.app_slug = "github-actions"
        self.app = self.g.get_app(slug=self.app_slug)
        # fetch lazy object
        self.app.id

    def testAttributes(self):
        app = self.app
        self.assertEqual(app.client_id, "Iv1.05c79e9ad1f6bdfa")
        self.assertIsNone(app.client_secret)
        self.assertEqual(app.created_at, datetime(2018, 7, 30, 9, 30, 17, tzinfo=timezone.utc))
        self.assertEqual(app.description, "Automate your workflow from idea to production")
        self.assertListEqual(
            app.events,
            [
                "branch_protection_rule",
                "check_run",
                "check_suite",
                "create",
                "delete",
                "deployment",
                "deployment_status",
                "discussion",
                "discussion_comment",
                "fork",
                "gollum",
                "issues",
                "issue_comment",
                "label",
                "merge_group",
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
        self.assertIsNone(app.installations_count)
        self.assertEqual(app.name, "GitHub Actions")
        self.assertEqual(app.node_id, "MDM6QXBwMTUzNjg=")
        self.assertIsInstance(app.owner, github.Organization.Organization)
        self.assertEqual(app.owner.login, "github")
        self.assertIsNone(app.pem)
        self.assertDictEqual(
            app.permissions,
            {
                "actions": "write",
                "administration": "read",
                "attestations": "write",
                "checks": "write",
                "contents": "write",
                "deployments": "write",
                "discussions": "write",
                "issues": "write",
                "merge_queues": "write",
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
        self.assertEqual(app.updated_at, datetime(2024, 4, 10, 20, 33, 16, tzinfo=timezone.utc))
        self.assertEqual(app.url, "/apps/github-actions")
        self.assertIsNone(app.webhook_secret)

    def testGetAuthenticatedApp(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        g = github.Github(auth=auth)

        with self.assertWarns(DeprecationWarning) as warning:
            # httpretty has some deprecation warnings in Python 3.12
            with self.ignoreWarning(category=DeprecationWarning, module="httpretty"):
                app = g.get_app()

            self.assertWarning(
                warning,
                "Argument slug is mandatory, calling this method without the slug argument is deprecated, "
                "please use github.GithubIntegration(auth=github.Auth.AppAuth(...)).get_app() instead",
            )

        self.assertEqual(app.created_at, datetime(2020, 8, 1, 17, 23, 46, tzinfo=timezone.utc))
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
        self.assertEqual(app.updated_at, datetime(2020, 8, 1, 17, 44, 31, tzinfo=timezone.utc))
        self.assertEqual(app.url, "/apps/pygithubtest")
