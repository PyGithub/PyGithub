# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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
# ##############################################################################

import Framework

import github


class Issue380(Framework.TestCase):  # https://github.com/PyGithub/PyGithub/issues/380

    def setUp(self):
        Framework.TestCase.setUp(self)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo("PyGithub")

    def testCreateGitRelease(self):
        release = self.repo.create_git_release("TaggedByPyGithub", "ReleasedByPyGithub", "Release created by PyGithub")
        self.assertEqual(release.title, "ReleasedByPyGithub")
        self.assertEquals(release.tag_name, "TaggedByPyGithub")
        self.assertEquals(release.upload_url, "https://uploads.github.com/repos/ben-whitney/PyGithub/releases/4386771/assets{?name,label}")
        self.assertEquals(release.body, "Release created by PyGithub")
        self.assertEquals(release.url, "https://api.github.com/repos/ben-whitney/PyGithub/releases/4386771")
        self.assertEquals(release.author._rawData['login'], 'ben-whitney')
        self.assertEqual(release.__repr__(), 'GitRelease(title="ReleasedByPyGithub")')

    def testCreateGitReleaseWithAllArguments(self):
        release = self.repo.create_git_release("TaggedByPyGithub1", "ReleasedByPyGithub", "Release created by PyGithub", target_commitish="43f61f9471cc4c1aab69524ba53bb11d6597d0bf", draft=True, prerelease=True)
        self.assertEqual(release.title, "ReleasedByPyGithub")
        self.assertEquals(release.tag_name, "TaggedByPyGithub1")
        self.assertEquals(release.upload_url, "https://uploads.github.com/repos/ben-whitney/PyGithub/releases/4386769/assets{?name,label}")
        self.assertEquals(release.body, "Release created by PyGithub")
        self.assertEquals(release.url, "https://api.github.com/repos/ben-whitney/PyGithub/releases/4386769")
        self.assertEquals(release.author._rawData['login'], 'ben-whitney')
        self.assertEqual(release.__repr__(), 'GitRelease(title="ReleasedByPyGithub")')

    def testCreateGitTagAndRelease(self):
        release = self.repo.create_git_tag_and_release("TaggedByPyGithub2", "Tag created by PyGithub", "ReleasedByPyGitHub", "Release created by PyGitHub", "43f61f9471cc4c1aab69524ba53bb11d6597d0bf", "commit")
        self.assertEqual(release.title, "ReleasedByPyGitHub")
        self.assertEquals(release.tag_name, "TaggedByPyGithub2")
        self.assertEquals(release.upload_url, "https://uploads.github.com/repos/ben-whitney/PyGithub/releases/4386766/assets{?name,label}")
        self.assertEquals(release.body, "Release created by PyGitHub")
        self.assertEquals(release.url, "https://api.github.com/repos/ben-whitney/PyGithub/releases/4386766")
        self.assertEquals(release.author._rawData['login'], 'ben-whitney')
        self.assertEqual(release.__repr__(), 'GitRelease(title="ReleasedByPyGitHub")')

    def testCreateGitTagAndReleaseWithAllArguments(self):
        release = self.repo.create_git_tag_and_release("TaggedByPyGithub3", "Tag created by PyGithub", "ReleasedByPyGitHub", "Release created by PyGitHub", "43f61f9471cc4c1aab69524ba53bb11d6597d0bf", "commit", tagger=github.InputGitAuthor("John Doe", "j.doe@vincent-jacques.net", "2008-07-09T16:13:30+12:00"), target_commitish="43f61f9471cc4c1aab69524ba53bb11d6597d0bf", draft=True, prerelease=True)
        self.assertEqual(release.title, "ReleasedByPyGitHub")
        self.assertEquals(release.tag_name, "TaggedByPyGithub3")
        self.assertEquals(release.upload_url, "https://uploads.github.com/repos/ben-whitney/PyGithub/releases/4386768/assets{?name,label}")
        self.assertEquals(release.body, "Release created by PyGitHub")
        self.assertEquals(release.url, "https://api.github.com/repos/ben-whitney/PyGithub/releases/4386768")
        self.assertEquals(release.author._rawData['login'], 'ben-whitney')
        self.assertEqual(release.__repr__(), 'GitRelease(title="ReleasedByPyGitHub")')
