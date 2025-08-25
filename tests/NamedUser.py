############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Bruce Richardson <itsbruce@workshy.org>                       #
# Copyright 2018 Riccardo Pittau <elfosardo@users.noreply.github.com>          #
# Copyright 2018 namc <namratachaudhary@users.noreply.github.com>              #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Surya Teja <94suryateja@gmail.com>                            #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Daniel Haas <thisisdhaas@gmail.com>                           #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from datetime import datetime, timezone

from . import Framework


class NamedUser(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user("jacquev6")

    def testAttributes(self):
        self.assertEqual(self.user.avatar_url, "https://avatars.githubusercontent.com/u/327146?v=4")
        self.assertIsNone(self.user.bio)
        self.assertEqual(self.user.blog, "http://vincent-jacques.net")
        self.assertIsNone(self.user.collaborators)
        self.assertIsNone(self.user.company)
        self.assertIsNone(self.user.contributions)
        self.assertEqual(self.user.created_at, datetime(2010, 7, 9, 6, 10, 6, tzinfo=timezone.utc))
        self.assertIsNone(self.user.disk_usage)
        self.assertIsNone(self.user.display_login)
        self.assertEqual(self.user.email, "vincent@vincent-jacques.net")
        self.assertEqual(self.user.events_url, "https://api.github.com/users/jacquev6/events{/privacy}")
        self.assertEqual(self.user.followers, 98)
        self.assertEqual(self.user.followers_url, "https://api.github.com/users/jacquev6/followers")
        self.assertEqual(self.user.following, 62)
        self.assertEqual(self.user.following_url, "https://api.github.com/users/jacquev6/following{/other_user}")
        self.assertEqual(self.user.gists_url, "https://api.github.com/users/jacquev6/gists{/gist_id}")
        self.assertEqual(self.user.gravatar_id, "")
        self.assertTrue(self.user.hireable)
        self.assertEqual(self.user.html_url, "https://github.com/jacquev6")
        self.assertEqual(self.user.id, 327146)
        self.assertEqual(self.user.location, "France")
        self.assertEqual(self.user.login, "jacquev6")
        self.assertEqual(self.user.name, "Vincent Jacques")
        self.assertEqual(self.user.node_id, "MDQ6VXNlcjMyNzE0Ng==")
        self.assertIsNone(self.user.notification_email)
        self.assertEqual(self.user.organizations_url, "https://api.github.com/users/jacquev6/orgs")
        self.assertIsNone(self.user.owned_private_repos)
        self.assertIsNone(self.user.permissions)
        self.assertIsNone(self.user.plan)
        self.assertIsNone(self.user.plan)
        self.assertIsNone(self.user.plan)
        self.assertIsNone(self.user.plan)
        self.assertIsNone(self.user.private_gists)
        self.assertEqual(self.user.public_gists, 18)
        self.assertEqual(self.user.public_repos, 38)
        self.assertEqual(self.user.received_events_url, "https://api.github.com/users/jacquev6/received_events")
        self.assertEqual(self.user.repos_url, "https://api.github.com/users/jacquev6/repos")
        self.assertIsNone(self.user.role_name)
        self.assertEqual(self.user.site_admin, False)
        self.assertIsNone(self.user.starred_at)
        self.assertEqual(self.user.starred_url, "https://api.github.com/users/jacquev6/starred{/owner}{/repo}")
        self.assertEqual(self.user.subscriptions_url, "https://api.github.com/users/jacquev6/subscriptions")
        self.assertIsNone(self.user.suspended_at)
        self.assertIsNone(self.user.text_matches)
        self.assertIsNone(self.user.total_private_repos)
        self.assertIsNone(self.user.twitter_username)
        self.assertEqual(self.user.type, "User")
        self.assertEqual(self.user.updated_at, datetime(2024, 10, 20, 7, 14, 52, tzinfo=timezone.utc))
        self.assertEqual(self.user.url, "https://api.github.com/users/jacquev6")
        self.assertEqual(self.user.node_id, "MDQ6VXNlcjMyNzE0Ng==")
        self.assertEqual(repr(self.user), 'NamedUser(login="jacquev6")')
        self.assertEqual(repr(self.user.plan), "None")
        self.assertEqual(self.user.user_view_type, "public")

    def testAttributesOfOtherUser(self):
        self.user = self.g.get_user("nvie")
        self.assertEqual(
            self.user.avatar_url,
            "https://secure.gravatar.com/avatar/c5a7f21b46df698f3db31c37ed0cf55a?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png",
        )
        self.assertEqual(self.user.bio, None)
        self.assertEqual(self.user.blog, "http://nvie.com")
        self.assertEqual(self.user.collaborators, None)
        self.assertEqual(self.user.company, "3rd Cloud")
        self.assertEqual(
            self.user.created_at,
            datetime(2009, 5, 12, 21, 19, 38, tzinfo=timezone.utc),
        )
        self.assertEqual(self.user.disk_usage, None)
        self.assertEqual(self.user.email, "vincent@3rdcloud.com")
        self.assertEqual(self.user.followers, 296)
        self.assertEqual(self.user.following, 41)
        self.assertEqual(self.user.gravatar_id, "c5a7f21b46df698f3db31c37ed0cf55a")
        self.assertFalse(self.user.hireable)
        self.assertEqual(self.user.html_url, "https://github.com/nvie")
        self.assertEqual(self.user.id, 83844)
        self.assertEqual(self.user.location, "Netherlands")
        self.assertEqual(self.user.login, "nvie")
        self.assertEqual(self.user.name, "Vincent Driessen")
        self.assertEqual(self.user.owned_private_repos, None)
        self.assertEqual(self.user.plan, None)
        self.assertEqual(self.user.private_gists, None)
        self.assertEqual(self.user.public_gists, 16)
        self.assertEqual(self.user.public_repos, 61)
        self.assertEqual(self.user.suspended_at, None)
        self.assertEqual(self.user.total_private_repos, None)
        self.assertEqual(self.user.twitter_username, "nvie")
        self.assertEqual(self.user.type, "User")
        self.assertEqual(self.user.url, "https://api.github.com/users/nvie")
        self.assertEqual(self.user.node_id, "MDQ6VXNlcjgzODQ0")
        self.assertEqual(repr(self.user), 'NamedUser(login="nvie")')

    def testGetGists(self):
        self.assertListKeyEqual(
            self.user.get_gists(),
            lambda g: g.description,
            [
                "Gist created by PyGithub",
                "FairThreadPoolPool.cpp",
                "How to error 500 Github API v3, as requested by Rick (GitHub Staff)",
                "Cadfael: order of episodes in French DVD edition",
            ],
        )
        self.assertListKeyEqual(
            self.user.get_gists(since=datetime(2012, 3, 1, 17, 0, 0)),
            lambda g: g.description,
            ["Gist created by PyGithub", "FairThreadPoolPool.cpp"],
        )

    def testGetFollowers(self):
        self.assertListKeyEqual(
            self.user.get_followers(),
            lambda f: f.login,
            [
                "jnorthrup",
                "brugidou",
                "regisb",
                "walidk",
                "afzalkhan",
                "sdanzan",
                "vineus",
                "gturri",
                "fjardon",
                "cjuniet",
                "jardon-u",
                "kamaradclimber",
                "L42y",
            ],
        )

    def testGetFollowing(self):
        self.assertListKeyEqual(
            self.user.get_following(),
            lambda f: f.login,
            [
                "nvie",
                "schacon",
                "jamis",
                "chad",
                "unclebob",
                "dabrahams",
                "jnorthrup",
                "brugidou",
                "regisb",
                "walidk",
                "tanzilli",
                "fjardon",
                "r3c",
                "sdanzan",
                "vineus",
                "cjuniet",
                "gturri",
                "ant9000",
                "asquini",
                "claudyus",
                "jardon-u",
                "s-bernard",
                "kamaradclimber",
                "Lyloa",
            ],
        )

    def testHasInFollowing(self):
        nvie = self.g.get_user("nvie")
        self.assertTrue(self.user.has_in_following(nvie))

    def testGetOrgs(self):
        self.assertListKeyEqual(self.user.get_orgs(), lambda o: o.login, ["BeaverSoftware"])

    def testGetOrganizationMembership(self):
        o = self.user.get_orgs()
        membership = self.user.get_organization_membership(o[0])
        self.assertEqual(
            repr(membership),
            'Membership(url="https://api.github.com/orgs/BeaverSoftware/memberships/jacquev6")',
        )
        self.assertEqual(self.user.login, membership.user.login)
        self.assertEqual(membership.state, "active")
        self.assertEqual(membership.role, "member")
        self.assertEqual(
            membership.url,
            "https://api.github.com/orgs/BeaverSoftware/memberships/jacquev6",
        )
        self.assertEqual(membership.organization.login, "BeaverSoftware")
        self.assertEqual(membership.organization_url, "https://api.github.com/orgs/BeaverSoftware")

    def testGetOrganizationMembershipNotMember(self):
        from github import UnknownObjectException

        self.assertRaises(
            UnknownObjectException,
            self.user.get_organization_membership,
            "BeaverSoftware",
        )

    def testGetRepo(self):
        self.assertEqual(
            self.user.get_repo("PyGithub").description,
            "Python library implementing the full Github API v3",
        )

    def testGetRepos(self):
        self.assertListKeyEqual(
            self.user.get_repos(),
            lambda r: r.name,
            [
                "TestPyGithub",
                "django",
                "PyGithub",
                "developer.github.com",
                "acme-public-website",
                "C4Planner",
                "DrawTurksHead",
                "DrawSyntax",
                "QuadProgMm",
                "Boost.HierarchicalEnum",
                "ViDE",
            ],
        )

    def testGetReposWithAllArgs(self):
        self.assertListKeyEqual(
            self.user.get_repos(type="owner", sort="created", direction="asc"),
            lambda r: r.name,
            [
                "DrawTurksHead",
                "vincent-jacques.net",
                "IpMap",
                "MockMockMock",
                "ActionTree",
                "InteractiveCommandLine",
                "RecursiveDocument",
                "MarblesCollide",
                "jacquev6.github.io",
                "LowVoltage",
            ],
        )

    def testGetWatched(self):
        self.assertListKeyEqual(
            self.user.get_watched(),
            lambda r: r.name,
            [
                "git",
                "boost.php",
                "capistrano",
                "boost.perl",
                "git-subtree",
                "git-hg",
                "homebrew",
                "celtic_knot",
                "twisted-intro",
                "markup",
                "hub",
                "gitflow",
                "murder",
                "boto",
                "agit",
                "d3",
                "pygit2",
                "git-pulls",
                "django_mathlatex",
                "scrumblr",
                "developer.github.com",
                "python-github3",
                "PlantUML",
                "bootstrap",
                "drawnby",
                "django-socketio",
                "django-realtime",
                "playground",
                "BozoCrack",
                "FatherBeaver",
                "PyGithub",
                "django",
                "django",
                "TestPyGithub",
            ],
        )

    def testGetStarred(self):
        self.assertListKeyEqual(
            self.user.get_starred(),
            lambda r: r.name,
            [
                "git",
                "boost.php",
                "capistrano",
                "boost.perl",
                "git-subtree",
                "git-hg",
                "homebrew",
                "celtic_knot",
                "twisted-intro",
                "markup",
                "hub",
                "gitflow",
                "murder",
                "boto",
                "agit",
                "d3",
                "pygit2",
                "git-pulls",
                "django_mathlatex",
                "scrumblr",
                "developer.github.com",
                "python-github3",
                "PlantUML",
                "bootstrap",
                "drawnby",
                "django-socketio",
                "django-realtime",
                "playground",
                "BozoCrack",
                "FatherBeaver",
                "amaunet",
                "django",
                "django",
                "moviePlanning",
                "folly",
            ],
        )

    def testGetSubscriptions(self):
        self.assertListKeyEqual(
            self.user.get_subscriptions(),
            lambda r: r.name,
            [
                "ViDE",
                "Boost.HierarchicalEnum",
                "QuadProgMm",
                "DrawSyntax",
                "DrawTurksHead",
                "PrivateStuff",
                "vincent-jacques.net",
                "Hacking",
                "C4Planner",
                "developer.github.com",
                "PyGithub",
                "PyGithub",
                "django",
                "CinePlanning",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "IpMap",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
                "PyGithub",
            ],
        )

    def testGetEvents(self):
        self.assertListKeyBegin(
            self.user.get_events(),
            lambda e: e.type,
            ["GistEvent", "IssueCommentEvent", "PushEvent", "IssuesEvent"],
        )

    def testGetPublicEvents(self):
        self.assertListKeyBegin(
            self.user.get_public_events(),
            lambda e: e.type,
            ["PushEvent", "CreateEvent", "GistEvent", "IssuesEvent"],
        )

    def testGetPublicReceivedEvents(self):
        self.assertListKeyBegin(
            self.user.get_public_received_events(),
            lambda e: e.type,
            [
                "IssueCommentEvent",
                "IssueCommentEvent",
                "IssueCommentEvent",
                "IssueCommentEvent",
            ],
        )

    def testGetReceivedEvents(self):
        self.assertListKeyBegin(
            self.user.get_received_events(),
            lambda e: e.type,
            [
                "IssueCommentEvent",
                "IssueCommentEvent",
                "IssueCommentEvent",
                "IssueCommentEvent",
            ],
        )

    def testGetKeys(self):
        self.assertListKeyEqual(
            self.user.get_keys(),
            lambda k: k.id,
            [3557894, 3791954, 3937333, 4051357, 4051492],
        )

    def testUserEquality(self):
        u1 = self.g.get_user("nvie")
        u2 = self.g.get_user("nvie")
        self.assertTrue(u1 == u2)
        self.assertEqual(u1, u2)
        self.assertEqual(u1.__hash__(), u2.__hash__())


class OrganizationInvitation(Framework.TestCase):
    def setUp(self):
        super().setUp()
        # TODO: create an instance of type OrganizationInvitation and assign to self.attr, then run:
        #   pytest tests/OrganizationInvitation.py -k testAttributes --record
        #   ./scripts/update-assertions.sh tests/OrganizationInvitation.py testAttributes
        self.org = self.g.get_organization("TestOrganization2072")
        self.invitations = list(self.org.invitations())
        self.assertGreater(len(self.invitations), 0)
        self.invitation = self.invitations[0]

    def testAttributes(self):
        self.assertIsNotNone(self.invitation)
        self.assertEqual(self.invitation.created_at, datetime(2021, 10, 12, 13, 32, 33, tzinfo=timezone.utc))
        self.assertEqual(self.invitation.email, "foo@bar.org")
        self.assertIsNone(self.invitation.failed_at)
        self.assertIsNone(self.invitation.failed_reason)
        self.assertEqual(self.invitation.id, 28984230)
        self.assertIsNone(self.invitation.invitation_source)
        self.assertEqual(
            self.invitation.invitation_teams_url,
            "https://api.github.com/organizations/92288976/invitations/28984230/teams",
        )
        self.assertEqual(self.invitation.inviter.login, "jsimpso")
        self.assertIsNone(self.invitation.login)
        self.assertEqual(self.invitation.node_id, "OI_kwDOBYA30M4BukOm")
        self.assertEqual(self.invitation.role, "direct_member")
        self.assertEqual(self.invitation.team_count, 0)

    def testCancel(self):
        self.assertFalse(any([i for i in self.org.invitations() if i.email == "foo@bar.org"]))
        self.org.invite_user(email="foo@bar.org")
        self.assertTrue(any([i for i in self.org.invitations() if i.email == "foo@bar.org"]))
        invitation = [i for i in self.org.invitations() if i.email == "foo@bar.org"][0]
        self.assertTrue(self.org.cancel_invitation(invitation))
        # copy replay data of self.org.cancel_invitation(invitation) call, fix HTTP path
        self.assertTrue(invitation.cancel())
