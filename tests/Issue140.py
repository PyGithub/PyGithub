############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 AetherDeity <aetherdeity+github@gmail.com>                    #
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

from . import Framework


class Issue140(Framework.TestCase):  # https://github.com/jacquev6/PyGithub/issues/140
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("twitter/bootstrap")

    def testGetDirContentsThenLazyCompletionOfFile(self):
        contents = self.repo.get_contents("js")
        self.assertEqual(len(contents), 15)
        n = 0
        for content in contents:
            if content.path == "js/bootstrap-affix.js":
                self.assertEqual(len(content.content), 4722)  # Lazy completion
                n += 1
            elif content.path == "js/tests":
                self.assertEqual(content.content, None)  # No completion at all
                n += 1
        self.assertEqual(n, 2)

    def testGetFileContents(self):
        contents = self.repo.get_contents("js/bootstrap-affix.js")
        self.assertEqual(contents.encoding, "base64")
        self.assertEqual(
            contents.url,
            "https://api.github.com/repos/twitter/bootstrap/contents/js/bootstrap-affix.js",
        )
        self.assertEqual(len(contents.content), 4722)

    def testGetDirContentsWithRef(self):
        self.assertEqual(
            len(self.repo.get_contents("js", "8c7f9c66a7d12f47f50618ef420868fe836d0c33")),
            15,
        )
