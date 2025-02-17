############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Colby Gallup <colbygallup@gmail.com>                          #
# Copyright 2020 Pascal Hofmann <mail@pascalhofmann.de>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from . import Framework


class DeploymentStatus(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.deployment = self.g.get_user().get_repo("PyGithub").get_deployment(263877258)
        self.status = self.deployment.get_status(388454671)

    def testAttributes(self):
        self.assertEqual(self.status.created_at, datetime(2020, 8, 26, 14, 32, 51, tzinfo=timezone.utc))
        self.assertEqual(self.status.creator.login, "jacquev6")
        self.assertEqual(
            self.status.deployment_url, "https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258"
        )
        self.assertEqual(self.status.description, "Deployment queued")
        self.assertEqual(self.status.environment, "test")
        self.assertEqual(self.status.environment_url, "https://example.com/environment")
        self.assertEqual(self.status.id, 388454671)
        created_at = datetime(2020, 8, 26, 14, 32, 51, tzinfo=timezone.utc)
        self.assertEqual(self.status.created_at, created_at)
        self.assertEqual(self.status.creator.login, "jacquev6")
        self.assertEqual(
            self.status.deployment_url,
            "https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258",
        )
        self.assertEqual(self.status.description, "Deployment queued")
        self.assertEqual(self.status.environment, "test")
        self.assertEqual(self.status.environment_url, "https://example.com/environment")
        self.assertEqual(self.status.log_url, "https://example.com/deployment.log")
        self.assertEqual(self.status.node_id, "MDE2OkRlcGxveW1lbnRTdGF0dXMzODg0NTQ2NzE=")
        self.assertIsNone(self.status.performed_via_github_app)
        self.assertEqual(
            self.status.repository_url,
            "https://api.github.com/repos/jacquev6/PyGithub",
        )
        self.assertEqual(self.status.state, "queued")
        self.assertEqual(self.status.target_url, "https://example.com/deployment.log")
        self.assertEqual(self.status.updated_at, created_at)
        self.assertEqual(
            self.status.url,
            "https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258/statuses/388454671",
        )
        self.assertEqual(
            self.status.node_id,
            "MDE2OkRlcGxveW1lbnRTdGF0dXMzODg0NTQ2NzE=",
        )
        self.assertEqual(
            repr(self.status),
            'DeploymentStatus(url="https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258/statuses/388454671", id=388454671)',
        )

    def testCreate(self):
        newStatus = self.deployment.create_status(
            "queued",
            target_url="https://example.com/deployment.log",
            description="Deployment queued",
            environment="test",
            environment_url="https://example.com/environment",
            auto_inactive=True,
        )
        self.assertEqual(newStatus.id, 388454671)
        self.assertEqual(newStatus.state, "queued")
        self.assertEqual(
            newStatus.repository_url,
            "https://api.github.com/repos/jacquev6/PyGithub",
        )

    def testGetStatuses(self):
        statuses = self.deployment.get_statuses()
        self.assertListKeyEqual(
            statuses,
            lambda s: s.id,
            [388454671, 388433743, 388432880],
        )
