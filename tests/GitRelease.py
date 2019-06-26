# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2015 Ed Holland <eholland@alertlogic.com>                          #
# Copyright 2016 Benjamin Whitney <benjamin.whitney@ironnetcybersecurity.com>  #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Andrew Smith <espadav8@gmail.com>                             #
# Copyright 2018 Daniel Kesler <kesler.daniel@gmail.com>                       #
# Copyright 2018 Kuba <jakub.glapa@adspired.com>                               #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 edquist <edquist@users.noreply.github.com>                    #
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

import os
import zipfile
import datetime
import Framework


class Release(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        # Do not get self.release here as it casues bad data to be saved in --record mode
        self.content_path = "content.txt"
        self.artifact_path = "archive.zip"

        with open(self.content_path, "w") as zip_content:
            zip_content.write("Pedro for president.")

        artifact = zipfile.ZipFile(self.artifact_path, "w")
        artifact.write(self.content_path)
        artifact.close()

    def tearDown(self):
        if os.path.exists(self.content_path):
            os.remove(self.content_path)
        if os.path.exists(self.artifact_path):
            os.remove(self.artifact_path)

    def testAttributes(self):
        self.release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        self.assertEqual(self.release.id, 1210814)
        self.assertEqual(self.release.tag_name, "v1.25.2")
        self.assertEqual(self.release.target_commitish, "master")
        self.assertEqual(self.release.upload_url, "https://uploads.github.com/repos/edhollandAL/PyGithub/releases/1210814/assets{?name}")
        self.assertEqual(self.release.body, "Body")
        self.assertEqual(self.release.title, "Test")
        self.assertEqual(self.release.draft, False)
        self.assertEqual(self.release.prerelease, False)
        self.assertEqual(self.release.url, "https://api.github.com/repos/edhollandAL/PyGithub/releases/1210814")
        self.assertEqual(self.release.author._rawData['login'], "edhollandAL")
        self.assertEqual(self.release.author.login, "edhollandAL")
        self.assertEqual(self.release.author.id, 11922660)
        self.assertEqual(self.release.author.type, "User")
        self.assertEqual(self.release.html_url, "https://github.com/edhollandAL/PyGithub/releases/tag/v1.25.2")
        self.assertEqual(self.release.created_at, datetime.datetime(2014, 10, 8, 1, 54))
        self.assertEqual(self.release.published_at, datetime.datetime(2015, 4, 24, 8, 36, 51))
        self.assertEqual(self.release.tarball_url, "https://api.github.com/repos/edhollandAL/PyGithub/tarball/v1.25.2")
        self.assertEqual(self.release.zipball_url, "https://api.github.com/repos/edhollandAL/PyGithub/zipball/v1.25.2")

        # test __repr__() based on this attributes
        self.assertEqual(self.release.__repr__(), 'GitRelease(title="Test")')

    def testDelete(self):
        self.release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        self.release.delete_release()

    def testUpdate(self):
        self.release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        new_release = self.release.update_release("Updated Test", "Updated Body")
        self.assertEqual(new_release.body, "Updated Body")
        self.assertEqual(new_release.title, "Updated Test")

    def testGetRelease(self):
        release_by_id = self.g.get_user().get_repo("PyGithub").get_release('v1.25.2')
        release_by_tag = self.g.get_user().get_repo("PyGithub").get_release(1210837)
        self.assertEqual(release_by_id, release_by_tag)

    def testCreateGitTagAndRelease(self):
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.release = self.repo.create_git_tag_and_release('v3.0.0', 'tag message', 'release title', 'release message', '5a05a5e58f682d315acd2447c87ac5b4d4fc55e8', 'commit')
        self.assertEqual(self.release.tag_name, "v3.0.0")
        self.assertEqual(self.release.body, "release message")
        self.assertEqual(self.release.title, "release title")
        self.assertEqual(self.release.author._rawData['login'], "edhollandAL")
        self.assertEqual(self.release.html_url, "https://github.com/edhollandAL/PyGithub/releases/tag/v3.0.0")

    def testGetLatestRelease(self):
        self.repo = self.g.get_user().get_repo('PyGithub')
        latest_release = self.repo.get_latest_release()
        self.assertEqual(latest_release.tag_name, "v1.25.2")

    def testGetAsset(self):
        """
        Test retrieving a release asset directly by its ID.
        """
        the_repo = self.g.get_user().get_repo("PyGithub")

        asset_id = 16
        the_asset = the_repo.get_release_asset(asset_id)
        self.assertTrue(the_asset is not None)
        self.assertEqual(the_asset.id, asset_id)

    def testGetAssets(self):
        """
        Test retrieving the set of assets for the current release.
        """
        release_id = 1210837
        the_repo = self.g.get_user().get_repo("PyGithub")
        the_release = the_repo.get_release(release_id)
        self.assertEqual(the_release.id, release_id)

        asset_list = [x for x in the_release.get_assets()]
        self.assertTrue(asset_list is not None)
        self.assertEqual(len(asset_list), 1)

    def testUploadAsset(self):
        """
        Test uploading a new asset to the release.
        """
        release_id = 1210837
        the_repo = self.g.get_user().get_repo("PyGithub")
        the_release = the_repo.get_release(release_id)
        self.assertEqual(the_release.id, release_id)

        the_release.upload_asset(self.artifact_path,
                                 "unit test artifact",
                                 "application/zip")

    def testUploadAssetWithName(self):
        release_id = 1210837
        repo = self.g.get_user().get_repo("PyGithub")
        release = repo.get_release(release_id)
        r = release.upload_asset(self.artifact_path, name="foobar.zip")
        self.assertEqual(r.name, "foobar.zip")
