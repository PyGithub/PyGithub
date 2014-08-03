# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv

import PyGithub.Blocking.User


class AuthenticatedUser(PyGithub.Blocking.User.User):
    """
    Base class: :class:`.User`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Github.get_authenticated_user`

    Methods accepting instances of this class as parameter: none.
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
