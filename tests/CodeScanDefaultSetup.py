############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

import json
import unittest
from datetime import datetime, timezone

import responses

from github import Auth, Github, GithubException
from github.CodeScanDefaultSetup import CodeScanDefaultSetup as Setup
from github.WorkflowRun import WorkflowRun


class CodeScanDefaultSetup(unittest.TestCase):
    def setUp(self):
        self.g = Github(auth=Auth.Token("test-token"), lazy=True)
        self.addCleanup(self.g.close)
        self.repo = self.g.get_repo("owner/repo")
        self.url = "https://api.github.com:443/repos/owner/repo/code-scanning/default-setup"

    @responses.activate
    def testGetConfiguration(self):
        responses.get(
            self.url,
            json={
                "state": "configured",
                "languages": ["python", "javascript-typescript"],
                "query_suite": "extended",
                "threat_model": "remote_and_local",
                "runner_type": "labeled",
                "runner_label": "codeql",
                "schedule": "weekly",
                "updated_at": "2023-01-19T11:21:34Z",
            },
        )
        setup = self.repo.get_codescan_default_setup()
        self.assertIsInstance(setup, Setup)
        self.assertEqual(setup.state, "configured")
        self.assertEqual(setup.languages, ["python", "javascript-typescript"])
        self.assertEqual(setup.query_suite, "extended")
        self.assertEqual(setup.threat_model, "remote_and_local")
        self.assertEqual(setup.runner_type, "labeled")
        self.assertEqual(setup.runner_label, "codeql")
        self.assertEqual(setup.schedule, "weekly")
        self.assertEqual(setup.updated_at, datetime(2023, 1, 19, 11, 21, 34, tzinfo=timezone.utc))
        self.assertEqual(len(responses.calls), 1)

    @responses.activate
    def testGetUnconfigured(self):
        responses.get(
            self.url,
            json={"state": "not-configured", "runner_label": None, "schedule": None, "updated_at": None},
        )
        setup = self.repo.get_codescan_default_setup()
        self.assertEqual(setup.state, "not-configured")
        self.assertIsNone(setup.runner_label)
        self.assertIsNone(setup.schedule)
        self.assertIsNone(setup.updated_at)

    @responses.activate
    def testUpdateStartsValidation(self):
        run_url = "https://api.github.com/repos/owner/repo/actions/runs/42"
        responses.patch(self.url, json={"run_id": 42, "run_url": run_url}, status=202)
        parameters = {
            "state": "configured",
            "runner_type": "standard",
            "runner_label": None,
            "query_suite": "extended",
            "threat_model": "remote_and_local",
            "languages": ["python"],
        }
        run = self.repo.set_codescan_default_setup(**parameters)
        self.assertIsInstance(run, WorkflowRun)
        self.assertEqual(run.id, 42)
        self.assertEqual(run.url, run_url)
        self.assertEqual(json.loads(responses.calls[0].request.body), parameters)
        self.assertEqual(len(responses.calls), 1)

    @responses.activate
    def testUpdateOmitsUnspecifiedParameters(self):
        responses.patch(self.url, json={}, status=200)
        self.assertIsNone(self.repo.set_codescan_default_setup(state="not-configured"))
        self.assertEqual(json.loads(responses.calls[0].request.body), {"state": "not-configured"})

    @responses.activate
    def testUpdatePropagatesErrors(self):
        responses.patch(self.url, json={"message": "Validation already in progress"}, status=409)
        with self.assertRaises(GithubException) as error:
            self.repo.set_codescan_default_setup(state="configured")
        self.assertEqual(error.exception.status, 409)
