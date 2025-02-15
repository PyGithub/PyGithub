############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Cameron White <cawhite@pdx.edu>                               #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 poulp <mathieu.nerv@gmail.com>                                #
# Copyright 2014 Tomas Radej <tradej@redhat.com>                               #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 E. Dunham <github@edunham.net>                                #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Balázs Rostás <rostas.balazs@gmail.com>                       #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2018 Bruce Richardson <itsbruce@workshy.org>                       #
# Copyright 2018 Riccardo Pittau <elfosardo@users.noreply.github.com>          #
# Copyright 2018 Shubham Singh <41840111+singh811@users.noreply.github.com>    #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 bryanhuntesl <31992054+bryanhuntesl@users.noreply.github.com> #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Jamie van Brunschot <j.brunschot@coolblue.nl>                 #
# Copyright 2019 Jon Dufresne <jon.dufresne@gmail.com>                         #
# Copyright 2019 Pavan Kunisetty <nagapavan@users.noreply.github.com>          #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Surya Teja <94suryateja@gmail.com>                            #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
# Copyright 2020 Glenn McDonald <testworksau@users.noreply.github.com>         #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 MeggyCal <MeggyCal@users.noreply.github.com>                  #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Yuya Nakamura <yuyan7sh@gmail.com>                            #
# Copyright 2021 sshekdar-VMware <87147229+sshekdar-VMware@users.noreply.github.com>#
# Copyright 2021 秋葉 <ambiguous404@gmail.com>                                   #
# Copyright 2022 KimSia Sim <245021+simkimsia@users.noreply.github.com>        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2023 Kevin Grandjean <Muscaw@users.noreply.github.com>             #
# Copyright 2023 Mark Amery <markamery@btinternet.com>                         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 chantra <chantra@users.noreply.github.com>                    #
# Copyright 2024 Chris Wells <ping@cwlls.com>                                  #
# Copyright 2024 Eduardo Ramírez <edu.rh90@gmail.com>                          #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Oskar Jansson <56458534+janssonoskar@users.noreply.github.com>#
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

import urllib.parse
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, NamedTuple

import github.Authorization
import github.Event
import github.Gist
import github.GithubObject
import github.Invitation
import github.Issue
import github.Membership
import github.Migration
import github.NamedUser
import github.Notification
import github.Organization
import github.Plan
import github.Repository
import github.UserKey
from github import Consts
from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    is_defined,
    is_optional,
    is_optional_list,
    is_undefined,
)
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.Authorization import Authorization
    from github.Event import Event
    from github.Gist import Gist
    from github.InputFileContent import InputFileContent
    from github.Installation import Installation
    from github.Invitation import Invitation
    from github.Issue import Issue
    from github.Label import Label
    from github.Membership import Membership
    from github.Migration import Migration
    from github.NamedUser import NamedUser
    from github.Notification import Notification
    from github.Organization import Organization
    from github.Plan import Plan
    from github.Project import Project
    from github.Repository import Repository
    from github.Team import Team
    from github.UserKey import UserKey


class EmailData(NamedTuple):
    email: str
    primary: bool
    verified: bool
    visibility: str


class AuthenticatedUser(CompletableGithubObject):
    """
    This class represents AuthenticatedUsers as returned by https://docs.github.com/en/rest/reference/users#get-the-authenticated-user

    An AuthenticatedUser object can be created by calling ``get_user()`` on a Github object.
    """

    def _initAttributes(self) -> None:
        self._avatar_url: Attribute[str] = NotSet
        self._bio: Attribute[str] = NotSet
        self._blog: Attribute[str] = NotSet
        self._collaborators: Attribute[int] = NotSet
        self._company: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._disk_usage: Attribute[int] = NotSet
        self._email: Attribute[str] = NotSet
        self._events_url: Attribute[str] = NotSet
        self._followers: Attribute[int] = NotSet
        self._followers_url: Attribute[str] = NotSet
        self._following: Attribute[int] = NotSet
        self._following_url: Attribute[str] = NotSet
        self._gists_url: Attribute[str] = NotSet
        self._gravatar_id: Attribute[str] = NotSet
        self._hireable: Attribute[bool] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._location: Attribute[str] = NotSet
        self._login: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._organizations_url: Attribute[str] = NotSet
        self._owned_private_repos: Attribute[int] = NotSet
        self._plan: Attribute[github.Plan.Plan] = NotSet
        self._private_gists: Attribute[int] = NotSet
        self._public_gists: Attribute[int] = NotSet
        self._public_repos: Attribute[int] = NotSet
        self._received_events_url: Attribute[str] = NotSet
        self._repos_url: Attribute[str] = NotSet
        self._site_admin: Attribute[bool] = NotSet
        self._starred_url: Attribute[str] = NotSet
        self._subscriptions_url: Attribute[str] = NotSet
        self._total_private_repos: Attribute[int] = NotSet
        self._two_factor_authentication: Attribute[bool] = NotSet
        self._type: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"login": self._login.value})

    @property
    def avatar_url(self) -> str:
        self._completeIfNotSet(self._avatar_url)
        return self._avatar_url.value

    @property
    def bio(self) -> str:
        self._completeIfNotSet(self._bio)
        return self._bio.value

    @property
    def blog(self) -> str:
        self._completeIfNotSet(self._blog)
        return self._blog.value

    @property
    def collaborators(self) -> int:
        self._completeIfNotSet(self._collaborators)
        return self._collaborators.value

    @property
    def company(self) -> str:
        self._completeIfNotSet(self._company)
        return self._company.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def disk_usage(self) -> int:
        self._completeIfNotSet(self._disk_usage)
        return self._disk_usage.value

    @property
    def email(self) -> str:
        self._completeIfNotSet(self._email)
        return self._email.value

    @property
    def events_url(self) -> str:
        self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    def followers(self) -> int:
        self._completeIfNotSet(self._followers)
        return self._followers.value

    @property
    def followers_url(self) -> str:
        self._completeIfNotSet(self._followers_url)
        return self._followers_url.value

    @property
    def following(self) -> int:
        self._completeIfNotSet(self._following)
        return self._following.value

    @property
    def following_url(self) -> str:
        self._completeIfNotSet(self._following_url)
        return self._following_url.value

    @property
    def gists_url(self) -> str:
        self._completeIfNotSet(self._gists_url)
        return self._gists_url.value

    @property
    def gravatar_id(self) -> str:
        self._completeIfNotSet(self._gravatar_id)
        return self._gravatar_id.value

    @property
    def hireable(self) -> bool:
        self._completeIfNotSet(self._hireable)
        return self._hireable.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def location(self) -> str:
        self._completeIfNotSet(self._location)
        return self._location.value

    @property
    def login(self) -> str:
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def organizations_url(self) -> str:
        self._completeIfNotSet(self._organizations_url)
        return self._organizations_url.value

    @property
    def owned_private_repos(self) -> int:
        self._completeIfNotSet(self._owned_private_repos)
        return self._owned_private_repos.value

    @property
    def plan(self) -> Plan:
        self._completeIfNotSet(self._plan)
        return self._plan.value

    @property
    def private_gists(self) -> int:
        self._completeIfNotSet(self._private_gists)
        return self._private_gists.value

    @property
    def public_gists(self) -> int:
        self._completeIfNotSet(self._public_gists)
        return self._public_gists.value

    @property
    def public_repos(self) -> int:
        self._completeIfNotSet(self._public_repos)
        return self._public_repos.value

    @property
    def received_events_url(self) -> str:
        self._completeIfNotSet(self._received_events_url)
        return self._received_events_url.value

    @property
    def repos_url(self) -> str:
        self._completeIfNotSet(self._repos_url)
        return self._repos_url.value

    @property
    def site_admin(self) -> bool:
        self._completeIfNotSet(self._site_admin)
        return self._site_admin.value

    @property
    def starred_url(self) -> str:
        self._completeIfNotSet(self._starred_url)
        return self._starred_url.value

    @property
    def subscriptions_url(self) -> str:
        self._completeIfNotSet(self._subscriptions_url)
        return self._subscriptions_url.value

    @property
    def total_private_repos(self) -> int:
        self._completeIfNotSet(self._total_private_repos)
        return self._total_private_repos.value

    @property
    def two_factor_authentication(self) -> bool:
        self._completeIfNotSet(self._two_factor_authentication)
        return self._two_factor_authentication.value

    @property
    def type(self) -> str:
        self._completeIfNotSet(self._type)
        return self._type.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def add_to_emails(self, *emails: str) -> None:
        """
        :calls: `POST /user/emails <http://docs.github.com/en/rest/reference/users#emails>`_
        """
        assert all(isinstance(element, str) for element in emails), emails
        post_parameters = {"emails": emails}
        headers, data = self._requester.requestJsonAndCheck("POST", "/user/emails", input=post_parameters)

    def add_to_following(self, following: NamedUser) -> None:
        """
        :calls: `PUT /user/following/{user} <http://docs.github.com/en/rest/reference/users#followers>`_
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        headers, data = self._requester.requestJsonAndCheck("PUT", f"/user/following/{following._identity}")

    def add_to_starred(self, starred: Repository) -> None:
        """
        :calls: `PUT /user/starred/{owner}/{repo} <http://docs.github.com/en/rest/reference/activity#starring>`_
        """
        assert isinstance(starred, github.Repository.Repository), starred
        headers, data = self._requester.requestJsonAndCheck("PUT", f"/user/starred/{starred._identity}")

    def add_to_subscriptions(self, subscription: Repository) -> None:
        """
        :calls: `PUT /user/subscriptions/{owner}/{repo} <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        assert isinstance(subscription, github.Repository.Repository), subscription
        headers, data = self._requester.requestJsonAndCheck("PUT", f"/user/subscriptions/{subscription._identity}")

    def add_to_watched(self, watched: Repository) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/subscription <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        assert isinstance(watched, github.Repository.Repository), watched
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            f"/repos/{watched._identity}/subscription",
            input={"subscribed": True},
        )

    def create_authorization(
        self,
        scopes: Opt[list[str]] = NotSet,
        note: Opt[str] = NotSet,
        note_url: Opt[str] = NotSet,
        client_id: Opt[str] = NotSet,
        client_secret: Opt[str] = NotSet,
        onetime_password: str | None = None,
    ) -> Authorization:
        """
        :calls: `POST /authorizations <https://docs.github.com/en/developers/apps/authorizing-oauth-apps>`_
        """
        assert is_optional_list(scopes, str), scopes
        assert is_optional(note, str), note
        assert is_optional(note_url, str), note_url
        assert is_optional(client_id, str), client_id
        assert is_optional(client_secret, str), client_secret
        assert onetime_password is None or isinstance(onetime_password, str), onetime_password
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "scopes": scopes,
                "note": note,
                "note_url": note_url,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )

        if onetime_password is not None:
            request_header = {Consts.headerOTP: onetime_password}  # pragma no cover (Should be covered)
        else:
            request_header = None
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/authorizations",
            input=post_parameters,
            headers=request_header,
        )
        return github.Authorization.Authorization(self._requester, headers, data, completed=True)

    @staticmethod
    def create_fork(
        repo: Repository,
        name: Opt[str] = NotSet,
        default_branch_only: Opt[bool] = NotSet,
    ) -> Repository:
        """
        :calls: `POST /repos/{owner}/{repo}/forks <http://docs.github.com/en/rest/reference/repos#forks>`_
        """
        assert isinstance(repo, github.Repository.Repository), repo
        return repo.create_fork(
            organization=github.GithubObject.NotSet,
            name=name,
            default_branch_only=default_branch_only,
        )

    def create_repo_from_template(
        self,
        name: str,
        repo: Repository,
        description: Opt[str] = NotSet,
        include_all_branches: Opt[bool] = NotSet,
        private: Opt[bool] = NotSet,
    ) -> Repository:
        """
        :calls: `POST /repos/{template_owner}/{template_repo}/generate <https://docs.github.com/en/rest/reference/repos#create-a-repository-using-a-template>`_
        """
        assert isinstance(name, str), name
        assert isinstance(repo, github.Repository.Repository), repo
        assert is_optional(description, str), description
        assert is_optional(include_all_branches, bool), include_all_branches
        assert is_optional(private, bool), private
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "name": name,
                "owner": self.login,
                "description": description,
                "include_all_branches": include_all_branches,
                "private": private,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"/repos/{repo.owner.login}/{repo.name}/generate",
            input=post_parameters,
            headers={"Accept": "application/vnd.github.v3+json"},
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def create_gist(
        self,
        public: bool,
        files: dict[str, InputFileContent],
        description: Opt[str] = NotSet,
    ) -> Gist:
        """
        :calls: `POST /gists <http://docs.github.com/en/rest/reference/gists>`_
        """
        assert isinstance(public, bool), public
        assert all(isinstance(element, github.InputFileContent) for element in files.values()), files
        assert is_undefined(description) or isinstance(description, str), description
        post_parameters = {
            "public": public,
            "files": {key: value._identity for key, value in files.items()},
        }
        if is_defined(description):
            post_parameters["description"] = description
        headers, data = self._requester.requestJsonAndCheck("POST", "/gists", input=post_parameters)
        return github.Gist.Gist(self._requester, headers, data, completed=True)

    def create_key(self, title: str, key: str) -> UserKey:
        """
        :calls: `POST /user/keys <http://docs.github.com/en/rest/reference/users#git-ssh-keys>`_
        :param title: string
        :param key: string
        :rtype: :class:`github.UserKey.UserKey`
        """
        assert isinstance(title, str), title
        assert isinstance(key, str), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        headers, data = self._requester.requestJsonAndCheck("POST", "/user/keys", input=post_parameters)
        return github.UserKey.UserKey(self._requester, headers, data, completed=True)

    def create_project(self, name: str, body: Opt[str] = NotSet) -> Project:
        """
        :calls: `POST /user/projects <https://docs.github.com/en/rest/reference/projects#create-a-user-project>`_
        :param name: string
        :param body: string
        :rtype: :class:`github.Project.Project`
        """
        assert isinstance(name, str), name
        assert is_undefined(body) or isinstance(body, str), body
        post_parameters = {
            "name": name,
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/user/projects",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return github.Project.Project(self._requester, headers, data, completed=True)

    def create_repo(
        self,
        name: str,
        description: Opt[str] = NotSet,
        homepage: Opt[str] = NotSet,
        private: Opt[bool] = NotSet,
        has_issues: Opt[bool] = NotSet,
        has_wiki: Opt[bool] = NotSet,
        has_downloads: Opt[bool] = NotSet,
        has_projects: Opt[bool] = NotSet,
        has_discussions: Opt[bool] = NotSet,
        auto_init: Opt[bool] = NotSet,
        license_template: Opt[str] = NotSet,
        gitignore_template: Opt[str] = NotSet,
        allow_squash_merge: Opt[bool] = NotSet,
        allow_merge_commit: Opt[bool] = NotSet,
        allow_rebase_merge: Opt[bool] = NotSet,
        delete_branch_on_merge: Opt[bool] = NotSet,
    ) -> Repository:
        """
        :calls: `POST /user/repos <http://docs.github.com/en/rest/reference/repos>`_
        """
        assert isinstance(name, str), name
        assert is_optional(description, str), description
        assert is_optional(homepage, str), homepage
        assert is_optional(private, bool), private
        assert is_optional(has_issues, bool), has_issues
        assert is_optional(has_wiki, bool), has_wiki
        assert is_optional(has_downloads, bool), has_downloads
        assert is_optional(has_projects, bool), has_projects
        assert is_optional(has_discussions, bool), has_discussions
        assert is_optional(auto_init, bool), auto_init
        assert is_optional(license_template, str), license_template
        assert is_optional(gitignore_template, str), gitignore_template
        assert is_optional(allow_squash_merge, bool), allow_squash_merge
        assert is_optional(allow_merge_commit, bool), allow_merge_commit
        assert is_optional(allow_rebase_merge, bool), allow_rebase_merge
        assert is_optional(delete_branch_on_merge, bool), delete_branch_on_merge
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "name": name,
                "description": description,
                "homepage": homepage,
                "private": private,
                "has_issues": has_issues,
                "has_wiki": has_wiki,
                "has_downloads": has_downloads,
                "has_projects": has_projects,
                "has_discussions": has_discussions,
                "auto_init": auto_init,
                "license_template": license_template,
                "gitignore_template": gitignore_template,
                "allow_squash_merge": allow_squash_merge,
                "allow_merge_commit": allow_merge_commit,
                "allow_rebase_merge": allow_rebase_merge,
                "delete_branch_on_merge": delete_branch_on_merge,
            }
        )

        headers, data = self._requester.requestJsonAndCheck("POST", "/user/repos", input=post_parameters)
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def edit(
        self,
        name: Opt[str] = NotSet,
        email: Opt[str] = NotSet,
        blog: Opt[str] = NotSet,
        company: Opt[str] = NotSet,
        location: Opt[str] = NotSet,
        hireable: Opt[bool] = NotSet,
        bio: Opt[str] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /user <http://docs.github.com/en/rest/reference/users>`_
        """
        assert is_optional(name, str), name
        assert is_optional(email, str), email
        assert is_optional(blog, str), blog
        assert is_optional(company, str), company
        assert is_optional(location, str), location
        assert is_optional(hireable, bool), hireable
        assert is_optional(bio, str), bio
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "name": name,
                "email": email,
                "blog": blog,
                "company": company,
                "location": location,
                "hireable": hireable,
                "bio": bio,
            }
        )

        headers, data = self._requester.requestJsonAndCheck("PATCH", "/user", input=post_parameters)
        self._useAttributes(data)

    def get_authorization(self, id: int) -> Authorization:
        """
        :calls: `GET /authorizations/{id} <https://docs.github.com/en/developers/apps/authorizing-oauth-apps>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"/authorizations/{id}")
        return github.Authorization.Authorization(self._requester, headers, data, completed=True)

    def get_authorizations(self) -> PaginatedList[Authorization]:
        """
        :calls: `GET /authorizations <https://docs.github.com/en/developers/apps/authorizing-oauth-apps>`_
        """
        return PaginatedList(github.Authorization.Authorization, self._requester, "/authorizations", None)

    def get_emails(self) -> list[EmailData]:
        """
        :calls: `GET /user/emails <http://docs.github.com/en/rest/reference/users#emails>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", "/user/emails")
        return [EmailData(**item) for item in data]

    def get_events(self) -> PaginatedList[Event]:
        """
        :calls: `GET /events <http://docs.github.com/en/rest/reference/activity#events>`_
        """
        return PaginatedList(github.Event.Event, self._requester, "/events", None)

    def get_followers(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /user/followers <http://docs.github.com/en/rest/reference/users#followers>`_
        """
        return PaginatedList(github.NamedUser.NamedUser, self._requester, "/user/followers", None)

    def get_following(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /user/following <http://docs.github.com/en/rest/reference/users#followers>`_
        """
        return PaginatedList(github.NamedUser.NamedUser, self._requester, "/user/following", None)

    def get_gists(self, since: Opt[datetime] = NotSet) -> PaginatedList[Gist]:
        """
        :calls: `GET /gists <http://docs.github.com/en/rest/reference/gists>`_
        :param since: datetime format YYYY-MM-DDTHH:MM:SSZ
        :rtype: :class:`PaginatedList` of :class:`github.Gist.Gist`
        """
        assert is_optional(since, datetime), since
        url_parameters: dict[str, Any] = {}
        if is_defined(since):
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return PaginatedList(github.Gist.Gist, self._requester, "/gists", url_parameters)

    def get_issues(
        self,
        filter: Opt[str] = NotSet,
        state: Opt[str] = NotSet,
        labels: Opt[list[Label]] = NotSet,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
        since: Opt[datetime] = NotSet,
    ) -> PaginatedList[Issue]:
        """
        :calls: `GET /issues <http://docs.github.com/en/rest/reference/issues>`_
        """
        assert is_optional(filter, str), filter
        assert is_optional(state, str), state
        assert is_optional_list(labels, github.Label.Label), labels
        assert is_optional(sort, str), sort
        assert is_optional(direction, str), direction
        assert is_optional(since, datetime), since
        url_parameters: dict[str, Any] = {}
        if is_defined(filter):
            url_parameters["filter"] = filter
        if is_defined(state):
            url_parameters["state"] = state
        if is_defined(labels):
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if is_defined(sort):
            url_parameters["sort"] = sort
        if is_defined(direction):
            url_parameters["direction"] = direction
        if is_defined(since):
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return PaginatedList(github.Issue.Issue, self._requester, "/issues", url_parameters)

    def get_user_issues(
        self,
        filter: Opt[str] = NotSet,
        state: Opt[str] = NotSet,
        labels: Opt[list[Label]] = NotSet,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
        since: Opt[datetime] = NotSet,
    ) -> PaginatedList[Issue]:
        """
        :calls: `GET /user/issues <http://docs.github.com/en/rest/reference/issues>`_
        """
        assert is_optional(filter, str), filter
        assert is_optional(state, str), state
        assert is_optional_list(labels, github.Label.Label), labels
        assert is_optional(sort, str), sort
        assert is_optional(direction, str), direction
        assert is_optional(since, datetime), since
        url_parameters: dict[str, Any] = {}
        if is_defined(filter):
            url_parameters["filter"] = filter
        if is_defined(state):
            url_parameters["state"] = state
        if is_defined(labels):
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if is_defined(sort):
            url_parameters["sort"] = sort
        if is_defined(direction):
            url_parameters["direction"] = direction
        if is_defined(since):
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return PaginatedList(github.Issue.Issue, self._requester, "/user/issues", url_parameters)

    def get_key(self, id: int) -> UserKey:
        """
        :calls: `GET /user/keys/{id} <http://docs.github.com/en/rest/reference/users#git-ssh-keys>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"/user/keys/{id}")
        return github.UserKey.UserKey(self._requester, headers, data, completed=True)

    def get_keys(self) -> PaginatedList[UserKey]:
        """
        :calls: `GET /user/keys <http://docs.github.com/en/rest/reference/users#git-ssh-keys>`_
        """
        return PaginatedList(github.UserKey.UserKey, self._requester, "/user/keys", None)

    def get_notification(self, id: str) -> Notification:
        """
        :calls: `GET /notifications/threads/{id} <http://docs.github.com/en/rest/reference/activity#notifications>`_
        """

        assert isinstance(id, str), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"/notifications/threads/{id}")
        return github.Notification.Notification(self._requester, headers, data, completed=True)

    def get_notifications(
        self,
        all: Opt[bool] = NotSet,
        participating: Opt[bool] = NotSet,
        since: Opt[datetime] = NotSet,
        before: Opt[datetime] = NotSet,
    ) -> PaginatedList[Notification]:
        """
        :calls: `GET /notifications <http://docs.github.com/en/rest/reference/activity#notifications>`_
        """

        assert is_optional(all, bool), all
        assert is_optional(participating, bool), participating
        assert is_optional(since, datetime), since
        assert is_optional(before, datetime), before

        params: dict[str, Any] = {}
        if is_defined(all):
            # convert True, False to true, false for api parameters
            params["all"] = "true" if all else "false"
        if is_defined(participating):
            # convert True, False to true, false for api parameters
            params["participating"] = "true" if participating else "false"
        if is_defined(since):
            params["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        if is_defined(before):
            params["before"] = before.strftime("%Y-%m-%dT%H:%M:%SZ")

        return PaginatedList(github.Notification.Notification, self._requester, "/notifications", params)

    def get_organization_events(self, org: Organization) -> PaginatedList[Event]:
        """
        :calls: `GET /users/{user}/events/orgs/{org} <http://docs.github.com/en/rest/reference/activity#events>`_
        """
        assert isinstance(org, github.Organization.Organization), org
        return PaginatedList(
            github.Event.Event,
            self._requester,
            f"/users/{self.login}/events/orgs/{org.login}",
            None,
        )

    def get_orgs(self) -> PaginatedList[Organization]:
        """
        :calls: `GET /user/orgs <http://docs.github.com/en/rest/reference/orgs>`_
        """
        return PaginatedList(github.Organization.Organization, self._requester, "/user/orgs", None)

    def get_repo(self, name: str) -> Repository:
        """
        :calls: `GET /repos/{owner}/{repo} <http://docs.github.com/en/rest/reference/repos>`_
        """
        assert isinstance(name, str), name
        name = urllib.parse.quote(name)
        headers, data = self._requester.requestJsonAndCheck("GET", f"/repos/{self.login}/{name}")
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def get_repos(
        self,
        visibility: Opt[str] = NotSet,
        affiliation: Opt[str] = NotSet,
        type: Opt[str] = NotSet,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
    ) -> PaginatedList[Repository]:
        """
        :calls: `GET /user/repos <http://docs.github.com/en/rest/reference/repos>`_
        """
        assert is_optional(visibility, str), visibility
        assert is_optional(affiliation, str), affiliation
        assert is_optional(type, str), type
        assert is_optional(sort, str), sort
        assert is_optional(direction, str), direction
        url_parameters = NotSet.remove_unset_items(
            {
                "visibility": visibility,
                "affiliation": affiliation,
                "type": type,
                "sort": sort,
                "direction": direction,
            }
        )
        return PaginatedList(github.Repository.Repository, self._requester, "/user/repos", url_parameters)

    def get_starred(self) -> PaginatedList[Repository]:
        """
        :calls: `GET /user/starred <http://docs.github.com/en/rest/reference/activity#starring>`_
        """
        return PaginatedList(github.Repository.Repository, self._requester, "/user/starred", None)

    def get_starred_gists(self) -> PaginatedList[Gist]:
        """
        :calls: `GET /gists/starred <http://docs.github.com/en/rest/reference/gists>`_
        """
        return PaginatedList(github.Gist.Gist, self._requester, "/gists/starred", None)

    def get_subscriptions(self) -> PaginatedList[Repository]:
        """
        :calls: `GET /user/subscriptions <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        return PaginatedList(github.Repository.Repository, self._requester, "/user/subscriptions", None)

    def get_teams(self) -> PaginatedList[Team]:
        """
        :calls: `GET /user/teams <http://docs.github.com/en/rest/reference/teams>`_
        """
        return PaginatedList(github.Team.Team, self._requester, "/user/teams", None)

    def get_watched(self) -> PaginatedList[Repository]:
        """
        :calls: `GET /user/subscriptions <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        return PaginatedList(github.Repository.Repository, self._requester, "/user/subscriptions", None)

    def get_installations(self) -> PaginatedList[Installation]:
        """
        :calls: `GET /user/installations <http://docs.github.com/en/rest/reference/apps>`_
        """
        return PaginatedList(
            github.Installation.Installation,
            self._requester,
            "/user/installations",
            None,
            headers={"Accept": Consts.mediaTypeIntegrationPreview},
            list_item="installations",
        )

    def has_in_following(self, following: NamedUser) -> bool:
        """
        :calls: `GET /user/following/{user} <http://docs.github.com/en/rest/reference/users#followers>`_
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        status, headers, data = self._requester.requestJson("GET", f"/user/following/{following._identity}")
        return status == 204

    def has_in_starred(self, starred: Repository) -> bool:
        """
        :calls: `GET /user/starred/{owner}/{repo} <http://docs.github.com/en/rest/reference/activity#starring>`_
        """
        assert isinstance(starred, github.Repository.Repository), starred
        status, headers, data = self._requester.requestJson("GET", f"/user/starred/{starred._identity}")
        return status == 204

    def has_in_subscriptions(self, subscription: Repository) -> bool:
        """
        :calls: `GET /user/subscriptions/{owner}/{repo} <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        assert isinstance(subscription, github.Repository.Repository), subscription
        status, headers, data = self._requester.requestJson("GET", f"/user/subscriptions/{subscription._identity}")
        return status == 204

    def has_in_watched(self, watched: Repository) -> bool:
        """
        :calls: `GET /repos/{owner}/{repo}/subscription <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        assert isinstance(watched, github.Repository.Repository), watched
        status, headers, data = self._requester.requestJson("GET", f"/repos/{watched._identity}/subscription")
        return status == 200

    def mark_notifications_as_read(self, last_read_at: datetime | None = None) -> None:
        """
        :calls: `PUT /notifications <https://docs.github.com/en/rest/reference/activity#notifications>`_
        """
        if last_read_at is None:
            last_read_at = datetime.now(timezone.utc)
        assert isinstance(last_read_at, datetime)
        put_parameters = {"last_read_at": last_read_at.strftime("%Y-%m-%dT%H:%M:%SZ")}

        headers, data = self._requester.requestJsonAndCheck("PUT", "/notifications", input=put_parameters)

    def remove_from_emails(self, *emails: str) -> None:
        """
        :calls: `DELETE /user/emails <http://docs.github.com/en/rest/reference/users#emails>`_
        """
        assert all(isinstance(element, str) for element in emails), emails
        post_parameters = {"emails": emails}
        headers, data = self._requester.requestJsonAndCheck("DELETE", "/user/emails", input=post_parameters)

    def remove_from_following(self, following: NamedUser) -> None:
        """
        :calls: `DELETE /user/following/{user} <http://docs.github.com/en/rest/reference/users#followers>`_
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"/user/following/{following._identity}")

    def remove_from_starred(self, starred: Repository) -> None:
        """
        :calls: `DELETE /user/starred/{owner}/{repo} <http://docs.github.com/en/rest/reference/activity#starring>`_
        """
        assert isinstance(starred, github.Repository.Repository), starred
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"/user/starred/{starred._identity}")

    def remove_from_subscriptions(self, subscription: Repository) -> None:
        """
        :calls: `DELETE /user/subscriptions/{owner}/{repo} <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        assert isinstance(subscription, github.Repository.Repository), subscription
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"/user/subscriptions/{subscription._identity}")

    def remove_from_watched(self, watched: Repository) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/subscription <http://docs.github.com/en/rest/reference/activity#watching>`_
        """
        assert isinstance(watched, github.Repository.Repository), watched
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"/repos/{watched._identity}/subscription")

    def accept_invitation(self, invitation: Invitation | int) -> None:
        """
        :calls: `PATCH /user/repository_invitations/{invitation_id} <https://docs.github.com/en/rest/reference/repos/invitations#>`_
        """
        assert isinstance(invitation, github.Invitation.Invitation) or isinstance(invitation, int)

        if isinstance(invitation, github.Invitation.Invitation):
            invitation = invitation.id

        headers, data = self._requester.requestJsonAndCheck(
            "PATCH", f"/user/repository_invitations/{invitation}", input={}
        )

    def get_invitations(self) -> PaginatedList[Invitation]:
        """
        :calls: `GET /user/repository_invitations <https://docs.github.com/en/rest/reference/repos#invitations>`_
        """
        return PaginatedList(
            github.Invitation.Invitation,
            self._requester,
            "/user/repository_invitations",
            None,
        )

    def create_migration(
        self,
        repos: list[Repository] | tuple[Repository],
        lock_repositories: Opt[bool] = NotSet,
        exclude_attachments: Opt[bool] = NotSet,
    ) -> Migration:
        """
        :calls: `POST /user/migrations <https://docs.github.com/en/rest/reference/migrations>`_
        """
        assert isinstance(repos, (list, tuple)), repos
        assert all(isinstance(repo, str) for repo in repos), repos
        assert is_optional(lock_repositories, bool), lock_repositories
        assert is_optional(exclude_attachments, bool), exclude_attachments
        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "repositories": repos,
                "lock_repositories": lock_repositories,
                "exclude_attachments": exclude_attachments,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/user/migrations",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeMigrationPreview},
        )
        return github.Migration.Migration(self._requester, headers, data, completed=True)

    def get_migrations(self) -> PaginatedList[Migration]:
        """
        :calls: `GET /user/migrations <https://docs.github.com/en/rest/reference/migrations>`_
        """
        return PaginatedList(
            github.Migration.Migration,
            self._requester,
            "/user/migrations",
            None,
            headers={"Accept": Consts.mediaTypeMigrationPreview},
        )

    def get_organization_memberships(self) -> PaginatedList[Membership]:
        """
        :calls: `GET /user/memberships/orgs/ <https://docs.github.com/en/rest/orgs/members#list-organization-memberships-for-the-authenticated-user>`_
        """
        return PaginatedList(
            github.Membership.Membership,
            self._requester,
            "/user/memberships/orgs",
            None,
        )

    def get_organization_membership(self, org: str) -> Membership:
        """
        :calls: `GET /user/memberships/orgs/{org} <https://docs.github.com/en/rest/reference/orgs#get-an-organization-membership-for-the-authenticated-user>`_
        """
        assert isinstance(org, str)
        org = urllib.parse.quote(org)
        headers, data = self._requester.requestJsonAndCheck("GET", f"/user/memberships/orgs/{org}")
        return github.Membership.Membership(self._requester, headers, data, completed=True)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "avatar_url" in attributes:  # pragma no branch
            self._avatar_url = self._makeStringAttribute(attributes["avatar_url"])
        if "bio" in attributes:  # pragma no branch
            self._bio = self._makeStringAttribute(attributes["bio"])
        if "blog" in attributes:  # pragma no branch
            self._blog = self._makeStringAttribute(attributes["blog"])
        if "collaborators" in attributes:  # pragma no branch
            self._collaborators = self._makeIntAttribute(attributes["collaborators"])
        if "company" in attributes:  # pragma no branch
            self._company = self._makeStringAttribute(attributes["company"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "disk_usage" in attributes:  # pragma no branch
            self._disk_usage = self._makeIntAttribute(attributes["disk_usage"])
        if "email" in attributes:  # pragma no branch
            self._email = self._makeStringAttribute(attributes["email"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "followers" in attributes:  # pragma no branch
            self._followers = self._makeIntAttribute(attributes["followers"])
        if "followers_url" in attributes:  # pragma no branch
            self._followers_url = self._makeStringAttribute(attributes["followers_url"])
        if "following" in attributes:  # pragma no branch
            self._following = self._makeIntAttribute(attributes["following"])
        if "following_url" in attributes:  # pragma no branch
            self._following_url = self._makeStringAttribute(attributes["following_url"])
        if "gists_url" in attributes:  # pragma no branch
            self._gists_url = self._makeStringAttribute(attributes["gists_url"])
        if "gravatar_id" in attributes:  # pragma no branch
            self._gravatar_id = self._makeStringAttribute(attributes["gravatar_id"])
        if "hireable" in attributes:  # pragma no branch
            self._hireable = self._makeBoolAttribute(attributes["hireable"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "location" in attributes:  # pragma no branch
            self._location = self._makeStringAttribute(attributes["location"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "organizations_url" in attributes:  # pragma no branch
            self._organizations_url = self._makeStringAttribute(attributes["organizations_url"])
        if "owned_private_repos" in attributes:  # pragma no branch
            self._owned_private_repos = self._makeIntAttribute(attributes["owned_private_repos"])
        if "plan" in attributes:  # pragma no branch
            self._plan = self._makeClassAttribute(github.Plan.Plan, attributes["plan"])
        if "private_gists" in attributes:  # pragma no branch
            self._private_gists = self._makeIntAttribute(attributes["private_gists"])
        if "public_gists" in attributes:  # pragma no branch
            self._public_gists = self._makeIntAttribute(attributes["public_gists"])
        if "public_repos" in attributes:  # pragma no branch
            self._public_repos = self._makeIntAttribute(attributes["public_repos"])
        if "received_events_url" in attributes:  # pragma no branch
            self._received_events_url = self._makeStringAttribute(attributes["received_events_url"])
        if "repos_url" in attributes:  # pragma no branch
            self._repos_url = self._makeStringAttribute(attributes["repos_url"])
        if "site_admin" in attributes:  # pragma no branch
            self._site_admin = self._makeBoolAttribute(attributes["site_admin"])
        if "starred_url" in attributes:  # pragma no branch
            self._starred_url = self._makeStringAttribute(attributes["starred_url"])
        if "subscriptions_url" in attributes:  # pragma no branch
            self._subscriptions_url = self._makeStringAttribute(attributes["subscriptions_url"])
        if "total_private_repos" in attributes:  # pragma no branch
            self._total_private_repos = self._makeIntAttribute(attributes["total_private_repos"])
        if "two_factor_authentication" in attributes:
            self._two_factor_authentication = self._makeBoolAttribute(attributes["two_factor_authentication"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
