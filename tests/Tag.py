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


class Tag(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.tag = self.g.get_repo("PyGithub/PyGithub").get_tags()[0]

    def testAttributes(self):
        self.assertEqual(self.tag.commit.sha, "19ddb9f4fd996e99a5010d271b3c2e76dd280fb5")
        self.assertEqual(self.tag.name, "v2.5.0")
        self.assertEqual(self.tag.node_id, "MDM6UmVmMzU0NDQ5MDpyZWZzL3RhZ3MvdjIuNS4w")
        self.assertEqual(
            self.tag.tarball_url, "https://api.github.com/repos/PyGithub/PyGithub/tarball/refs/tags/v2.5.0"
        )
        self.assertEqual(
            self.tag.zipball_url, "https://api.github.com/repos/PyGithub/PyGithub/zipball/refs/tags/v2.5.0"
        )
        self.assertEqual(
            repr(self.tag),
            'Tag(name="v2.5.0", commit=Commit(sha="19ddb9f4fd996e99a5010d271b3c2e76dd280fb5"))',
        )
