# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Github(_bgo.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Builder.Build`

    Methods accepting instances of this class as parameter: none.
    """

    class GitIgnoreTemplate(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_gitignore_template`

        Methods accepting instances of this class as parameter:
          * :meth:`.AuthenticatedUser.create_repo`
          * :meth:`.Organization.create_repo`
        """

        def _initAttributes(self, name=None, source=None, **kwds):
            super(Github.GitIgnoreTemplate, self)._initAttributes(**kwds)
            self.__name = _rcv.Attribute("Github.GitIgnoreTemplate.name", _rcv.StringConverter, name)
            self.__source = _rcv.Attribute("Github.GitIgnoreTemplate.source", _rcv.StringConverter, source)

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

        @property
        def source(self):
            """
            :type: :class:`string`
            """
            return self.__source.value

    class Meta(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_meta`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, git=None, hooks=None, verifiable_password_authentication=None, **kwds):
            super(Github.Meta, self)._initAttributes(**kwds)
            self.__git = _rcv.Attribute("Github.Meta.git", _rcv.ListConverter(_rcv.StringConverter), git)
            self.__hooks = _rcv.Attribute("Github.Meta.hooks", _rcv.ListConverter(_rcv.StringConverter), hooks)
            self.__verifiable_password_authentication = _rcv.Attribute("Github.Meta.verifiable_password_authentication", _rcv.BoolConverter, verifiable_password_authentication)

        @property
        def git(self):
            """
            :type: :class:`list` of :class:`string`
            """
            return self.__git.value

        @property
        def hooks(self):
            """
            :type: :class:`list` of :class:`string`
            """
            return self.__hooks.value

        @property
        def verifiable_password_authentication(self):
            """
            :type: :class:`bool`
            """
            return self.__verifiable_password_authentication.value

    class RateLimit(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_rate_limit`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, resources=None, rate=None, **kwds):
            super(Github.RateLimit, self)._initAttributes(**kwds)
            self.__resources = _rcv.Attribute("Github.RateLimit.resources", _rcv.StructureConverter(self.Session, Github.Resources), resources)

        @property
        def resources(self):
            """
            :type: :class:`.Resources`
            """
            return self.__resources.value

    class RateLimits(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Resources.core`
          * :attr:`.Resources.search`
          * :attr:`.Session.RateLimit`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, limit=None, remaining=None, reset=None, **kwds):
            super(Github.RateLimits, self)._initAttributes(**kwds)
            self.__limit = _rcv.Attribute("Github.RateLimits.limit", _rcv.IntConverter, limit)
            self.__remaining = _rcv.Attribute("Github.RateLimits.remaining", _rcv.IntConverter, remaining)
            self.__reset = _rcv.Attribute("Github.RateLimits.reset", _rcv.DatetimeConverter, reset)

        def _updateAttributes(self, limit=None, remaining=None, reset=None, **kwds):
            super(Github.RateLimits, self)._updateAttributes(**kwds)
            self.__limit.update(limit)
            self.__remaining.update(remaining)
            self.__reset.update(reset)

        @property
        def limit(self):
            """
            :type: :class:`int`
            """
            return self.__limit.value

        @property
        def remaining(self):
            """
            :type: :class:`int`
            """
            return self.__remaining.value

        @property
        def reset(self):
            """
            :type: :class:`datetime`
            """
            return self.__reset.value

    class Resources(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.RateLimit.resources`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, core=None, search=None, **kwds):
            super(Github.Resources, self)._initAttributes(**kwds)
            self.__core = _rcv.Attribute("Github.Resources.core", _rcv.StructureConverter(self.Session, Github.RateLimits), core)
            self.__search = _rcv.Attribute("Github.Resources.search", _rcv.StructureConverter(self.Session, Github.RateLimits), search)

        @property
        def core(self):
            """
            :type: :class:`.RateLimits`
            """
            return self.__core.value

        @property
        def search(self):
            """
            :type: :class:`.RateLimits`
            """
            return self.__search.value

    def create_anonymous_gist(self, files, description=None, public=None):
        """
        Calls the `POST /gists <http://developer.github.com/v3/gists#create-a-gist>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.create_gist`

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
        r = self.Session._requestAnonymous("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist)(None, r.json(), r.headers.get("ETag"))

    def get_authenticated_user(self):
        """
        Calls the `GET /user <http://developer.github.com/v3/users#get-the-authenticated-user>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.AuthenticatedUser`
        """
        import PyGithub.Blocking.AuthenticatedUser

        url = uritemplate.expand("https://api.github.com/user")
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser)(None, r.json(), r.headers.get("ETag"))

    def get_emojis(self):
        """
        Calls the `GET /emojis <http://developer.github.com/v3/emojis#emojis>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`dict` of :class:`string` to :class:`string`
        """

        url = uritemplate.expand("https://api.github.com/emojis")
        r = self.Session._request("GET", url)
        return _rcv.DictConverter(_rcv.StringConverter, _rcv.StringConverter)(None, r.json())

    def get_gist(self, id):
        """
        Calls the `GET /gists/:id <http://developer.github.com/v3/gists#get-a-single-gist>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`string`
        :rtype: :class:`.Gist`
        """
        import PyGithub.Blocking.Gist

        id = _snd.normalizeString(id)

        url = uritemplate.expand("https://api.github.com/gists/{id}", id=id)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist)(None, r.json(), r.headers.get("ETag"))

    def get_gitignore_template(self, name):
        """
        Calls the `GET /gitignore/templates/:name <http://developer.github.com/v3/gitignore#get-a-single-template>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :rtype: :class:`.GitIgnoreTemplate`
        """

        name = _snd.normalizeString(name)

        url = uritemplate.expand("https://api.github.com/gitignore/templates/{name}", name=name)
        r = self.Session._request("GET", url)
        return _rcv.StructureConverter(self.Session, Github.GitIgnoreTemplate)(None, r.json())

    def get_gitignore_templates(self):
        """
        Calls the `GET /gitignore/templates <http://developer.github.com/v3/gitignore#listing-available-templates>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`string`
        """

        url = uritemplate.expand("https://api.github.com/gitignore/templates")
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.StringConverter)(None, r.json())

    def get_meta(self):
        """
        Calls the `GET /meta <http://developer.github.com/v3/meta#meta>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.Meta`
        """

        url = uritemplate.expand("https://api.github.com/meta")
        r = self.Session._request("GET", url)
        return _rcv.StructureConverter(self.Session, Github.Meta)(None, r.json())

    def get_org(self, org):
        """
        Calls the `GET /orgs/:org <http://developer.github.com/v3/orgs#get-an-organization>`__ end point.

        This is the only method calling this end point.

        :param org: mandatory :class:`string`
        :rtype: :class:`.Organization`
        """
        import PyGithub.Blocking.Organization

        org = _snd.normalizeString(org)

        url = uritemplate.expand("https://api.github.com/orgs/{org}", org=org)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization)(None, r.json(), r.headers.get("ETag"))

    def get_public_gists(self, since=None, per_page=None):
        """
        Calls the `GET /gists/public <http://developer.github.com/v3/gists#list-gists>`__ end point.

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

        url = uritemplate.expand("https://api.github.com/gists/public")
        urlArguments = _snd.dictionary(per_page=per_page, since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist))(None, r)

    def get_rate_limit(self):
        """
        Calls the `GET /rate_limit <http://developer.github.com/v3/rate_limit#get-your-current-rate-limit-status>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.RateLimit`
        """

        url = uritemplate.expand("https://api.github.com/rate_limit")
        r = self.Session._request("GET", url)
        return _rcv.StructureConverter(self.Session, Github.RateLimit)(None, r.json())

    def get_repo(self, repo):
        """
        Calls the `GET /repos/:owner/:repo <http://developer.github.com/v3/repos#get>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.get_repo`
          * :meth:`.Organization.get_repo`
          * :meth:`.User.get_repo`

        :param repo: mandatory :class:`(string, string)` or :class:`string`
        :rtype: :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        repo = _snd.normalizeTwoStringsString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def get_repos(self, since=None):
        """
        Calls the `GET /repositories <http://developer.github.com/v3/repos#list-all-public-repositories>`__ end point.

        This is the only method calling this end point.

        :param since: optional :class:`.Repository` or :class:`int` (its :attr:`.Repository.id`)
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if since is not None:
            since = _snd.normalizeRepositoryId(since)

        url = uritemplate.expand("https://api.github.com/repositories")
        urlArguments = _snd.dictionary(since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_team(self, id):
        """
        Calls the `GET /teams/:id <http://developer.github.com/v3/orgs/teams#get-team>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.Team`
        """
        import PyGithub.Blocking.Team

        id = _snd.normalizeInt(id)

        url = uritemplate.expand("https://api.github.com/teams/{id}", id=str(id))
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team)(None, r.json(), r.headers.get("ETag"))

    def get_user(self, username):
        """
        Calls the `GET /users/:username <http://developer.github.com/v3/users#get-a-single-user>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`string`
        :rtype: :class:`.User`
        """
        import PyGithub.Blocking.User

        username = _snd.normalizeString(username)

        url = uritemplate.expand("https://api.github.com/users/{username}", username=username)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User)(None, r.json(), r.headers.get("ETag"))

    def get_users(self, since=None):
        """
        Calls the `GET /users <http://developer.github.com/v3/users#get-all-users>`__ end point.

        This is the only method calling this end point.

        :param since: optional :class:`.User` or :class:`int` (its :attr:`.Entity.id`)
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if since is not None:
            since = _snd.normalizeUserId(since)

        url = uritemplate.expand("https://api.github.com/users")
        urlArguments = _snd.dictionary(since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)
