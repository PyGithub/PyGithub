############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Jan Orel <jan.orel@gooddata.com>                              #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Aron Culotta <aronwc@gmail.com>                               #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2016 mattjmorrison <mattjmorrison@mattjmorrison.com>               #
# Copyright 2018 Isuru Fernando <isuruf@gmail.com>                             #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 James D'Amato <james.j.damato@gmail.com>                      #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Manu Hortet <manuhortet@gmail.com>                            #
# Copyright 2018 Michał Górny <mgorny@gentoo.org>                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Tim Boring <tboring@hearst.com>                               #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Shibasis Patel <smartshibasish@gmail.com>                     #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Adrian Bridgett <58699309+tl-adrian-bridgett@users.noreply.github.com>#
# Copyright 2020 Andy Grunwald <andygrunwald@gmail.com>                        #
# Copyright 2020 Gilad Shefer <giladshefer@gmail.com>                          #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Tal Machani <12785464+talmachani@users.noreply.github.com>    #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 秋葉 <ambiguous404@gmail.com>                                   #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Kevin Grandjean <Muscaw@users.noreply.github.com>             #
# Copyright 2023 Mark Amery <markamery@btinternet.com>                         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Andrii Kezikov <cheshirez@gmail.com>                          #
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
from typing import TYPE_CHECKING, Any

from deprecated import deprecated

import github.NamedUser
import github.Organization
import github.PaginatedList
import github.Repository
import github.TeamDiscussion
from github import Consts
from github.GithubException import UnknownObjectException
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt

if TYPE_CHECKING:
    from github.Membership import Membership
    from github.NamedUser import NamedUser
    from github.Organization import Organization
    from github.PaginatedList import PaginatedList
    from github.Permissions import Permissions
    from github.Repository import Repository
    from github.TeamDiscussion import TeamDiscussion


class Team(CompletableGithubObject):
    """
    This class represents Teams.

    The reference can be found here
    https://docs.github.com/en/rest/reference/teams

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._members_count: Attribute[int] = NotSet
        self._members_url: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._notification_setting: Attribute[str] = NotSet
        self._permission: Attribute[str] = NotSet
        self._repos_count: Attribute[int] = NotSet
        self._repositories_url: Attribute[str] = NotSet
        self._slug: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._organization: Attribute[github.Organization.Organization] = NotSet
        self._privacy: Attribute[str] = NotSet
        self._parent: Attribute[github.Team.Team] = NotSet
        self._html_url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "name": self._name.value})

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def members_count(self) -> int:
        self._completeIfNotSet(self._members_count)
        return self._members_count.value

    @property
    def members_url(self) -> str:
        self._completeIfNotSet(self._members_url)
        return self._members_url.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def notification_setting(self) -> str:
        self._completeIfNotSet(self._notification_setting)
        return self._notification_setting.value

    @property
    def permission(self) -> str:
        self._completeIfNotSet(self._permission)
        return self._permission.value

    @property
    def repos_count(self) -> int:
        self._completeIfNotSet(self._repos_count)
        return self._repos_count.value

    @property
    def repositories_url(self) -> str:
        self._completeIfNotSet(self._repositories_url)
        return self._repositories_url.value

    @property
    def slug(self) -> str:
        self._completeIfNotSet(self._slug)
        return self._slug.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def organization(self) -> Organization:
        self._completeIfNotSet(self._organization)
        return self._organization.value

    @property
    def privacy(self) -> str:
        self._completeIfNotSet(self._privacy)
        return self._privacy.value

    @property
    def parent(self) -> Team:
        self._completeIfNotSet(self._parent)
        return self._parent.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    def add_to_members(self, member: NamedUser) -> None:
        """
        This API call is deprecated. Use `add_membership` instead.
        https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy

        :calls: `PUT /teams/{id}/members/{user} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck("PUT", f"{self.url}/members/{member._identity}")

    def add_membership(self, member: NamedUser, role: Opt[str] = NotSet) -> None:
        """
        :calls: `PUT /teams/{id}/memberships/{user} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        assert role is NotSet or isinstance(role, str), role
        if role is not NotSet:
            assert role in ["member", "maintainer"]
            put_parameters = {
                "role": role,
            }
        else:
            put_parameters = {
                "role": "member",
            }
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/memberships/{member._identity}", input=put_parameters
        )

    def get_team_membership(self, member: str | NamedUser) -> Membership:
        """
        :calls: `GET /orgs/{org}/memberships/team/{team_id}/{username} <https://docs.github.com/en/rest/reference/teams#get-team-membership-for-a-user>`_
        """
        assert isinstance(member, str) or isinstance(member, github.NamedUser.NamedUser), member
        if isinstance(member, github.NamedUser.NamedUser):
            member = member._identity
        else:
            member = urllib.parse.quote(member)
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/memberships/{member}")
        return github.Membership.Membership(self._requester, headers, data, completed=True)

    def add_to_repos(self, repo: Repository) -> None:
        """
        :calls: `PUT /teams/{id}/repos/{org}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, github.Repository.Repository), repo
        headers, data = self._requester.requestJsonAndCheck("PUT", f"{self.url}/repos/{repo._identity}")

    def get_repo_permission(self, repo: Repository) -> Permissions | None:
        """
        :calls: `GET /teams/{id}/repos/{org}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, github.Repository.Repository) or isinstance(repo, str), repo
        if isinstance(repo, github.Repository.Repository):
            repo = repo._identity  # type: ignore
        else:
            repo = urllib.parse.quote(repo)
        try:
            headers, data = self._requester.requestJsonAndCheck(
                "GET",
                f"{self.url}/repos/{repo}",
                headers={"Accept": Consts.teamRepositoryPermissions},
            )
            return github.Permissions.Permissions(self._requester, headers, data["permissions"], completed=True)
        except UnknownObjectException:
            return None

    @deprecated(
        reason="""
        Team.set_repo_permission() is deprecated, use Team.update_team_repository() instead.
        """
    )
    def set_repo_permission(self, repo: Repository, permission: str) -> None:
        """
        :calls: `PUT /teams/{id}/repos/{org}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        :param repo: :class:`github.Repository.Repository`
        :param permission: string
        :rtype: None
        """

        assert isinstance(repo, github.Repository.Repository), repo
        put_parameters = {
            "permission": permission,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/repos/{repo._identity}", input=put_parameters
        )

    def update_team_repository(self, repo: Repository, permission: str) -> bool:
        """
        :calls: `PUT /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams#check-team-permissions-for-a-repository>`_
        """
        assert isinstance(repo, github.Repository.Repository) or isinstance(repo, str), repo
        assert isinstance(permission, str), permission
        if isinstance(repo, github.Repository.Repository):
            repo_url_param = repo._identity
        else:
            repo_url_param = urllib.parse.quote(repo)
        put_parameters = {
            "permission": permission,
        }
        status, _, _ = self._requester.requestJson(
            "PUT",
            f"{self.organization.url}/teams/{self.slug}/repos/{repo_url_param}",
            input=put_parameters,
        )
        return status == 204

    def delete(self) -> None:
        """
        :calls: `DELETE /teams/{id} <https://docs.github.com/en/rest/reference/teams#delete-a-team>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def edit(
        self,
        name: str,
        description: Opt[str] = NotSet,
        permission: Opt[str] = NotSet,
        privacy: Opt[str] = NotSet,
        parent_team_id: Opt[int] = NotSet,
        notification_setting: Opt[str] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /teams/{id} <https://docs.github.com/en/rest/reference/teams#update-a-team>`_
        """
        assert isinstance(name, str), name
        assert description is NotSet or isinstance(description, str), description
        assert permission is NotSet or isinstance(permission, str), permission
        assert privacy is NotSet or isinstance(privacy, str), privacy
        assert parent_team_id is NotSet or isinstance(parent_team_id, (int, type(None))), parent_team_id
        assert notification_setting in ["notifications_enabled", "notifications_disabled", NotSet], notification_setting
        post_parameters = NotSet.remove_unset_items(
            {
                "name": name,
                "description": description,
                "permission": permission,
                "privacy": privacy,
                "parent_team_id": parent_team_id,
                "notification_setting": notification_setting,
            }
        )

        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def get_teams(self) -> PaginatedList[Team]:
        """
        :calls: `GET /teams/{id}/teams <https://docs.github.com/en/rest/reference/teams#list-teams>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Team.Team,
            self._requester,
            f"{self.url}/teams",
            None,
        )

    def get_discussions(self) -> PaginatedList[TeamDiscussion]:
        """
        :calls: `GET /teams/{id}/discussions <https://docs.github.com/en/rest/reference/teams#list-discussions>`_
        """
        return github.PaginatedList.PaginatedList(
            github.TeamDiscussion.TeamDiscussion,
            self._requester,
            f"{self.url}/discussions",
            None,
            headers={"Accept": Consts.mediaTypeTeamDiscussionsPreview},
        )

    def get_members(self, role: Opt[str] = NotSet) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /teams/{id}/members <https://docs.github.com/en/rest/reference/teams#list-team-members>`_
        """
        assert role is NotSet or isinstance(role, str), role
        url_parameters: dict[str, Any] = {}
        if role is not NotSet:
            assert role in ["member", "maintainer", "all"]
            url_parameters["role"] = role
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            f"{self.url}/members",
            url_parameters,
        )

    def get_repos(self) -> PaginatedList[Repository]:
        """
        :calls: `GET /teams/{id}/repos <https://docs.github.com/en/rest/reference/teams>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository, self._requester, f"{self.url}/repos", None
        )

    def invitations(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /teams/{id}/invitations <https://docs.github.com/en/rest/reference/teams#members>`_
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            f"{self.url}/invitations",
            None,
            headers={"Accept": Consts.mediaTypeOrganizationInvitationPreview},
        )

    def has_in_members(self, member: NamedUser) -> bool:
        """
        :calls: `GET /teams/{id}/members/{user} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        status, headers, data = self._requester.requestJson("GET", f"{self.url}/members/{member._identity}")
        return status == 204

    def has_in_repos(self, repo: Repository) -> bool:
        """
        :calls: `GET /teams/{id}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, github.Repository.Repository), repo
        status, headers, data = self._requester.requestJson("GET", f"{self.url}/repos/{repo._identity}")
        return status == 204

    def remove_membership(self, member: NamedUser) -> None:
        """
        :calls: `DELETE /teams/{team_id}/memberships/{username} <https://docs.github.com/en/rest/reference/teams#remove-team-membership-for-a-user>`_
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/memberships/{member._identity}")

    def remove_from_members(self, member: NamedUser) -> None:
        """
        This API call is deprecated. Use `remove_membership` instead:
        https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy

        :calls: `DELETE /teams/{id}/members/{user} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/members/{member._identity}")

    def remove_from_repos(self, repo: Repository) -> None:
        """
        :calls: `DELETE /teams/{id}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, github.Repository.Repository), repo
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/repos/{repo._identity}")

    @property
    def _identity(self) -> int:
        return self.id

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "members_count" in attributes:  # pragma no branch
            self._members_count = self._makeIntAttribute(attributes["members_count"])
        if "members_url" in attributes:  # pragma no branch
            self._members_url = self._makeStringAttribute(attributes["members_url"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "notification_setting" in attributes:  # pragma no branch
            self._notification_setting = self._makeStringAttribute(attributes["notification_setting"])
        if "permission" in attributes:  # pragma no branch
            self._permission = self._makeStringAttribute(attributes["permission"])
        if "repos_count" in attributes:  # pragma no branch
            self._repos_count = self._makeIntAttribute(attributes["repos_count"])
        if "repositories_url" in attributes:  # pragma no branch
            self._repositories_url = self._makeStringAttribute(attributes["repositories_url"])
        if "slug" in attributes:  # pragma no branch
            self._slug = self._makeStringAttribute(attributes["slug"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "organization" in attributes:  # pragma no branch
            self._organization = self._makeClassAttribute(github.Organization.Organization, attributes["organization"])
        if "privacy" in attributes:  # pragma no branch
            self._privacy = self._makeStringAttribute(attributes["privacy"])
        if "parent" in attributes:  # pragma no branch
            self._parent = self._makeClassAttribute(github.Team.Team, attributes["parent"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
