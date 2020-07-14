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

import datetime
import os
import zipfile

from . import Framework
from github import GithubException

repo_name = "RepoTest"
user = "rickrickston123"
release_id = 28524234
author_id = 64711998
tag = "v1.0"
create_date = datetime.datetime(2020, 7, 12, 7, 34, 42)
publish_date = datetime.datetime(2020, 7, 14, 0, 58, 20)


class ReleaseRead(Framework.TestCase):
    """
    Tests that only involve reading, not modification. All data comes from an existing release manually crafted.
    """

    # Note that it's not possible to specify `self.release` in setUp() because something goes wonky when using --record
    def testAttributes(self):
        release = self.g.get_user(user).get_repo(repo_name).get_latest_release()
        self.assertEqual(release.id, release_id)
        self.assertEqual(release.tag_name, tag)
        self.assertEqual(release.target_commitish, "master")
        self.assertEqual(
            release.upload_url,
            "https://uploads.github.com/repos/{}/{}/releases/{}/assets{{?name,label}}".format(
                user, repo_name, release_id
            ),
        )
        self.assertEqual(release.body, "Body")
        self.assertEqual(release.title, "Test")
        self.assertEqual(release.draft, False)
        self.assertEqual(release.prerelease, False)
        self.assertEqual(
            release.url,
            "https://api.github.com/repos/{}/{}/releases/{}".format(
                user, repo_name, release_id
            ),
        )
        self.assertEqual(release.author._rawData["login"], user)
        self.assertEqual(release.author.login, user)
        self.assertEqual(release.author.id, author_id)
        self.assertEqual(release.author.type, "User")
        self.assertEqual(
            release.html_url,
            "https://github.com/{}/{}/releases/tag/{}".format(user, repo_name, tag),
        )
        self.assertEqual(release.created_at, create_date)
        self.assertEqual(release.published_at, publish_date)
        self.assertEqual(
            release.tarball_url,
            "https://api.github.com/repos/{}/{}/tarball/{}".format(
                user, repo_name, tag
            ),
        )
        self.assertEqual(
            release.zipball_url,
            "https://api.github.com/repos/{}/{}/zipball/{}".format(
                user, repo_name, tag
            ),
        )
        self.assertEqual(repr(release), 'GitRelease(title="Test")')

    def testGetRelease(self):
        release_by_id = (
            self.g.get_user(user).get_repo(repo_name).get_release(release_id)
        )
        release_by_tag = self.g.get_user(user).get_repo(repo_name).get_release(tag)
        self.assertEqual(release_by_id, release_by_tag)

    def testGetLatestRelease(self):
        repo = self.g.get_user(user).get_repo(repo_name)
        latest_release = repo.get_latest_release()
        self.assertEqual(latest_release.tag_name, tag)

    def testGetAssets(self):
        """
        Test retrieving the set of assets for the current release, as well as directly by id.
        """
        repo = self.g.get_user(user).get_repo(repo_name)
        release = repo.get_release(release_id)
        self.assertEqual(release.id, release_id)

        asset_list = [x for x in release.get_assets()]
        self.assertTrue(asset_list is not None)
        self.assertEqual(len(asset_list), 1)

        asset_id = asset_list[0].id
        asset = repo.get_release_asset(asset_id)
        self.assertTrue(asset is not None)
        self.assertEqual(asset.id, asset_id)


class ReleaseModify(Framework.TestCase):
    """ Tests involving creating/updating/deleting releases."""

    def setUp(self):
        super().setUp()
        self.new_tag = "v1.25.2"  # Used for new releases
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

        super().tearDown()

    # At time of writing (2020-07) the --record option only records setUp() once for the entire class. This causes issues here because for each different test you'll want to create a new release, but the release ID will change between calls, leading to --record collecting bad data.
    # The workaround I've come up with is to have a seperate setup/teardown method that gets manually called in each test method.
    def setUpEach(self):
        self.repo = self.g.get_user(user).get_repo(repo_name)
        repo = self.repo
        commit_sha = repo.get_commits()[0].sha  # Just need any commit
        new_release = repo.create_git_tag_and_release(
            self.new_tag,
            "tag message",
            "release title",
            "release message",
            commit_sha,
            "commit",
        )
        self.new_release_id = new_release.id
        # assert self.new_release_id != release_id

    def tearDownEach(self):
        try:
            new_release = self.repo.get_release(self.new_release_id)
            new_release.delete_release()
        except GithubException:
            pass  # Already deleted

    def testDelete(self):
        # repo = self.g.get_user(user).get_repo(repo_name)
        self.setUpEach()
        to_delete = self.repo.get_release(self.new_release_id)
        to_delete.delete_release()
        self.tearDownEach()

    def testUpdate(self):
        self.setUpEach()
        repo = self.repo
        release = repo.get_release(self.new_release_id)
        new_release = release.update_release("Updated Test", "Updated Body")
        self.assertEqual(new_release.title, "Updated Test")
        self.assertEqual(new_release.body, "Updated Body")
        self.tearDownEach()

    def testUploadAsset(self):
        """
        Test uploading a new asset to the release.
        """
        self.setUpEach()
        repo = self.repo
        release = repo.get_release(self.new_release_id)
        self.assertEqual(release.id, self.new_release_id)

        release.upload_asset(
            self.artifact_path, "unit test artifact", "application/zip"
        )
        self.tearDownEach()

    def testUploadAssetWithName(self):
        self.setUpEach()
        release = self.repo.get_release(self.new_release_id)
        r = release.upload_asset(self.artifact_path, name="foobar.zip")
        self.assertEqual(r.name, "foobar.zip")
        self.tearDownEach()

    def testCreateGitTagAndRelease(self):
        self.setUpEach()
        # Creation code already done in setup, so we'll just test what's already here.
        repo = self.repo
        release = repo.get_release(self.new_release_id)
        self.assertEqual(release.tag_name, self.new_tag)
        self.assertEqual(release.body, "release message")
        self.assertEqual(release.title, "release title")
        self.assertEqual(release.author._rawData["login"], user)
        self.assertEqual(
            release.html_url,
            "https://github.com/{}/{}/releases/tag/{}".format(
                user, repo_name, self.new_tag
            ),
        )
        self.tearDownEach()
