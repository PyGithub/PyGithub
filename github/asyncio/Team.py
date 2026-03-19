# FILE AUTO GENERATED DO NOT TOUCH
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
# Copyright 2025 Christoph Reiter <reiter.christoph@gmail.com>                 #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Oscar van Leusen <oscarvanleusen@gmail.com>                   #
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

from typing_extensions import deprecated

import github
from github import Consts
from github.GithubException import UnknownObjectException

from . import Membership, NamedUser, Organization, PaginatedList, Permissions, Repository, TeamDiscussion
from .GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_defined, is_undefined, method_returns

if TYPE_CHECKING:
    from .NamedUser import OrganizationInvitation


class Team(CompletableGithubObject):
    """
    This class represents Teams.

    The reference can be found here
    https://docs.github.com/en/rest/reference/teams

    The OpenAPI schema can be found at

    - /components/schemas/enterprise-team
    - /components/schemas/nullable-team-simple
    - /components/schemas/team
    - /components/schemas/team-full
    - /components/schemas/team-simple

    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._enterprise_id: Attribute[int] = NotSet
        self._group_id: Attribute[int] = NotSet
        self._group_name: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._ldap_dn: Attribute[str] = NotSet
        self._members_count: Attribute[int] = NotSet
        self._members_url: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._notification_setting: Attribute[str] = NotSet
        self._organization: Attribute[Organization.Organization] = NotSet
        self._organization_id: Attribute[int] = NotSet
        self._organization_selection_type: Attribute[str] = NotSet
        self._parent: Attribute[Team] = NotSet
        self._permission: Attribute[str] = NotSet
        self._permissions: Attribute[Permissions.Permissions] = NotSet
        self._privacy: Attribute[str] = NotSet
        self._repos_count: Attribute[int] = NotSet
        self._repositories_url: Attribute[str] = NotSet
        self._slug: Attribute[str] = NotSet
        self._sync_to_organizations: Attribute[str] = NotSet
        self._type: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "name": self._name.value})

    @property
    async def _identity(self) -> int:
        return await self.id

    @property
    async def created_at(self) -> datetime:
        await self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    async def description(self) -> str:
        await self._completeIfNotSet(self._description)
        return self._description.value

    @property
    async def enterprise_id(self) -> int:
        await self._completeIfNotSet(self._enterprise_id)
        return self._enterprise_id.value

    @property
    async def group_id(self) -> int:
        await self._completeIfNotSet(self._group_id)
        return self._group_id.value

    @property
    async def group_name(self) -> str:
        await self._completeIfNotSet(self._group_name)
        return self._group_name.value

    @property
    async def html_url(self) -> str:
        await self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    async def id(self) -> int:
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def ldap_dn(self) -> str:
        await self._completeIfNotSet(self._ldap_dn)
        return self._ldap_dn.value

    @property
    async def members_count(self) -> int:
        await self._completeIfNotSet(self._members_count)
        return self._members_count.value

    @property
    async def members_url(self) -> str:
        await self._completeIfNotSet(self._members_url)
        return self._members_url.value

    @property
    async def name(self) -> str:
        await self._completeIfNotSet(self._name)
        return self._name.value

    @property
    async def node_id(self) -> str:
        await self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    async def notification_setting(self) -> str:
        await self._completeIfNotSet(self._notification_setting)
        return self._notification_setting.value

    @property
    async def organization(self) -> Organization.Organization:
        await self._completeIfNotSet(self._organization)
        return self._organization.value

    @property
    async def organization_id(self) -> int:
        await self._completeIfNotSet(self._organization_id)
        return self._organization_id.value

    @property
    async def organization_selection_type(self) -> str:
        await self._completeIfNotSet(self._organization_selection_type)
        return self._organization_selection_type.value

    @property
    async def parent(self) -> Team:
        await self._completeIfNotSet(self._parent)
        return self._parent.value

    @property
    async def permission(self) -> str:
        await self._completeIfNotSet(self._permission)
        return self._permission.value

    @property
    async def permissions(self) -> Permissions.Permissions:
        await self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    async def privacy(self) -> str:
        await self._completeIfNotSet(self._privacy)
        return self._privacy.value

    @property
    async def repos_count(self) -> int:
        await self._completeIfNotSet(self._repos_count)
        return self._repos_count.value

    @property
    async def repositories_url(self) -> str:
        await self._completeIfNotSet(self._repositories_url)
        return self._repositories_url.value

    @property
    async def slug(self) -> str:
        await self._completeIfNotSet(self._slug)
        return self._slug.value

    @property
    async def sync_to_organizations(self) -> str:
        await self._completeIfNotSet(self._sync_to_organizations)
        return self._sync_to_organizations.value

    @property
    async def type(self) -> str:
        await self._completeIfNotSet(self._type)
        return self._type.value

    @property
    async def updated_at(self) -> datetime:
        await self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    @deprecated("Use add_membership instead")
    async def add_to_members(self, member: NamedUser.NamedUser) -> None:
        """
        This API call is deprecated. Use `add_membership` instead.
        https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy

        :calls: `PUT /teams/{team_id}/members/{username} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, (NamedUser.NamedUser, github.NamedUser.NamedUser)), member
        headers, data = await self._requester.requestJsonAndCheck(
            "PUT", f"{await self.url}/members/{(await member._identity)}"
        )

    async def add_membership(self, member: NamedUser.NamedUser, role: Opt[str] = NotSet) -> None:
        """
        :calls: `PUT /teams/{team_id}/memberships/{username} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, (NamedUser.NamedUser, github.NamedUser.NamedUser)), member
        assert is_undefined(role) or isinstance(role, str), role
        if is_defined(role):
            assert role in ["member", "maintainer"]
            put_parameters = {
                "role": role,
            }
        else:
            put_parameters = {
                "role": "member",
            }
        headers, data = await self._requester.requestJsonAndCheck(
            "PUT", f"{await self.url}/memberships/{(await member._identity)}", input=put_parameters
        )

    async def get_team_membership(self, member: str | NamedUser.NamedUser) -> Membership.Membership:
        """
        :calls: `GET /orgs/{org}/teams/{team_slug}/memberships/{username} <https://docs.github.com/en/rest/reference/teams#get-team-membership-for-a-user>`_
        """
        assert isinstance(member, str) or isinstance(member, (NamedUser.NamedUser, github.NamedUser.NamedUser)), member
        if isinstance(member, (NamedUser.NamedUser, github.NamedUser.NamedUser)):
            member = await member._identity
        else:
            member = urllib.parse.quote(member, safe="")
        headers, data = await self._requester.requestJsonAndCheck("GET", f"{await self.url}/memberships/{member}")
        return Membership.Membership(self._requester, headers, data, completed=True)

    async def add_to_repos(self, repo: str | Repository.Repository) -> None:
        """
        :calls: `PUT /teams/{team_id}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, (str, Repository.Repository, github.Repository.Repository)), repo
        headers, data = await self._requester.requestJsonAndCheck(
            "PUT", f"{await self.url}/repos/{await Repository.Repository.as_url_param(repo)}"
        )

    @method_returns(schema_property="permissions")
    async def get_repo_permission(self, repo: str | Repository.Repository) -> Permissions.Permissions | None:
        """
        :calls: `GET /teams/{team_id}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, (str, Repository.Repository, github.Repository.Repository)), repo
        try:
            headers, data = await self._requester.requestJsonAndCheck(
                "GET",
                f"{await self.url}/repos/{await Repository.Repository.as_url_param(repo)}",
                headers={"Accept": Consts.teamRepositoryPermissions},
            )
            return Permissions.Permissions(self._requester, headers, data["permissions"])
        except UnknownObjectException:
            return None

    @deprecated(
        """
        Team.set_repo_permission() is deprecated, use Team.update_team_repository() instead.
        """
    )
    async def set_repo_permission(self, repo: str | Repository.Repository, permission: str) -> None:
        """
        :calls: `PUT /teams/{team_id}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        :param repo: :class:`Repository.Repository`
        :param permission: string
        :rtype: None
        """
        assert isinstance(repo, (str, Repository.Repository, github.Repository.Repository)), repo
        put_parameters = {
            "permission": permission,
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "PUT", f"{await self.url}/repos/{await Repository.Repository.as_url_param(repo)}", input=put_parameters
        )

    async def update_team_repository(self, repo: str | Repository.Repository, permission: str) -> bool:
        """
        :calls: `PUT /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams#check-team-permissions-for-a-repository>`_
        """
        assert isinstance(repo, (str, Repository.Repository, github.Repository.Repository)), repo
        assert isinstance(permission, str), permission
        put_parameters = {
            "permission": permission,
        }
        status, _, _ = await self._requester.requestJson(
            "PUT",
            f"{await (await self.organization).url}/teams/{await self.slug}/repos/{await Repository.Repository.as_url_param(repo)}",
            input=put_parameters,
        )
        return status == 204

    async def delete(self) -> None:
        """
        :calls: `DELETE /teams/{team_id} <https://docs.github.com/en/rest/reference/teams#delete-a-team>`_
        """
        headers, data = await self._requester.requestJsonAndCheck("DELETE", await self.url)

    async def edit(
        self,
        name: str,
        description: Opt[str] = NotSet,
        permission: Opt[str] = NotSet,
        privacy: Opt[str] = NotSet,
        parent_team_id: Opt[int] = NotSet,
        notification_setting: Opt[str] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /teams/{team_id} <https://docs.github.com/en/rest/reference/teams#update-a-team>`_
        """
        assert isinstance(name, str), name
        assert is_undefined(description) or isinstance(description, str), description
        assert is_undefined(permission) or isinstance(permission, str), permission
        assert is_undefined(privacy) or isinstance(privacy, str), privacy
        assert is_undefined(parent_team_id) or isinstance(parent_team_id, (int, type(None))), parent_team_id
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

        headers, data = await self._requester.requestJsonAndCheck("PATCH", await self.url, input=post_parameters)
        self._useAttributes(data)
        self._set_complete()

    async def get_teams(self) -> PaginatedList.PaginatedList[Team]:
        """
        :calls: `GET /teams/{team_id}/teams <https://docs.github.com/en/rest/reference/teams#list-teams>`_
        """
        return PaginatedList.PaginatedList(
            Team,
            self._requester,
            f"{await self.url}/teams",
            None,
        )

    async def get_discussions(self) -> PaginatedList.PaginatedList[TeamDiscussion.TeamDiscussion]:
        """
        :calls: `GET /teams/{team_id}/discussions <https://docs.github.com/en/rest/reference/teams#list-discussions>`_
        """
        return PaginatedList.PaginatedList(
            TeamDiscussion.TeamDiscussion,
            self._requester,
            f"{await self.url}/discussions",
            None,
            headers={"Accept": Consts.mediaTypeTeamDiscussionsPreview},
        )

    async def get_members(self, role: Opt[str] = NotSet) -> PaginatedList.PaginatedList[NamedUser.NamedUser]:
        """
        :calls: `GET /teams/{team_id}/members <https://docs.github.com/en/rest/reference/teams#list-team-members>`_
        """
        assert is_undefined(role) or isinstance(role, str), role
        url_parameters: dict[str, Any] = {}
        if is_defined(role):
            assert role in ["member", "maintainer", "all"]
            url_parameters["role"] = role
        return PaginatedList.PaginatedList(
            NamedUser.NamedUser,
            self._requester,
            f"{await self.url}/members",
            url_parameters,
        )

    async def get_repos(self) -> PaginatedList.PaginatedList[Repository.Repository]:
        """
        :calls: `GET /teams/{team_id}/repos <https://docs.github.com/en/rest/reference/teams>`_
        """
        return PaginatedList.PaginatedList(Repository.Repository, self._requester, f"{await self.url}/repos", None)

    async def invitations(self) -> PaginatedList.PaginatedList[OrganizationInvitation]:
        """
        :calls: `GET /teams/{team_id}/invitations <https://docs.github.com/en/rest/reference/teams#members>`_
        """
        return PaginatedList.PaginatedList(
            NamedUser.OrganizationInvitation,
            self._requester,
            f"{await self.url}/invitations",
            None,
            headers={"Accept": Consts.mediaTypeOrganizationInvitationPreview},
        )

    async def has_in_members(self, member: NamedUser.NamedUser) -> bool:
        """
        :calls: `GET /teams/{team_id}/members/{username} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, (NamedUser.NamedUser, github.NamedUser.NamedUser)), member
        status, headers, data = await self._requester.requestJson(
            "GET", f"{await self.url}/members/{(await member._identity)}"
        )
        return status == 204

    async def has_in_repos(self, repo: str | Repository.Repository) -> bool:
        """
        :calls: `GET /teams/{team_id}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, (str, Repository.Repository, github.Repository.Repository)), repo
        status, headers, data = await self._requester.requestJson(
            "GET", f"{await self.url}/repos/{await Repository.Repository.as_url_param(repo)}"
        )
        return status == 204

    async def remove_membership(self, member: NamedUser.NamedUser) -> None:
        """
        :calls: `DELETE /teams/{team_id}/memberships/{username} <https://docs.github.com/en/rest/reference/teams#remove-team-membership-for-a-user>`_
        """
        assert isinstance(member, (NamedUser.NamedUser, github.NamedUser.NamedUser)), member
        headers, data = await self._requester.requestJsonAndCheck(
            "DELETE", f"{await self.url}/memberships/{(await member._identity)}"
        )

    @deprecated("Use remove_membership instead")
    async def remove_from_members(self, member: NamedUser.NamedUser) -> None:
        """
        This API call is deprecated. Use `remove_membership` instead:
        https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy

        :calls: `DELETE /teams/{team_id}/members/{username} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(member, (NamedUser.NamedUser, github.NamedUser.NamedUser)), member
        headers, data = await self._requester.requestJsonAndCheck(
            "DELETE", f"{await self.url}/members/{(await member._identity)}"
        )

    async def remove_from_repos(self, repo: str | Repository.Repository) -> None:
        """
        :calls: `DELETE /teams/{team_id}/repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/teams>`_
        """
        assert isinstance(repo, (str, Repository.Repository, github.Repository.Repository)), repo
        headers, data = await self._requester.requestJsonAndCheck(
            "DELETE", f"{await self.url}/repos/{await Repository.Repository.as_url_param(repo)}"
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "enterprise_id" in attributes:  # pragma no branch
            self._enterprise_id = self._makeIntAttribute(attributes["enterprise_id"])
        if "group_id" in attributes:  # pragma no branch
            self._group_id = self._makeIntAttribute(attributes["group_id"])
        if "group_name" in attributes:  # pragma no branch
            self._group_name = self._makeStringAttribute(attributes["group_name"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        elif "url" in attributes and attributes["url"]:
            id = attributes["url"].split("/")[-1]
            if id.isnumeric():
                self._id = self._makeIntAttribute(int(id))
        if "ldap_dn" in attributes:  # pragma no branch
            self._ldap_dn = self._makeStringAttribute(attributes["ldap_dn"])
        if "members_count" in attributes:  # pragma no branch
            self._members_count = self._makeIntAttribute(attributes["members_count"])
        if "members_url" in attributes:  # pragma no branch
            self._members_url = self._makeStringAttribute(attributes["members_url"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "notification_setting" in attributes:  # pragma no branch
            self._notification_setting = self._makeStringAttribute(attributes["notification_setting"])
        if "organization" in attributes:  # pragma no branch
            self._organization = self._makeClassAttribute(Organization.Organization, attributes["organization"])
        if "organization_id" in attributes:  # pragma no branch
            self._organization_id = self._makeIntAttribute(attributes["organization_id"])
        if "organization_selection_type" in attributes:  # pragma no branch
            self._organization_selection_type = self._makeStringAttribute(attributes["organization_selection_type"])
        if "parent" in attributes:  # pragma no branch
            self._parent = self._makeClassAttribute(Team, attributes["parent"])
        if "permission" in attributes:  # pragma no branch
            self._permission = self._makeStringAttribute(attributes["permission"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeClassAttribute(Permissions.Permissions, attributes["permissions"])
        if "privacy" in attributes:  # pragma no branch
            self._privacy = self._makeStringAttribute(attributes["privacy"])
        if "repos_count" in attributes:  # pragma no branch
            self._repos_count = self._makeIntAttribute(attributes["repos_count"])
        if "repositories_url" in attributes:  # pragma no branch
            self._repositories_url = self._makeStringAttribute(attributes["repositories_url"])
        if "slug" in attributes:  # pragma no branch
            self._slug = self._makeStringAttribute(attributes["slug"])
        if "sync_to_organizations" in attributes:  # pragma no branch
            self._sync_to_organizations = self._makeStringAttribute(attributes["sync_to_organizations"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
