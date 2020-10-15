# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Uriel Corfa <uriel@corfa.fr>                                  #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Laurent Mazuel <lmazuel@microsoft.com>                        #
# Copyright 2018 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
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


import github

from . import Framework


class TestCase(Framework.BasicTestCase):
    def doCheckFrame(self, obj, frame):
        if obj._headers == {} and frame is None:
            return
        if obj._headers is None and frame == {}:
            return
        self.assertEqual(obj._headers, frame[2])

    def getFrameChecker(self):
        return lambda requester, obj, frame: self.doCheckFrame(obj, frame)

    def setUp(self):
        super().setUp()

        # Set up frame debugging
        github.GithubObject.GithubObject.setCheckAfterInitFlag(False)
        # github.Requester.Requester.setDebugFlag(True)
        # github.Requester.Requester.setOnCheckMe(self.getFrameChecker())
        self.user_dict = {
            "login": "octocat",
            "id": 1,
            "node_id": "MDQ6VXNlcjE=",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/octocat",
            "html_url": "https://github.com/octocat",
            "followers_url": "https://api.github.com/users/octocat/followers",
            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "organizations_url": "https://api.github.com/users/octocat/orgs",
            "repos_url": "https://api.github.com/users/octocat/repos",
            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
            "received_events_url": "https://api.github.com/users/octocat/received_events",
            "type": "User",
            "site_admin": False,
            "name": "monalisa octocat",
            "company": "GitHub",
            "blog": "https://github.com/blog",
            "location": "San Francisco",
            "email": "octocat@github.com",
            "hireable": False,
            "bio": "There once was...",
            "twitter_username": "monatheoctocat",
            "public_repos": 2,
            "public_gists": 1,
            "followers": 20,
            "following": 0,
            "created_at": "2008-01-14T04:33:35Z",
            "updated_at": "2008-01-14T04:33:35Z",
        }
        self.repo_dict = {
            "id": 1296269,
            "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
            "name": "Hello-World",
            "full_name": "octocat/Hello-World",
            "owner": {
                "login": "octocat",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "html_url": "https://github.com/octocat",
                "followers_url": "https://api.github.com/users/octocat/followers",
                "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                "organizations_url": "https://api.github.com/users/octocat/orgs",
                "repos_url": "https://api.github.com/users/octocat/repos",
                "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                "received_events_url": "https://api.github.com/users/octocat/received_events",
                "type": "User",
                "site_admin": False,
            },
            "private": False,
            "html_url": "https://github.com/octocat/Hello-World",
            "description": "This your first repo!",
            "fork": False,
            "url": "https://api.github.com/repos/octocat/Hello-World",
            "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
            "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
            "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
            "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
            "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
            "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
            "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
            "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
            "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
            "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
            "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
            "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
            "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
            "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
            "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
            "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
            "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
            "git_url": "git:github.com/octocat/Hello-World.git",
            "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
            "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
            "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
            "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
            "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
            "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
            "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
            "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
            "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
            "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
            "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
            "ssh_url": "git@github.com:octocat/Hello-World.git",
            "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
            "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
            "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
            "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
            "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
            "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
            "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
            "clone_url": "https://github.com/octocat/Hello-World.git",
            "mirror_url": "git:git.example.com/octocat/Hello-World",
            "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
            "svn_url": "https://svn.github.com/octocat/Hello-World",
            "homepage": "https://github.com",
            "language": None,
            "forks_count": 9,
            "stargazers_count": 80,
            "watchers_count": 80,
            "size": 108,
            "default_branch": "master",
            "open_issues_count": 0,
            "is_template": True,
            "topics": ["octocat", "atom", "electron", "api"],
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True,
            "has_pages": False,
            "has_downloads": True,
            "archived": False,
            "disabled": False,
            "visibility": "public",
            "pushed_at": "2011-01-26T19:06:43Z",
            "created_at": "2011-01-26T19:01:12Z",
            "updated_at": "2011-01-26T19:14:43Z",
            "permissions": {
                "pull": True,
                "triage": True,
                "push": False,
                "maintain": False,
                "admin": False,
            },
            "allow_rebase_merge": True,
            "template_repository": None,
            "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
            "allow_squash_merge": True,
            "delete_branch_on_merge": True,
            "allow_merge_commit": True,
            "subscribers_count": 42,
            "network_count": 0,
            "license": {
                "key": "mit",
                "name": "MIT License",
                "spdx_id": "MIT",
                "url": "https://api.github.com/licenses/mit",
                "node_id": "MDc6TGljZW5zZW1pdA==",
            },
            "organization": {
                "login": "octocat",
                "id": 1,
                "node_id": "MDQ6VXNlcjE=",
                "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                "gravatar_id": "",
                "url": "https://api.github.com/users/octocat",
                "html_url": "https://github.com/octocat",
                "followers_url": "https://api.github.com/users/octocat/followers",
                "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                "organizations_url": "https://api.github.com/users/octocat/orgs",
                "repos_url": "https://api.github.com/users/octocat/repos",
                "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                "received_events_url": "https://api.github.com/users/octocat/received_events",
                "type": "Organization",
                "site_admin": False,
            },
            "parent": {
                "id": 1296269,
                "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
                "name": "Hello-World",
                "full_name": "octocat/Hello-World",
                "owner": {
                    "login": "octocat",
                    "id": 1,
                    "node_id": "MDQ6VXNlcjE=",
                    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/octocat",
                    "html_url": "https://github.com/octocat",
                    "followers_url": "https://api.github.com/users/octocat/followers",
                    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                    "organizations_url": "https://api.github.com/users/octocat/orgs",
                    "repos_url": "https://api.github.com/users/octocat/repos",
                    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/octocat/received_events",
                    "type": "User",
                    "site_admin": False,
                },
                "private": False,
                "html_url": "https://github.com/octocat/Hello-World",
                "description": "This your first repo!",
                "fork": False,
                "url": "https://api.github.com/repos/octocat/Hello-World",
                "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
                "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
                "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
                "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
                "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
                "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
                "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
                "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
                "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
                "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
                "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
                "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
                "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
                "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
                "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
                "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
                "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
                "git_url": "git:github.com/octocat/Hello-World.git",
                "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
                "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
                "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
                "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
                "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
                "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
                "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
                "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
                "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
                "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
                "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
                "ssh_url": "git@github.com:octocat/Hello-World.git",
                "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
                "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
                "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
                "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
                "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
                "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
                "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
                "clone_url": "https://github.com/octocat/Hello-World.git",
                "mirror_url": "git:git.example.com/octocat/Hello-World",
                "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
                "svn_url": "https://svn.github.com/octocat/Hello-World",
                "homepage": "https://github.com",
                "language": False,
                "forks_count": 9,
                "stargazers_count": 80,
                "watchers_count": 80,
                "size": 108,
                "default_branch": "master",
                "open_issues_count": 0,
                "is_template": True,
                "topics": ["octocat", "atom", "electron", "api"],
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True,
                "has_pages": False,
                "has_downloads": True,
                "archived": False,
                "disabled": False,
                "visibility": "public",
                "pushed_at": "2011-01-26T19:06:43Z",
                "created_at": "2011-01-26T19:01:12Z",
                "updated_at": "2011-01-26T19:14:43Z",
                "permissions": {"admin": False, "push": False, "pull": True},
                "allow_rebase_merge": True,
                "template_repository": None,
                "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
                "allow_squash_merge": True,
                "delete_branch_on_merge": True,
                "allow_merge_commit": True,
                "subscribers_count": 42,
                "network_count": 0,
            },
            "source": {
                "id": 1296269,
                "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
                "name": "Hello-World",
                "full_name": "octocat/Hello-World",
                "owner": {
                    "login": "octocat",
                    "id": 1,
                    "node_id": "MDQ6VXNlcjE=",
                    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/octocat",
                    "html_url": "https://github.com/octocat",
                    "followers_url": "https://api.github.com/users/octocat/followers",
                    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                    "organizations_url": "https://api.github.com/users/octocat/orgs",
                    "repos_url": "https://api.github.com/users/octocat/repos",
                    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/octocat/received_events",
                    "type": "User",
                    "site_admin": False,
                },
                "private": False,
                "html_url": "https://github.com/octocat/Hello-World",
                "description": "This your first repo!",
                "fork": False,
                "url": "https://api.github.com/repos/octocat/Hello-World",
                "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
                "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
                "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
                "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
                "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
                "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
                "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
                "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
                "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
                "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
                "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
                "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
                "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
                "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
                "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
                "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
                "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
                "git_url": "git:github.com/octocat/Hello-World.git",
                "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
                "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
                "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
                "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
                "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
                "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
                "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
                "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
                "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
                "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
                "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
                "ssh_url": "git@github.com:octocat/Hello-World.git",
                "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
                "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
                "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
                "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
                "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
                "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
                "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
                "clone_url": "https://github.com/octocat/Hello-World.git",
                "mirror_url": "git:git.example.com/octocat/Hello-World",
                "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
                "svn_url": "https://svn.github.com/octocat/Hello-World",
                "homepage": "https://github.com",
                "language": None,
                "forks_count": 9,
                "stargazers_count": 80,
                "watchers_count": 80,
                "size": 108,
                "default_branch": "master",
                "open_issues_count": 0,
                "is_template": True,
                "topics": ["octocat", "atom", "electron", "api"],
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True,
                "has_pages": False,
                "has_downloads": True,
                "archived": False,
                "disabled": False,
                "visibility": "public",
                "pushed_at": "2011-01-26T19:06:43Z",
                "created_at": "2011-01-26T19:01:12Z",
                "updated_at": "2011-01-26T19:14:43Z",
                "permissions": {"admin": False, "push": False, "pull": True},
                "allow_rebase_merge": True,
                "template_repository": None,
                "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
                "allow_squash_merge": True,
                "delete_branch_on_merge": True,
                "allow_merge_commit": True,
                "subscribers_count": 42,
                "network_count": 0,
            },
        }
        # self.repo_dict["repository"] = "https://github.com/octocat/PyGithub.git"
        # self.repo_dict["clone_url"] = "https://github.com/octocat/PyGithub.git"

        mock_dict = {
            "/repos/octocat/Hello-World": {
                "GET": {"status": 200, "body": self.repo_dict}
            },
            "/user": {
                "GET": {
                    "status": 200,
                    "body": self.user_dict,
                }
            },
        }

        if self.tokenAuthMode:
            self.g = github.Github(self.oauth_token, retry=self.retry, mock=mock_dict)
        elif self.jwtAuthMode:
            self.g = github.Github(jwt=self.jwt, retry=self.retry, mock=mock_dict)
        else:
            self.g = github.Github(
                self.login, self.password, retry=self.retry, mock=mock_dict
            )
