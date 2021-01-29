############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from . import Framework


class Workflow(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.workflow = self.g.get_repo("PyGithub/PyGithub").get_workflow("check.yml")

    def testAttributes(self):
        self.assertEqual(
            repr(self.workflow),
            'Workflow(url="https://api.github.com/repos/PyGithub/PyGithub/actions/workflows/1026390", name="check")',
        )
        self.assertEqual(self.workflow.id, 1026390)
        self.assertEqual(self.workflow.name, "check")
        self.assertEqual(self.workflow.path, ".github/workflows/check.yml")
        self.assertEqual(self.workflow.state, "active")
        timestamp = datetime.datetime(
            2020, 4, 15, 0, 48, 32, tzinfo=datetime.timezone.utc
        )
        self.assertEqual(self.workflow.created_at, timestamp)
        self.assertEqual(self.workflow.updated_at, timestamp)
        self.assertEqual(
            self.workflow.url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/workflows/1026390",
        )
        self.assertEqual(
            self.workflow.html_url,
            "https://github.com/PyGithub/PyGithub/blob/master/.github/workflows/check.yml",
        )
        self.assertEqual(
            self.workflow.badge_url,
            "https://github.com/PyGithub/PyGithub/workflows/check/badge.svg",
        )

    def testGetRunsWithNoArguments(self):
        self.assertListKeyEqual(
            self.workflow.get_runs(),
            lambda r: r.id,
            [109950033, 109168419, 108934155, 108817672],
        )

    def testGetRunsWithObjects(self):
        sfdye = self.g.get_user("sfdye")
        master = self.g.get_repo("PyGithub/PyGithub").get_branch("master")
        self.assertListKeyEqual(
            self.workflow.get_runs(
                actor=sfdye, branch=master, event="push", status="completed"
            ),
            lambda r: r.id,
            [100957683, 94845611, 93946842, 92714488],
        )

    def testGetRunsWithStrings(self):
        self.assertListKeyEqual(
            self.workflow.get_runs(actor="s-t-e-v-e-n-k", branch="master"),
            lambda r: r.id,
            [109950033, 108817672, 108794468, 107927403, 105213061, 105212023],
        )

    def testCreateDispatchWithBranch(self):
        dispatch_inputs = {"logLevel": "Warning", "message": "Log Message"}
        workflow = self.g.get_repo("wrecker/PyGithub").get_workflow(
            "manual_dispatch.yml"
        )
        branch = self.g.get_repo("wrecker/PyGithub").get_branch(
            "workflow_dispatch_branch"
        )
        self.assertTrue(workflow.create_dispatch(branch, dispatch_inputs))

    def testCreateDispatchWithTag(self):
        dispatch_inputs = {"logLevel": "Warning", "message": "Log Message"}
        workflow = self.g.get_repo("wrecker/PyGithub").get_workflow(
            "manual_dispatch.yml"
        )
        tags = self.g.get_repo("wrecker/PyGithub").get_tags()
        tag = [t for t in tags if t.name == "workflow_dispatch_tag"].pop()
        self.assertTrue(workflow.create_dispatch(tag, dispatch_inputs))

    def testCreateDispatchWithString(self):
        dispatch_inputs = {"logLevel": "Warning", "message": "Log Message"}
        workflow = self.g.get_repo("wrecker/PyGithub").get_workflow(
            "manual_dispatch.yml"
        )
        ref_str = "main"
        self.assertTrue(workflow.create_dispatch(ref_str, dispatch_inputs))

    def testCreateDispatchForNonTriggerEnabled(self):
        workflow = self.g.get_repo("wrecker/PyGithub").get_workflow("check.yml")
        self.assertFalse(workflow.create_dispatch("main"))
