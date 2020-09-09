# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Colby Gallup <colbygallup@gmail.com>                          #
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


class DeploymentStatus(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.deployment = (
            self.g.get_user().get_repo("PyGithub").get_deployment(242997115)
        )
        self.status = self.deployment.get_status(344110026)

    def testAttributes(self):
        self.assertEqual(self.status.id, 344110026)
        created_at = datetime.datetime(2020, 6, 27, 18, 57, 35)
        self.assertEqual(self.status.created_at, created_at)
        self.assertEqual(self.status.creator.login, "colbygallup")
        self.assertEqual(
            self.status.deployment_url,
            "https://api.github.com/repos/colbygallup/PyGithub/deployments/242997115",
        )
        self.assertEqual(self.status.description, "")
        self.assertEqual(self.status.environment, "production")
        self.assertEqual(
            self.status.repository_url,
            "https://api.github.com/repos/colbygallup/PyGithub",
        )
        self.assertEqual(self.status.state, "failure")
        self.assertEqual(self.status.target_url, "")
        self.assertEqual(self.status.updated_at, created_at)
        self.assertEqual(
            self.status.url,
            "https://api.github.com/repos/colbygallup/PyGithub/deployments/242997115/statuses/344110026",
        )
        self.assertEqual(
            self.status.node_id,
            "MDE2OkRlcGxveW1lbnRTdGF0dXMzNDQxMTAwMjY=",
        )
        self.assertEqual(
            repr(self.status),
            'DeploymentStatus(url="https://api.github.com/repos/colbygallup/PyGithub/deployments/242997115/statuses/344110026", id=344110026)',
        )

    def testCreate(self):
        newStatus = self.deployment.create_status("success")
        self.assertEqual(newStatus.state, "success")
        self.assertEqual(
            newStatus.repository_url,
            "https://api.github.com/repos/colbygallup/PyGithub",
        )

    def testGetStatuses(self):
        statuses = self.deployment.get_statuses()
        self.assertListKeyEqual(
            statuses,
            lambda s: s.id,
            [346100235, 344427441, 344110026, 344109923, 344107728],
        )
