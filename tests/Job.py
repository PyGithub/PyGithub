############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Denis Blanchette <dblanchette@coveo.com>                      #
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
from datetime import datetime, timezone

from . import Framework


class Job(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("coveo")
        self.repo = self.org.get_repo("github-app")

    def testAttributes(self):
        workflow_runs = self.repo.get_workflow_runs()
        job = workflow_runs[0].get_jobs()[0]

        self.assertEqual(2993004021, job.id)
        self.assertEqual(1002152666, job.run_id)
        self.assertEqual("MDg6Q2hlY2tSdW4yOTkzMDA0MDIx", job.node_id)
        self.assertEqual("ba2ad8220081ac147afaa5e53e895a9db0ceefda", job.head_sha)
        self.assertEqual("completed", job.status)
        self.assertEqual("success", job.conclusion)
        self.assertEqual(datetime(2021, 7, 5, 19, 25, 20, tzinfo=timezone.utc), job.started_at)
        self.assertEqual(datetime(2021, 7, 5, 19, 26, 28, tzinfo=timezone.utc), job.completed_at)
        self.assertEqual("stew ci", job.name)
        self.assertEqual(10, len(job.steps))

        step = job.steps[0]
        self.assertEqual("Set up job", step.name)
        self.assertEqual("completed", step.status)
        self.assertEqual("success", step.conclusion)
        self.assertEqual(1, step.number)
        self.assertEqual(datetime(2021, 7, 5, 19, 25, 20, tzinfo=timezone.utc), step.started_at)
        self.assertEqual(datetime(2021, 7, 5, 19, 25, 21, tzinfo=timezone.utc), step.completed_at)
