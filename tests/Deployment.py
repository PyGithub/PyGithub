# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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


class Deployment(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.deployment = (
            self.g.get_user().get_repo("PyGithub").get_deployment(201741959)
        )

    def testAttributes(self):
        self.assertEqual(self.deployment.id, 201741959)
        self.assertEqual(
            self.deployment.url,
            "https://api.github.com/repos/jacquev6/PyGithub/deployments/201741959",
        )
        self.assertEqual(
            self.deployment.sha, "8f039d9c4ebd6f24b4bb04634ed062375c11b751"
        )
        self.assertEqual(self.deployment.task, "deploy")
        self.assertEqual(self.deployment.payload, {})
        self.assertEqual(self.deployment.original_environment, "production")
        self.assertEqual(self.deployment.environment, "production")
        self.assertIs(self.deployment.description, None)
        self.assertEqual(self.deployment.creator.login, "jacquev6")
        created_at = datetime.datetime(2020, 2, 14, 3, 41, 5)
        self.assertEqual(self.deployment.created_at, created_at)
        self.assertEqual(self.deployment.updated_at, created_at)
        self.assertEqual(
            self.deployment.statuses_url,
            "https://api.github.com/repos/jacquev6/PyGithub/deployments/201741959/statuses",
        )
        self.assertEqual(
            self.deployment.repository_url,
            "https://api.github.com/repos/jacquev6/PyGithub",
        )
        self.assertEqual(
            repr(self.deployment),
            'Deployment(url="https://api.github.com/repos/jacquev6/PyGithub/deployments/201741959", id=201741959)',
        )
