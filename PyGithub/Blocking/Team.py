# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking._base_github_object as bgo
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv


class Team(bgo.UpdatableGithubObject):
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

    def _initAttributes(self, id=rcv.Absent, members_count=rcv.Absent, members_url=rcv.Absent, name=rcv.Absent, organization=rcv.Absent, permission=rcv.Absent, repos_count=rcv.Absent, repositories_url=rcv.Absent, slug=rcv.Absent, url=rcv.Absent, **kwds):
        import PyGithub.Blocking.Organization
        super(Team, self)._initAttributes(**kwds)
        self.__id = rcv.Attribute("Team.id", rcv.IntConverter, id)
        self.__members_count = rcv.Attribute("Team.members_count", rcv.IntConverter, members_count)
        self.__members_url = rcv.Attribute("Team.members_url", rcv.StringConverter, members_url)
        self.__name = rcv.Attribute("Team.name", rcv.StringConverter, name)
        self.__organization = rcv.Attribute("Team.organization", rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization), organization)
        self.__permission = rcv.Attribute("Team.permission", rcv.StringConverter, permission)
        self.__repos_count = rcv.Attribute("Team.repos_count", rcv.IntConverter, repos_count)
        self.__repositories_url = rcv.Attribute("Team.repositories_url", rcv.StringConverter, repositories_url)
        self.__slug = rcv.Attribute("Team.slug", rcv.StringConverter, slug)
        self.__url = rcv.Attribute("Team.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, id=rcv.Absent, members_count=rcv.Absent, members_url=rcv.Absent, name=rcv.Absent, organization=rcv.Absent, permission=rcv.Absent, repos_count=rcv.Absent, repositories_url=rcv.Absent, slug=rcv.Absent, url=rcv.Absent, **kwds):
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

    def add_to_members(self, username):
        """
        Calls the `PUT /teams/:id/members/:username <http://developer.github.com/v3/orgs/teams#add-team-member>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: None
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.members_url, member=username)
        r = self.Session._request("PUT", url)

    def add_to_repos(self, repo):
        """
        Calls the `PUT /teams/:id/repos/:org/:repo <http://developer.github.com/v3/orgs/teams#add-team-repo>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: None
        """

        repo = snd.normalizeRepositoryFullName(repo)

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
            name = snd.normalizeString(name)
        if permission is not None:
            permission = snd.normalizeEnum(permission, "push", "pull", "admin")

        url = uritemplate.expand(self.url)
        postArguments = snd.dictionary(name=name, permission=permission)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_members(self, per_page=None):
        """
        Calls the `GET /teams/:id/members <http://developer.github.com/v3/orgs/teams#list-team-members>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.members_url)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_repos(self, per_page=None):
        """
        Calls the `GET /teams/:id/repos <http://developer.github.com/v3/orgs/teams#list-team-repos>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.repositories_url)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def has_in_members(self, username):
        """
        Calls the `GET /teams/:id/members/:username <http://developer.github.com/v3/orgs/teams#get-team-member>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: :class:`bool`
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.members_url, member=username)
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)

    def has_in_repos(self, repo):
        """
        Calls the `GET /teams/:id/repos/:owner/:repo <http://developer.github.com/v3/orgs/teams#get-team-repo>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: :class:`bool`
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/teams/{id}/repos/{owner}/{repo}", id=str(self.id), owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)

    def remove_from_members(self, username):
        """
        Calls the `DELETE /teams/:id/members/:username <http://developer.github.com/v3/orgs/teams#remove-team-member>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: None
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.members_url, member=username)
        r = self.Session._request("DELETE", url)

    def remove_from_repos(self, repo):
        """
        Calls the `DELETE /teams/:id/repos/:owner/:repo <http://developer.github.com/v3/orgs/teams#remove-team-repo>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: None
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/teams/{id}/repos/{owner}/{repo}", id=str(self.id), owner=repo[0], repo=repo[1])
        r = self.Session._request("DELETE", url)
