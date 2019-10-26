# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Christopher Wilcox <git@crwilcox.com>                         #
# Copyright 2015 Dan Vanderkam <danvdk@gmail.com>                              #
# Copyright 2015 Enix Yu <enix223@163.com>                                     #
# Copyright 2015 Kyle Hornberg <khornberg@users.noreply.github.com>            #
# Copyright 2015 Uriel Corfa <uriel@corfa.fr>                                  #
# Copyright 2016 @tmshn <tmshn@r.recruit.co.jp>                                #
# Copyright 2016 Enix Yu <enix223@163.com>                                     #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Jimmy Zelinskie <jimmyzelinskie@gmail.com>                    #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Hayden Fuss <wifu1234@gmail.com>                              #
# Copyright 2018 Iraquitan Cordeiro Filho <iraquitanfilho@gmail.com>           #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Mateusz Loskot <mateusz@loskot.net>                           #
# Copyright 2018 Raihaan <31362124+res0nance@users.noreply.github.com>         #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Victor Granic <vmg@boreal321.com>                             #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Will Yardley <wyardley@users.noreply.github.com>              #
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
