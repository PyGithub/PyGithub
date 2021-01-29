############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
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


class ReleaseAsset(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        self.asset = self.release.get_assets()[0]

    def testAttributes(self):
        self.assertEqual(self.release.id, 1210814)
        self.assertEqual(self.asset.id, 16)
        self.assertEqual(
            self.asset.url,
            "https://api.github.com/api/v3/repos/edhollandAL/PyGithub/releases/assets/16",
        )
        self.assertEqual(self.asset.name, "Archive.zip")
        self.assertEqual(self.asset.label, "Installation msi & runbook zipped")
        self.assertEqual(self.asset.content_type, "application/zip")
        self.assertEqual(self.asset.state, "uploaded")
        self.assertEqual(self.asset.size, 3783)
        self.assertEqual(self.asset.download_count, 2)
        self.assertEqual(
            self.asset.created_at,
            datetime.datetime(2017, 2, 1, 22, 40, 58, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.asset.updated_at,
            datetime.datetime(2017, 2, 1, 22, 44, 58, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.asset.browser_download_url,
            "https://github.com/edhollandAL/PyGithub/releases/download/v1.25.2/Asset.zip",
        )
        self.assertEqual(self.asset.uploader.login, "PyGithub")
        self.assertEqual(
            repr(self.asset),
            'GitReleaseAsset(url="https://api.github.com/api/v3/repos/edhollandAL/PyGithub/releases/assets/16")',
        )

    def testDelete(self):
        self.assertTrue(self.asset.delete_asset())

    def testUpdate(self):
        new_name = "updated-name.zip"
        new_label = "Updated label"
        updated_asset = self.asset.update_asset(new_name, new_label)
        self.assertEqual(updated_asset.name, new_name)
        self.assertNotEqual(self.asset.name, updated_asset.name)
        self.assertEqual(updated_asset.label, new_label)
        self.assertNotEqual(self.asset.label, updated_asset.label)
