############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from datetime import datetime, timezone

from . import Framework


class GitCommit(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.commit = self.g.get_user().get_repo("PyGithub").get_git_commit("4303c5b90e2216d927155e9609436ccb8984c495")

    def testAttributes(self):
        self.assertEqual(self.commit.author.name, "Vincent Jacques")
        self.assertEqual(self.commit.author.email, "vincent@vincent-jacques.net")
        self.assertEqual(
            self.commit.author.date,
            datetime(2012, 4, 17, 17, 55, 16, tzinfo=timezone.utc),
        )
        self.assertEqual(self.commit.committer.name, "Vincent Jacques")
        self.assertEqual(self.commit.committer.email, "vincent@vincent-jacques.net")
        self.assertEqual(
            self.commit.committer.date,
            datetime(2012, 4, 17, 17, 55, 16, tzinfo=timezone.utc),
        )
        self.assertEqual(self.commit.message, "Merge branch 'develop'\n")
        self.assertEqual(len(self.commit.parents), 2)
        self.assertEqual(self.commit.parents[0].sha, "936f4a97f1a86392637ec002bbf89ff036a5062d")
        self.assertEqual(self.commit.parents[1].sha, "2a7e80e6421c5d4d201d60619068dea6bae612cb")
        self.assertEqual(self.commit.sha, "4303c5b90e2216d927155e9609436ccb8984c495")
        self.assertEqual(self.commit.tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad")
        self.assertEqual(
            self.commit.url,
            "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495",
        )
        self.assertEqual(
            repr(self.commit),
            'GitCommit(sha="4303c5b90e2216d927155e9609436ccb8984c495")',
        )
        self.assertEqual(repr(self.commit.author), 'GitAuthor(name="Vincent Jacques")')
