# -*- coding: utf-8 -*-

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
import Framework


class ReleaseAsset(Framework.TestCase):
    """
    Test harness for functionality related to release assets (files attached to
    the github release).
    """
    def setUp(self):
        Framework.TestCase.setUp(self)
        # Do not get self.release here as it causes bad data to be saved in --record mode

    def testAttributes(self):
        """
        Test properties & to-string.
        """
        release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        self.assertEqual(release.id, 1210814)

        asset = release.get_assets()[0]
        self.assertEqual(asset.id, 16)
        self.assertEqual(asset.url, "https://api.github.com/api/v3/repos/edhollandAL/PyGithub/releases/assets/16")
        self.assertEqual(asset.name, "Archive.zip")
        self.assertEqual(asset.label, "Installation msi & runbook zipped")
        self.assertEqual(asset.content_type, "application/zip")
        self.assertEqual(asset.state, "uploaded")
        self.assertEqual(asset.size, 3783)
        self.assertEqual(asset.download_count, 2)
        self.assertEqual(asset.created_at, datetime.datetime(2017, 2, 1, 22, 40, 58))
        self.assertEqual(asset.updated_at, datetime.datetime(2017, 2, 1, 22, 44, 58))
        self.assertEqual(asset.browser_download_url, "https://github.com/edhollandAL/PyGithub/releases/download/v1.25.2/Asset.zip")
        self.assertEqual(asset.uploader.login, "PyGithub")
        self.assertEqual(asset.__repr__(), 'GitReleaseAsset(url="https://api.github.com/api/v3/repos/edhollandAL/PyGithub/releases/assets/16")')

    def testDelete(self):
        """
        Test deleting a release asset.
        """
        release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        self.assertEqual(release.id, 1210814)
        asset = release.get_assets()[0]
        self.assertEqual(asset.id, 16)

        self.assertTrue(asset.delete_asset(), msg="Asset deletion failed.")

    def testUpdate(self):
        """
        Test updating the editable properties of a release asset.
        """
        release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        self.assertEqual(release.id, 1210814)

        asset = release.get_assets()[0]

        self.assertEqual(asset.id, 16)
        self.assertEqual(asset.name, "Archive.zip")
        self.assertEqual(asset.label, "Installation msi & runbook zipped")

        new_name = "updated-name.zip"
        new_label = "Updated label"
        updated_asset = asset.update_asset(new_name, new_label)
        self.assertEqual(updated_asset.name, new_name)
        self.assertNotEqual(asset.name, updated_asset.name)
        self.assertEqual(updated_asset.label, new_label)
        self.assertNotEqual(asset.label, updated_asset.label)
