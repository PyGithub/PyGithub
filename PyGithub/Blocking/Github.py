# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.PaginatedList
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv

import PyGithub.Blocking.AuthenticatedUser
import PyGithub.Blocking.Organization
import PyGithub.Blocking.Repository
import PyGithub.Blocking.Team
import PyGithub.Blocking.User


class Github(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Builder.Build`
    """

    class GitIgnoreTemplate(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_gitignore_template`
        """

        def _initAttributes(self, name=None, source=None, **kwds):
            super(Github.GitIgnoreTemplate, self)._initAttributes(**kwds)
            self.__name = rcv.Attribute("Github.GitIgnoreTemplate.name", rcv.StringConverter, name)
            self.__source = rcv.Attribute("Github.GitIgnoreTemplate.source", rcv.StringConverter, source)

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

    class Meta(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_meta`
        """

        def _initAttributes(self, git=None, hooks=None, verifiable_password_authentication=None, **kwds):
            super(Github.Meta, self)._initAttributes(**kwds)
            self.__git = rcv.Attribute("Github.Meta.git", rcv.ListConverter(rcv.StringConverter), git)
            self.__hooks = rcv.Attribute("Github.Meta.hooks", rcv.ListConverter(rcv.StringConverter), hooks)
            self.__verifiable_password_authentication = rcv.Attribute("Github.Meta.verifiable_password_authentication", rcv.BoolConverter, verifiable_password_authentication)

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

    class RateLimit(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_rate_limit`
        """

        def _initAttributes(self, resources=None, rate=None, **kwds):
            super(Github.RateLimit, self)._initAttributes(**kwds)
            self.__resources = rcv.Attribute("Github.RateLimit.resources", rcv.StructureConverter(self.Session, Github.Resources), resources)

        @property
        def resources(self):
            """
            :type: :class:`.Resources`
            """
            return self.__resources.value

    class RateLimits(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Resources.core`
          * :attr:`.Resources.search`
        """

        def _initAttributes(self, limit=None, remaining=None, reset=None, **kwds):
            super(Github.RateLimits, self)._initAttributes(**kwds)
            self.__limit = rcv.Attribute("Github.RateLimits.limit", rcv.IntConverter, limit)
            self.__remaining = rcv.Attribute("Github.RateLimits.remaining", rcv.IntConverter, remaining)
            self.__reset = rcv.Attribute("Github.RateLimits.reset", rcv.DatetimeConverter, reset)

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

    class Resources(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.RateLimit.resources`
        """

        def _initAttributes(self, core=None, search=None, **kwds):
            super(Github.Resources, self)._initAttributes(**kwds)
            self.__core = rcv.Attribute("Github.Resources.core", rcv.StructureConverter(self.Session, Github.RateLimits), core)
            self.__search = rcv.Attribute("Github.Resources.search", rcv.StructureConverter(self.Session, Github.RateLimits), search)

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

    def get_authenticated_user(self):
        """
        Calls the `GET /user <http://developer.github.com/v3/users#get-the-authenticated-user>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.AuthenticatedUser`
        """

        url = uritemplate.expand("https://api.github.com/user")
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser)(None, r.json(), r.headers.get("ETag"))

    def get_emojis(self):
        """
        Calls the `GET /emojis <http://developer.github.com/v3/emojis#emojis>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`dict` of :class:`string` to :class:`string`
        """

        url = uritemplate.expand("https://api.github.com/emojis")
        r = self.Session._request("GET", url)
        return rcv.DictConverter(rcv.StringConverter, rcv.StringConverter)(None, r.json())

    def get_gitignore_template(self, name):
        """
        Calls the `GET /gitignore/templates/:name <http://developer.github.com/v3/gitignore#get-a-single-template>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :rtype: :class:`.GitIgnoreTemplate`
        """

        name = snd.normalizeString(name)

        url = uritemplate.expand("https://api.github.com/gitignore/templates/{name}", name=name)
        r = self.Session._request("GET", url)
        return rcv.StructureConverter(self.Session, Github.GitIgnoreTemplate)(None, r.json())

    def get_gitignore_templates(self):
        """
        Calls the `GET /gitignore/templates <http://developer.github.com/v3/gitignore#listing-available-templates>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`string`
        """

        url = uritemplate.expand("https://api.github.com/gitignore/templates")
        r = self.Session._request("GET", url)
        return rcv.ListConverter(rcv.StringConverter)(None, r.json())

    def get_meta(self):
        """
        Calls the `GET /meta <http://developer.github.com/v3/meta#meta>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.Meta`
        """

        url = uritemplate.expand("https://api.github.com/meta")
        r = self.Session._request("GET", url)
        return rcv.StructureConverter(self.Session, Github.Meta)(None, r.json())

    def get_org(self, org):
        """
        Calls the `GET /orgs/:org <http://developer.github.com/v3/orgs#get-an-organization>`__ end point.

        This is the only method calling this end point.

        :param org: mandatory :class:`string`
        :rtype: :class:`.Organization`
        """

        org = snd.normalizeString(org)

        url = uritemplate.expand("https://api.github.com/orgs/{org}", org=org)
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization)(None, r.json(), r.headers.get("ETag"))

    def get_rate_limit(self):
        """
        Calls the `GET /rate_limit <http://developer.github.com/v3/rate_limit#get-your-current-rate-limit-status>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.RateLimit`
        """

        url = uritemplate.expand("https://api.github.com/rate_limit")
        r = self.Session._request("GET", url)
        return rcv.StructureConverter(self.Session, Github.RateLimit)(None, r.json())

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

        repo = snd.normalizeTwoStringsString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def get_repos(self, since=None):
        """
        Calls the `GET /repositories <http://developer.github.com/v3/repos#list-all-public-repositories>`__ end point.

        This is the only method calling this end point.

        :param since: optional :class:`.Repository` or :class:`int` (its :attr:`.Repository.id`)
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if since is not None:
            since = snd.normalizeRepositoryId(since)

        url = uritemplate.expand("https://api.github.com/repositories")
        urlArguments = snd.dictionary(since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_team(self, id):
        """
        Calls the `GET /teams/:id <http://developer.github.com/v3/orgs/teams#get-team>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.Team`
        """

        id = snd.normalizeInt(id)

        url = uritemplate.expand("https://api.github.com/teams/{id}", id=str(id))
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team)(None, r.json(), r.headers.get("ETag"))

    def get_user(self, user):
        """
        Calls the `GET /users/:user <http://developer.github.com/v3/users#get-a-single-user>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`string`
        :rtype: :class:`.User`
        """

        user = snd.normalizeString(user)

        url = uritemplate.expand("https://api.github.com/users/{user}", user=user)
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User)(None, r.json(), r.headers.get("ETag"))

    def get_users(self, since=None):
        """
        Calls the `GET /users <http://developer.github.com/v3/users#get-all-users>`__ end point.

        This is the only method calling this end point.

        :param since: optional :class:`.User` or :class:`int` (its :attr:`.User.id`)
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if since is not None:
            since = snd.normalizeUserId(since)

        url = uritemplate.expand("https://api.github.com/users")
        urlArguments = snd.dictionary(since=since)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)
