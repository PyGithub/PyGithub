############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Benoit Latinier <benoit@latinier.fr>                          #
# Copyright 2018 Yossarian King <yggy@blackbirdinteractive.com>                #
# Copyright 2019 Benoit Latinier <benoit@latinier.fr>                          #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Jody McIntyre <scjody@modernduck.com>                         #
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


class Project(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.proj = self.g.get_project(1682941)

    # See https://developer.github.com/v3/projects/#get-a-project
    def testAttributes(self):
        self.assertEqual(self.proj.body, "To be used for testing project access API for PyGithub.")
        self.assertEqual(self.proj.columns_url, "https://api.github.com/projects/1682941/columns")
        self.assertEqual(self.proj.created_at, datetime(2018, 8, 1, 4, 6, 57, tzinfo=timezone.utc))
        self.assertEqual(self.proj.creator.login, "bbi-yggy")
        self.assertEqual(self.proj.html_url, "https://github.com/bbi-yggy/PyGithub/projects/1")
        self.assertEqual(self.proj.id, 1682941)
        self.assertEqual(self.proj.name, "TestProject")
        self.assertEqual(repr(self.proj), 'Project(name="TestProject")')
        self.assertEqual(self.proj.node_id, "MDc6UHJvamVjdDE2ODI5NDE=")
        self.assertEqual(self.proj.number, 1)
        self.assertIsNone(self.proj.organization_permission)
        self.assertEqual(self.proj.owner_url, "https://api.github.com/repos/bbi-yggy/PyGithub")
        self.assertIsNone(self.proj.private)
        self.assertEqual(self.proj.state, "open")
        self.assertEqual(self.proj.updated_at, datetime(2018, 8, 3, 0, 31, 17, tzinfo=timezone.utc))
        self.assertEqual(self.proj.url, "https://api.github.com/projects/1682941")

    def testGetOrganizationProjects(self):
        expectedProjects = ["Project1", "Project2", "Project3"]
        org = self.g.get_organization("PyGithubTestOrg")
        projects = [proj.name for proj in org.get_projects("open")]
        self.assertEqual(projects, expectedProjects)

    def testGetRepositoryProjects(self):
        expectedProjects = ["TestProject", "TestProjectClosed"]
        projects = [proj.name for proj in self.repo.get_projects("all")]
        self.assertEqual(projects, expectedProjects)
