############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Olof-Joachim Frahm <olof@macrolet.net>                        #
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


class PullRequest1169(Framework.TestCase):
    def setUp(self):
        super().setUp()
        ferada_repo = self.g.get_repo("coleslaw-org/coleslaw", lazy=True)
        self.pull = ferada_repo.get_pull(173)

    def testReviewApproveWithoutBody(self):
        r = self.pull.create_review(event="APPROVE")
        self.assertEqual(r.id, 261942907)
        self.assertEqual(r.user.login, "Ferada")
