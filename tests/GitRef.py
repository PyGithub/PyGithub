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

from . import Framework


class GitRef(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.ref = self.g.get_user().get_repo("PyGithub").get_git_ref("heads/BranchCreatedByPyGithub")

    def testAttributes(self):
        self.assertIsNone(self.ref.node_id)
        self.assertEqual(self.ref.object.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a")
        self.assertEqual(self.ref.object.type, "commit")
        self.assertEqual(
            self.ref.object.url,
            "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a",
        )
        self.assertEqual(self.ref.ref, "refs/heads/BranchCreatedByPyGithub")
        self.assertEqual(
            self.ref.url,
            "https://api.github.com/repos/jacquev6/PyGithub/git/refs/heads/BranchCreatedByPyGithub",
        )

        self.assertEqual(repr(self.ref), 'GitRef(ref="refs/heads/BranchCreatedByPyGithub")')
        self.assertEqual(
            repr(self.ref.object),
            'GitObject(sha="1292bf0e22c796e91cc3d6e24b544aece8c21f2a")',
        )

    def testEdit(self):
        self.ref.edit("04cde900a0775b51f762735637bd30de392a2793")

    def testEditWithForce(self):
        self.ref.edit("4303c5b90e2216d927155e9609436ccb8984c495", force=True)

    def testDelete(self):
        self.ref.delete()
