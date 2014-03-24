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

import PyGithub.Blocking.Entity
import PyGithub.Blocking.Organization
import PyGithub.Blocking.PublicKey
import PyGithub.Blocking.Repository


class User(PyGithub.Blocking.Entity.Entity):
    """
    Base class: :class:`.Entity`

    Derived classes:
      * :class:`.AuthenticatedUser`
      * :class:`.Contributor`

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.get_followers`
      * :meth:`.AuthenticatedUser.get_following`
      * :meth:`.Github.get_user`
      * :meth:`.Github.get_users`
      * :meth:`.Organization.get_members`
      * :meth:`.Organization.get_public_members`
      * :meth:`.Repository.get_assignees`
      * :meth:`.Repository.get_collaborators`
      * :meth:`.Repository.get_stargazers`
      * :meth:`.Repository.get_subscribers`
      * :attr:`.Repository.owner`
      * :meth:`.Team.get_members`
      * :meth:`.User.get_followers`
      * :meth:`.User.get_following`
    """

    def _initAttributes(self, followers_url=PyGithub.Blocking.Attributes.Absent, following_url=PyGithub.Blocking.Attributes.Absent, gists_url=PyGithub.Blocking.Attributes.Absent, gravatar_id=PyGithub.Blocking.Attributes.Absent, hireable=PyGithub.Blocking.Attributes.Absent, organizations_url=PyGithub.Blocking.Attributes.Absent, received_events_url=PyGithub.Blocking.Attributes.Absent, site_admin=PyGithub.Blocking.Attributes.Absent, starred_url=PyGithub.Blocking.Attributes.Absent, subscriptions_url=PyGithub.Blocking.Attributes.Absent, bio=None, **kwds):
        super(User, self)._initAttributes(**kwds)
        self.__followers_url = PyGithub.Blocking.Attributes.StringAttribute("User.followers_url", followers_url)
        self.__following_url = PyGithub.Blocking.Attributes.StringAttribute("User.following_url", following_url)
        self.__gists_url = PyGithub.Blocking.Attributes.StringAttribute("User.gists_url", gists_url)
        self.__gravatar_id = PyGithub.Blocking.Attributes.StringAttribute("User.gravatar_id", gravatar_id)
        self.__hireable = PyGithub.Blocking.Attributes.BoolAttribute("User.hireable", hireable)
        self.__organizations_url = PyGithub.Blocking.Attributes.StringAttribute("User.organizations_url", organizations_url)
        self.__received_events_url = PyGithub.Blocking.Attributes.StringAttribute("User.received_events_url", received_events_url)
        self.__site_admin = PyGithub.Blocking.Attributes.BoolAttribute("User.site_admin", site_admin)
        self.__starred_url = PyGithub.Blocking.Attributes.StringAttribute("User.starred_url", starred_url)
        self.__subscriptions_url = PyGithub.Blocking.Attributes.StringAttribute("User.subscriptions_url", subscriptions_url)

    def _updateAttributes(self, eTag, followers_url=PyGithub.Blocking.Attributes.Absent, following_url=PyGithub.Blocking.Attributes.Absent, gists_url=PyGithub.Blocking.Attributes.Absent, gravatar_id=PyGithub.Blocking.Attributes.Absent, hireable=PyGithub.Blocking.Attributes.Absent, organizations_url=PyGithub.Blocking.Attributes.Absent, received_events_url=PyGithub.Blocking.Attributes.Absent, site_admin=PyGithub.Blocking.Attributes.Absent, starred_url=PyGithub.Blocking.Attributes.Absent, subscriptions_url=PyGithub.Blocking.Attributes.Absent, bio=None, **kwds):
        super(User, self)._updateAttributes(eTag, **kwds)
        self.__followers_url.update(followers_url)
        self.__following_url.update(following_url)
        self.__gists_url.update(gists_url)
        self.__gravatar_id.update(gravatar_id)
        self.__hireable.update(hireable)
        self.__organizations_url.update(organizations_url)
        self.__received_events_url.update(received_events_url)
        self.__site_admin.update(site_admin)
        self.__starred_url.update(starred_url)
        self.__subscriptions_url.update(subscriptions_url)

    @property
    def followers_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__followers_url.needsLazyCompletion)
        return self.__followers_url.value

    @property
    def following_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__following_url.needsLazyCompletion)
        return self.__following_url.value

    @property
    def gists_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__gists_url.needsLazyCompletion)
        return self.__gists_url.value

    @property
    def gravatar_id(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__gravatar_id.needsLazyCompletion)
        return self.__gravatar_id.value

    @property
    def hireable(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__hireable.needsLazyCompletion)
        return self.__hireable.value

    @property
    def organizations_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__organizations_url.needsLazyCompletion)
        return self.__organizations_url.value

    @property
    def received_events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__received_events_url.needsLazyCompletion)
        return self.__received_events_url.value

    @property
    def site_admin(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__site_admin.needsLazyCompletion)
        return self.__site_admin.value

    @property
    def starred_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__starred_url.needsLazyCompletion)
        return self.__starred_url.value

    @property
    def subscriptions_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__subscriptions_url.needsLazyCompletion)
        return self.__subscriptions_url.value

    def get_followers(self, per_page=None):
        """
        Calls the `GET /users/:user/followers <http://developer.github.com/v3/users/followers#list-followers-of-a-user>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.followers_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(User, self.Session, "GET", url, urlArguments=urlArguments)

    def get_following(self, per_page=None):
        """
        Calls the `GET /users/:user/following <http://developer.github.com/v3/users/followers#list-users-followed-by-another-user>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.following_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(User, self.Session, "GET", url, urlArguments=urlArguments)

    def get_keys(self):
        """
        Calls the `GET /users/:user/keys <http://developer.github.com/v3/users/keys#list-public-keys-for-a-user>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.PublicKey`
        """

        url = uritemplate.expand("https://api.github.com/users/{user}/keys", user=self.login)
        r = self.Session._request("GET", url)
        return [PyGithub.Blocking.PublicKey.PublicKey(self.Session, a) for a in r.json()]

    def get_orgs(self, per_page=None):
        """
        Calls the `GET /users/:user/orgs <http://developer.github.com/v3/orgs#list-user-organizations>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Organization`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.organizations_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.Organization.Organization, self.Session, "GET", url, urlArguments=urlArguments)

    def get_repo(self, repo):
        """
        Calls the `GET /repos/:owner/:repo <http://developer.github.com/v3/repos#get>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.get_repo`
          * :meth:`.Github.get_repo`
          * :meth:`.Organization.get_repo`

        :param repo: mandatory :class:`string`
        :rtype: :class:`.Repository`
        """

        repo = PyGithub.Blocking.Parameters.normalizeString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=self.login, repo=repo)
        r = self.Session._request("GET", url)
        return PyGithub.Blocking.Repository.Repository(self.Session, r.json(), r.headers.get("ETag"))

    def get_repos(self, sort=None, direction=None, type=None, per_page=None):
        """
        Calls the `GET /users/:user/repos <http://developer.github.com/v3/repos#list-user-repositories>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "created" or "updated" or "pushed" or "full_name"
        :param direction: optional "asc" or "desc"
        :param type: optional "all" or "owner" or "forks" or "sources" or "member"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if sort is not None:
            sort = PyGithub.Blocking.Parameters.normalizeEnum(sort, "created", "updated", "pushed", "full_name")
        if direction is not None:
            direction = PyGithub.Blocking.Parameters.normalizeEnum(direction, "asc", "desc")
        if type is not None:
            type = PyGithub.Blocking.Parameters.normalizeEnum(type, "all", "owner", "forks", "sources", "member")
        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.repos_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(sort=sort, direction=direction, type=type, per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.Repository.Repository, self.Session, "GET", url, urlArguments=urlArguments)

    def get_starred(self, sort=None, direction=None, per_page=None):
        """
        Calls the `GET /users/:user/starred <http://developer.github.com/v3/activity/starring#list-repositories-being-starred>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "created" or "updated"
        :param direction: optional "asc" or "desc"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if sort is not None:
            sort = PyGithub.Blocking.Parameters.normalizeEnum(sort, "created", "updated")
        if direction is not None:
            direction = PyGithub.Blocking.Parameters.normalizeEnum(direction, "asc", "desc")
        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.starred_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(sort=sort, direction=direction, per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.Repository.Repository, self.Session, "GET", url, urlArguments=urlArguments)

    def get_subscriptions(self, per_page=None):
        """
        Calls the `GET /users/:user/subscriptions <http://developer.github.com/v3/activity/watching#list-repositories-being-watched>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.subscriptions_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.Repository.Repository, self.Session, "GET", url, urlArguments=urlArguments)

    def has_in_following(self, target_user):
        """
        Calls the `GET /users/:user/following/:target_user <http://developer.github.com/v3/users/followers#check-if-one-user-follows-another>`__ end point.

        This is the only method calling this end point.

        :param target_user: mandatory :class:`.User` or :class:`string`
        :rtype: :class:`bool`
        """

        target_user = PyGithub.Blocking.Parameters.normalizeUser(target_user)

        url = uritemplate.expand(self.following_url, other_user=target_user)
        r = self.Session._request("GET", url, accept404=True)
        if r.status_code == 204:
            return True
        else:
            return False
