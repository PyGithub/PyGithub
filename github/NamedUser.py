############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Bruce Richardson <itsbruce@workshy.org>                       #
# Copyright 2018 Iraquitan Cordeiro Filho <iraquitanfilho@gmail.com>           #
# Copyright 2018 Riccardo Pittau <elfosardo@users.noreply.github.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Victor Granic <vmg@boreal321.com>                             #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 namc <namratachaudhary@users.noreply.github.com>              #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Pavan Kunisetty <nagapavan@users.noreply.github.com>          #
# Copyright 2019 Shibasis Patel <smartshibasish@gmail.com>                     #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Surya Teja <94suryateja@gmail.com>                            #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
# Copyright 2020 Daniel Haas <thisisdhaas@gmail.com>                           #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Mark Amery <markamery@btinternet.com>                         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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
from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.Event
import github.Gist
import github.GithubObject
import github.Organization
import github.PaginatedList
import github.Permissions
import github.Plan
import github.Repository
from github import Consts
from github.GithubObject import Attribute, NotSet, Opt, is_defined
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.Event import Event
    from github.Gist import Gist
    from github.Membership import Membership
    from github.Organization import Organization
    from github.Permissions import Permissions
    from github.Plan import Plan
    from github.Project import Project
    from github.Repository import Repository
    from github.UserKey import UserKey


class NamedUser(github.GithubObject.CompletableGithubObject):
    """
    This class represents NamedUsers.

    The reference can be found here
    https://docs.github.com/en/rest/reference/users#get-a-user

    """

    def _initAttributes(self) -> None:
        self._avatar_url: Attribute[str] = NotSet
        self._bio: Attribute[str | None] = NotSet
        self._blog: Attribute[str | None] = NotSet
        self._collaborators: Attribute[int] = NotSet
        self._company: Attribute[str | None] = NotSet
        self._contributions: Attribute[int] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._disk_usage: Attribute[int] = NotSet
        self._email: Attribute[str | None] = NotSet
        self._events_url: Attribute[str] = NotSet
        self._followers: Attribute[int] = NotSet
        self._followers_url: Attribute[str] = NotSet
        self._following: Attribute[int] = NotSet
        self._following_url: Attribute[str] = NotSet
        self._gists_url: Attribute[str] = NotSet
        self._gravatar_id: Attribute[str | None] = NotSet
        self._hireable: Attribute[bool | None] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._invitation_teams_url: Attribute[str] = NotSet
        self._inviter: Attribute[NamedUser] = NotSet
        self._location: Attribute[str | None] = NotSet
        self._login: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._organizations_url: Attribute[str] = NotSet
        self._owned_private_repos: Attribute[int] = NotSet
        self._permissions: Attribute[Permissions] = NotSet
        self._plan: Attribute[Plan] = NotSet
        self._private_gists: Attribute[int] = NotSet
        self._public_gists: Attribute[int] = NotSet
        self._public_repos: Attribute[int] = NotSet
        self._received_events_url: Attribute[str] = NotSet
        self._repos_url: Attribute[str] = NotSet
        self._role: Attribute[str] = NotSet
        self._site_admin: Attribute[bool] = NotSet
        self._starred_url: Attribute[str] = NotSet
        self._subscriptions_url: Attribute[str] = NotSet
        self._suspended_at: Attribute[datetime | None] = NotSet
        self._team_count: Attribute[int] = NotSet
        self._total_private_repos: Attribute[int] = NotSet
        self._twitter_username: Attribute[str | None] = NotSet
        self._type: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"login": self._login.value})

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def twitter_username(self) -> str | None:
        self._completeIfNotSet(self._twitter_username)
        return self._twitter_username.value

    def __hash__(self) -> int:
        return hash((self.id, self.login))

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, type(self)) and self.login == other.login and self.id == other.id

    @property
    def avatar_url(self) -> str:
        self._completeIfNotSet(self._avatar_url)
        return self._avatar_url.value

    @property
    def bio(self) -> str | None:
        self._completeIfNotSet(self._bio)
        return self._bio.value

    @property
    def blog(self) -> str | None:
        self._completeIfNotSet(self._blog)
        return self._blog.value

    @property
    def collaborators(self) -> int | None:
        self._completeIfNotSet(self._collaborators)
        return self._collaborators.value

    @property
    def company(self) -> str | None:
        self._completeIfNotSet(self._company)
        return self._company.value

    @property
    def contributions(self) -> int:
        self._completeIfNotSet(self._contributions)
        return self._contributions.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def disk_usage(self) -> int:
        self._completeIfNotSet(self._disk_usage)
        return self._disk_usage.value

    @property
    def email(self) -> str | None:
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
    def gravatar_id(self) -> str | None:
        self._completeIfNotSet(self._gravatar_id)
        return self._gravatar_id.value

    @property
    def hireable(self) -> bool | None:
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
    def invitation_teams_url(self) -> str:
        self._completeIfNotSet(self._invitation_teams_url)
        return self._invitation_teams_url.value

    @property
    def inviter(self) -> NamedUser:
        self._completeIfNotSet(self._inviter)
        return self._inviter.value

    @property
    def location(self) -> str | None:
        self._completeIfNotSet(self._location)
        return self._location.value

    @property
    def login(self) -> str:
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def name(self) -> str | None:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def organizations_url(self) -> str:
        self._completeIfNotSet(self._organizations_url)
        return self._organizations_url.value

    @property
    def owned_private_repos(self) -> int | None:
        self._completeIfNotSet(self._owned_private_repos)
        return self._owned_private_repos.value

    @property
    def permissions(self) -> Permissions:
        self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    def plan(self) -> Plan | None:
        self._completeIfNotSet(self._plan)
        return self._plan.value

    @property
    def private_gists(self) -> int | None:
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
    def role(self) -> str:
        self._completeIfNotSet(self._role)
        return self._role.value

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
    def suspended_at(self) -> datetime | None:
        self._completeIfNotSet(self._suspended_at)
        return self._suspended_at.value

    @property
    def team_count(self) -> int:
        self._completeIfNotSet(self._team_count)
        return self._team_count.value

    @property
    def total_private_repos(self) -> int | None:
        self._completeIfNotSet(self._total_private_repos)
        return self._total_private_repos.value

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

    def get_events(self) -> PaginatedList[Event]:
        """
        :calls: `GET /users/{user}/events <https://docs.github.com/en/rest/reference/activity#events>`_
        """
        return github.PaginatedList.PaginatedList(github.Event.Event, self._requester, f"{self.url}/events", None)

    def get_followers(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /users/{user}/followers <https://docs.github.com/en/rest/reference/users#followers>`_
        """
        return github.PaginatedList.PaginatedList(NamedUser, self._requester, f"{self.url}/followers", None)

    def get_following(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /users/{user}/following <https://docs.github.com/en/rest/reference/users#followers>`_
        """
        return github.PaginatedList.PaginatedList(NamedUser, self._requester, f"{self.url}/following", None)

    def get_gists(self, since: Opt[datetime] = NotSet) -> PaginatedList[Gist]:
        """
        :calls: `GET /users/{user}/gists <https://docs.github.com/en/rest/reference/gists>`_
        """
        assert since is NotSet or isinstance(since, datetime), since
        url_parameters = dict()
        if is_defined(since):
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.Gist.Gist, self._requester, f"{self.url}/gists", url_parameters
        )

    def get_keys(self) -> PaginatedList[UserKey]:
        """
        :calls: `GET /users/{user}/keys <https://docs.github.com/en/rest/reference/users#create-a-public-ssh-key-for-the-authenticated-user>`_
        """
        return github.PaginatedList.PaginatedList(github.UserKey.UserKey, self._requester, f"{self.url}/keys", None)

    def get_orgs(self) -> PaginatedList[Organization]:
        """
        :calls: `GET /users/{user}/orgs <https://docs.github.com/en/rest/reference/orgs>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Organization.Organization, self._requester, f"{self.url}/orgs", None
        )

    def get_projects(self, state: str = "open") -> PaginatedList[Project]:
        """
        :calls: `GET /users/{user}/projects <https://docs.github.com/en/rest/reference/projects#list-user-projects>`_
        """
        assert isinstance(state, str), state
        url_parameters = {"state": state}
        return github.PaginatedList.PaginatedList(
            github.Project.Project,
            self._requester,
            f"{self.url}/projects",
            url_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )

    def get_public_events(self) -> PaginatedList[Event]:
        """
        :calls: `GET /users/{user}/events/public <https://docs.github.com/en/rest/reference/activity#events>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event, self._requester, f"{self.url}/events/public", None
        )

    def get_public_received_events(self) -> PaginatedList[Event]:
        """
        :calls: `GET /users/{user}/received_events/public <https://docs.github.com/en/rest/reference/activity#events>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            f"{self.url}/received_events/public",
            None,
        )

    def get_received_events(self) -> PaginatedList[Event]:
        """
        :calls: `GET /users/{user}/received_events <https://docs.github.com/en/rest/reference/activity#events>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event, self._requester, f"{self.url}/received_events", None
        )

    def get_repo(self, name: str) -> Repository:
        """
        :calls: `GET /repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/repos>`_
        """
        assert isinstance(name, str), name
        headers, data = self._requester.requestJsonAndCheck("GET", f"/repos/{self.login}/{name}")
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def get_repos(
        self,
        type: Opt[str] = NotSet,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
    ) -> PaginatedList[Repository]:
        """
        :calls: `GET /users/{user}/repos <https://docs.github.com/en/rest/reference/repos>`_
        """
        assert type is NotSet or isinstance(type, str), type
        assert sort is NotSet or isinstance(sort, str), sort
        assert direction is NotSet or isinstance(direction, str), direction
        url_parameters = dict()
        if type is not NotSet:
            url_parameters["type"] = type
        if sort is not NotSet:
            url_parameters["sort"] = sort
        if direction is not NotSet:
            url_parameters["direction"] = direction
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            f"{self.url}/repos",
            url_parameters,
        )

    def get_starred(self) -> PaginatedList[Repository]:
        """
        :calls: `GET /users/{user}/starred <https://docs.github.com/en/rest/reference/activity#starring>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository, self._requester, f"{self.url}/starred", None
        )

    def get_subscriptions(self) -> PaginatedList[Repository]:
        """
        :calls: `GET /users/{user}/subscriptions <https://docs.github.com/en/rest/reference/activity#watching>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            f"{self.url}/subscriptions",
            None,
        )

    def get_watched(self) -> PaginatedList[Repository]:
        """
        :calls: `GET /users/{user}/watched <https://docs.github.com/en/rest/reference/activity#starring>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository, self._requester, f"{self.url}/watched", None
        )

    def has_in_following(self, following: NamedUser) -> bool:
        """
        :calls: `GET /users/{user}/following/{target_user} <https://docs.github.com/en/rest/reference/users#check-if-a-user-follows-another-user>`_
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        status, headers, data = self._requester.requestJson("GET", f"{self.url}/following/{following._identity}")
        return status == 204

    @property
    def _identity(self) -> str:
        return self.login

    def get_organization_membership(self, org: str | Organization) -> Membership:
        """
        :calls: `GET /orgs/{org}/memberships/{username} <https://docs.github.com/en/rest/reference/orgs#check-organization-membership-for-a-user>`_
        """
        assert isinstance(org, str) or isinstance(org, github.Organization.Organization), org
        if isinstance(org, github.Organization.Organization):
            org = org.login  # type: ignore
        org = urllib.parse.quote(org)
        headers, data = self._requester.requestJsonAndCheck("GET", f"/orgs/{org}/memberships/{self.login}")
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
        if "contributions" in attributes:  # pragma no branch
            self._contributions = self._makeIntAttribute(attributes["contributions"])
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
        if "invitation_teams_url" in attributes:  # pragma no branch
            self._invitation_teams_url = self._makeStringAttribute(attributes["invitation_teams_url"])
        if "inviter" in attributes:  # pragma no branch
            self._inviter = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["inviter"])
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
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeClassAttribute(github.Permissions.Permissions, attributes["permissions"])
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
        if "role" in attributes:  # pragma no branch
            self._role = self._makeStringAttribute(attributes["role"])
        if "site_admin" in attributes:  # pragma no branch
            self._site_admin = self._makeBoolAttribute(attributes["site_admin"])
        if "starred_url" in attributes:  # pragma no branch
            self._starred_url = self._makeStringAttribute(attributes["starred_url"])
        if "subscriptions_url" in attributes:  # pragma no branch
            self._subscriptions_url = self._makeStringAttribute(attributes["subscriptions_url"])
        if "suspended_at" in attributes:  # pragma no branch
            self._suspended_at = self._makeDatetimeAttribute(attributes["suspended_at"])
        if "team_count" in attributes:
            self._team_count = self._makeIntAttribute(attributes["team_count"])
        if "total_private_repos" in attributes:  # pragma no branch
            self._total_private_repos = self._makeIntAttribute(attributes["total_private_repos"])
        if "twitter_username" in attributes:  # pragma no branch
            self._twitter_username = self._makeStringAttribute(attributes["twitter_username"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
