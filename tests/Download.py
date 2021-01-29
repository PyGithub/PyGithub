############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import datetime

from . import Framework


class Download(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.download = self.g.get_user().get_repo("PyGithub").get_download(242550)

    def testAttributes(self):
        self.assertEqual(self.download.accesskeyid, None)
        self.assertEqual(self.download.acl, None)
        self.assertEqual(self.download.bucket, None)
        self.assertEqual(self.download.content_type, "text/plain")
        self.assertEqual(
            self.download.created_at,
            datetime.datetime(2012, 5, 22, 18, 58, 32, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.download.description, None)
        self.assertEqual(self.download.download_count, 0)
        self.assertEqual(self.download.expirationdate, None)
        self.assertEqual(
            self.download.html_url,
            "https://github.com/downloads/jacquev6/PyGithub/Foobar.txt",
        )
        self.assertEqual(self.download.id, 242550)
        self.assertEqual(self.download.mime_type, None)
        self.assertEqual(self.download.name, "Foobar.txt")
        self.assertEqual(self.download.path, None)
        self.assertEqual(self.download.policy, None)
        self.assertEqual(self.download.prefix, None)
        self.assertEqual(self.download.redirect, None)
        self.assertEqual(self.download.s3_url, None)
        self.assertEqual(self.download.signature, None)
        self.assertEqual(self.download.size, 1024)
        self.assertEqual(
            self.download.url,
            "https://api.github.com/repos/jacquev6/PyGithub/downloads/242550",
        )
        self.assertEqual(repr(self.download), "Download(id=242550)")

    def testDelete(self):
        self.download.delete()
