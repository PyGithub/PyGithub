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
# Copyright 2020 Pascal Hofmann <mail@pascalhofmann.de>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Nevins <nevins-b@users.noreply.github.com>                    #
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


class Deployment(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.deployment = self.g.get_user().get_repo("PyGithub").get_deployment(263877258)

    def testAttributes(self):
        self.assertEqual(self.deployment.created_at, datetime(2020, 8, 26, 11, 44, 53, tzinfo=timezone.utc))
        self.assertEqual(self.deployment.creator.login, "jacquev6")
        self.assertEqual(self.deployment.description, "Test deployment")
        self.assertEqual(self.deployment.environment, "test")
        self.assertEqual(self.deployment.id, 263877258)
        self.assertEqual(self.deployment.node_id, "MDEwOkRlcGxveW1lbnQyNjIzNTE3NzY=")
        self.assertEqual(self.deployment.original_environment, "test")
        self.assertEqual(self.deployment.payload, {"test": True})
        self.assertIsNone(self.deployment.performed_via_github_app)
        self.assertEqual(self.deployment.production_environment, False)
        self.assertEqual(self.deployment.ref, "743f5a58b0bce91c4eab744ff7e39dfca9e6e8a5")
        self.assertEqual(self.deployment.repository_url, "https://api.github.com/repos/jacquev6/PyGithub")
        self.assertEqual(self.deployment.sha, "743f5a58b0bce91c4eab744ff7e39dfca9e6e8a5")
        self.assertEqual(
            self.deployment.statuses_url,
            "https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258/statuses",
        )
        self.assertEqual(self.deployment.task, "deploy")
        self.assertEqual(self.deployment.transient_environment, True)
        self.assertEqual(self.deployment.updated_at, datetime(2020, 8, 26, 11, 44, 53, tzinfo=timezone.utc))
        self.assertEqual(
            self.deployment.url,
            "https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258",
        )
        self.assertEqual(self.deployment.ref, "743f5a58b0bce91c4eab744ff7e39dfca9e6e8a5")
        self.assertEqual(self.deployment.sha, "743f5a58b0bce91c4eab744ff7e39dfca9e6e8a5")
        self.assertEqual(self.deployment.task, "deploy")
        self.assertEqual(self.deployment.payload, {"test": True})
        self.assertEqual(self.deployment.original_environment, "test")
        self.assertEqual(self.deployment.environment, "test")
        self.assertEqual(self.deployment.description, "Test deployment")
        self.assertEqual(self.deployment.creator.login, "jacquev6")
        created_at = datetime(2020, 8, 26, 11, 44, 53, tzinfo=timezone.utc)
        self.assertEqual(self.deployment.created_at, created_at)
        self.assertEqual(self.deployment.updated_at, created_at)
        self.assertEqual(self.deployment.transient_environment, True)
        self.assertEqual(self.deployment.production_environment, False)
        self.assertEqual(
            self.deployment.statuses_url,
            "https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258/statuses",
        )
        self.assertEqual(
            self.deployment.repository_url,
            "https://api.github.com/repos/jacquev6/PyGithub",
        )
        self.assertEqual(
            repr(self.deployment),
            'Deployment(url="https://api.github.com/repos/jacquev6/PyGithub/deployments/263877258", id=263877258)',
        )
