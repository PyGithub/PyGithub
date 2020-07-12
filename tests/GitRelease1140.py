# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Jesse Li (https://github.com/jesseli2002)                     #
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


class Release1140(Framework.TestCase):
    # https://github.com/PyGithub/PyGithub/issues/1140
    def setUp(self):
        # Following the comment in tests/GitRelease.py:
        #   "Do not get self.release here as it casues bad data to be saved in --record mode"
        # Guessing that it's a bad idea to write something like self.release = self.g.get_user().get_repo("RepoTest").get_releases()[0]
        super().setUp()
        self.content_path = "content.txt"
        with open(self.content_path, "w") as content:
            content.write("Files are my favorite!")

    def tearDown(self):
        if os.path.exists(self.content_path):
            os.remove(self.content_path)

    def testUploadAssetFromMemory(self):
        release = self.g.get_user().get_repo("RepoTest").get_releases()[0]

        content_size = os.path.getsize(self.content_path)
        with open(self.content_path, "rb") as f:
            release.upload_asset_from_memory(
                f,
                content_size,
                name="file_name",
                content_type="text/plain",
                label="unit test artifact",
            )

    def testUploadAssetFileLike(self):
        release = self.g.get_user().get_repo("RepoTest").get_releases()[0]
        file_like = FileLikeStub()
        release.upload_asset_from_memory(
            file_like,
            file_like.file_length,
            name="file_like",
            content_type="text/plain",
            label="another unit test artifact",
        )
