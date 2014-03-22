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
      * :meth:`.Builder.build`
    """

    class GitIgnoreTemplate(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_gitignore_template`
        """

        def _initAttributes(self, name=None, source=None, **kwds):
            super(Github.GitIgnoreTemplate, self)._initAttributes(**kwds)
            self.__name = PyGithub.Blocking.Attributes.StringAttribute("Github.GitIgnoreTemplate.name", name)
            self.__source = PyGithub.Blocking.Attributes.StringAttribute("Github.GitIgnoreTemplate.source", source)

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

    class RateLimit(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Github.get_rate_limit`
        """

        def _initAttributes(self, resources=None, rate=None, **kwds):
            super(Github.RateLimit, self)._initAttributes(**kwds)
            self.__resources = PyGithub.Blocking.Attributes.StructAttribute("Github.RateLimit.resources", self.Session, Github.Resources, resources)

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
            self.__limit = PyGithub.Blocking.Attributes.IntAttribute("Github.RateLimits.limit", limit)
            self.__remaining = PyGithub.Blocking.Attributes.IntAttribute("Github.RateLimits.remaining", remaining)
            self.__reset = PyGithub.Blocking.Attributes.DatetimeAttribute("Github.RateLimits.reset", reset)

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
            self.__core = PyGithub.Blocking.Attributes.StructAttribute("Github.Resources.core", self.Session, Github.RateLimits, core)
            self.__search = PyGithub.Blocking.Attributes.StructAttribute("Github.Resources.search", self.Session, Github.RateLimits, search)

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
        return PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser(self.Session, r.json(), r.headers.get("ETag"))

    def get_gitignore_template(self, name):
        """
        Calls the `GET /gitignore/templates/:name <http://developer.github.com/v3/gitignore#get-a-single-template>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :rtype: :class:`.GitIgnoreTemplate`
        """

        name = PyGithub.Blocking.Parameters.normalizeString(name)

        url = uritemplate.expand("https://api.github.com/gitignore/templates/{name}", name=name)
        r = self.Session._request("GET", url)
        return Github.GitIgnoreTemplate(self.Session, r.json())

    def get_gitignore_templates(self):
        """
        Calls the `GET /gitignore/templates <http://developer.github.com/v3/gitignore#listing-available-templates>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`string`
        """

        url = uritemplate.expand("https://api.github.com/gitignore/templates")
        r = self.Session._request("GET", url)
        return r.json()

    def get_org(self, org):
        """
        Calls the `GET /orgs/:org <http://developer.github.com/v3/orgs#get-an-organization>`__ end point.

        This is the only method calling this end point.

        :param org: mandatory :class:`string`
        :rtype: :class:`.Organization`
        """

        org = PyGithub.Blocking.Parameters.normalizeString(org)

        url = uritemplate.expand("https://api.github.com/orgs/{org}", org=org)
        r = self.Session._request("GET", url)
        return PyGithub.Blocking.Organization.Organization(self.Session, r.json(), r.headers.get("ETag"))

    def get_rate_limit(self):
        """
        Calls the `GET /rate_limit <http://developer.github.com/v3/rate_limit#get-your-current-rate-limit-status>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.RateLimit`
        """

        url = uritemplate.expand("https://api.github.com/rate_limit")
        r = self.Session._request("GET", url)
        return Github.RateLimit(self.Session, r.json())

    def get_repo(self, repo):
        """
        Calls the `GET /repos/:owner/:repo <http://developer.github.com/v3/repos#get>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.get_repo`
          * :meth:`.Organization.get_repo`
          * :meth:`.User.get_repo`

        :param repo: mandatory :class:`TwoStrings` or :class:`string`
        :rtype: :class:`.Repository`
        """

        repo = PyGithub.Blocking.Parameters.normalizeTwoStringsString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url)
        return PyGithub.Blocking.Repository.Repository(self.Session, r.json(), r.headers.get("ETag"))

    def get_repos(self, since=None):
        """
        Calls the `GET /repositories <http://developer.github.com/v3/repos#list-all-public-repositories>`__ end point.

        This is the only method calling this end point.

        :param since: optional :class:`.Repository` or :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if since is not None:
            since = PyGithub.Blocking.Parameters.normalizeRepositoryId(since)

        url = uritemplate.expand("https://api.github.com/repositories")
        urlArguments = PyGithub.Blocking.Parameters.dictionary(since=since)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.Repository.Repository, self.Session, "GET", url, urlArguments=urlArguments)

    def get_team(self, id):
        """
        Calls the `GET /teams/:id <http://developer.github.com/v3/orgs/teams#get-team>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.Team`
        """

        id = PyGithub.Blocking.Parameters.normalizeInt(id)

        url = uritemplate.expand("https://api.github.com/teams/{id}", id=str(id))
        r = self.Session._request("GET", url)
        return PyGithub.Blocking.Team.Team(self.Session, r.json(), r.headers.get("ETag"))

    def get_user(self, user):
        """
        Calls the `GET /users/:user <http://developer.github.com/v3/users#get-a-single-user>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`string`
        :rtype: :class:`.User`
        """

        user = PyGithub.Blocking.Parameters.normalizeString(user)

        url = uritemplate.expand("https://api.github.com/users/{user}", user=user)
        r = self.Session._request("GET", url)
        return PyGithub.Blocking.User.User(self.Session, r.json(), r.headers.get("ETag"))

    def get_users(self, since=None):
        """
        Calls the `GET /users <http://developer.github.com/v3/users#get-all-users>`__ end point.

        This is the only method calling this end point.

        :param since: optional :class:`.User` or :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if since is not None:
            since = PyGithub.Blocking.Parameters.normalizeUserId(since)

        url = uritemplate.expand("https://api.github.com/users")
        urlArguments = PyGithub.Blocking.Parameters.dictionary(since=since)
        return PyGithub.Blocking.PaginatedList.PaginatedList(PyGithub.Blocking.User.User, self.Session, "GET", url, urlArguments=urlArguments)
