# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.Parameters
import PyGithub.Blocking.Attributes

import PyGithub.Blocking.Organization
import PyGithub.Blocking.Repository
import PyGithub.Blocking.User


class Team(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.get_teams`
      * :meth:`.Github.get_team`
      * :meth:`.Organization.create_team`
      * :meth:`.Organization.get_teams`
      * :meth:`.Repository.get_teams`
    """

    def _initAttributes(self, id=PyGithub.Blocking.Attributes.Absent, members_count=PyGithub.Blocking.Attributes.Absent, members_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, organization=PyGithub.Blocking.Attributes.Absent, permission=PyGithub.Blocking.Attributes.Absent, repos_count=PyGithub.Blocking.Attributes.Absent, repositories_url=PyGithub.Blocking.Attributes.Absent, slug=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(Team, self)._initAttributes(**kwds)
        self.__id = PyGithub.Blocking.Attributes.Attribute("Team.id", PyGithub.Blocking.Attributes.IntConverter, id)
        self.__members_count = PyGithub.Blocking.Attributes.Attribute("Team.members_count", PyGithub.Blocking.Attributes.IntConverter, members_count)
        self.__members_url = PyGithub.Blocking.Attributes.Attribute("Team.members_url", PyGithub.Blocking.Attributes.StringConverter, members_url)
        self.__name = PyGithub.Blocking.Attributes.Attribute("Team.name", PyGithub.Blocking.Attributes.StringConverter, name)
        self.__organization = PyGithub.Blocking.Attributes.Attribute("Team.organization", PyGithub.Blocking.Attributes.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization), organization)
        self.__permission = PyGithub.Blocking.Attributes.Attribute("Team.permission", PyGithub.Blocking.Attributes.StringConverter, permission)
        self.__repos_count = PyGithub.Blocking.Attributes.Attribute("Team.repos_count", PyGithub.Blocking.Attributes.IntConverter, repos_count)
        self.__repositories_url = PyGithub.Blocking.Attributes.Attribute("Team.repositories_url", PyGithub.Blocking.Attributes.StringConverter, repositories_url)
        self.__slug = PyGithub.Blocking.Attributes.Attribute("Team.slug", PyGithub.Blocking.Attributes.StringConverter, slug)
        self.__url = PyGithub.Blocking.Attributes.Attribute("Team.url", PyGithub.Blocking.Attributes.StringConverter, url)

    def _updateAttributes(self, eTag, id=PyGithub.Blocking.Attributes.Absent, members_count=PyGithub.Blocking.Attributes.Absent, members_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, organization=PyGithub.Blocking.Attributes.Absent, permission=PyGithub.Blocking.Attributes.Absent, repos_count=PyGithub.Blocking.Attributes.Absent, repositories_url=PyGithub.Blocking.Attributes.Absent, slug=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(Team, self)._updateAttributes(eTag, **kwds)
        self.__id.update(id)
        self.__members_count.update(members_count)
        self.__members_url.update(members_url)
        self.__name.update(name)
        self.__organization.update(organization)
        self.__permission.update(permission)
        self.__repos_count.update(repos_count)
        self.__repositories_url.update(repositories_url)
        self.__slug.update(slug)
        self.__url.update(url)

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def members_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__members_count.needsLazyCompletion)
        return self.__members_count.value

    @property
    def members_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__members_url.needsLazyCompletion)
        return self.__members_url.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def organization(self):
        """
        :type: :class:`.Organization`
        """
        self._completeLazily(self.__organization.needsLazyCompletion)
        return self.__organization.value

    @property
    def permission(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__permission.needsLazyCompletion)
        return self.__permission.value

    @property
    def repos_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__repos_count.needsLazyCompletion)
        return self.__repos_count.value

    @property
    def repositories_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__repositories_url.needsLazyCompletion)
        return self.__repositories_url.value

    @property
    def slug(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__slug.needsLazyCompletion)
        return self.__slug.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    def add_to_members(self, user):
        """
        Calls the `PUT /teams/:id/members/:user <http://developer.github.com/v3/orgs/teams#add-team-member>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: None
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.members_url, member=user)
        r = self.Session._request("PUT", url)

    def add_to_repos(self, repo):
        """
        Calls the `PUT /teams/:id/repos/:org/:repo <http://developer.github.com/v3/orgs/teams#add-team-repo>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`TwoStrings`
        :rtype: None
        """

        repo = PyGithub.Blocking.Parameters.normalizeRepository(repo)

        url = uritemplate.expand("https://api.github.com/teams/{id}/repos/{org}/{repo}", id=str(self.id), org=repo[0], repo=repo[1])
        r = self.Session._request("PUT", url)

    def delete(self):
        """
        Calls the `DELETE /teams/:id <http://developer.github.com/v3/orgs/teams#delete-team>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)

    def edit(self, name=None, permission=None):
        """
        Calls the `PATCH /teams/:id <http://developer.github.com/v3/orgs/teams#edit-team>`__ end point.

        This is the only method calling this end point.

        :param name: optional :class:`string`
        :param permission: optional "push" or "pull" or "admin"
        :rtype: None
        """

        if name is not None:
            name = PyGithub.Blocking.Parameters.normalizeString(name)
        if permission is not None:
            permission = PyGithub.Blocking.Parameters.normalizeEnum(permission, "push", "pull", "admin")

        url = uritemplate.expand(self.url)
        postArguments = PyGithub.Blocking.Parameters.dictionary(name=name, permission=permission)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_members(self, per_page=None):
        """
        Calls the `GET /teams/:id/members <http://developer.github.com/v3/orgs/teams#list-team-members>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.members_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.User.User, self.Session, "GET", url, urlArguments=urlArguments)

    def get_repos(self, per_page=None):
        """
        Calls the `GET /teams/:id/repos <http://developer.github.com/v3/orgs/teams#list-team-repos>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.repositories_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.Repository.Repository, self.Session, "GET", url, urlArguments=urlArguments)

    def has_in_members(self, user):
        """
        Calls the `GET /teams/:id/members/:user <http://developer.github.com/v3/orgs/teams#get-team-member>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: :class:`bool`
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.members_url, member=user)
        r = self.Session._request("GET", url, accept404=True)
        if r.status_code == 204:
            return True
        else:
            return False

    def has_in_repos(self, repo):
        """
        Calls the `GET /teams/:id/repos/:owner/:repo <http://developer.github.com/v3/orgs/teams#get-team-repo>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`TwoStrings`
        :rtype: :class:`bool`
        """

        repo = PyGithub.Blocking.Parameters.normalizeRepository(repo)

        url = uritemplate.expand("https://api.github.com/teams/{id}/repos/{owner}/{repo}", id=str(self.id), owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url, accept404=True)
        if r.status_code == 204:
            return True
        else:
            return False

    def remove_from_members(self, user):
        """
        Calls the `DELETE /teams/:id/members/:user <http://developer.github.com/v3/orgs/teams#remove-team-member>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: None
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.members_url, member=user)
        r = self.Session._request("DELETE", url)

    def remove_from_repos(self, repo):
        """
        Calls the `DELETE /teams/:id/repos/:owner/:repo <http://developer.github.com/v3/orgs/teams#remove-team-repo>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`TwoStrings`
        :rtype: None
        """

        repo = PyGithub.Blocking.Parameters.normalizeRepository(repo)

        url = uritemplate.expand("https://api.github.com/teams/{id}/repos/{owner}/{repo}", id=str(self.id), owner=repo[0], repo=repo[1])
        r = self.Session._request("DELETE", url)
