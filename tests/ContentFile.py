############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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


class ContentFile(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.file = self.g.get_repo("PyGithub/PyGithub").get_readme()

    def testAttributes(self):
        self.assertEqual(
            self.file._links,
            {
                "self": "https://api.github.com/repos/PyGithub/PyGithub/contents/README.md?ref=main",
                "git": "https://api.github.com/repos/PyGithub/PyGithub/git/blobs/0d9df5bfb7d4b93443c130bc8f4eea5dd3f01205",
                "html": "https://github.com/PyGithub/PyGithub/blob/main/README.md",
            },
        )
        self.assertIsNone(self.file.commit)
        self.assertTrue(self.file.content.startswith("IyBQeUdpdEh1YgoKWyFbUHlQSV0oaHR0cHM6Ly9p"))
        self.assertEqual(self.file.download_url, "https://raw.githubusercontent.com/PyGithub/PyGithub/main/README.md")
        self.assertEqual(self.file.encoding, "base64")
        self.assertIsNone(self.file.file_size)
        self.assertEqual(
            self.file.git_url,
            "https://api.github.com/repos/PyGithub/PyGithub/git/blobs/0d9df5bfb7d4b93443c130bc8f4eea5dd3f01205",
        )
        self.assertEqual(self.file.html_url, "https://github.com/PyGithub/PyGithub/blob/main/README.md")
        self.assertIsNone(self.file.language)
        self.assertIsNone(self.file.last_modified_at)
        self.assertIsNone(self.file.license)
        self.assertIsNone(self.file.line_numbers)
        self.assertEqual(self.file.name, "README.md")
        self.assertEqual(self.file.path, "README.md")
        self.assertEqual(self.file.sha, "0d9df5bfb7d4b93443c130bc8f4eea5dd3f01205")
        self.assertEqual(self.file.size, 2524)
        self.assertIsNone(self.file.submodule_git_url)
        self.assertIsNone(self.file.target)
        self.assertIsNone(self.file.text_matches)
        self.assertEqual(self.file.type, "file")
        self.assertEqual(self.file.encoding, "base64")
        self.assertEqual(self.file.size, 2524)
        self.assertEqual(self.file.name, "README.md")
        self.assertEqual(self.file.path, "README.md")
        self.assertEqual(len(self.file.content), 3425)
        self.assertEqual(len(self.file.decoded_content), 2524)
        self.assertEqual(self.file.sha, "0d9df5bfb7d4b93443c130bc8f4eea5dd3f01205")
        self.assertEqual(self.file.download_url, "https://raw.githubusercontent.com/PyGithub/PyGithub/main/README.md")
        self.assertIsNone(self.file.license)
        self.assertEqual(repr(self.file), 'ContentFile(path="README.md")')
        self.assertEqual(self.file.url, "https://api.github.com/repos/PyGithub/PyGithub/contents/README.md?ref=main")
