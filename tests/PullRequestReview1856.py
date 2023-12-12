############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Claire Johns <42869556+johnsc1@users.noreply.github.com>      #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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


class PullRequestReview1856(Framework.TestCase):
    def setUp(self):
        super().setUp()
        pumpkin_repo = self.g.get_repo("CS481-Team-Pumpkin/PyGithub", lazy=True)
        self.pumpkin_pull = pumpkin_repo.get_pull(4)
        self.pullreview = self.pumpkin_pull.get_review(631460061)

    def testDelete(self):
        self.pullreview.delete()
        reviews = self.pumpkin_pull.get_reviews()
        self.assertEqual(list(reviews), [])
