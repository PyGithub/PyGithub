# -*- coding: utf-8 -*-

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
# Copyright 2018 Michał Górny <mgorny@gentoo.org>                            #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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

import github.GithubObject
import github.NamedUser
import github.Organization
import github.PaginatedList
import github.Repository
import github.TeamDiscussion

from . import Consts


class Team(github.GithubObject.CompletableGithubObject):
    """
    This class represents Teams. The reference can be found here http://developer.github.com/v3/orgs/teams/
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value, "name": self._name.value})

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def members_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._members_count)
        return self._members_count.value

    @property
    def members_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._members_url)
        return self._members_url.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def permission(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._permission)
        return self._permission.value

    @property
    def repos_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._repos_count)
        return self._repos_count.value

    @property
    def repositories_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._repositories_url)
        return self._repositories_url.value

    @property
    def slug(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._slug)
        return self._slug.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def organization(self):
        """
        :type: :class:`github.Organization.Organization`
        """
        self._completeIfNotSet(self._organization)
        return self._organization.value

    @property
    def privacy(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._privacy)
        return self._privacy.value

    @property
    def parent(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._parent)
        return self._parent.value

    def add_to_members(self, member):
        """
        This API call is deprecated. Use `add_membership` instead.
        https://developer.github.com/v3/teams/members/#deprecation-notice-1

        :calls: `PUT /teams/:id/members/:user <http://developer.github.com/v3/orgs/teams>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", self.url + "/members/" + member._identity
        )

    def add_membership(self, member, role=github.GithubObject.NotSet):
        """
        :calls: `PUT /teams/:id/memberships/:user <http://developer.github.com/v3/orgs/teams>`_
        :param member: :class:`github.Nameduser.NamedUser`
        :param role: string
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        assert role is github.GithubObject.NotSet or isinstance(role, str), role
        if role is not github.GithubObject.NotSet:
            assert role in ["member", "maintainer"]
            put_parameters = {
                "role": role,
            }
        else:
            put_parameters = {
                "role": "member",
            }
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", self.url + "/memberships/" + member._identity, input=put_parameters
        )

    def add_to_repos(self, repo):
        """
        :calls: `PUT /teams/:id/repos/:org/:repo <http://developer.github.com/v3/orgs/teams>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(repo, github.Repository.Repository), repo
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", self.url + "/repos/" + repo._identity
        )

    def set_repo_permission(self, repo, permission):
        """
        :calls: `PUT /teams/:id/repos/:org/:repo <http://developer.github.com/v3/orgs/teams>`_
        :param repo: :class:`github.Repository.Repository`
        :param permission: string
        :rtype: None
        """
        assert isinstance(repo, github.Repository.Repository), repo
        put_parameters = {
            "permission": permission,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", self.url + "/repos/" + repo._identity, input=put_parameters
        )

    def delete(self):
        """
        :calls: `DELETE /teams/:id <http://developer.github.com/v3/orgs/teams>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def edit(
        self,
        name,
        description=github.GithubObject.NotSet,
        permission=github.GithubObject.NotSet,
        privacy=github.GithubObject.NotSet,
    ):
        """
        :calls: `PATCH /teams/:id <http://developer.github.com/v3/orgs/teams>`_
        :param name: string
        :param description: string
        :param permission: string
        :param privacy: string
        :rtype: None
        """
        assert isinstance(name, str), name
        assert description is github.GithubObject.NotSet or isinstance(
            description, str
        ), description
        assert permission is github.GithubObject.NotSet or isinstance(
            permission, str
        ), permission
        assert privacy is github.GithubObject.NotSet or isinstance(
            privacy, str
        ), privacy
        post_parameters = {
            "name": name,
        }
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if permission is not github.GithubObject.NotSet:
            post_parameters["permission"] = permission
        if privacy is not github.GithubObject.NotSet:
            post_parameters["privacy"] = privacy
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH", self.url, input=post_parameters
        )
        self._useAttributes(data)

    def get_teams(self):
        """
        :calls: `GET /teams/:id/teams <https://developer.github.com/v3/teams/#list-child-teams>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Team.Team`
        """
        return github.PaginatedList.PaginatedList(
            github.Team.Team, self._requester, self.url + "/teams", None,
        )

    def get_discussions(self):
        """
        :calls: `GET /teams/:id/discussions <https://developer.github.com/v3/teams/discussions/#list-discussions>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.TeamDiscussion.TeamDiscussion`
        """
        return github.PaginatedList.PaginatedList(
            github.TeamDiscussion.TeamDiscussion,
            self._requester,
            self.url + "/discussions",
            None,
            headers={"Accept": Consts.mediaTypeTeamDiscussionsPreview},
        )

    def get_members(self, role=github.GithubObject.NotSet):
        """
        :calls: `GET /teams/:id/members <https://developer.github.com/v3/teams/members/#list-team-members>`_
        :param role: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert role is github.GithubObject.NotSet or isinstance(role, str), role
        url_parameters = dict()
        if role is not github.GithubObject.NotSet:
            assert role in ["member", "maintainer", "all"]
            url_parameters["role"] = role
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/members",
            url_parameters,
        )

    def get_repos(self):
        """
        :calls: `GET /teams/:id/repos <http://developer.github.com/v3/orgs/teams>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository, self._requester, self.url + "/repos", None
        )

    def invitations(self):
        """
        :calls: `GET /teams/:id/invitations <https://developer.github.com/v3/teams/members>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/invitations",
            None,
            headers={"Accept": Consts.mediaTypeOrganizationInvitationPreview},
        )

    def has_in_members(self, member):
        """
        :calls: `GET /teams/:id/members/:user <http://developer.github.com/v3/orgs/teams>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        status, headers, data = self._requester.requestJson(
            "GET", self.url + "/members/" + member._identity
        )
        return status == 204

    def has_in_repos(self, repo):
        """
        :calls: `GET /teams/:id/repos/:owner/:repo <http://developer.github.com/v3/orgs/teams>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: bool
        """
        assert isinstance(repo, github.Repository.Repository), repo
        status, headers, data = self._requester.requestJson(
            "GET", self.url + "/repos/" + repo._identity
        )
        return status == 204

    def remove_membership(self, member):
        """
        :calls: `DELETE /teams/:team_id/memberships/:username <https://developer.github.com/v3/teams/members/#remove-team-membership>`
        :param member:
        :return:
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.url + "/memberships/" + member._identity
        )

    def remove_from_members(self, member):
        """
        This API call is deprecated. Use `remove_membership` instead:
        https://developer.github.com/v3/teams/members/#deprecation-notice-2

        :calls: `DELETE /teams/:id/members/:user <http://developer.github.com/v3/orgs/teams>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.url + "/members/" + member._identity
        )

    def remove_from_repos(self, repo):
        """
        :calls: `DELETE /teams/:id/repos/:owner/:repo <http://developer.github.com/v3/orgs/teams>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(repo, github.Repository.Repository), repo
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.url + "/repos/" + repo._identity
        )

    @property
    def _identity(self):
        return self.id

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._members_count = github.GithubObject.NotSet
        self._members_url = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._permission = github.GithubObject.NotSet
        self._repos_count = github.GithubObject.NotSet
        self._repositories_url = github.GithubObject.NotSet
        self._slug = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._organization = github.GithubObject.NotSet
        self._privacy = github.GithubObject.NotSet
        self._parent = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
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
        if "permission" in attributes:  # pragma no branch
            self._permission = self._makeStringAttribute(attributes["permission"])
        if "repos_count" in attributes:  # pragma no branch
            self._repos_count = self._makeIntAttribute(attributes["repos_count"])
        if "repositories_url" in attributes:  # pragma no branch
            self._repositories_url = self._makeStringAttribute(
                attributes["repositories_url"]
            )
        if "slug" in attributes:  # pragma no branch
            self._slug = self._makeStringAttribute(attributes["slug"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "organization" in attributes:  # pragma no branch
            self._organization = self._makeClassAttribute(
                github.Organization.Organization, attributes["organization"]
            )
        if "privacy" in attributes:  # pragma no branch
            self._privacy = self._makeStringAttribute(attributes["privacy"])
        if "parent" in attributes:  # pragma no branch
            self._parent = self._makeClassAttribute(
                github.Team.Team, attributes["parent"]
            )
