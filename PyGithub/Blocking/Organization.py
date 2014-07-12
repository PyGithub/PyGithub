# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking._base_github_object as bgo
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv

import PyGithub.Blocking.Entity


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

    def _initAttributes(self, billing_email=rcv.Absent, members_url=rcv.Absent, public_members_url=rcv.Absent, followers_url=None, following_url=None, gists_url=None, gravatar_id=None, organizations_url=None, received_events_url=None, site_admin=None, starred_url=None, subscriptions_url=None, **kwds):
        super(Organization, self)._initAttributes(**kwds)
        self.__billing_email = rcv.Attribute("Organization.billing_email", rcv.StringConverter, billing_email)
        self.__members_url = rcv.Attribute("Organization.members_url", rcv.StringConverter, members_url)
        self.__public_members_url = rcv.Attribute("Organization.public_members_url", rcv.StringConverter, public_members_url)

    def _updateAttributes(self, eTag, billing_email=rcv.Absent, members_url=rcv.Absent, public_members_url=rcv.Absent, followers_url=None, following_url=None, gists_url=None, gravatar_id=None, organizations_url=None, received_events_url=None, site_admin=None, starred_url=None, subscriptions_url=None, **kwds):
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

    def add_to_public_members(self, username):
        """
        Calls the `PUT /orgs/:org/public_members/:username <http://developer.github.com/v3/orgs/members#publicize-a-users-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.public_members_url, member=username)
        r = self.Session._request("PUT", url)

    def create_fork(self, repo):
        """
        Calls the `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks#create-a-fork>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.create_fork`

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/forks", owner=repo[0], repo=repo[1])
        postArguments = snd.dictionary(organization=self.login)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def create_repo(self, name, description=None, homepage=None, private=None, has_issues=None, has_wiki=None, has_downloads=None, team_id=None, auto_init=None, gitignore_template=None, license_template=None):
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
        :param team_id: optional :class:`.Team` or :class:`int` (its :attr:`.Team.id`)
        :param auto_init: optional :class:`bool`
        :param gitignore_template: optional :class:`.GitIgnoreTemplate` or :class:`string` (its :attr:`.GitIgnoreTemplate.name`)
        :param license_template: optional :class:`string`
        :rtype: :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        name = snd.normalizeString(name)
        if description is not None:
            description = snd.normalizeString(description)
        if homepage is not None:
            homepage = snd.normalizeString(homepage)
        if private is not None:
            private = snd.normalizeBool(private)
        if has_issues is not None:
            has_issues = snd.normalizeBool(has_issues)
        if has_wiki is not None:
            has_wiki = snd.normalizeBool(has_wiki)
        if has_downloads is not None:
            has_downloads = snd.normalizeBool(has_downloads)
        if team_id is not None:
            team_id = snd.normalizeTeamId(team_id)
        if auto_init is not None:
            auto_init = snd.normalizeBool(auto_init)
        if gitignore_template is not None:
            gitignore_template = snd.normalizeGitIgnoreTemplateName(gitignore_template)
        if license_template is not None:
            license_template = snd.normalizeString(license_template)

        url = uritemplate.expand(self.repos_url)
        postArguments = snd.dictionary(name=name, description=description, homepage=homepage, private=private, has_downloads=has_downloads, has_issues=has_issues, has_wiki=has_wiki, team_id=team_id, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def create_team(self, name, repo_names=None, permission=None):
        """
        Calls the `POST /orgs/:org/teams <http://developer.github.com/v3/orgs/teams#create-team>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param repo_names: optional :class:`list` of :class:`.Repository`
        :param permission: optional "pull" or "push" or "admin"
        :rtype: :class:`.Team`
        """
        import PyGithub.Blocking.Team

        name = snd.normalizeString(name)
        if repo_names is not None:
            repo_names = snd.normalizeList(snd.normalizeRepositoryFullName, repo_names)
        if permission is not None:
            permission = snd.normalizeEnum(permission, "pull", "push", "admin")

        url = uritemplate.expand("https://api.github.com/orgs/{org}/teams", org=self.login)
        postArguments = snd.dictionary(name=name, permission=permission, repo_names=repo_names)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team)(None, r.json(), r.headers.get("ETag"))

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
            billing_email = snd.normalizeString(billing_email)
        if blog is not None:
            blog = snd.normalizeStringReset(blog)
        if company is not None:
            company = snd.normalizeStringReset(company)
        if email is not None:
            email = snd.normalizeStringReset(email)
        if location is not None:
            location = snd.normalizeStringReset(location)
        if name is not None:
            name = snd.normalizeStringReset(name)

        url = uritemplate.expand(self.url)
        postArguments = snd.dictionary(billing_email=billing_email, blog=blog, company=company, email=email, location=location, name=name)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_members(self, filter=None, per_page=None):
        """
        Calls the `GET /orgs/:org/members <http://developer.github.com/v3/orgs/members#members-list>`__ end point.

        This is the only method calling this end point.

        :param filter: optional "all" or "2fa_disabled"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if filter is not None:
            filter = snd.normalizeEnum(filter, "all", "2fa_disabled")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.members_url)
        urlArguments = snd.dictionary(filter=filter, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

    def get_public_members(self, per_page=None):
        """
        Calls the `GET /orgs/:org/public_members <http://developer.github.com/v3/orgs/members#public-members-list>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.public_members_url)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

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
        import PyGithub.Blocking.Repository

        repo = snd.normalizeString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=self.login, repo=repo)
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def get_repos(self, type=None, per_page=None):
        """
        Calls the `GET /orgs/:org/repos <http://developer.github.com/v3/repos#list-organization-repositories>`__ end point.

        This is the only method calling this end point.

        :param type: optional "all" or "public" or "private" or "forks" or "sources" or "member"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if type is not None:
            type = snd.normalizeEnum(type, "all", "public", "private", "forks", "sources", "member")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand(self.repos_url)
        urlArguments = snd.dictionary(type=type, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

    def get_teams(self, per_page=None):
        """
        Calls the `GET /orgs/:org/teams <http://developer.github.com/v3/orgs/teams#list-teams>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Team`
        """
        import PyGithub.Blocking.Team

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/orgs/{org}/teams", org=self.login)
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team))(None, r)

    def has_in_members(self, username):
        """
        Calls the `GET /orgs/:org/members/:username <http://developer.github.com/v3/orgs/members#check-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: :class:`bool`
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.members_url, member=username)
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)

    def has_in_public_members(self, username):
        """
        Calls the `GET /orgs/:org/public_members/:username <http://developer.github.com/v3/orgs/members#check-public-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: :class:`bool`
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.public_members_url, member=username)
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)

    def remove_from_members(self, username):
        """
        Calls the `DELETE /orgs/:org/members/:username <http://developer.github.com/v3/orgs/members#remove-a-member>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.members_url, member=username)
        r = self.Session._request("DELETE", url)

    def remove_from_public_members(self, username):
        """
        Calls the `DELETE /orgs/:org/public_members/:username <http://developer.github.com/v3/orgs/members#conceal-a-users-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.public_members_url, member=username)
        r = self.Session._request("DELETE", url)
