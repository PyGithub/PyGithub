# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Victor Zeng <zacker150@hotmail.com>                           #
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

from . import Framework


class PullRequest1682(Framework.TestCase):
    def setUp(self):
        super().setUp()

    def testActorParamObj(self):
        repo = self.g.get_repo('PyGithub/PyGithub')
        user = self.g.get_user('s-t-e-v-e-n-k')
        runs = repo.get_workflow_runs(actor=user)
        first_run = runs[0]
        self.assertEqual(235543673, first_run.id)

    def testActorParamObjStr(self):
        repo = self.g.get_repo('PyGithub/PyGithub')
        runs = repo.get_workflow_runs(actor='s-t-e-v-e-n-k')
        first_run = runs[0]
        self.assertEqual(235543673, first_run.id)

    def testBranchParam(self):
        repo = self.g.get_repo("zacker150/DownloaderForReddit")
        branch = repo.get_branch('release_action')
        runs = repo.get_workflow_runs(branch=branch)
        first_run = runs[0]
        self.assertEqual(151007846, first_run.id)
        self.assertEqual(54, runs.totalCount)

    def testEventParam(self):
        repo = self.g.get_repo("zacker150/DownloaderForReddit")
        runs = repo.get_workflow_runs(event='pull_request')
        first_run = runs[0]
        self.assertEqual(33321769, first_run.id)
        self.assertEqual(1, runs.totalCount)

    def testStatusParam1(self):
        repo = self.g.get_repo("zacker150/DownloaderForReddit")
        runs = repo.get_workflow_runs(status='in_progress')
        first_run = runs[0]
        self.assertEqual(223464742, first_run.id)
        self.assertEqual(1, runs.totalCount)

    def testStatusParam2(self):
        repo = self.g.get_repo("zacker150/DownloaderForReddit")
        runs = repo.get_workflow_runs(status='failure')
        first_run = runs[0]
        self.assertEqual(223464742, first_run.id)



