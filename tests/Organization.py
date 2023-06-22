############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Balázs Rostás <rostas.balazs@gmail.com>                     #
# Copyright 2018 Anton Nguyen <afnguyen85@gmail.com>                           #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Jasper van Wanrooy <jasper@vanwanrooy.net>                    #
# Copyright 2018 Raihaan <31362124+res0nance@users.noreply.github.com>         #
# Copyright 2018 Tim Boring <tboring@hearst.com>                               #
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

from datetime import datetime, timezone
from unittest import mock

import github

from . import Framework


class Organization(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("BeaverSoftware")

    def testAttributes(self):
        self.assertEqual(
            self.org.avatar_url, "https://avatars1.githubusercontent.com/u/1?v=4"
        )
        self.assertEqual(self.org.billing_email, "foo@example.com")
        self.assertEqual(self.org.blog, "http://www.example.com")
        self.assertEqual(self.org.collaborators, 9)
        self.assertEqual(self.org.company, None)
        self.assertEqual(
            self.org.created_at,
            datetime(2014, 1, 9, 16, 56, 17, tzinfo=timezone.utc),
        )
        self.assertEqual(self.org.default_repository_permission, "none")
        self.assertEqual(self.org.description, "BeaverSoftware writes software.")
        self.assertEqual(self.org.disk_usage, 2)
        self.assertEqual(self.org.email, "")
        self.assertEqual(self.org.followers, 0)
        self.assertEqual(self.org.following, 0)
        self.assertEqual(self.org.gravatar_id, None)
        self.assertTrue(self.org.has_organization_projects)
        self.assertTrue(self.org.has_repository_projects)
        self.assertEqual(
            self.org.hooks_url, "https://api.github.com/orgs/BeaverSoftware/hooks"
        )
        self.assertEqual(self.org.html_url, "https://github.com/BeaverSoftware")
        self.assertEqual(self.org.id, 1)
        self.assertEqual(
            self.org.issues_url, "https://api.github.com/orgs/BeaverSoftware/issues"
        )
        self.assertEqual(self.org.location, "Paris, France")
        self.assertEqual(self.org.login, "BeaverSoftware")
        self.assertFalse(self.org.members_can_create_repositories)
        self.assertEqual(self.org.name, "BeaverSoftware")
        self.assertEqual(self.org.owned_private_repos, 0)
        self.assertEqual(self.org.plan.name, "free")
        self.assertEqual(self.org.plan.private_repos, 3)
        self.assertEqual(self.org.plan.space, 1)
        self.assertEqual(self.org.plan.filled_seats, 3)
        self.assertEqual(self.org.plan.seats, 0)
        self.assertEqual(self.org.private_gists, 0)
        self.assertEqual(self.org.public_gists, 0)
        self.assertEqual(self.org.public_repos, 27)
        self.assertEqual(self.org.total_private_repos, 7)
        self.assertEqual(self.org.two_factor_requirement_enabled, None)
        self.assertEqual(self.org.type, "Organization")
        self.assertEqual(self.org.url, "https://api.github.com/orgs/BeaverSoftware")
        self.assertEqual(repr(self.org), 'Organization(login="BeaverSoftware")')

    def testAddMembersDefaultRole(self):
        lyloa = self.g.get_user("lyloa")
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.add_to_members(lyloa, role="member")
        # 'Pending' members won't be in /orgs/:org/members/:user
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.remove_from_membership(lyloa)
        self.assertFalse(self.org.has_in_members(lyloa))

    def testAddMembersAdminRole(self):
        lyloa = self.g.get_user("lyloa")
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.add_to_members(lyloa, role="admin")
        # 'Pending' members won't be in /orgs/:org/members/:user
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.remove_from_membership(lyloa)
        self.assertFalse(self.org.has_in_members(lyloa))

    def testEditWithoutArguments(self):
        self.org.edit()

    def testEditWithAllArguments(self):
        self.org.edit(
            "BeaverSoftware2@vincent-jacques.net",
            "http://vincent-jacques.net",
            "Company edited by PyGithub",
            "Description edited by PyGithub",
            "BeaverSoftware2@vincent-jacques.net",
            "Location edited by PyGithub",
            "Name edited by PyGithub",
        )
        self.assertEqual(self.org.billing_email, "BeaverSoftware2@vincent-jacques.net")
        self.assertEqual(self.org.blog, "http://vincent-jacques.net")
        self.assertEqual(self.org.company, "Company edited by PyGithub")
        self.assertEqual(self.org.description, "Description edited by PyGithub")
        self.assertEqual(self.org.email, "BeaverSoftware2@vincent-jacques.net")
        self.assertEqual(self.org.location, "Location edited by PyGithub")
        self.assertEqual(self.org.name, "Name edited by PyGithub")

    def testEditHookWithMinimalParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"})
        hook = self.org.edit_hook(hook.id, "mobile", {"url": "http://barfoo.com"})
        self.assertEqual(hook.name, "mobile")

    def testEditHookWithAllParameters(self):
        hook = self.org.create_hook(
            "web", {"url": "http://foobar.com"}, ["fork"], False
        )
        hook = self.org.edit_hook(
            hook.id, "mobile", {"url": "http://barfoo.com"}, ["spoon"], True
        )
        self.assertEqual(hook.name, "mobile")
        self.assertEqual(hook.events, ["spoon"])
        self.assertEqual(hook.active, True)

    def testCreateTeam(self):
        team = self.org.create_team("Team created by PyGithub")
        self.assertEqual(team.id, 189850)

    def testCreateTeamWithAllArguments(self):
        repo = self.org.get_repo("FatherBeaver")
        team = self.org.create_team(
            "Team also created by PyGithub",
            [repo],
            "push",
            "secret",
            "Description also created by PyGithub",
        )
        self.assertEqual(team.id, 189852)
        self.assertEqual(team.description, "Description also created by PyGithub")

    def testDeleteHook(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"})
        self.org.delete_hook(hook.id)

    def testPublicMembers(self):
        lyloa = self.g.get_user("Lyloa")
        self.assertFalse(self.org.has_in_public_members(lyloa))
        self.org.add_to_public_members(lyloa)
        self.assertTrue(self.org.has_in_public_members(lyloa))
        self.org.remove_from_public_members(lyloa)
        self.assertFalse(self.org.has_in_public_members(lyloa))

    def testGetPublicMembers(self):
        self.assertListKeyEqual(
            self.org.get_public_members(), lambda u: u.login, ["jacquev6"]
        )

    def testGetHook(self):
        hook = self.org.get_hook(257993)
        self.assertEqual(hook.name, "web")

    def testGetHooks(self):
        self.assertListKeyEqual(self.org.get_hooks(), lambda h: h.id, [257993])

    def testGetHookDelivery(self):
        delivery = self.org.get_hook_delivery(257993, 12345)
        self.assertEqual(delivery.id, 12345)
        self.assertEqual(delivery.guid, "abcde-12345")
        self.assertEqual(
            delivery.delivered_at,
            datetime(2012, 5, 27, 6, 0, 32, tzinfo=timezone.utc),
        )
        self.assertEqual(delivery.redelivery, False)
        self.assertEqual(delivery.duration, 0.27)
        self.assertEqual(delivery.status, "OK")
        self.assertEqual(delivery.status_code, 200)
        self.assertEqual(delivery.event, "issues")
        self.assertEqual(delivery.action, "opened")
        self.assertEqual(delivery.installation_id, 123)
        self.assertEqual(delivery.repository_id, 456)
        self.assertEqual(delivery.url, "https://www.example-webhook.com")
        self.assertIsInstance(delivery.request, github.HookDelivery.HookDeliveryRequest)
        self.assertEqual(delivery.request.headers, {"content-type": "application/json"})
        self.assertEqual(delivery.request.payload, {"action": "opened"})
        self.assertIsInstance(
            delivery.response, github.HookDelivery.HookDeliveryResponse
        )
        self.assertEqual(
            delivery.response.headers, {"content-type": "text/html;charset=utf-8"}
        )
        self.assertEqual(delivery.response.payload, "ok")

    def testGetHookDeliveries(self):
        deliveries = list(self.org.get_hook_deliveries(257993))
        self.assertEqual(len(deliveries), 1)
        self.assertEqual(deliveries[0].id, 12345)
        self.assertEqual(deliveries[0].guid, "abcde-12345")
        self.assertEqual(
            deliveries[0].delivered_at,
            datetime(2012, 5, 27, 6, 0, 32, tzinfo=timezone.utc),
        )
        self.assertEqual(deliveries[0].redelivery, False)
        self.assertEqual(deliveries[0].duration, 0.27)
        self.assertEqual(deliveries[0].status, "OK")
        self.assertEqual(deliveries[0].status_code, 200)
        self.assertEqual(deliveries[0].event, "issues")
        self.assertEqual(deliveries[0].action, "opened")
        self.assertEqual(deliveries[0].installation_id, 123)
        self.assertEqual(deliveries[0].repository_id, 456)
        self.assertEqual(deliveries[0].url, "https://www.example-webhook.com")

    def testGetIssues(self):
        self.assertListKeyEqual(self.org.get_issues(), lambda i: i.id, [])

    def testGetIssuesWithAllArguments(self):
        requestedByUser = (
            self.g.get_user().get_repo("PyGithub").get_label("Requested by user")
        )
        issues = self.org.get_issues(
            "assigned",
            "closed",
            [requestedByUser],
            "comments",
            "asc",
            datetime(2012, 5, 28, 23, 0, 0, tzinfo=timezone.utc),
        )
        self.assertListKeyEqual(issues, lambda i: i.id, [])

    def testGetMembers(self):
        self.assertListKeyEqual(
            self.org.get_members(), lambda u: u.login, ["cjuniet", "jacquev6", "Lyloa"]
        )

    def testGetOutsideCollaborators(self):
        self.assertListKeyEqual(
            self.org.get_outside_collaborators(), lambda u: u.login, ["octocat"]
        )

    def testOutsideCollaborators(self):
        octocat = self.g.get_user("octocat")
        self.org.convert_to_outside_collaborator(octocat)
        self.assertListKeyEqual(
            self.org.get_outside_collaborators(), lambda u: u.login, ["octocat"]
        )
        self.org.remove_outside_collaborator(octocat)
        self.assertEqual(list(self.org.get_outside_collaborators()), [])

    def testMembers(self):
        lyloa = self.g.get_user("Lyloa")
        self.assertTrue(self.org.has_in_members(lyloa))
        self.org.remove_from_members(lyloa)
        self.assertFalse(self.org.has_in_members(lyloa))

    def testGetRepos(self):
        repos = self.org.get_repos()
        self.assertListKeyEqual(
            repos, lambda r: r.name, ["FatherBeaver", "TestPyGithub"]
        )
        self.assertListKeyEqual(repos, lambda r: r.has_pages, [True, False])
        self.assertListKeyEqual(repos, lambda r: r.has_wiki, [True, True])

    def testGetReposSorted(self):
        repos = self.org.get_repos(sort="updated", direction="desc")
        self.assertListKeyEqual(
            repos,
            lambda r: r.name,
            ["TestPyGithub", "FatherBeaver"],
        )
        self.assertListKeyEqual(
            repos,
            lambda r: r.has_pages,
            [False, True],
        )

    def testGetReposWithType(self):
        repos = self.org.get_repos("public")
        self.assertListKeyEqual(repos, lambda r: r.name, ["FatherBeaver", "PyGithub"])
        self.assertListKeyEqual(repos, lambda r: r.has_pages, [True, True])

    def testGetEvents(self):
        self.assertListKeyEqual(
            self.org.get_events(),
            lambda e: e.type,
            [
                "CreateEvent",
                "CreateEvent",
                "PushEvent",
                "PushEvent",
                "DeleteEvent",
                "DeleteEvent",
                "PushEvent",
                "PushEvent",
                "DeleteEvent",
                "DeleteEvent",
                "PushEvent",
                "PushEvent",
                "PushEvent",
                "CreateEvent",
                "CreateEvent",
                "CreateEvent",
                "CreateEvent",
                "CreateEvent",
                "PushEvent",
                "PushEvent",
                "PushEvent",
                "PushEvent",
                "PushEvent",
                "PushEvent",
                "ForkEvent",
                "CreateEvent",
            ],
        )

    def testGetTeams(self):
        self.assertListKeyEqual(
            self.org.get_teams(), lambda t: t.name, ["Members", "Owners"]
        )

    def testGetTeamBySlug(self):
        team = self.org.get_team_by_slug("Members")
        self.assertEqual(team.id, 141496)

    def testCreateHookWithMinimalParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"})
        self.assertEqual(hook.id, 257967)

    def testCreateHookWithAllParameters(self):
        hook = self.org.create_hook(
            "web", {"url": "http://foobar.com"}, ["fork"], False
        )
        self.assertTrue(hook.active)
        self.assertEqual(hook.id, 257993)

    def testCreateRepoWithMinimalArguments(self):
        repo = self.org.create_repo(name="TestPyGithub")
        self.assertEqual(
            repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub"
        )
        self.assertTrue(repo.has_wiki)
        self.assertTrue(repo.has_pages)

    def testCreateRepoWithAllArguments(self):
        team = self.org.get_team(141496)
        repo = self.org.create_repo(
            name="TestPyGithub2",
            description="Repo created by PyGithub",
            homepage="http://foobar.com",
            private=False,
            visibility="public",
            has_issues=False,
            has_projects=False,
            has_wiki=False,
            has_downloads=False,
            team_id=team.id,
            allow_update_branch=True,
            allow_squash_merge=False,
            allow_merge_commit=False,
            allow_rebase_merge=True,
            delete_branch_on_merge=False,
        )
        self.assertEqual(
            repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub2"
        )
        self.assertTrue(repo.allow_update_branch)
        self.assertFalse(repo.has_wiki)
        self.assertFalse(repo.has_pages)

    def testCreateRepositoryWithAutoInit(self):
        repo = self.org.create_repo(
            name="TestPyGithub", auto_init=True, gitignore_template="Python"
        )
        self.assertEqual(
            repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub"
        )
        self.assertTrue(repo.has_pages)
        self.assertTrue(repo.has_wiki)

    def testCreateFork(self):
        pygithub = self.g.get_user("jacquev6").get_repo("PyGithub")
        repo = self.org.create_fork(pygithub)
        self.assertEqual(
            repo.url, "https://api.github.com/repos/BeaverSoftware/PyGithub"
        )
        self.assertFalse(repo.has_wiki)
        self.assertFalse(repo.has_pages)

    def testCreateRepoFromTemplate(self):
        template_repo = self.g.get_repo("actions/hello-world-docker-action")

        repo = self.org.create_repo_from_template(
            "hello-world-docker-action-new", template_repo
        )
        self.assertEqual(
            repo.url,
            "https://api.github.com/repos/BeaverSoftware/hello-world-docker-action-new",
        )
        self.assertFalse(repo.is_template)

    def testCreateRepoFromTemplateWithAllArguments(self):
        template_repo = self.g.get_repo("actions/hello-world-docker-action")

        description = "My repo from template"
        private = True
        repo = self.org.create_repo_from_template(
            "hello-world-docker-action-new",
            template_repo,
            description=description,
            private=private,
        )
        self.assertEqual(repo.description, description)
        self.assertTrue(repo.private)

    @mock.patch("github.PublicKey.encrypt")
    def testCreateSecret(self, encrypt):
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        self.assertTrue(self.org.create_secret("secret-name", "secret-value", "all"))

    @mock.patch("github.PublicKey.encrypt")
    def testCreateSecretSelected(self, encrypt):
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        repos = [self.org.get_repo("TestPyGithub"), self.org.get_repo("FatherBeaver")]
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        self.assertTrue(
            self.org.create_secret("secret-name", "secret-value", "selected", repos)
        )

    def testDeleteSecret(self):
        self.assertTrue(self.org.delete_secret("secret-name"))

    def testInviteUserWithNeither(self):
        with self.assertRaises(AssertionError) as raisedexp:
            self.org.invite_user()
        self.assertEqual("specify only one of email or user", str(raisedexp.exception))

    def testInviteUserWithBoth(self):
        jacquev6 = self.g.get_user("jacquev6")
        with self.assertRaises(AssertionError) as raisedexp:
            self.org.invite_user(email="foo", user=jacquev6)
        self.assertEqual("specify only one of email or user", str(raisedexp.exception))

    def testInviteUserByName(self):
        jacquev6 = self.g.get_user("jacquev6")
        self.org.invite_user(user=jacquev6)

    def testInviteUserByEmail(self):
        self.org.invite_user(email="foo@example.com")

    def testInviteUserWithRoleAndTeam(self):
        team = self.org.create_team("Team created by PyGithub")
        self.org.invite_user(
            email="foo@example.com", role="billing_manager", teams=[team]
        )

    def testInviteUserAsNonOwner(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.org.invite_user(email="bar@example.com")
        self.assertEqual(raisedexp.exception.status, 403)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/orgs/members/#create-organization-invitation",
                "message": "You must be an admin to create an invitation to an organization.",
            },
        )

    def testCreateMigration(self):
        self.org = self.g.get_organization("sample-test-organisation")
        self.assertTrue(
            isinstance(
                self.org.create_migration(["sample-repo"]), github.Migration.Migration
            )
        )

    def testGetMigrations(self):
        self.org = self.g.get_organization("sample-test-organisation")
        self.assertEqual(self.org.get_migrations().totalCount, 2)

    def testGetInstallations(self):
        installations = self.org.get_installations()
        self.assertEqual(installations[0].id, 123456)
        self.assertEqual(installations[0].app_id, 10101)
        self.assertEqual(installations[0].target_id, 3344556)
        self.assertEqual(installations[0].target_type, "User")
        self.assertEqual(installations.totalCount, 1)
