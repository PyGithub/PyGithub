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
from datetime import datetime, timezone


class ContentFile(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.file = self.g.get_user().get_repo("PyGithub").get_readme()

    def testAttributes(self):
        self.assertEqual(self.file._links, {'self': 'https://api.github.com/repos/jacquev6/PyGithub/contents/ReadMe.md', 'html': 'https://github.com/jacquev6/PyGithub/blob/master/ReadMe.md', 'git': 'https://api.github.com/repos/jacquev6/PyGithub/git/blobs/5628799a7d517a4aaa0c1a7004d07569cd154df0'})
        self.assertIsNone(self.file.commit)
        self.assertTrue(self.file.content.startswith('VGhpcyBpcyBhIFB5dGhvbiBsaWJyYXJ5IHRvIGFjY'))
        self.assertEqual(self.file.download_url, 'https://raw.githubusercontent.com/jacquev6/PyGithub/master/README.md')
        self.assertEqual(self.file.encoding, 'base64')
        self.assertIsNone(self.file.file_size)
        self.assertIsNone(self.file.git_url)
        self.assertIsNone(self.file.html_url)
        self.assertIsNone(self.file.language)
        self.assertIsNone(self.file.last_modified_at)
        self.assertIsNone(self.file.license)
        self.assertIsNone(self.file.line_numbers)
        self.assertEqual(self.file.name, 'ReadMe.md')
        self.assertEqual(self.file.path, 'ReadMe.md')
        self.assertEqual(self.file.score, None)
        self.assertEqual(self.file.sha, '5628799a7d517a4aaa0c1a7004d07569cd154df0')
        self.assertEqual(self.file.size, 7531)
        self.assertIsNone(self.file.submodule_git_url)
        self.assertIsNone(self.file.target)
        self.assertIsNone(self.file.text_matches)
        self.assertEqual(self.file.type, "file")
        self.assertEqual(self.file.encoding, "base64")
        self.assertEqual(self.file.size, 7531)
        self.assertEqual(self.file.name, "ReadMe.md")
        self.assertEqual(self.file.path, "ReadMe.md")
        self.assertEqual(len(self.file.content), 10212)
        self.assertEqual(len(self.file.decoded_content), 7531)
        self.assertEqual(self.file.sha, "5628799a7d517a4aaa0c1a7004d07569cd154df0")
        self.assertEqual(
            self.file.download_url,
            "https://raw.githubusercontent.com/jacquev6/PyGithub/master/README.md",
        )
        self.assertIsNone(self.file.license)
        self.assertEqual(repr(self.file), 'ContentFile(path="ReadMe.md")')
        self.assertIsNone(self.file.url)
