############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Alson van der Meulen <alson.vandermeulen@dearhealth.com>      #
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

import pytest  # type: ignore

import github
import github.EnvironmentDeploymentBranchPolicy
import github.EnvironmentProtectionRule
import github.EnvironmentProtectionRuleReviewer
import github.NamedUser
import github.Team

from . import Framework


class Environment(Framework.TestCase):
    def setUp(self):
        self.tokenAuthMode = True
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.environment = self.repo.get_environment("dev")

    def testAttributes(self):
        self.assertEqual(self.environment.name, "dev")
        self.assertEqual(self.environment.id, 464814513)
        self.assertEqual(self.environment.node_id, "EN_kwDOHKhL9c4btIGx")
        self.assertEqual(
            self.environment.url,
            "https://api.github.com/repos/alson/PyGithub/environments/dev",
        )
        self.assertEqual(
            self.environment.html_url,
            "https://github.com/alson/PyGithub/deployments/activity_log?environments_filter=dev",
        )
        self.assertEqual(
            self.environment.created_at,
            datetime(2022, 4, 13, 15, 6, 32, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.environment.updated_at,
            datetime(2022, 4, 13, 15, 6, 32, tzinfo=timezone.utc),
        )
        self.assertTrue(self.environment.deployment_branch_policy.protected_branches)
        self.assertFalse(
            self.environment.deployment_branch_policy.custom_branch_policies
        )

    def testProtectionRules(self):
        protection_rules = self.environment.protection_rules
        self.assertEqual(len(protection_rules), 3)
        self.assertEqual(protection_rules[0].id, 216323)
        self.assertEqual(protection_rules[0].node_id, "GA_kwDOHKhL9c4AA00D")
        self.assertEqual(protection_rules[0].type, "branch_policy")
        self.assertEqual(protection_rules[1].id, 216324)
        self.assertEqual(protection_rules[1].node_id, "GA_kwDOHKhL9c4AA00E")
        self.assertEqual(protection_rules[1].type, "required_reviewers")
        self.assertEqual(protection_rules[2].id, 216325)
        self.assertEqual(protection_rules[2].node_id, "GA_kwDOHKhL9c4AA00F")
        self.assertEqual(protection_rules[2].type, "wait_timer")
        self.assertEqual(protection_rules[2].wait_timer, 15)

    def testReviewers(self):
        # This is necessary so we can maintain our own expectations, which have been manually editted, for this test.
        reviewers = self.repo.get_environment("dev").protection_rules[1].reviewers
        self.assertEqual(len(reviewers), 2)
        self.assertEqual(reviewers[0].type, "User")
        self.assertIsInstance(reviewers[0].reviewer, github.NamedUser.NamedUser)
        assert isinstance(
            reviewers[0].reviewer, github.NamedUser.NamedUser
        )  # Make type checker happy
        self.assertEqual(reviewers[0].reviewer.id, 19245)
        self.assertEqual(reviewers[0].reviewer.login, "alson")
        self.assertEqual(reviewers[0].reviewer.type, "User")
        self.assertEqual(reviewers[1].type, "Team")
        self.assertIsInstance(reviewers[1].reviewer, github.Team.Team)
        assert isinstance(
            reviewers[1].reviewer, github.Team.Team
        )  # Make type checker happy
        self.assertEqual(reviewers[1].reviewer.id, 1)
        self.assertEqual(reviewers[1].reviewer.slug, "justice-league")
        self.assertEqual(reviewers[1].reviewer.url, "https://api.github.com/teams/1")

    def testGetEnvironments(self):
        environments = self.repo.get_environments()
        self.assertEqual(environments.totalCount, 1)
        self.assertEqual(
            environments[0].url,
            "https://api.github.com/repos/alson/PyGithub/environments/dev",
        )
        self.assertEqual(environments[0].name, "dev")

    def testCreateEnvironment(self):
        environment = self.repo.create_environment("test")
        self.assertEqual(environment.name, "test")
        self.assertEqual(environment.id, 470015651)
        self.assertEqual(environment.node_id, "EN_kwDOHKhL9c4cA96j")
        self.assertEqual(
            environment.url,
            "https://api.github.com/repos/alson/PyGithub/environments/test",
        )
        self.assertEqual(
            environment.html_url,
            "https://github.com/alson/PyGithub/deployments/activity_log?environments_filter=test",
        )
        self.assertEqual(
            environment.created_at,
            datetime(2022, 4, 19, 14, 4, 32, tzinfo=timezone.utc),
        )
        self.assertEqual(
            environment.updated_at,
            datetime(2022, 4, 19, 14, 4, 32, tzinfo=timezone.utc),
        )
        self.assertEqual(len(environment.protection_rules), 0)
        self.assertIsNone(environment.deployment_branch_policy)

    def testUpdateEnvironment(self):
        environment = self.repo.create_environment(
            "test",
            wait_timer=42,
            reviewers=[
                github.EnvironmentProtectionRuleReviewer.ReviewerParams(
                    type_="User", id_=19245
                )
            ],
            deployment_branch_policy=github.EnvironmentDeploymentBranchPolicy.EnvironmentDeploymentBranchPolicyParams(
                protected_branches=True, custom_branch_policies=False
            ),
        )
        self.assertEqual(environment.name, "test")
        self.assertEqual(environment.id, 470015651)
        self.assertEqual(environment.node_id, "EN_kwDOHKhL9c4cA96j")
        self.assertEqual(
            environment.url,
            "https://api.github.com/repos/alson/PyGithub/environments/test",
        )
        self.assertEqual(
            environment.html_url,
            "https://github.com/alson/PyGithub/deployments/activity_log?environments_filter=test",
        )
        self.assertEqual(
            environment.created_at,
            datetime(2022, 4, 19, 14, 4, 32, tzinfo=timezone.utc),
        )
        self.assertEqual(
            environment.updated_at,
            datetime(2022, 4, 19, 14, 4, 32, tzinfo=timezone.utc),
        )
        self.assertEqual(len(environment.protection_rules), 3)
        self.assertEqual(environment.protection_rules[0].type, "required_reviewers")
        self.assertEqual(len(environment.protection_rules[0].reviewers), 1)
        self.assertEqual(environment.protection_rules[0].reviewers[0].type, "User")
        self.assertEqual(
            environment.protection_rules[0].reviewers[0].reviewer.id, 19245
        )
        self.assertEqual(environment.protection_rules[1].type, "wait_timer")
        self.assertEqual(environment.protection_rules[1].wait_timer, 42)
        self.assertEqual(environment.protection_rules[2].type, "branch_policy")
        self.assertTrue(environment.deployment_branch_policy.protected_branches)
        self.assertFalse(environment.deployment_branch_policy.custom_branch_policies)

    def testDeleteEnvironment(self):
        self.repo.delete_environment("test")
        with pytest.raises(github.UnknownObjectException):
            self.repo.get_environment("test")
