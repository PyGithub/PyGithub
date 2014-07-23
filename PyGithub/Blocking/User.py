# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv

import PyGithub.Blocking.Entity


class User(PyGithub.Blocking.Entity.Entity):
    """
    Base class: :class:`.Entity`

    Derived classes:
      * :class:`.AuthenticatedUser`
      * :class:`.Contributor`

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.get_followers`
      * :meth:`.AuthenticatedUser.get_following`
      * :attr:`.Commit.author`
      * :attr:`.Commit.committer`
      * :attr:`.Gist.owner`
      * :attr:`.Gist.user`
      * :attr:`.GistCommit.user`
      * :meth:`.Github.get_user`
      * :meth:`.Github.get_users`
      * :attr:`.HistoryElement.user`
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

    class Key(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.User.get_keys`
        """

        def _initAttributes(self, id=None, key=None, **kwds):
            super(User.Key, self)._initAttributes(**kwds)
            self.__id = _rcv.Attribute("User.Key.id", _rcv.IntConverter, id)
            self.__key = _rcv.Attribute("User.Key.key", _rcv.StringConverter, key)

        @property
        def id(self):
            """
            :type: :class:`int`
            """
            return self.__id.value

        @property
        def key(self):
            """
            :type: :class:`string`
            """
            return self.__key.value

    def _initAttributes(self, followers_url=_rcv.Absent, following_url=_rcv.Absent, gists_url=_rcv.Absent, gravatar_id=_rcv.Absent, hireable=_rcv.Absent, organizations_url=_rcv.Absent, received_events_url=_rcv.Absent, site_admin=_rcv.Absent, starred_url=_rcv.Absent, subscriptions_url=_rcv.Absent, bio=None, **kwds):
        super(User, self)._initAttributes(**kwds)
        self.__followers_url = _rcv.Attribute("User.followers_url", _rcv.StringConverter, followers_url)
        self.__following_url = _rcv.Attribute("User.following_url", _rcv.StringConverter, following_url)
        self.__gists_url = _rcv.Attribute("User.gists_url", _rcv.StringConverter, gists_url)
        self.__gravatar_id = _rcv.Attribute("User.gravatar_id", _rcv.StringConverter, gravatar_id)
        self.__hireable = _rcv.Attribute("User.hireable", _rcv.BoolConverter, hireable)
        self.__organizations_url = _rcv.Attribute("User.organizations_url", _rcv.StringConverter, organizations_url)
        self.__received_events_url = _rcv.Attribute("User.received_events_url", _rcv.StringConverter, received_events_url)
        self.__site_admin = _rcv.Attribute("User.site_admin", _rcv.BoolConverter, site_admin)
        self.__starred_url = _rcv.Attribute("User.starred_url", _rcv.StringConverter, starred_url)
        self.__subscriptions_url = _rcv.Attribute("User.subscriptions_url", _rcv.StringConverter, subscriptions_url)

    def _updateAttributes(self, eTag, followers_url=_rcv.Absent, following_url=_rcv.Absent, gists_url=_rcv.Absent, gravatar_id=_rcv.Absent, hireable=_rcv.Absent, organizations_url=_rcv.Absent, received_events_url=_rcv.Absent, site_admin=_rcv.Absent, starred_url=_rcv.Absent, subscriptions_url=_rcv.Absent, bio=None, **kwds):
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
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.followers_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, User))(None, r)

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
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.following_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, User))(None, r)

    def get_gists(self, since=None, per_page=None):
        """
        Calls the `GET /users/:username/gists <http://developer.github.com/v3/gists#list-gists>`__ end point.

        This is the only method calling this end point.

        :param since: optional :class:`datetime`
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Gist`
        """
        import PyGithub.Blocking.Gist

        if since is not None:
            since = _snd.normalizeDatetime(since)
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.gists_url)
        urlArguments = _snd.dictionary(per_page=per_page, since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist))(None, r)

    def get_keys(self):
        """
        Calls the `GET /users/:username/keys <http://developer.github.com/v3/users/keys#list-public-keys-for-a-user>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.Key`
        """

        url = uritemplate.expand("https://api.github.com/users/{username}/keys", username=self.login)
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.StructureConverter(self.Session, User.Key))(None, r.json())

    def get_orgs(self, per_page=None):
        """
        Calls the `GET /users/:username/orgs <http://developer.github.com/v3/orgs#list-user-organizations>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Organization`
        """
        import PyGithub.Blocking.Organization

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.organizations_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization))(None, r)

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
        import PyGithub.Blocking.Repository

        repo = _snd.normalizeString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=self.login, repo=repo)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def get_repos(self, type=None, sort=None, direction=None, per_page=None):
        """
        Calls the `GET /users/:username/repos <http://developer.github.com/v3/repos#list-user-repositories>`__ end point.

        This is the only method calling this end point.

        :param type: optional "all" or "forks" or "member" or "owner" or "sources"
        :param sort: optional "created" or "full_name" or "pushed" or "updated"
        :param direction: optional "asc" or "desc"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if type is not None:
            type = _snd.normalizeEnum(type, "all", "forks", "member", "owner", "sources")
        if sort is not None:
            sort = _snd.normalizeEnum(sort, "created", "full_name", "pushed", "updated")
        if direction is not None:
            direction = _snd.normalizeEnum(direction, "asc", "desc")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.repos_url)
        urlArguments = _snd.dictionary(direction=direction, per_page=per_page, sort=sort, type=type)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_starred(self, sort=None, direction=None, per_page=None):
        """
        Calls the `GET /users/:username/starred <http://developer.github.com/v3/activity/starring#list-repositories-being-starred>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "created" or "updated"
        :param direction: optional "asc" or "desc"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if sort is not None:
            sort = _snd.normalizeEnum(sort, "created", "updated")
        if direction is not None:
            direction = _snd.normalizeEnum(direction, "asc", "desc")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.starred_url)
        urlArguments = _snd.dictionary(direction=direction, per_page=per_page, sort=sort)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_subscriptions(self, per_page=None):
        """
        Calls the `GET /users/:username/subscriptions <http://developer.github.com/v3/activity/watching#list-repositories-being-watched>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.subscriptions_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def has_in_following(self, target_user):
        """
        Calls the `GET /users/:username/following/:target_user <http://developer.github.com/v3/users/followers#check-if-one-user-follows-another>`__ end point.

        This is the only method calling this end point.

        :param target_user: mandatory :class:`.User` or :class:`string` (its :attr:`.Entity.login`)
        :rtype: :class:`bool`
        """

        target_user = _snd.normalizeUserLogin(target_user)

        url = uritemplate.expand(self.following_url, other_user=target_user)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)
