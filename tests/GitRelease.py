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
# Copyright 2018 Ggicci <ggicci.t@gmail.com>                                   #
# Copyright 2018 Kuba <jakub.glapa@adspired.com>                               #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 edquist <edquist@users.noreply.github.com>                    #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Jesse Li <jesse.li2002@gmail.com>                             #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Sam Morgan <sama4mail@gmail.com>                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Mikhail f. Shiryaev <mr.felixoid@gmail.com>                   #
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

import os
import zipfile
from datetime import datetime, timezone

from github import GithubException

from . import Framework


class FileLikeStub:
    def __init__(self):
        self.dat = b"I wanted to come up with some clever phrase or something here to test with but my mind is blank."
        self.file_length = len(self.dat)
        self.index = 0

    def read(self, size=-1):
        if size < 0 or size is None:
            start = self.index
            self.index = self.file_length
            return self.dat[start:]
        else:
            start = self.index
            end = start + size
            self.index = end
            return self.dat[start:end]


repo_name = "RepoTest"
user = "rickrickston123"
release_id = 28524234
author_id = 64711998
tag = "v1.0"
create_date = datetime(2020, 7, 12, 7, 34, 42, tzinfo=timezone.utc)
publish_date = datetime(2020, 7, 14, 0, 58, 20, tzinfo=timezone.utc)


class GitRelease(Framework.TestCase):
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
        self.repo = self.g.get_user(user).get_repo(repo_name)
        self.release = self.repo.get_release(release_id)

    def tearDown(self):
        if os.path.exists(self.content_path):
            os.remove(self.content_path)
        if os.path.exists(self.artifact_path):
            os.remove(self.artifact_path)

        super().tearDown()

    def setUpNewRelease(self):
        repo = self.repo
        commit_sha = repo.get_commits()[0].sha  # Just need any commit
        self.new_release = repo.create_git_tag_and_release(
            self.new_tag,
            "tag message",
            "release title",
            "release message",
            commit_sha,
            "commit",
        )
        self.new_release_id = self.new_release.id

    def tearDownNewRelease(self):
        try:
            new_release = self.repo.get_release(self.new_release_id)
            new_release.delete_release()
        except GithubException:
            pass  # Already deleted

    def testAttributes(self):
        release = self.release
        self.assertEqual(
            release.assets[0].url, "https://api.github.com/repos/rickrickston123/RepoTest/releases/assets/22848494"
        )
        self.assertEqual(
            release.assets_url, "https://api.github.com/repos/rickrickston123/RepoTest/releases/28524234/assets"
        )
        self.assertEqual(release.author.login, "rickrickston123")
        self.assertEqual(release.body, "Body")
        self.assertIsNone(release.body_html)
        self.assertIsNone(release.body_text)
        self.assertEqual(release.created_at, datetime(2020, 7, 12, 7, 34, 42, tzinfo=timezone.utc))
        self.assertIsNone(release.discussion_url)
        self.assertIsNone(release.documentation_url)
        self.assertEqual(release.draft, False)
        self.assertEqual(release.html_url, "https://github.com/rickrickston123/RepoTest/releases/tag/v1.0")
        self.assertEqual(release.id, release_id)
        self.assertIsNone(release.immutable)
        self.assertIsNone(release.mentions_count)
        self.assertIsNone(release.message)
        self.assertEqual(release.name, "Test")
        self.assertEqual(release.node_id, "MDc6UmVsZWFzZTI4NTI0MjM0")
        self.assertEqual(release.prerelease, False)
        self.assertEqual(release.published_at, datetime(2020, 7, 14, 0, 58, 20, tzinfo=timezone.utc))
        self.assertIsNone(release.reactions)
        self.assertIsNone(release.status)
        self.assertEqual(release.tag_name, tag)
        self.assertEqual(release.tarball_url, "https://api.github.com/repos/rickrickston123/RepoTest/tarball/v1.0")
        self.assertEqual(release.target_commitish, "master")
        self.assertEqual(
            release.upload_url,
            f"https://uploads.github.com/repos/{user}/{repo_name}/releases/{release_id}/assets{{?name,label}}",
        )
        self.assertEqual(release.body, "Body")
        self.assertFalse(release.draft)
        self.assertFalse(release.prerelease)
        self.assertEqual(
            release.url,
            f"https://api.github.com/repos/{user}/{repo_name}/releases/{release_id}",
        )
        self.assertEqual(release.author._rawData["login"], user)
        self.assertEqual(release.author.login, user)
        self.assertEqual(release.author.id, author_id)
        self.assertEqual(release.author.type, "User")
        self.assertEqual(
            release.html_url,
            f"https://github.com/{user}/{repo_name}/releases/tag/{tag}",
        )
        self.assertEqual(release.created_at, create_date)
        self.assertEqual(release.published_at, publish_date)
        self.assertEqual(
            release.tarball_url,
            f"https://api.github.com/repos/{user}/{repo_name}/tarball/{tag}",
        )
        self.assertEqual(
            release.zipball_url,
            f"https://api.github.com/repos/{user}/{repo_name}/zipball/{tag}",
        )
        self.assertEqual(repr(release), 'GitRelease(name="Test")')
        self.assertEqual(len(release.assets), 1)
        self.assertEqual(
            repr(release.assets[0]),
            'GitReleaseAsset(url="https://api.github.com/repos/'
            f'{user}/{repo_name}/releases/assets/{release.raw_data["assets"][0]["id"]}")',
        )

    def testGetRelease(self):
        release_by_id = self.release
        release_by_tag = self.repo.get_release(tag)
        self.assertEqual(release_by_id, release_by_tag)

    def testGetLatestRelease(self):
        latest_release = self.repo.get_latest_release()
        self.assertEqual(latest_release.tag_name, tag)

    def testGetAssets(self):
        repo = self.repo
        release = self.release
        self.assertEqual(release.id, release_id)

        asset_list = [x for x in release.get_assets()]
        self.assertTrue(asset_list is not None)
        self.assertEqual(len(asset_list), 1)

        asset_id = asset_list[0].id
        asset = repo.get_release_asset(asset_id)
        self.assertTrue(asset is not None)
        self.assertEqual(asset.id, asset_id)

    def testDelete(self):
        self.setUpNewRelease()
        self.new_release.delete_release()
        self.tearDownNewRelease()

    def testUpdate(self):
        self.setUpNewRelease()
        release = self.new_release
        new_release = release.update_release("Updated Test", "Updated Body")
        self.assertEqual(new_release.name, "Updated Test")
        self.assertEqual(new_release.body, "Updated Body")
        self.tearDownNewRelease()

    def testUploadAsset(self):
        self.setUpNewRelease()
        release = self.new_release
        self.assertEqual(release.id, self.new_release_id)

        release.upload_asset(self.artifact_path, "unit test artifact", "application/zip")
        self.tearDownNewRelease()

    def testUploadAssetWithName(self):
        self.setUpNewRelease()
        release = self.new_release
        r = release.upload_asset(self.artifact_path, name="foobar.zip", content_type="application/zip")
        self.assertEqual(r.name, "foobar.zip")
        self.tearDownNewRelease()

    def testCreateGitTagAndRelease(self):
        self.setUpNewRelease()
        # Creation code already done in setup, so we'll just test what's already here.
        release = self.new_release
        self.assertEqual(release.tag_name, self.new_tag)
        self.assertEqual(release.body, "release message")
        self.assertEqual(release.name, "release title")
        self.assertEqual(release.author._rawData["login"], user)
        self.assertEqual(
            release.html_url,
            f"https://github.com/{user}/{repo_name}/releases/tag/{self.new_tag}",
        )
        self.tearDownNewRelease()

    def testUploadAssetFromMemory(self):
        self.setUpNewRelease()
        release = self.new_release
        content_size = os.path.getsize(self.content_path)
        with open(self.content_path, "rb") as f:
            release.upload_asset_from_memory(
                f,
                content_size,
                name="file_name",
                content_type="text/plain",
                label="unit test artifact",
            )
        asset_list = [x for x in release.get_assets()]
        self.assertTrue(asset_list is not None)
        self.assertEqual(len(asset_list), 1)
        self.tearDownNewRelease()

    def testUploadAssetFileLike(self):
        self.setUpNewRelease()
        file_like = FileLikeStub()
        release = self.new_release
        release.upload_asset_from_memory(
            file_like,
            file_like.file_length,
            name="file_like",
            content_type="text/plain",
            label="another unit test artifact",
        )
        asset_list = [x for x in release.get_assets()]
        self.assertTrue(asset_list is not None)
        self.assertEqual(len(asset_list), 1)
        self.tearDownNewRelease()
