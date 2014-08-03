# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class AuthenticatedUser(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Github.get_authenticated_user`

    Methods accepting instances of this class as parameter:
      * :meth:`.Issue.edit`
      * :meth:`.Organization.add_to_public_members`
      * :meth:`.Organization.has_in_members`
      * :meth:`.Organization.has_in_public_members`
      * :meth:`.Organization.remove_from_members`
      * :meth:`.Organization.remove_from_public_members`
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

    class Email(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.AuthenticatedUser.get_emails`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, email=None, primary=None, verified=None, **kwds):
            super(AuthenticatedUser.Email, self)._initAttributes(**kwds)
            self.__email = _rcv.Attribute("AuthenticatedUser.Email.email", _rcv.StringConverter, email)
            self.__primary = _rcv.Attribute("AuthenticatedUser.Email.primary", _rcv.BoolConverter, primary)
            self.__verified = _rcv.Attribute("AuthenticatedUser.Email.verified", _rcv.BoolConverter, verified)

        @property
        def email(self):
            """
            :type: :class:`string`
            """
            return self.__email.value

        @property
        def primary(self):
            """
            :type: :class:`bool`
            """
            return self.__primary.value

        @property
        def verified(self):
            """
            :type: :class:`bool`
            """
            return self.__verified.value

    def _initAttributes(self, avatar_url=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, followers_url=_rcv.Absent, following=_rcv.Absent, following_url=_rcv.Absent, gists_url=_rcv.Absent, gravatar_id=_rcv.Absent, hireable=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, name=_rcv.Absent, organizations_url=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_repos=_rcv.Absent, received_events_url=_rcv.Absent, repos_url=_rcv.Absent, site_admin=_rcv.Absent, starred_url=_rcv.Absent, subscriptions_url=_rcv.Absent, suspended_at=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, bio=None, **kwds):
        import PyGithub.Blocking.User
        super(AuthenticatedUser, self)._initAttributes(**kwds)
        self.__avatar_url = _rcv.Attribute("AuthenticatedUser.avatar_url", _rcv.StringConverter, avatar_url)
        self.__blog = _rcv.Attribute("AuthenticatedUser.blog", _rcv.StringConverter, blog)
        self.__collaborators = _rcv.Attribute("AuthenticatedUser.collaborators", _rcv.IntConverter, collaborators)
        self.__company = _rcv.Attribute("AuthenticatedUser.company", _rcv.StringConverter, company)
        self.__created_at = _rcv.Attribute("AuthenticatedUser.created_at", _rcv.DatetimeConverter, created_at)
        self.__disk_usage = _rcv.Attribute("AuthenticatedUser.disk_usage", _rcv.IntConverter, disk_usage)
        self.__email = _rcv.Attribute("AuthenticatedUser.email", _rcv.StringConverter, email)
        self.__events_url = _rcv.Attribute("AuthenticatedUser.events_url", _rcv.StringConverter, events_url)
        self.__followers = _rcv.Attribute("AuthenticatedUser.followers", _rcv.IntConverter, followers)
        self.__followers_url = _rcv.Attribute("AuthenticatedUser.followers_url", _rcv.StringConverter, followers_url)
        self.__following = _rcv.Attribute("AuthenticatedUser.following", _rcv.IntConverter, following)
        self.__following_url = _rcv.Attribute("AuthenticatedUser.following_url", _rcv.StringConverter, following_url)
        self.__gists_url = _rcv.Attribute("AuthenticatedUser.gists_url", _rcv.StringConverter, gists_url)
        self.__gravatar_id = _rcv.Attribute("AuthenticatedUser.gravatar_id", _rcv.StringConverter, gravatar_id)
        self.__hireable = _rcv.Attribute("AuthenticatedUser.hireable", _rcv.BoolConverter, hireable)
        self.__html_url = _rcv.Attribute("AuthenticatedUser.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("AuthenticatedUser.id", _rcv.IntConverter, id)
        self.__location = _rcv.Attribute("AuthenticatedUser.location", _rcv.StringConverter, location)
        self.__login = _rcv.Attribute("AuthenticatedUser.login", _rcv.StringConverter, login)
        self.__name = _rcv.Attribute("AuthenticatedUser.name", _rcv.StringConverter, name)
        self.__organizations_url = _rcv.Attribute("AuthenticatedUser.organizations_url", _rcv.StringConverter, organizations_url)
        self.__owned_private_repos = _rcv.Attribute("AuthenticatedUser.owned_private_repos", _rcv.IntConverter, owned_private_repos)
        self.__plan = _rcv.Attribute("AuthenticatedUser.plan", _rcv.StructureConverter(self.Session, PyGithub.Blocking.User.User.Plan), plan)
        self.__private_gists = _rcv.Attribute("AuthenticatedUser.private_gists", _rcv.IntConverter, private_gists)
        self.__public_gists = _rcv.Attribute("AuthenticatedUser.public_gists", _rcv.IntConverter, public_gists)
        self.__public_repos = _rcv.Attribute("AuthenticatedUser.public_repos", _rcv.IntConverter, public_repos)
        self.__received_events_url = _rcv.Attribute("AuthenticatedUser.received_events_url", _rcv.StringConverter, received_events_url)
        self.__repos_url = _rcv.Attribute("AuthenticatedUser.repos_url", _rcv.StringConverter, repos_url)
        self.__site_admin = _rcv.Attribute("AuthenticatedUser.site_admin", _rcv.BoolConverter, site_admin)
        self.__starred_url = _rcv.Attribute("AuthenticatedUser.starred_url", _rcv.StringConverter, starred_url)
        self.__subscriptions_url = _rcv.Attribute("AuthenticatedUser.subscriptions_url", _rcv.StringConverter, subscriptions_url)
        self.__suspended_at = _rcv.Attribute("AuthenticatedUser.suspended_at", _rcv.DatetimeConverter, suspended_at)
        self.__total_private_repos = _rcv.Attribute("AuthenticatedUser.total_private_repos", _rcv.IntConverter, total_private_repos)
        self.__type = _rcv.Attribute("AuthenticatedUser.type", _rcv.StringConverter, type)
        self.__updated_at = _rcv.Attribute("AuthenticatedUser.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, avatar_url=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, followers_url=_rcv.Absent, following=_rcv.Absent, following_url=_rcv.Absent, gists_url=_rcv.Absent, gravatar_id=_rcv.Absent, hireable=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, name=_rcv.Absent, organizations_url=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_repos=_rcv.Absent, received_events_url=_rcv.Absent, repos_url=_rcv.Absent, site_admin=_rcv.Absent, starred_url=_rcv.Absent, subscriptions_url=_rcv.Absent, suspended_at=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, bio=None, **kwds):
        super(AuthenticatedUser, self)._updateAttributes(eTag, **kwds)
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

    def add_to_emails(self, *email):
        """
        Calls the `POST /user/emails <http://developer.github.com/v3/users/emails#add-email-addresses>`__ end point.

        This is the only method calling this end point.

        :param email: mandatory :class:`string`
        :rtype: None
        """

        email = _snd.normalizeList(_snd.normalizeString, email)

        url = uritemplate.expand("https://api.github.com/user/emails")
        postArguments = email
        r = self.Session._request("POST", url, postArguments=postArguments)

    def add_to_following(self, username):
        """
        Calls the `PUT /user/following/:username <http://developer.github.com/v3/users/followers#follow-a-user>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand("https://api.github.com/user/following/{username}", username=username)
        r = self.Session._request("PUT", url)

    def add_to_starred(self, repo):
        """
        Calls the `PUT /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring#star-a-repository>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: None
        """

        repo = _snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/starred/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("PUT", url)

    def add_to_starred_gists(self, gist):
        """
        Calls the `PUT /gists/:id/star <http://developer.github.com/v3/gists#star-a-gist>`__ end point.

        This is the only method calling this end point.

        :param gist: mandatory :class:`.Gist` or :class:`string` (its :attr:`.Gist.id`)
        :rtype: None
        """

        gist = _snd.normalizeGistId(gist)

        url = uritemplate.expand("https://api.github.com/gists/{id}/star", id=gist)
        r = self.Session._request("PUT", url)

    def create_fork(self, repo):
        """
        Calls the `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks#create-a-fork>`__ end point.

        The following methods also call this end point:
          * :meth:`.Organization.create_fork`

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        repo = _snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/forks", owner=repo[0], repo=repo[1])
        r = self.Session._request("POST", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def create_gist(self, files, description=None, public=None):
        """
        Calls the `POST /gists <http://developer.github.com/v3/gists#create-a-gist>`__ end point.

        The following methods also call this end point:
          * :meth:`.Github.create_anonymous_gist`

        :param files: mandatory :class:`bool`
        :param description: optional :class:`string`
        :param public: optional :class:`bool`
        :rtype: :class:`.Gist`
        """
        import PyGithub.Blocking.Gist

        if description is not None:
            description = _snd.normalizeString(description)
        if public is not None:
            public = _snd.normalizeBool(public)

        url = uritemplate.expand("https://api.github.com/gists")
        postArguments = _snd.dictionary(description=description, files=files, public=public)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist)(None, r.json(), r.headers.get("ETag"))

    def create_gist_fork(self, gist):
        """
        Calls the `POST /gists/:id/forks <http://developer.github.com/v3/gists#fork-a-gist>`__ end point.

        This is the only method calling this end point.

        :param gist: mandatory :class:`.Gist` or :class:`string` (its :attr:`.Gist.id`)
        :rtype: :class:`.Gist`
        """
        import PyGithub.Blocking.Gist

        gist = _snd.normalizeGistId(gist)

        url = uritemplate.expand("https://api.github.com/gists/{id}/forks", id=gist)
        r = self.Session._request("POST", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist)(None, r.json(), r.headers.get("ETag"))

    def create_key(self, title, key):
        """
        Calls the `POST /user/keys <http://developer.github.com/v3/users/keys#create-a-public-key>`__ end point.

        This is the only method calling this end point.

        :param title: mandatory :class:`string`
        :param key: mandatory :class:`string`
        :rtype: :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        title = _snd.normalizeString(title)
        key = _snd.normalizeString(key)

        url = uritemplate.expand("https://api.github.com/user/keys")
        postArguments = _snd.dictionary(key=key, title=title)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey)(None, r.json(), r.headers.get("ETag"))

    def create_repo(self, name, description=None, homepage=None, private=None, has_issues=None, has_wiki=None, auto_init=None, gitignore_template=None, license_template=None):
        """
        Calls the `POST /user/repos <http://developer.github.com/v3/repos#create>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param description: optional :class:`string`
        :param homepage: optional :class:`string`
        :param private: optional :class:`bool`
        :param has_issues: optional :class:`bool`
        :param has_wiki: optional :class:`bool`
        :param auto_init: optional :class:`bool`
        :param gitignore_template: optional :class:`.Github.GitIgnoreTemplate` or :class:`string` (its :attr:`.Github.GitIgnoreTemplate.name`)
        :param license_template: optional :class:`string`
        :rtype: :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        name = _snd.normalizeString(name)
        if description is not None:
            description = _snd.normalizeString(description)
        if homepage is not None:
            homepage = _snd.normalizeString(homepage)
        if private is not None:
            private = _snd.normalizeBool(private)
        if has_issues is not None:
            has_issues = _snd.normalizeBool(has_issues)
        if has_wiki is not None:
            has_wiki = _snd.normalizeBool(has_wiki)
        if auto_init is not None:
            auto_init = _snd.normalizeBool(auto_init)
        if gitignore_template is not None:
            gitignore_template = _snd.normalizeGitIgnoreTemplateName(gitignore_template)
        if license_template is not None:
            license_template = _snd.normalizeString(license_template)

        url = uritemplate.expand("https://api.github.com/user/repos")
        postArguments = _snd.dictionary(auto_init=auto_init, description=description, gitignore_template=gitignore_template, has_issues=has_issues, has_wiki=has_wiki, homepage=homepage, license_template=license_template, name=name, private=private)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def create_subscription(self, repo, subscribed, ignored):
        """
        Calls the `PUT /repos/:owner/:repo/subscription <http://developer.github.com/v3/activity/watching#set-a-repository-subscription>`__ end point.

        The following methods also call this end point:
          * :meth:`.Subscription.edit`

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :param subscribed: mandatory :class:`bool`
        :param ignored: mandatory :class:`bool`
        :rtype: :class:`.Subscription`
        """
        import PyGithub.Blocking.Subscription

        repo = _snd.normalizeRepositoryFullName(repo)
        subscribed = _snd.normalizeBool(subscribed)
        ignored = _snd.normalizeBool(ignored)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/subscription", owner=repo[0], repo=repo[1])
        postArguments = _snd.dictionary(ignored=ignored, subscribed=subscribed)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Subscription.Subscription)(None, r.json(), r.headers.get("ETag"))

    def edit(self, name=None, email=None, blog=None, company=None, location=None, hireable=None):
        """
        Calls the `PATCH /user <http://developer.github.com/v3/users#update-the-authenticated-user>`__ end point.

        This is the only method calling this end point.

        :param name: optional :class:`string` or :class:`Reset`
        :param email: optional :class:`string` or :class:`Reset`
        :param blog: optional :class:`string` or :class:`Reset`
        :param company: optional :class:`string` or :class:`Reset`
        :param location: optional :class:`string` or :class:`Reset`
        :param hireable: optional :class:`bool` or :class:`Reset`
        :rtype: None
        """

        if name is not None:
            name = _snd.normalizeStringReset(name)
        if email is not None:
            email = _snd.normalizeStringReset(email)
        if blog is not None:
            blog = _snd.normalizeStringReset(blog)
        if company is not None:
            company = _snd.normalizeStringReset(company)
        if location is not None:
            location = _snd.normalizeStringReset(location)
        if hireable is not None:
            hireable = _snd.normalizeBoolReset(hireable)

        url = uritemplate.expand("https://api.github.com/user")
        postArguments = _snd.dictionary(blog=blog, company=company, email=email, hireable=hireable, location=location, name=name)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_emails(self):
        """
        Calls the `GET /user/emails <http://developer.github.com/v3/users/emails#list-email-addresses-for-a-user>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.AuthenticatedUser.Email`
        """

        url = uritemplate.expand("https://api.github.com/user/emails")
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.StructureConverter(self.Session, AuthenticatedUser.Email))(None, r.json())

    def get_followers(self, per_page=None):
        """
        Calls the `GET /user/followers <http://developer.github.com/v3/users/followers#list-followers-of-a-user>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/followers")
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_following(self, per_page=None):
        """
        Calls the `GET /user/following <http://developer.github.com/v3/users/followers#list-users-followed-by-another-user>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/following")
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_gists(self, since=None, per_page=None):
        """
        Calls the `GET /gists <http://developer.github.com/v3/gists#list-gists>`__ end point.

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

        url = uritemplate.expand("https://api.github.com/gists")
        urlArguments = _snd.dictionary(per_page=per_page, since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist))(None, r)

    def get_issues(self, filter=None, state=None, labels=None, sort=None, direction=None, since=None, per_page=None):
        """
        Calls the `GET /user/issues <http://developer.github.com/v3/issues#list-issues>`__ end point.

        This is the only method calling this end point.

        :param filter: optional "all" or "assigned" or "created" or "mentioned" or "subscribed"
        :param state: optional "all" or "closed" or "open"
        :param labels: optional :class:`list` of :class:`.Label` or :class:`string` (its :attr:`.Label.name`)
        :param sort: optional "comments" or "created" or "updated"
        :param direction: optional "asc" or "desc"
        :param since: optional :class:`datetime`
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Issue`
        """
        import PyGithub.Blocking.Issue

        if filter is not None:
            filter = _snd.normalizeEnum(filter, "all", "assigned", "created", "mentioned", "subscribed")
        if state is not None:
            state = _snd.normalizeEnum(state, "all", "closed", "open")
        if labels is not None:
            labels = _snd.normalizeList(_snd.normalizeLabelName, labels)
        if sort is not None:
            sort = _snd.normalizeEnum(sort, "comments", "created", "updated")
        if direction is not None:
            direction = _snd.normalizeEnum(direction, "asc", "desc")
        if since is not None:
            since = _snd.normalizeDatetime(since)
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/issues")
        urlArguments = _snd.dictionary(direction=direction, filter=filter, labels=labels, per_page=per_page, since=since, sort=sort, state=state)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Issue.Issue))(None, r)

    def get_key(self, id):
        """
        Calls the `GET /user/keys/:id <http://developer.github.com/v3/users/keys#get-a-single-public-key>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        id = _snd.normalizeInt(id)

        url = uritemplate.expand("https://api.github.com/user/keys/{id}", id=str(id))
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey)(None, r.json(), r.headers.get("ETag"))

    def get_keys(self):
        """
        Calls the `GET /user/keys <http://developer.github.com/v3/users/keys#list-your-public-keys>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        url = uritemplate.expand("https://api.github.com/user/keys")
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.ClassConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey))(None, r.json())

    def get_orgs(self, per_page=None):
        """
        Calls the `GET /user/orgs <http://developer.github.com/v3/orgs#list-user-organizations>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Organization`
        """
        import PyGithub.Blocking.Organization

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/orgs")
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization))(None, r)

    def get_repo(self, repo):
        """
        Calls the `GET /repos/:owner/:repo <http://developer.github.com/v3/repos#get>`__ end point.

        The following methods also call this end point:
          * :meth:`.Github.get_repo`
          * :meth:`.Organization.get_repo`
          * :meth:`.User.get_repo`

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
        Calls the `GET /user/repos <http://developer.github.com/v3/repos#list-your-repositories>`__ end point.

        This is the only method calling this end point.

        :param type: optional "all" or "member" or "owner" or "private" or "public"
        :param sort: optional "created" or "full_name" or "pushed" or "updated"
        :param direction: optional "asc" or "desc"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if type is not None:
            type = _snd.normalizeEnum(type, "all", "member", "owner", "private", "public")
        if sort is not None:
            sort = _snd.normalizeEnum(sort, "created", "full_name", "pushed", "updated")
        if direction is not None:
            direction = _snd.normalizeEnum(direction, "asc", "desc")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/repos")
        urlArguments = _snd.dictionary(direction=direction, per_page=per_page, sort=sort, type=type)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_starred(self, sort=None, direction=None, per_page=None):
        """
        Calls the `GET /user/starred <http://developer.github.com/v3/activity/starring#list-repositories-being-starred>`__ end point.

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

        url = uritemplate.expand("https://api.github.com/user/starred")
        urlArguments = _snd.dictionary(direction=direction, per_page=per_page, sort=sort)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_starred_gists(self, since=None, per_page=None):
        """
        Calls the `GET /gists/starred <http://developer.github.com/v3/gists#list-gists>`__ end point.

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

        url = uritemplate.expand("https://api.github.com/gists/starred")
        urlArguments = _snd.dictionary(per_page=per_page, since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist))(None, r)

    def get_subscription(self, repo):
        """
        Calls the `GET /repos/:owner/:repo/subscription <http://developer.github.com/v3/activity/watching#get-a-repository-subscription>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: :class:`.Subscription`
        """
        import PyGithub.Blocking.Subscription

        repo = _snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/subscription", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Subscription.Subscription)(None, r.json(), r.headers.get("ETag"))

    def get_subscriptions(self, per_page=None):
        """
        Calls the `GET /user/subscriptions <http://developer.github.com/v3/activity/watching#list-repositories-being-watched>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/subscriptions")
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_teams(self, per_page=None):
        """
        Calls the `GET /user/teams <http://developer.github.com/v3/orgs/teams#list-user-teams>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Team`
        """
        import PyGithub.Blocking.Team

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/teams")
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team))(None, r)

    def has_in_following(self, username):
        """
        Calls the `GET /user/following/:username <http://developer.github.com/v3/users/followers#check-if-you-are-following-a-user>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: :class:`bool`
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand("https://api.github.com/user/following/{username}", username=username)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def has_in_starred(self, repo):
        """
        Calls the `GET /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring#check-if-you-are-starring-a-repository>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: :class:`bool`
        """

        repo = _snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/starred/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def has_in_starred_gists(self, gist):
        """
        Calls the `GET /gists/:id/star <http://developer.github.com/v3/gists#check-if-a-gist-is-starred>`__ end point.

        This is the only method calling this end point.

        :param gist: mandatory :class:`.Gist` or :class:`string` (its :attr:`.Gist.id`)
        :rtype: :class:`bool`
        """

        gist = _snd.normalizeGistId(gist)

        url = uritemplate.expand("https://api.github.com/gists/{id}/star", id=gist)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def remove_from_emails(self, *email):
        """
        Calls the `DELETE /user/emails <http://developer.github.com/v3/users/emails#delete-email-addresses>`__ end point.

        This is the only method calling this end point.

        :param email: mandatory :class:`string`
        :rtype: None
        """

        email = _snd.normalizeList(_snd.normalizeString, email)

        url = uritemplate.expand("https://api.github.com/user/emails")
        postArguments = email
        r = self.Session._request("DELETE", url, postArguments=postArguments)

    def remove_from_following(self, username):
        """
        Calls the `DELETE /user/following/:username <http://developer.github.com/v3/users/followers#unfollow-a-user>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand("https://api.github.com/user/following/{username}", username=username)
        r = self.Session._request("DELETE", url)

    def remove_from_starred(self, repo):
        """
        Calls the `DELETE /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring#unstar-a-repository>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: None
        """

        repo = _snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/starred/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("DELETE", url)

    def remove_from_starred_gists(self, gist):
        """
        Calls the `DELETE /gists/:id/star <http://developer.github.com/v3/gists#unstar-a-gist>`__ end point.

        This is the only method calling this end point.

        :param gist: mandatory :class:`.Gist` or :class:`string` (its :attr:`.Gist.id`)
        :rtype: None
        """

        gist = _snd.normalizeGistId(gist)

        url = uritemplate.expand("https://api.github.com/gists/{id}/star", id=gist)
        r = self.Session._request("DELETE", url)
