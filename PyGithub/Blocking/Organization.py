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
import PyGithub.Blocking.Repository
import PyGithub.Blocking.Team
import PyGithub.Blocking.User


class Organization(PyGithub.Blocking.Entity.Entity):
    """
    Base class: :class:`.Entity`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.get_orgs`
      * :meth:`.Github.get_org`
      * :attr:`.Repository.owner`
      * :attr:`.Team.organization`
      * :meth:`.User.get_orgs`
    """

    def _initAttributes(self, billing_email=PyGithub.Blocking.Attributes.Absent, members_url=PyGithub.Blocking.Attributes.Absent, public_members_url=PyGithub.Blocking.Attributes.Absent, followers_url=None, following_url=None, gists_url=None, gravatar_id=None, organizations_url=None, received_events_url=None, site_admin=None, starred_url=None, subscriptions_url=None, **kwds):
        super(Organization, self)._initAttributes(**kwds)
        self.__billing_email = self._createStringAttribute("Organization.billing_email", billing_email)
        self.__members_url = self._createStringAttribute("Organization.members_url", members_url)
        self.__public_members_url = self._createStringAttribute("Organization.public_members_url", public_members_url)

    def _updateAttributes(self, eTag, billing_email=PyGithub.Blocking.Attributes.Absent, members_url=PyGithub.Blocking.Attributes.Absent, public_members_url=PyGithub.Blocking.Attributes.Absent, followers_url=None, following_url=None, gists_url=None, gravatar_id=None, organizations_url=None, received_events_url=None, site_admin=None, starred_url=None, subscriptions_url=None, **kwds):
        super(Organization, self)._updateAttributes(eTag, **kwds)
        self.__billing_email.update(billing_email)
        self.__members_url.update(members_url)
        self.__public_members_url.update(public_members_url)

    @property
    def billing_email(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__billing_email.needsLazyCompletion)
        return self.__billing_email.value

    @property
    def members_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__members_url.needsLazyCompletion)
        return self.__members_url.value

    @property
    def public_members_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__public_members_url.needsLazyCompletion)
        return self.__public_members_url.value

    def add_to_public_members(self, user):
        """
        Calls the `PUT /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members#publicize-a-users-membership>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: None
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.public_members_url, member=user)
        self._triggerSideEffect("PUT", url)

    def create_fork(self, repo):
        """
        Calls the `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks#create-a-fork>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.create_fork`

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`TwoStrings`
        :rtype: :class:`.Repository`
        """

        repo = PyGithub.Blocking.Parameters.normalizeRepository(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/forks", owner=repo[0], repo=repo[1])
        postArguments = PyGithub.Blocking.Parameters.dictionary(organization=self.login)
        return self._createInstance(PyGithub.Blocking.Repository.Repository, "POST", url, postArguments=postArguments)

    def create_repo(self, name, description=None, homepage=None, private=None, has_issues=None, has_wiki=None, has_downloads=None, team_id=None, auto_init=None, gitignore_template=None):
        """
        Calls the `POST /orgs/:org/repos <http://developer.github.com/v3/repos#create>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param description: optional :class:`string`
        :param homepage: optional :class:`string`
        :param private: optional :class:`bool`
        :param has_issues: optional :class:`bool`
        :param has_wiki: optional :class:`bool`
        :param has_downloads: optional :class:`bool`
        :param team_id: optional :class:`.Team` or :class:`string`
        :param auto_init: optional :class:`bool`
        :param gitignore_template: optional :class:`.GitIgnoreTemplate` or :class:`string`
        :rtype: :class:`.Repository`
        """

        name = PyGithub.Blocking.Parameters.normalizeString(name)
        if description is not None:
            description = PyGithub.Blocking.Parameters.normalizeString(description)
        if homepage is not None:
            homepage = PyGithub.Blocking.Parameters.normalizeString(homepage)
        if private is not None:
            private = PyGithub.Blocking.Parameters.normalizeBool(private)
        if has_issues is not None:
            has_issues = PyGithub.Blocking.Parameters.normalizeBool(has_issues)
        if has_wiki is not None:
            has_wiki = PyGithub.Blocking.Parameters.normalizeBool(has_wiki)
        if has_downloads is not None:
            has_downloads = PyGithub.Blocking.Parameters.normalizeBool(has_downloads)
        if team_id is not None:
            team_id = PyGithub.Blocking.Parameters.normalizeTeam(team_id)
        if auto_init is not None:
            auto_init = PyGithub.Blocking.Parameters.normalizeBool(auto_init)
        if gitignore_template is not None:
            gitignore_template = PyGithub.Blocking.Parameters.normalizeGitIgnoreTemplateString(gitignore_template)

        url = uritemplate.expand(self.repos_url)
        postArguments = PyGithub.Blocking.Parameters.dictionary(name=name, description=description, homepage=homepage, private=private, has_downloads=has_downloads, has_issues=has_issues, has_wiki=has_wiki, team_id=team_id, auto_init=auto_init, gitignore_template=gitignore_template)
        return self._createInstance(PyGithub.Blocking.Repository.Repository, "POST", url, postArguments=postArguments)

    def create_team(self, name, repo_names=None, permission=None):
        """
        Calls the `POST /orgs/:org/teams <http://developer.github.com/v3/orgs/teams#create-team>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param repo_names: optional :class:`list` of :class:`.Repository`
        :param permission: optional "pull" or "push" or "admin"
        :rtype: :class:`.Team`
        """

        name = PyGithub.Blocking.Parameters.normalizeString(name)
        if repo_names is not None:
            repo_names = PyGithub.Blocking.Parameters.normalizeList(PyGithub.Blocking.Parameters.normalizeRepository, repo_names)
        if permission is not None:
            permission = PyGithub.Blocking.Parameters.normalizeEnum(permission, "pull", "push", "admin")

        url = uritemplate.expand("https://api.github.com/orgs/{org}/teams", org=self.login)
        postArguments = PyGithub.Blocking.Parameters.dictionary(name=name, permission=permission, repo_names=repo_names)
        return self._createInstance(PyGithub.Blocking.Team.Team, "POST", url, postArguments=postArguments)

    def edit(self, billing_email=None, blog=None, company=None, email=None, location=None, name=None):
        """
        Calls the `PATCH /orgs/:org <http://developer.github.com/v3/orgs#edit-an-organization>`__ end point.

        This is the only method calling this end point.

        :param billing_email: optional :class:`string`
        :param blog: optional :class:`string` or :class:`Reset`
        :param company: optional :class:`string` or :class:`Reset`
        :param email: optional :class:`string` or :class:`Reset`
        :param location: optional :class:`string` or :class:`Reset`
        :param name: optional :class:`string` or :class:`Reset`
        :rtype: None
        """

        if billing_email is not None:
            billing_email = PyGithub.Blocking.Parameters.normalizeString(billing_email)
        if blog is not None:
            blog = PyGithub.Blocking.Parameters.normalizeStringReset(blog)
        if company is not None:
            company = PyGithub.Blocking.Parameters.normalizeStringReset(company)
        if email is not None:
            email = PyGithub.Blocking.Parameters.normalizeStringReset(email)
        if location is not None:
            location = PyGithub.Blocking.Parameters.normalizeStringReset(location)
        if name is not None:
            name = PyGithub.Blocking.Parameters.normalizeStringReset(name)

        url = uritemplate.expand(self.url)
        postArguments = PyGithub.Blocking.Parameters.dictionary(billing_email=billing_email, blog=blog, company=company, email=email, location=location, name=name)
        self._updateWith("PATCH", url, postArguments=postArguments)

    def get_members(self, filter=None, per_page=None):
        """
        Calls the `GET /orgs/:org/members <http://developer.github.com/v3/orgs/members#members-list>`__ end point.

        This is the only method calling this end point.

        :param filter: optional "all" or "2fa_disabled"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if filter is not None:
            filter = PyGithub.Blocking.Parameters.normalizeEnum(filter, "all", "2fa_disabled")
        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.members_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(filter=filter, per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.User.User, "GET", url, urlArguments=urlArguments)

    def get_public_members(self, per_page=None):
        """
        Calls the `GET /orgs/:org/public_members <http://developer.github.com/v3/orgs/members#public-members-list>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.public_members_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.User.User, "GET", url, urlArguments=urlArguments)

    def get_repo(self, repo):
        """
        Calls the `GET /repos/:owner/:repo <http://developer.github.com/v3/repos#get>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.get_repo`
          * :meth:`.Github.get_repo`
          * :meth:`.User.get_repo`

        :param repo: mandatory :class:`string`
        :rtype: :class:`.Repository`
        """

        repo = PyGithub.Blocking.Parameters.normalizeString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=self.login, repo=repo)
        return self._createInstance(PyGithub.Blocking.Repository.Repository, "GET", url)

    def get_repos(self, type=None, per_page=None):
        """
        Calls the `GET /orgs/:org/repos <http://developer.github.com/v3/repos#list-organization-repositories>`__ end point.

        This is the only method calling this end point.

        :param type: optional "all" or "public" or "private" or "forks" or "sources" or "member"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """

        if type is not None:
            type = PyGithub.Blocking.Parameters.normalizeEnum(type, "all", "public", "private", "forks", "sources", "member")
        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand(self.repos_url)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(type=type, per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.Repository.Repository, "GET", url, urlArguments=urlArguments)

    def get_teams(self, per_page=None):
        """
        Calls the `GET /orgs/:org/teams <http://developer.github.com/v3/orgs/teams#list-teams>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Team`
        """

        if per_page is not None:
            per_page = PyGithub.Blocking.Parameters.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/orgs/{org}/teams", org=self.login)
        urlArguments = PyGithub.Blocking.Parameters.dictionary(per_page=per_page)
        return self._createPaginatedList(PyGithub.Blocking.Team.Team, "GET", url, urlArguments=urlArguments)

    def has_in_members(self, user):
        """
        Calls the `GET /orgs/:org/members/:user <http://developer.github.com/v3/orgs/members#check-membership>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: :class:`bool`
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.members_url, member=user)
        return self._createBool("GET", url)

    def has_in_public_members(self, user):
        """
        Calls the `GET /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members#check-public-membership>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: :class:`bool`
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.public_members_url, member=user)
        return self._createBool("GET", url)

    def remove_from_members(self, user):
        """
        Calls the `DELETE /orgs/:org/members/:user <http://developer.github.com/v3/orgs/members#remove-a-member>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: None
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.members_url, member=user)
        self._triggerSideEffect("DELETE", url)

    def remove_from_public_members(self, user):
        """
        Calls the `DELETE /orgs/:org/public_members/:user <http://developer.github.com/v3/orgs/members#conceal-a-users-membership>`__ end point.

        This is the only method calling this end point.

        :param user: mandatory :class:`.User` or :class:`string`
        :rtype: None
        """

        user = PyGithub.Blocking.Parameters.normalizeUser(user)

        url = uritemplate.expand(self.public_members_url, member=user)
        self._triggerSideEffect("DELETE", url)
