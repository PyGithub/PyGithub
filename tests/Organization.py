############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Balázs Rostás <rostas.balazs@gmail.com>                       #
# Copyright 2018 Anton Nguyen <afnguyen85@gmail.com>                           #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Jasper van Wanrooy <jasper@vanwanrooy.net>                    #
# Copyright 2018 Raihaan <31362124+res0nance@users.noreply.github.com>         #
# Copyright 2018 Shubham Singh <41840111+singh811@users.noreply.github.com>    #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Tim Boring <tboring@hearst.com>                               #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Brian Choy <byceee@gmail.com>                                 #
# Copyright 2019 Geoffroy Jabouley <gjabouley@invensense.com>                  #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2019 ebrown <brownierin@users.noreply.github.com>                  #
# Copyright 2020 Geoff Low <glow@mdsol.com>                                    #
# Copyright 2020 Glenn McDonald <testworksau@users.noreply.github.com>         #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 latacora-daniel <71085674+latacora-daniel@users.noreply.github.com>#
# Copyright 2020 ton-katsu <sakamoto.yoshihisa@gmail.com>                      #
# Copyright 2021 Marina Peresypkina <mi9onev@gmail.com>                        #
# Copyright 2021 Tanner <51724788+lightningboltemoji@users.noreply.github.com> #
# Copyright 2022 KimSia Sim <245021+simkimsia@users.noreply.github.com>        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Felipe Peter <mr-peipei@web.de>                               #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Greg <31892308+jmgreg31@users.noreply.github.com>    #
# Copyright 2023 Mauricio Alejandro Martínez Pacheco <mauricio.martinez@premise.com>#
# Copyright 2023 Mauricio Alejandro Martínez Pacheco <n_othing@hotmail.com>    #
# Copyright 2024 Andrii Kezikov <cheshirez@gmail.com>                          #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jacky Lam <jacky.lam@r2studiohk.com>                          #
# Copyright 2024 Mohamed Mostafa <112487260+mohy01@users.noreply.github.com>   #
# Copyright 2024 Oskar Jansson <56458534+janssonoskar@users.noreply.github.com>#
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
# Copyright 2024 Thomas Crowley <15927917+thomascrowley@users.noreply.github.com>#
# Copyright 2025 Bill Napier <napier@pobox.com>                                #
# Copyright 2025 Dom Heinzeller <dom.heinzeller@icloud.com>                    #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Greg Fogelberg <52933995+gfog-floqast@users.noreply.github.com>#
# Copyright 2025 Pavel Abramov <31950564+uncleDecart@users.noreply.github.com> #
# Copyright 2025 Zachary <6599715+interifter@users.noreply.github.com>         #
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

from datetime import datetime, timedelta, timezone
from unittest import mock

import github
from github.OrganizationCustomProperty import CustomProperty

from . import Framework


class Organization(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("BeaverSoftware")

    def testAttributes(self):
        self.assertIsNone(self.org.advanced_security_enabled_for_new_repositories)
        self.assertIsNone(self.org.archived_at)
        self.assertEqual(self.org.avatar_url, "https://avatars.githubusercontent.com/u/12345678?v=4")
        self.assertEqual(self.org.billing_email, "foo@example.com")
        self.assertEqual(self.org.blog, "http://www.example.com")
        self.assertEqual(self.org.collaborators, 9)
        self.assertEqual(self.org.company, None)
        self.assertEqual(self.org.created_at, datetime(2014, 1, 9, 16, 56, 17, tzinfo=timezone.utc))
        self.assertIsNone(self.org.default_repository_branch)
        self.assertIsNone(self.org.default_repository_permission)
        self.assertIsNone(self.org.dependabot_alerts_enabled_for_new_repositories)
        self.assertIsNone(self.org.dependabot_security_updates_enabled_for_new_repositories)
        self.assertIsNone(self.org.dependency_graph_enabled_for_new_repositories)
        self.assertEqual(self.org.deploy_keys_enabled_for_repositories, True)
        self.assertEqual(self.org.description, "BeaverSoftware writes software.")
        self.assertIsNone(self.org.disk_usage)
        self.assertIsNone(self.org.display_commenter_full_name_setting_enabled)
        self.assertIsNone(self.org.display_login)
        self.assertEqual(self.org.email, "foo@example.com")
        self.assertEqual(self.org.events_url, "https://api.github.com/orgs/BeaverSoftware/events")
        self.assertEqual(self.org.followers, 130)
        self.assertIsNone(self.org.followers_url)
        self.assertEqual(self.org.following, 1)
        self.assertIsNone(self.org.following_url)
        self.assertIsNone(self.org.gists_url)
        self.assertEqual(self.org.gravatar_id, None)
        self.assertEqual(self.org.has_organization_projects, True)
        self.assertEqual(self.org.has_repository_projects, True)
        self.assertEqual(self.org.hooks_url, "https://api.github.com/orgs/BeaverSoftware/hooks")
        self.assertEqual(self.org.html_url, "https://github.com/BeaverSoftware")
        self.assertEqual(self.org.id, 21341965)
        self.assertEqual(self.org.is_verified, False)
        self.assertEqual(self.org.issues_url, "https://api.github.com/orgs/BeaverSoftware/issues")
        self.assertEqual(self.org.location, "Paris, France")
        self.assertEqual(self.org.login, "BeaverSoftware")
        self.assertEqual(self.org.members_allowed_repository_creation_type, "none")
        self.assertIsNone(self.org.members_can_change_repo_visibility)
        self.assertEqual(self.org.members_can_create_internal_repositories, False)
        self.assertEqual(self.org.members_can_create_pages, True)
        self.assertEqual(self.org.members_can_create_private_pages, True)
        self.assertEqual(self.org.members_can_create_private_repositories, False)
        self.assertEqual(self.org.members_can_create_public_pages, True)
        self.assertEqual(self.org.members_can_create_public_repositories, False)
        self.assertEqual(self.org.members_can_create_repositories, False)
        self.assertIsNone(self.org.members_can_create_teams)
        self.assertIsNone(self.org.members_can_delete_issues)
        self.assertIsNone(self.org.members_can_delete_repositories)
        self.assertEqual(self.org.members_can_fork_private_repositories, False)
        self.assertIsNone(self.org.members_can_invite_outside_collaborators)
        self.assertIsNone(self.org.members_can_view_dependency_insights)
        self.assertEqual(self.org.members_url, "https://api.github.com/orgs/BeaverSoftware/members{/member}")
        self.assertEqual(self.org.name, "BeaverSoftware")
        self.assertEqual(self.org.node_id, "AbCdEfG")
        self.assertIsNone(self.org.organizations_url)
        self.assertEqual(self.org.owned_private_repos, 191)
        self.assertEqual(self.org.plan.name, "enterprise")
        self.assertEqual(self.org.plan.private_repos, 999999)
        self.assertEqual(self.org.plan.space, 123456789)
        self.assertEqual(self.org.plan.filled_seats, 640)
        self.assertEqual(self.org.plan.seats, 1024)
        self.assertIsNone(self.org.private_gists)
        self.assertEqual(self.org.public_gists, 0)
        self.assertEqual(
            self.org.public_members_url, "https://api.github.com/orgs/BeaverSoftware/public_members{/member}"
        )
        self.assertEqual(self.org.public_repos, 121)
        self.assertIsNone(self.org.readers_can_create_discussions)
        self.assertIsNone(self.org.received_events_url)
        self.assertEqual(self.org.repos_url, "https://api.github.com/orgs/BeaverSoftware/repos")
        self.assertIsNone(self.org.secret_scanning_enabled_for_new_repositories)
        self.assertIsNone(self.org.secret_scanning_push_protection_custom_link)
        self.assertIsNone(self.org.secret_scanning_push_protection_custom_link_enabled)
        self.assertIsNone(self.org.secret_scanning_push_protection_enabled_for_new_repositories)
        self.assertIsNone(self.org.site_admin)
        self.assertIsNone(self.org.starred_at)
        self.assertIsNone(self.org.starred_url)
        self.assertIsNone(self.org.subscriptions_url)
        self.assertEqual(self.org.total_private_repos, 176)
        self.assertIsNone(self.org.twitter_username)
        self.assertEqual(self.org.two_factor_requirement_enabled, True)
        self.assertEqual(self.org.type, "Organization")
        self.assertEqual(self.org.updated_at, datetime(2024, 8, 20, 8, 44, 26, tzinfo=timezone.utc))
        self.assertEqual(self.org.url, "https://api.github.com/orgs/BeaverSoftware")
        self.assertEqual(repr(self.org), 'Organization(login="BeaverSoftware")')
        self.assertIsNone(self.org.user_view_type)
        self.assertEqual(self.org.web_commit_signoff_required, False)

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
        hook = self.org.create_hook("web", {"url": "http://foobar.com"}, ["fork"], False)
        hook = self.org.edit_hook(hook.id, "mobile", {"url": "http://barfoo.com"}, ["spoon"], True)
        self.assertEqual(hook.name, "mobile")
        self.assertEqual(hook.events, ["spoon"])
        self.assertEqual(hook.active, True)

    def testCreateTeam(self):
        team = self.org.create_team("Team created by PyGithub")
        self.assertEqual(team.id, 189850)

    def testCreateTeamWithAllArguments(self):
        repo = self.org.get_repo("FatherBeaver")
        parent_team = self.org.get_team(141496)
        maintainer = self.g.get_user("jacquev6")
        team = self.org.create_team(
            "Team also created by PyGithub",
            [repo],
            "push",
            "secret",
            "Description also created by PyGithub",
            parent_team.id,
            [maintainer.login],
            "notifications_disabled",
        )
        self.assertEqual(team.id, 189852)
        self.assertEqual(team.description, "Description also created by PyGithub")
        self.assertEqual(team.parent, parent_team)
        self.assertEqual(team.notification_setting, "notifications_disabled")
        self.assertEqual(maintainer.login, team.get_members(role="maintainer")[0].name)

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
        self.assertListKeyEqual(self.org.get_public_members(), lambda u: u.login, ["jacquev6"])

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
        self.assertIsNone(delivery.throttled_at)
        self.assertEqual(delivery.event, "issues")
        self.assertEqual(delivery.action, "opened")
        self.assertEqual(delivery.installation_id, 123)
        self.assertEqual(delivery.repository_id, 456)
        self.assertEqual(delivery.url, "https://www.example-webhook.com")
        self.assertIsInstance(delivery.request, github.HookDelivery.HookDeliveryRequest)
        self.assertEqual(delivery.request.headers, {"content-type": "application/json"})
        self.assertEqual(delivery.request.payload, {"action": "opened"})
        self.assertIsInstance(delivery.response, github.HookDelivery.HookDeliveryResponse)
        self.assertEqual(delivery.response.headers, {"content-type": "text/html;charset=utf-8"})
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
        requestedByUser = self.g.get_user().get_repo("PyGithub").get_label("Requested by user")
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
        self.assertListKeyEqual(self.org.get_members(), lambda u: u.login, ["cjuniet", "jacquev6", "Lyloa"])

    def testGetOutsideCollaborators(self):
        self.assertListKeyEqual(self.org.get_outside_collaborators(), lambda u: u.login, ["octocat"])

    def testOutsideCollaborators(self):
        octocat = self.g.get_user("octocat")
        self.org.convert_to_outside_collaborator(octocat)
        self.assertListKeyEqual(self.org.get_outside_collaborators(), lambda u: u.login, ["octocat"])
        self.org.remove_outside_collaborator(octocat)
        self.assertEqual(list(self.org.get_outside_collaborators()), [])

    def testMembers(self):
        lyloa = self.g.get_user("Lyloa")
        self.assertTrue(self.org.has_in_members(lyloa))
        self.org.remove_from_members(lyloa)
        self.assertFalse(self.org.has_in_members(lyloa))

    def testGetRepos(self):
        repos = self.org.get_repos()
        self.assertListKeyEqual(repos, lambda r: r.name, ["FatherBeaver", "TestPyGithub"])
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
        self.assertListKeyEqual(self.org.get_teams(), lambda t: t.name, ["Members", "Owners"])

    def testGetTeamBySlug(self):
        team = self.org.get_team_by_slug("Members")
        self.assertEqual(team.id, 141496)

    def testCreateHookWithMinimalParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"})
        self.assertEqual(hook.id, 257967)

    def testCreateHookWithAllParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"}, ["fork"], False)
        self.assertTrue(hook.active)
        self.assertEqual(hook.id, 257993)

    def testCreateRepoWithMinimalArguments(self):
        repo = self.org.create_repo(name="TestPyGithub")
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub")
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
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub2")
        self.assertTrue(repo.allow_update_branch)
        self.assertFalse(repo.has_wiki)
        self.assertFalse(repo.has_pages)

    def testCreateRepositoryWithAutoInit(self):
        repo = self.org.create_repo(name="TestPyGithub", auto_init=True, gitignore_template="Python")
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub")
        self.assertTrue(repo.has_pages)
        self.assertTrue(repo.has_wiki)

    def testCreateFork(self):
        pygithub = self.g.get_user("jacquev6").get_repo("PyGithub")
        repo = self.org.create_fork(pygithub)
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/PyGithub")
        self.assertFalse(repo.has_wiki)
        self.assertFalse(repo.has_pages)

    def testCreateRepoFromTemplate(self):
        template_repo = self.g.get_repo("actions/hello-world-docker-action")

        repo = self.org.create_repo_from_template("hello-world-docker-action-new", template_repo)
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
            include_all_branches=True,
            private=private,
        )
        self.assertEqual(repo.description, description)
        self.assertTrue(repo.private)

    @mock.patch("github.PublicKey.encrypt")
    def testCreateSecretSelected(self, encrypt):
        repos = [self.org.get_repo("TestPyGithub"), self.org.get_repo("FatherBeaver")]
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = self.org.create_secret(
            secret_name="secret-name",
            unencrypted_value="secret-value",
            visibility="selected",
            secret_type="actions",
            selected_repositories=repos,
        )

        self.assertIsNotNone(secret)
        self.assertEqual(secret.visibility, "selected")
        self.assertEqual(list(secret.selected_repositories), repos)

    def testGetSecret(self):
        repos = [self.org.get_repo("TestPyGithub"), self.org.get_repo("FatherBeaver")]
        secret = self.org.get_secret("secret-name")
        self.assertEqual(secret.name, "secret-name")
        self.assertEqual(secret.created_at, datetime(2019, 8, 10, 14, 59, 22, tzinfo=timezone.utc))
        self.assertEqual(secret.updated_at, datetime(2020, 1, 10, 14, 59, 22, tzinfo=timezone.utc))
        self.assertEqual(secret.visibility, "selected")
        self.assertEqual(list(secret.selected_repositories), repos)
        self.assertEqual(secret.url, "https://api.github.com/orgs/BeaverSoftware/actions/secrets/secret-name")

    def testGetSecrets(self):
        secrets = self.org.get_secrets()
        self.assertEqual(len(list(secrets)), 1)

    def testGetDependabotSecrets(self):
        secrets = self.org.get_secrets(secret_type="dependabot")
        self.assertEqual(len(list(secrets)), 1)

    def testGetDependabotAlerts(self):
        alerts = self.org.get_dependabot_alerts()
        alert_list = list(alerts)
        self.assertEqual(len(list(alerts)), 8)
        self.assertEqual(alert_list[0].number, 1)
        self.assertEqual(alert_list[0].repository.full_name, "BeaverSoftware/PyGithub")

    def testGetDependabotAlertsWithAllArguments(self):
        alerts = self.org.get_dependabot_alerts(
            "open",
            "medium",
            "pip",
            "jinja2",
            "runtime",
            "updated",
            "asc",
        )
        alert_list = list(alerts)
        self.assertEqual(len(list(alerts)), 1)
        self.assertEqual(alert_list[0].number, 1)
        self.assertEqual(alert_list[0].state, "open")
        self.assertEqual(alert_list[0].security_advisory.severity, "medium")
        self.assertEqual(alert_list[0].dependency.package.ecosystem, "pip")
        self.assertEqual(alert_list[0].dependency.package.name, "jinja2")
        self.assertEqual(alert_list[0].dependency.scope, "runtime")
        self.assertEqual(alert_list[0].repository.full_name, "BeaverSoftware/PyGithub")

    def testGetSecretsFail(self):
        with self.assertRaises(AssertionError) as raisedexp:
            self.org.get_secrets(secret_type="secret")
        self.assertEqual("secret_type should be actions or dependabot", str(raisedexp.exception))

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
        self.org.invite_user(email="foo@example.com", role="billing_manager", teams=[team])

    def testInviteUserAsNonOwner(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.org.invite_user(email="bar@example.com")
        self.assertEqual(
            raisedexp.exception.message, "You must be an admin to create an invitation to an organization."
        )
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
        self.assertTrue(isinstance(self.org.create_migration(["sample-repo"]), github.Migration.Migration))

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

    def testCreateVariable(self):
        variable = self.org.create_variable("variable-name", "variable-value", "all")
        self.assertIsNotNone(variable)

    def testCreateVariableSelected(self):
        repos = [self.org.get_repo("TestPyGithub"), self.org.get_repo("FatherBeaver")]
        variable = self.org.create_variable("variable-name", "variable-value", "selected", repos)
        self.assertIsNotNone(variable)
        self.assertEqual(list(variable.selected_repositories), repos)

    def testGetVariable(self):
        repos = [self.org.get_repo("TestPyGithub"), self.org.get_repo("FatherBeaver")]
        variable = self.org.get_variable("variable-name")
        self.assertEqual(variable.name, "variable-name")
        self.assertEqual(variable.created_at, datetime(2019, 8, 10, 14, 59, 22, tzinfo=timezone.utc))
        self.assertEqual(variable.updated_at, datetime(2020, 1, 10, 14, 59, 22, tzinfo=timezone.utc))
        self.assertEqual(variable.visibility, "selected")
        self.assertEqual(list(variable.selected_repositories), repos)
        self.assertEqual(variable.url, "https://api.github.com/orgs/BeaverSoftware/actions/variables/variable-name")

    def testGetVariables(self):
        variables = self.org.get_variables()
        self.assertEqual(len(list(variables)), 1)

    @mock.patch("github.PublicKey.encrypt")
    def testCreateActionsSecret(self, encrypt):
        org = self.g.get_organization("demoorg")
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = org.create_secret("secret_name", "secret-value", visibility="all")
        self.assertIsNotNone(secret)

    @mock.patch("github.PublicKey.encrypt")
    def testCreateDependabotSecret(self, encrypt):
        org = self.g.get_organization("demoorg")
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = org.create_secret("secret_name", "secret-value", secret_type="dependabot", visibility="all")
        self.assertIsNotNone(secret)

    def testOrgGetSecretAssertion(self):
        org = self.g.get_organization("demoorg")
        with self.assertRaises(AssertionError) as exc:
            org.get_secret(secret_name="splat", secret_type="supersecret")
        self.assertEqual(str(exc.exception), "secret_type should be actions or dependabot")

    @mock.patch("github.PublicKey.encrypt")
    def testCreateDependabotSecretSelected(self, encrypt):
        org = self.g.get_organization("demoorg")
        repos = [org.get_repo("demo-repo-1"), org.get_repo("demo-repo-2")]
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = org.create_secret(
            secret_name="SECRET_DEP_NAME",
            unencrypted_value="secret-value",
            visibility="selected",
            secret_type="dependabot",
            selected_repositories=repos,
        )

        self.assertIsNotNone(secret)
        self.assertEqual(secret.visibility, "selected")
        self.assertEqual(list(secret.selected_repositories), repos)

    @mock.patch("github.PublicKey.encrypt")
    def testOrgSecretEdit(self, encrypt):
        org = self.g.get_organization("demoorg")
        repos = [org.get_repo("demo-repo-1"), org.get_repo("demo-repo-2")]
        # encrypt returns a non-deterministic value, we need to mock it so the replay data matches
        encrypt.return_value = "M+5Fm/BqTfB90h3nC7F3BoZuu3nXs+/KtpXwxm9gG211tbRo0F5UiN0OIfYT83CKcx9oKES9Va4E96/b"
        secret = org.create_secret(
            secret_name="secret_act_name",
            unencrypted_value="secret-value",
            visibility="selected",
            secret_type="actions",
            selected_repositories=repos,
        )

        with self.assertRaises(AssertionError) as exc:
            secret.edit(value="newvalue", secret_type="supersecret")
        self.assertEqual(str(exc.exception), "secret_type should be actions or dependabot")

    def testCreateCustomProperties(self):
        properties = [
            CustomProperty(
                property_name="property_1",
                value_type="string",
                required=False,
                description="description",
                values_editable_by="org_actors",
            ),
            CustomProperty(
                property_name="property_2",
                value_type="single_select",
                required=True,
                default_value="bar",
                description="Lorem ipsum",
                allowed_values=["foo", "bar"],
                values_editable_by="org_and_repo_actors",
            ),
            CustomProperty(
                property_name="property_3",
                value_type="multi_select",
                required=True,
                default_value="bar",
                description="Lorem ipsum",
                allowed_values=["foo", "bar"],
                values_editable_by="org_and_repo_actors",
            ),
            CustomProperty(
                property_name="property_4",
                value_type="true_false",
                required=False,
                description="description",
                values_editable_by="org_actors",
            ),
        ]
        properties = self.org.create_custom_properties(properties)
        properties_map = {p.property_name: p for p in properties}
        property_1 = properties_map["property_1"]
        self.assertEqual(property_1.value_type, "string")
        property_2 = properties_map["property_2"]
        self.assertEqual(property_2.description, "Lorem ipsum")
        property_3 = properties_map["property_3"]
        self.assertEqual(property_3.value_type, "multi_select")
        property_4 = properties_map["property_4"]
        self.assertEqual(property_4.value_type, "true_false")

    def testCreateCustomProperty(self):
        custom_property = CustomProperty(
            property_name="property_1",
            value_type="string",
            required=True,
            default_value="foo",
            description="description",
        )
        created_property = self.org.create_custom_property(custom_property)
        self.assertEqual(created_property.property_name, "property_1")
        self.assertEqual(created_property.value_type, "string")
        self.assertEqual(created_property.required, True)
        self.assertEqual(created_property.default_value, "foo")
        self.assertEqual(created_property.description, "description")
        self.assertIsNone(created_property.url)
        self.assertEqual(created_property.values_editable_by, "org_actors")

    def testGetCustomProperties(self):
        properties = self.org.get_custom_properties()
        properties_map = {p.property_name: p for p in properties}
        self.assertIn("property_1", properties_map)
        self.assertIn("property_2", properties_map)

    def testGetCustomProperty(self):
        custom_property = self.org.get_custom_property("property_1")
        self.assertEqual(custom_property.property_name, "property_1")
        self.assertEqual(custom_property.value_type, "string")
        self.assertEqual(custom_property.required, True)
        self.assertEqual(custom_property.default_value, "foo")
        self.assertEqual(custom_property.description, "description")
        self.assertIsNone(custom_property.url)
        self.assertEqual(custom_property.values_editable_by, "org_actors")

    def testCreateCustomPropertyValues(self):
        self.org.create_custom_property_values(["TestPyGithub"], {"property_1": "bar"})
        self.testListCustomPropertyValues()

    def testListCustomPropertyValues(self):
        repos = list(self.org.list_custom_property_values("repo:BeaverSoftware/TestPyGithub"))
        repos_map = {r.repository_name: r for r in repos}
        self.assertIn("TestPyGithub", repos_map)
        self.assertIn("property_1", repos_map["TestPyGithub"].properties)
        self.assertEqual(repos_map["TestPyGithub"].properties["property_1"], "bar")

    def testRemoveCustomProperty(self):
        self.org.remove_custom_property("property_1")
        with self.assertRaises(github.UnknownObjectException):
            self.org.get_custom_property("property_1")

    def testGetSelfHostedRunners(self):
        runners = self.org.get_self_hosted_runners()
        self.assertEqual(runners.totalCount, 602)

    def testDeleteSelfHostedRunner(self):
        self.org.delete_self_hosted_runner("42")

    def testGetSelfHostedRunnerApplications(self):
        self.assertListKeyEqual(
            self.org.get_self_hosted_runner_applications(),
            lambda h: h.os,
            ["osx", "linux", "linux", "win", "linux", "osx", "win"],
        )

    def testSelfHostedRunnerJitConfig(self):
        runner = self.org.create_self_hosted_runner_jitconfig(name="self_hosted", runner_group_id=1, labels=["default"])
        # Now remove the runner
        for runner in self.org.get_self_hosted_runners():
            if runner.name == "self_hosted":
                runner = self.org.get_self_hosted_runner(runner_id=runner.id)
                self.org.delete_self_hosted_runner(runner_id=runner.id)

    def testSelfHostedRunnerGetRegistrationToken(self):
        token = self.org.create_self_hosted_runner_registration_token()
        self.assertEqual(token.token, "XXXXXX")
        self.assertEqual(
            token.expires_at, datetime(2025, 2, 17, 21, 11, 49, 260000, tzinfo=timezone(timedelta(hours=-8)))
        )

    def testSelfHostedRunnerGetRemoveToken(self):
        token = self.org.create_self_hosted_runner_remove_token()
        self.assertEqual(token.token, "XXXXXX")
        self.assertEqual(
            token.expires_at, datetime(2025, 2, 17, 21, 12, 28, 308000, tzinfo=timezone(timedelta(hours=-8)))
        )

    def testGetCodeSecurityConfigs(self):
        configs = list(self.org.get_code_security_configs())
        self.assertEqual(configs.pop().id, 17)

    def testCreateCodeSecurityConfigs(self):
        config = self.org.create_code_security_config(name="test1", description="This is a description")
        self.assertEqual(config.name, "test1")

        self.org.delete_code_security_config(id=config.id)

    def testGetCodeSecurityConfig(self):
        config = self.org.get_code_security_config(id=17)
        self.assertEqual(config.id, 17)

    def testSetDefaultCodeSecurityConfig(self):
        self.org.set_default_code_security_config(id=17, default_for_new_repos="all")
        configs = self.org.get_default_code_security_configs()
        for config in configs:
            if config.default_for_new_repos == "all":
                self.assertEqual(config.configuration.id, 17)

    def testAttachDetachSecurityConfig(self):
        config = self.org.create_code_security_config(name="test1", description="This is a description")
        repo = self.org.get_repo("test1")
        repo.attach_security_config(id=config.id)
        status = "unknown"
        while status != "enforced":
            repo_config = repo.get_security_config()
            if repo_config:
                status = repo_config.status
            else:
                status = "unknown"

        self.assertEqual(config.id, repo_config.configuration.id)
        repo.detach_security_config()

    def testGetReposForCodeSecurityConfig(self):
        repo_statuses = self.org.get_repos_for_code_security_config(id=182032)
        status = repo_statuses[0]
        self.assertEqual(status.status, "enforced")
        self.assertIsNotNone(status.repository)
        self.assertEqual(status.repository.full_name, "BeaverSoftware/truth")
