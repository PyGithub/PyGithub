############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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


class GitRef(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.ref = self.g.get_user().get_repo("PyGithub").get_git_ref("heads/BranchCreatedByPyGithub")

    def testAttributes(self):
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
