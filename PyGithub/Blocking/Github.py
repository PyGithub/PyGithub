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
            self.__name = self._createStringAttribute("Github.GitIgnoreTemplate.name", name)
            self.__source = self._createStringAttribute("Github.GitIgnoreTemplate.source", source)

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
            self.__resources = self._createStructAttribute("Github.RateLimit.resources", Github.Resources, resources)

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
            self.__limit = self._createIntAttribute("Github.RateLimits.limit", limit)
            self.__remaining = self._createIntAttribute("Github.RateLimits.remaining", remaining)
            self.__reset = self._createDatetimeAttribute("Github.RateLimits.reset", reset)

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
            self.__core = self._createStructAttribute("Github.Resources.core", Github.RateLimits, core)
            self.__search = self._createStructAttribute("Github.Resources.search", Github.RateLimits, search)

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
        return self._createInstance(PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser, "GET", url)

    def get_gitignore_template(self, name):
        """
        Calls the `GET /gitignore/templates/:name <http://developer.github.com/v3/gitignore#get-a-single-template>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :rtype: :class:`.GitIgnoreTemplate`
        """

        name = PyGithub.Blocking.Parameters.normalizeString(name)

        url = uritemplate.expand("https://api.github.com/gitignore/templates/{name}", name=name)
        return self._createStruct(Github.GitIgnoreTemplate, "GET", url)

    def get_gitignore_templates(self):
        """
        Calls the `GET /gitignore/templates <http://developer.github.com/v3/gitignore#listing-available-templates>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`string`
        """

        url = uritemplate.expand("https://api.github.com/gitignore/templates")
        return self._returnRawData("GET", url)

    def get_org(self, org):
        """
        Calls the `GET /orgs/:org <http://developer.github.com/v3/orgs#get-an-organization>`__ end point.

        This is the only method calling this end point.

        :param org: mandatory :class:`string`
        :rtype: :class:`.Organization`
        """

        org = PyGithub.Blocking.Parameters.normalizeString(org)

        url = uritemplate.expand("https://api.github.com/orgs/{org}", org=org)
        return self._createInstance(PyGithub.Blocking.Organization.Organization, "GET", url)

    def get_rate_limit(self):
        """
        Calls the `GET /rate_limit <http://developer.github.com/v3/rate_limit#get-your-current-rate-limit-status>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.RateLimit`
        """

        url = uritemplate.expand("https://api.github.com/rate_limit")
        return self._createStruct(Github.RateLimit, "GET", url)

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
        return self._createInstance(PyGithub.Blocking.Repository.Repository, "GET", url)

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
        return self._createPaginatedList(PyGithub.Blocking.Repository.Repository, "GET", url, urlArguments=urlArguments)

    def get_team(self, id):
        """
        Calls the `GET /teams/:id <http://developer.github.com/v3/orgs/teams#get-team>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.Team`
        """

        id = PyGithub.Blocking.Parameters.normalizeInt(id)

        url = uritemplate.expand("https://api.github.com/teams/{id}", id=str(id))
        return self._createInstance(PyGithub.Blocking.Team.Team, "GET", url)

    def get_user(self, user):
        """
        Calls the `GET /users/:user <http://developer.github.com/v3/users#get-a-single-user>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`string`
        :rtype: :class:`.User`
        """

        user = PyGithub.Blocking.Parameters.normalizeString(user)

        url = uritemplate.expand("https://api.github.com/users/{user}", user=user)
        return self._createInstance(PyGithub.Blocking.User.User, "GET", url)

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
        return self._createPaginatedList(PyGithub.Blocking.User.User, "GET", url, urlArguments=urlArguments)
