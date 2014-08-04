# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class User(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes:
      * :class:`.Contributor`

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.get_followers`
      * :meth:`.AuthenticatedUser.get_following`
      * :attr:`.Commit.author`
      * :attr:`.Commit.committer`
      * :attr:`.Gist.Commit.user`
      * :attr:`.Gist.HistoryElement.user`
      * :attr:`.Gist.owner`
      * :attr:`.Gist.user`
      * :meth:`.Github.get_user`
      * :meth:`.Github.get_users`
      * :attr:`.Issue.assignee`
      * :attr:`.Issue.closed_by`
      * :attr:`.Issue.user`
      * :attr:`.Milestone.creator`
      * :meth:`.Organization.get_members`
      * :meth:`.Organization.get_public_members`
      * :attr:`.PullRequest.End.user`
      * :attr:`.PullRequest.assignee`
      * :attr:`.PullRequest.merged_by`
      * :attr:`.PullRequest.user`
      * :meth:`.Repository.get_assignees`
      * :meth:`.Repository.get_collaborators`
      * :meth:`.Repository.get_stargazers`
      * :meth:`.Repository.get_subscribers`
      * :attr:`.Repository.owner`
      * :meth:`.Team.get_members`
      * :meth:`.User.get_followers`
      * :meth:`.User.get_following`

    Methods accepting instances of this class as parameter:
      * :meth:`.AuthenticatedUser.add_to_following`
      * :meth:`.AuthenticatedUser.has_in_following`
      * :meth:`.AuthenticatedUser.remove_from_following`
      * :meth:`.Github.get_users`
      * :meth:`.Issue.edit`
      * :meth:`.Organization.has_in_members`
      * :meth:`.Organization.has_in_public_members`
      * :meth:`.Organization.remove_from_members`
      * :meth:`.Organization.remove_from_public_members`
      * :meth:`.Repository.add_to_collaborators`
      * :meth:`.Repository.create_issue`
      * :meth:`.Repository.get_commits`
      * :meth:`.Repository.get_issues`
      * :meth:`.Repository.has_in_assignees`
      * :meth:`.Repository.has_in_collaborators`
      * :meth:`.Repository.remove_from_collaborators`
      * :meth:`.Team.add_to_members`
      * :meth:`.Team.has_in_members`
      * :meth:`.Team.remove_from_members`
      * :meth:`.User.has_in_following`
    """

    class Key(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.User.get_keys`

        Methods accepting instances of this class as parameter: none.
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

    class Plan(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.AuthenticatedUser.plan`
          * :attr:`.Organization.plan`
          * :attr:`.User.plan`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, collaborators=None, name=None, private_repos=None, space=None, **kwds):
            super(User.Plan, self)._initAttributes(**kwds)
            self.__collaborators = _rcv.Attribute("User.Plan.collaborators", _rcv.IntConverter, collaborators)
            self.__name = _rcv.Attribute("User.Plan.name", _rcv.StringConverter, name)
            self.__private_repos = _rcv.Attribute("User.Plan.private_repos", _rcv.IntConverter, private_repos)
            self.__space = _rcv.Attribute("User.Plan.space", _rcv.IntConverter, space)

        def _updateAttributes(self, collaborators=None, name=None, private_repos=None, space=None, **kwds):
            super(User.Plan, self)._updateAttributes(**kwds)
            self.__collaborators.update(collaborators)
            self.__name.update(name)
            self.__private_repos.update(private_repos)
            self.__space.update(space)

        @property
        def collaborators(self):
            """
            :type: :class:`int`
            """
            return self.__collaborators.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

        @property
        def private_repos(self):
            """
            :type: :class:`int`
            """
            return self.__private_repos.value

        @property
        def space(self):
            """
            :type: :class:`int`
            """
            return self.__space.value

    def _initAttributes(self, avatar_url=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, followers_url=_rcv.Absent, following=_rcv.Absent, following_url=_rcv.Absent, gists_url=_rcv.Absent, gravatar_id=_rcv.Absent, hireable=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, name=_rcv.Absent, organizations_url=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_repos=_rcv.Absent, received_events_url=_rcv.Absent, repos_url=_rcv.Absent, site_admin=_rcv.Absent, starred_url=_rcv.Absent, subscriptions_url=_rcv.Absent, suspended_at=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, bio=None, **kwds):
        super(User, self)._initAttributes(**kwds)
        self.__avatar_url = _rcv.Attribute("User.avatar_url", _rcv.StringConverter, avatar_url)
        self.__blog = _rcv.Attribute("User.blog", _rcv.StringConverter, blog)
        self.__collaborators = _rcv.Attribute("User.collaborators", _rcv.IntConverter, collaborators)
        self.__company = _rcv.Attribute("User.company", _rcv.StringConverter, company)
        self.__created_at = _rcv.Attribute("User.created_at", _rcv.DatetimeConverter, created_at)
        self.__disk_usage = _rcv.Attribute("User.disk_usage", _rcv.IntConverter, disk_usage)
        self.__email = _rcv.Attribute("User.email", _rcv.StringConverter, email)
        self.__events_url = _rcv.Attribute("User.events_url", _rcv.StringConverter, events_url)
        self.__followers = _rcv.Attribute("User.followers", _rcv.IntConverter, followers)
        self.__followers_url = _rcv.Attribute("User.followers_url", _rcv.StringConverter, followers_url)
        self.__following = _rcv.Attribute("User.following", _rcv.IntConverter, following)
        self.__following_url = _rcv.Attribute("User.following_url", _rcv.StringConverter, following_url)
        self.__gists_url = _rcv.Attribute("User.gists_url", _rcv.StringConverter, gists_url)
        self.__gravatar_id = _rcv.Attribute("User.gravatar_id", _rcv.StringConverter, gravatar_id)
        self.__hireable = _rcv.Attribute("User.hireable", _rcv.BoolConverter, hireable)
        self.__html_url = _rcv.Attribute("User.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("User.id", _rcv.IntConverter, id)
        self.__location = _rcv.Attribute("User.location", _rcv.StringConverter, location)
        self.__login = _rcv.Attribute("User.login", _rcv.StringConverter, login)
        self.__name = _rcv.Attribute("User.name", _rcv.StringConverter, name)
        self.__organizations_url = _rcv.Attribute("User.organizations_url", _rcv.StringConverter, organizations_url)
        self.__owned_private_repos = _rcv.Attribute("User.owned_private_repos", _rcv.IntConverter, owned_private_repos)
        self.__plan = _rcv.Attribute("User.plan", _rcv.StructureConverter(self.Session, User.Plan), plan)
        self.__private_gists = _rcv.Attribute("User.private_gists", _rcv.IntConverter, private_gists)
        self.__public_gists = _rcv.Attribute("User.public_gists", _rcv.IntConverter, public_gists)
        self.__public_repos = _rcv.Attribute("User.public_repos", _rcv.IntConverter, public_repos)
        self.__received_events_url = _rcv.Attribute("User.received_events_url", _rcv.StringConverter, received_events_url)
        self.__repos_url = _rcv.Attribute("User.repos_url", _rcv.StringConverter, repos_url)
        self.__site_admin = _rcv.Attribute("User.site_admin", _rcv.BoolConverter, site_admin)
        self.__starred_url = _rcv.Attribute("User.starred_url", _rcv.StringConverter, starred_url)
        self.__subscriptions_url = _rcv.Attribute("User.subscriptions_url", _rcv.StringConverter, subscriptions_url)
        self.__suspended_at = _rcv.Attribute("User.suspended_at", _rcv.DatetimeConverter, suspended_at)
        self.__total_private_repos = _rcv.Attribute("User.total_private_repos", _rcv.IntConverter, total_private_repos)
        self.__type = _rcv.Attribute("User.type", _rcv.StringConverter, type)
        self.__updated_at = _rcv.Attribute("User.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, avatar_url=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, followers_url=_rcv.Absent, following=_rcv.Absent, following_url=_rcv.Absent, gists_url=_rcv.Absent, gravatar_id=_rcv.Absent, hireable=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, name=_rcv.Absent, organizations_url=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_repos=_rcv.Absent, received_events_url=_rcv.Absent, repos_url=_rcv.Absent, site_admin=_rcv.Absent, starred_url=_rcv.Absent, subscriptions_url=_rcv.Absent, suspended_at=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, bio=None, **kwds):
        super(User, self)._updateAttributes(eTag, **kwds)
        self.__avatar_url.update(avatar_url)
        self.__blog.update(blog)
        self.__collaborators.update(collaborators)
        self.__company.update(company)
        self.__created_at.update(created_at)
        self.__disk_usage.update(disk_usage)
        self.__email.update(email)
        self.__events_url.update(events_url)
        self.__followers.update(followers)
        self.__followers_url.update(followers_url)
        self.__following.update(following)
        self.__following_url.update(following_url)
        self.__gists_url.update(gists_url)
        self.__gravatar_id.update(gravatar_id)
        self.__hireable.update(hireable)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__location.update(location)
        self.__login.update(login)
        self.__name.update(name)
        self.__organizations_url.update(organizations_url)
        self.__owned_private_repos.update(owned_private_repos)
        self.__plan.update(plan)
        self.__private_gists.update(private_gists)
        self.__public_gists.update(public_gists)
        self.__public_repos.update(public_repos)
        self.__received_events_url.update(received_events_url)
        self.__repos_url.update(repos_url)
        self.__site_admin.update(site_admin)
        self.__starred_url.update(starred_url)
        self.__subscriptions_url.update(subscriptions_url)
        self.__suspended_at.update(suspended_at)
        self.__total_private_repos.update(total_private_repos)
        self.__type.update(type)
        self.__updated_at.update(updated_at)

    @property
    def avatar_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__avatar_url.needsLazyCompletion)
        return self.__avatar_url.value

    @property
    def blog(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__blog.needsLazyCompletion)
        return self.__blog.value

    @property
    def collaborators(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__collaborators.needsLazyCompletion)
        return self.__collaborators.value

    @property
    def company(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__company.needsLazyCompletion)
        return self.__company.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def disk_usage(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__disk_usage.needsLazyCompletion)
        return self.__disk_usage.value

    @property
    def email(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__email.needsLazyCompletion)
        return self.__email.value

    @property
    def events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__events_url.needsLazyCompletion)
        return self.__events_url.value

    @property
    def followers(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__followers.needsLazyCompletion)
        return self.__followers.value

    @property
    def followers_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__followers_url.needsLazyCompletion)
        return self.__followers_url.value

    @property
    def following(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__following.needsLazyCompletion)
        return self.__following.value

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
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def location(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__location.needsLazyCompletion)
        return self.__location.value

    @property
    def login(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__login.needsLazyCompletion)
        return self.__login.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def organizations_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__organizations_url.needsLazyCompletion)
        return self.__organizations_url.value

    @property
    def owned_private_repos(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__owned_private_repos.needsLazyCompletion)
        return self.__owned_private_repos.value

    @property
    def plan(self):
        """
        :type: :class:`.User.Plan`
        """
        self._completeLazily(self.__plan.needsLazyCompletion)
        return self.__plan.value

    @property
    def private_gists(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__private_gists.needsLazyCompletion)
        return self.__private_gists.value

    @property
    def public_gists(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__public_gists.needsLazyCompletion)
        return self.__public_gists.value

    @property
    def public_repos(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__public_repos.needsLazyCompletion)
        return self.__public_repos.value

    @property
    def received_events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__received_events_url.needsLazyCompletion)
        return self.__received_events_url.value

    @property
    def repos_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__repos_url.needsLazyCompletion)
        return self.__repos_url.value

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

    @property
    def suspended_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__suspended_at.needsLazyCompletion)
        return self.__suspended_at.value

    @property
    def total_private_repos(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__total_private_repos.needsLazyCompletion)
        return self.__total_private_repos.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

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

        :rtype: :class:`list` of :class:`.User.Key`
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

        :param target_user: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`) or :class:`.AuthenticatedUser` or :class:`string` (its :attr:`.AuthenticatedUser.login`)
        :rtype: :class:`bool`
        """

        target_user = _snd.normalizeUserLoginAuthenticatedUserLogin(target_user)

        url = uritemplate.expand(self.following_url, other_user=target_user)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)
