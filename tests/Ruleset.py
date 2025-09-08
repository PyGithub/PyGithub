############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Jens Keiner <jens.keiner@gmail.com>                           #
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

from datetime import datetime

from . import Framework


class Ruleset(Framework.TestCase):
    def setUp(self):
        super().setUp()
        repo = self.g.get_repo("PyGithub/PyGithub")
        self.ruleset = repo.get_ruleset(3474546)

    def testAttributes(self):
        self.assertEqual(self.ruleset.id, 3474546)
        self.assertEqual(self.ruleset.name, "main protection")
        self.assertEqual(self.ruleset.target, "branch")
        self.assertEqual(self.ruleset.source_type, "Repository")
        self.assertEqual(self.ruleset.source, "PyGithub/PyGithub")
        self.assertEqual(self.ruleset.enforcement, "active")
        self.assertEqual(self.ruleset.node_id, "RRS_lACqUmVwb3NpdG9yec43HleVzgA1BHI")
        self.assertEqual(self.ruleset.created_at, datetime.fromisoformat("2025-01-30T22:27:33.194+01:00"))
        self.assertEqual(self.ruleset.updated_at, datetime.fromisoformat("2025-01-30T22:27:33.194+01:00"))
        self.assertEqual(
            self.ruleset.conditions, {"ref_name": {"exclude": [], "include": ["refs/heads/master", "refs/heads/main"]}}
        )
        self.assertEqual(len(self.ruleset.rules), 6)
        self.assertEqual(self.ruleset.rules[0].type, "deletion")
        self.assertEqual(self.ruleset.rules[1].type, "non_fast_forward")
        self.assertEqual(self.ruleset.rules[2].type, "creation")
        self.assertEqual(self.ruleset.rules[3].type, "update")
        self.assertEqual(self.ruleset.rules[3].parameters, {"update_allows_fetch_and_merge": True})
        self.assertEqual(self.ruleset.rules[4].type, "required_signatures")
        self.assertEqual(self.ruleset.rules[5].type, "pull_request")
        self.assertEqual(
            self.ruleset.rules[5].parameters,
            {
                "required_approving_review_count": 0,
                "dismiss_stale_reviews_on_push": False,
                "require_code_owner_review": False,
                "require_last_push_approval": False,
                "required_review_thread_resolution": False,
                "automatic_copilot_code_review_enabled": False,
                "allowed_merge_methods": ["merge", "squash", "rebase"],
            },
        )
        self.assertEqual(len(self.ruleset.bypass_actors), 1)
        self.assertEqual(
            self.ruleset.bypass_actors[0], {"actor_id": 5, "actor_type": "RepositoryRole", "bypass_mode": "always"}
        )
        self.assertEqual(self.ruleset.current_user_can_bypass, "always")
        self.assertEqual(
            self.ruleset._links,
            {
                "self": {"href": "https://api.github.com/repos/PyGithub/PyGithub/rulesets/3474546"},
                "html": {"href": "https://github.com/PyGithub/PyGithub/rules/3474546"},
            },
        )

    def testUpdate(self):
        ruleset = self.ruleset.update(
            name="updated rule set",
            target="branch",
            enforcement="disabled",
            bypass_actors=[],
            conditions={
                "ref_name": {"exclude": [], "include": ["refs/heads/master", "refs/heads/main", "refs/heads/develop"]}
            },
            rules=[
                {"type": "deletion"},
                {"type": "creation"},
            ],
        )
        self.assertEqual(ruleset.id, 3474546)
        self.assertEqual(ruleset.name, "updated rule set")
        self.assertEqual(ruleset.target, "branch")
        self.assertEqual(ruleset.source_type, "Repository")
        self.assertEqual(ruleset.source, "PyGithub/PyGithub")
        self.assertEqual(ruleset.enforcement, "disabled")
        self.assertEqual(ruleset.node_id, "RRS_lACqUmVwb3NpdG9yec43HleVzgA1BHI")
        self.assertEqual(ruleset.created_at, datetime.fromisoformat("2025-01-31T20:59:12.515+01:00"))
        self.assertEqual(ruleset.updated_at, datetime.fromisoformat("2025-01-31T21:09:07.855+01:00"))
        self.assertEqual(
            ruleset.conditions,
            {"ref_name": {"exclude": [], "include": ["refs/heads/master", "refs/heads/main", "refs/heads/develop"]}},
        )
        self.assertEqual(len(ruleset.rules), 2)
        self.assertEqual(ruleset.rules[0].type, "deletion")
        self.assertEqual(ruleset.rules[1].type, "creation")
        self.assertEqual(ruleset.bypass_actors, [])
        self.assertEqual(ruleset.current_user_can_bypass, "never")
        self.assertEqual(
            ruleset._links,
            {
                "self": {"href": "https://api.github.com/repos/PyGithub/PyGithub/rulesets/3490869"},
                "html": {"href": "https://github.com/PyGithub/PyGithub/rules/3490869"},
            },
        )

    def testDelete(self):
        deleted = self.ruleset.delete()
        self.assertTrue(deleted)
