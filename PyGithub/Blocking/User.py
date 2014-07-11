# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.PaginatedList
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv

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
      * :attr:`.Issue.assignee`
      * :attr:`.Issue.closed_by`
      * :attr:`.Issue.user`
      * :attr:`.Milestone.creator`
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

    def _initAttributes(self, followers_url=rcv.Absent, following_url=rcv.Absent, gists_url=rcv.Absent, gravatar_id=rcv.Absent, hireable=rcv.Absent, organizations_url=rcv.Absent, received_events_url=rcv.Absent, site_admin=rcv.Absent, starred_url=rcv.Absent, subscriptions_url=rcv.Absent, bio=None, **kwds):
        super(User, self)._initAttributes(**kwds)
        self.__followers_url = rcv.Attribute("User.followers_url", rcv.StringConverter, followers_url)
        self.__following_url = rcv.Attribute("User.following_url", rcv.StringConverter, following_url)
        self.__gists_url = rcv.Attribute("User.gists_url", rcv.StringConverter, gists_url)
        self.__gravatar_id = rcv.Attribute("User.gravatar_id", rcv.StringConverter, gravatar_id)
        self.__hireable = rcv.Attribute("User.hireable", rcv.BoolConverter, hireable)
        self.__organizations_url = rcv.Attribute("User.organizations_url", rcv.StringConverter, organizations_url)
        self.__received_events_url = rcv.Attribute("User.received_events_url", rcv.StringConverter, received_events_url)
        self.__site_admin = rcv.Attribute("User.site_admin", rcv.BoolConverter, site_admin)
        self.__starred_url = rcv.Attribute("User.starred_url", rcv.StringConverter, starred_url)
        self.__subscriptions_url = rcv.Attribute("User.subscriptions_url", rcv.StringConverter, subscriptions_url)

    def _updateAttributes(self, eTag, followers_url=rcv.Absent, following_url=rcv.Absent, gists_url=rcv.Absent, gravatar_id=rcv.Absent, hireable=rcv.Absent, organizations_url=rcv.Absent, received_events_url=rcv.Absent, site_admin=rcv.Absent, starred_url=rcv.Absent, subscriptions_url=rcv.Absent, bio=None, **kwds):
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
        Calls the `GET /users/:username/followers <http://developer.github.com/v3/users/followers#list-followers-of-a-user>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.followers_url)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, User))(None, r)

    def get_following(self, per_page=None):
        """
        Calls the `GET /users/:username/following <http://developer.github.com/v3/users/followers#list-users-followed-by-another-user>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.following_url)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, User))(None, r)

    def get_keys(self):
        """
        Calls the `GET /users/:username/keys <http://developer.github.com/v3/users/keys#list-public-keys-for-a-user>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.PublicKey`
        """

        url = uritemplate.expand("https://api.github.com/users/{username}/keys", username=self.login)
        r = self.Session._request("GET", url)
        return rcv.ListConverter(rcv.StructureConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey))(None, r.json())

    def get_orgs(self, per_page=None):
        """
        Calls the `GET /users/:username/orgs <http://developer.github.com/v3/orgs#list-user-organizations>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Organization`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.organizations_url)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization))(None, r)

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

        repo = snd.normalizeString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=self.login, repo=repo)
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def get_repos(self, sort=None, direction=None, type=None, per_page=None):
        """
        Calls the `GET /users/:username/repos <http://developer.github.com/v3/repos#list-user-repositories>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "created" or "updated" or "pushed" or "full_name"
        :param direction: optional "asc" or "desc"
        :param type: optional "all" or "owner" or "forks" or "sources" or "member"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if sort is not None:
            sort = snd.normalizeEnum(sort, "created", "updated", "pushed", "full_name")
        if direction is not None:
            direction = snd.normalizeEnum(direction, "asc", "desc")
        if type is not None:
            type = snd.normalizeEnum(type, "all", "owner", "forks", "sources", "member")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.repos_url)
        urlArguments = snd.dictionary(sort=sort, direction=direction, type=type, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_starred(self, sort=None, direction=None, per_page=None):
        """
        Calls the `GET /users/:username/starred <http://developer.github.com/v3/activity/starring#list-repositories-being-starred>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "created" or "updated"
        :param direction: optional "asc" or "desc"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if sort is not None:
            sort = snd.normalizeEnum(sort, "created", "updated")
        if direction is not None:
            direction = snd.normalizeEnum(direction, "asc", "desc")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.starred_url)
        urlArguments = snd.dictionary(sort=sort, direction=direction, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_subscriptions(self, per_page=None):
        """
        Calls the `GET /users/:username/subscriptions <http://developer.github.com/v3/activity/watching#list-repositories-being-watched>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.subscriptions_url)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def has_in_following(self, target_user):
        """
        Calls the `GET /users/:username/following/:target_user <http://developer.github.com/v3/users/followers#check-if-one-user-follows-another>`__ end point.

        This is the only method calling this end point.

        :param target_user: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: :class:`bool`
        """

        target_user = snd.normalizeUserLogin(target_user)

        url = uritemplate.expand(self.following_url, other_user=target_user)
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)
