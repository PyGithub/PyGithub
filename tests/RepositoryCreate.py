# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 anderstornkvist <dev@anderstornkvist.se>                      #
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

from __future__ import absolute_import

from github.Repository import Repository
from . import Framework


class RepositoryCreate(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)

    def testCreateRepoWithoutParameters(self):
        repo_name = 'test-repo-1'
        new_repo = self.g.create_repo(repo_name)  # type: Repository
        self.assertEqual(new_repo.name, repo_name)
        print(new_repo.name)

    def testCreateRepoWithParameters(self):
        repo_name = 'test-repo-2'
        repo_description = 'Just a test repo'
        private = True
        new_repo = self.g.create_repo(repo_name, description=repo_description, homepage='http://example.com/',
                                      private=private, has_issues=False, has_projects=False, has_wiki=False,
                                      is_template=False, auto_init=True,
                                      gitignore_template='Python', license_template='MIT', allow_squash_merge=False,
                                      allow_merge_commit=True, allow_rebase_merge=False)  # type: Repository

        self.assertEqual(new_repo.name, repo_name)
        self.assertEqual(new_repo.description, repo_description)
        self.assertEqual(new_repo.private, private)
