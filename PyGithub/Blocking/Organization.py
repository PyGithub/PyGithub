# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Organization(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.get_orgs`
      * :meth:`.Github.get_org`
      * :attr:`.Repository.owner`
      * :attr:`.Team.organization`
      * :meth:`.User.get_orgs`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, avatar_url=_rcv.Absent, billing_email=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, following=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, members_url=_rcv.Absent, name=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_members_url=_rcv.Absent, public_repos=_rcv.Absent, repos_url=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, followers_url=None, following_url=None, gists_url=None, gravatar_id=None, organizations_url=None, received_events_url=None, site_admin=None, starred_url=None, subscriptions_url=None, **kwds):
        import PyGithub.Blocking.User
        super(Organization, self)._initAttributes(**kwds)
        self.__avatar_url = _rcv.Attribute("Organization.avatar_url", _rcv.StringConverter, avatar_url)
        self.__billing_email = _rcv.Attribute("Organization.billing_email", _rcv.StringConverter, billing_email)
        self.__blog = _rcv.Attribute("Organization.blog", _rcv.StringConverter, blog)
        self.__collaborators = _rcv.Attribute("Organization.collaborators", _rcv.IntConverter, collaborators)
        self.__company = _rcv.Attribute("Organization.company", _rcv.StringConverter, company)
        self.__created_at = _rcv.Attribute("Organization.created_at", _rcv.DatetimeConverter, created_at)
        self.__disk_usage = _rcv.Attribute("Organization.disk_usage", _rcv.IntConverter, disk_usage)
        self.__email = _rcv.Attribute("Organization.email", _rcv.StringConverter, email)
        self.__events_url = _rcv.Attribute("Organization.events_url", _rcv.StringConverter, events_url)
        self.__followers = _rcv.Attribute("Organization.followers", _rcv.IntConverter, followers)
        self.__following = _rcv.Attribute("Organization.following", _rcv.IntConverter, following)
        self.__html_url = _rcv.Attribute("Organization.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("Organization.id", _rcv.IntConverter, id)
        self.__location = _rcv.Attribute("Organization.location", _rcv.StringConverter, location)
        self.__login = _rcv.Attribute("Organization.login", _rcv.StringConverter, login)
        self.__members_url = _rcv.Attribute("Organization.members_url", _rcv.StringConverter, members_url)
        self.__name = _rcv.Attribute("Organization.name", _rcv.StringConverter, name)
        self.__owned_private_repos = _rcv.Attribute("Organization.owned_private_repos", _rcv.IntConverter, owned_private_repos)
        self.__plan = _rcv.Attribute("Organization.plan", _rcv.StructureConverter(self.Session, PyGithub.Blocking.User.User.Plan), plan)
        self.__private_gists = _rcv.Attribute("Organization.private_gists", _rcv.IntConverter, private_gists)
        self.__public_gists = _rcv.Attribute("Organization.public_gists", _rcv.IntConverter, public_gists)
        self.__public_members_url = _rcv.Attribute("Organization.public_members_url", _rcv.StringConverter, public_members_url)
        self.__public_repos = _rcv.Attribute("Organization.public_repos", _rcv.IntConverter, public_repos)
        self.__repos_url = _rcv.Attribute("Organization.repos_url", _rcv.StringConverter, repos_url)
        self.__total_private_repos = _rcv.Attribute("Organization.total_private_repos", _rcv.IntConverter, total_private_repos)
        self.__type = _rcv.Attribute("Organization.type", _rcv.StringConverter, type)
        self.__updated_at = _rcv.Attribute("Organization.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, avatar_url=_rcv.Absent, billing_email=_rcv.Absent, blog=_rcv.Absent, collaborators=_rcv.Absent, company=_rcv.Absent, created_at=_rcv.Absent, disk_usage=_rcv.Absent, email=_rcv.Absent, events_url=_rcv.Absent, followers=_rcv.Absent, following=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, location=_rcv.Absent, login=_rcv.Absent, members_url=_rcv.Absent, name=_rcv.Absent, owned_private_repos=_rcv.Absent, plan=_rcv.Absent, private_gists=_rcv.Absent, public_gists=_rcv.Absent, public_members_url=_rcv.Absent, public_repos=_rcv.Absent, repos_url=_rcv.Absent, total_private_repos=_rcv.Absent, type=_rcv.Absent, updated_at=_rcv.Absent, followers_url=None, following_url=None, gists_url=None, gravatar_id=None, organizations_url=None, received_events_url=None, site_admin=None, starred_url=None, subscriptions_url=None, **kwds):
        super(Organization, self)._updateAttributes(eTag, **kwds)
        self.__avatar_url.update(avatar_url)
        self.__billing_email.update(billing_email)
        self.__blog.update(blog)
        self.__collaborators.update(collaborators)
        self.__company.update(company)
        self.__created_at.update(created_at)
        self.__disk_usage.update(disk_usage)
        self.__email.update(email)
        self.__events_url.update(events_url)
        self.__followers.update(followers)
        self.__following.update(following)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__location.update(location)
        self.__login.update(login)
        self.__members_url.update(members_url)
        self.__name.update(name)
        self.__owned_private_repos.update(owned_private_repos)
        self.__plan.update(plan)
        self.__private_gists.update(private_gists)
        self.__public_gists.update(public_gists)
        self.__public_members_url.update(public_members_url)
        self.__public_repos.update(public_repos)
        self.__repos_url.update(repos_url)
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
    def billing_email(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__billing_email.needsLazyCompletion)
        return self.__billing_email.value

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
    def following(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__following.needsLazyCompletion)
        return self.__following.value

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
    def members_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__members_url.needsLazyCompletion)
        return self.__members_url.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

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
    def public_members_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__public_members_url.needsLazyCompletion)
        return self.__public_members_url.value

    @property
    def public_repos(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__public_repos.needsLazyCompletion)
        return self.__public_repos.value

    @property
    def repos_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__repos_url.needsLazyCompletion)
        return self.__repos_url.value

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

    def add_to_public_members(self, username):
        """
        Calls the `PUT /orgs/:org/public_members/:username <http://developer.github.com/v3/orgs/members#publicize-a-users-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.public_members_url, member=username)
        r = self.Session._request("PUT", url)

    def create_fork(self, repo):
        """
        Calls the `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks#create-a-fork>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.create_fork`

        :param repo: mandatory :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :rtype: :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        repo = _snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/forks", owner=repo[0], repo=repo[1])
        postArguments = _snd.dictionary(organization=self.login)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def create_repo(self, name, description=None, homepage=None, private=None, has_issues=None, has_wiki=None, team_id=None, auto_init=None, gitignore_template=None, license_template=None):
        """
        Calls the `POST /orgs/:org/repos <http://developer.github.com/v3/repos#create>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param description: optional :class:`string`
        :param homepage: optional :class:`string`
        :param private: optional :class:`bool`
        :param has_issues: optional :class:`bool`
        :param has_wiki: optional :class:`bool`
        :param team_id: optional :class:`.Team` or :class:`int` (its :attr:`.Team.id`)
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
        if team_id is not None:
            team_id = _snd.normalizeTeamId(team_id)
        if auto_init is not None:
            auto_init = _snd.normalizeBool(auto_init)
        if gitignore_template is not None:
            gitignore_template = _snd.normalizeGitIgnoreTemplateName(gitignore_template)
        if license_template is not None:
            license_template = _snd.normalizeString(license_template)

        url = uritemplate.expand(self.repos_url)
        postArguments = _snd.dictionary(auto_init=auto_init, description=description, gitignore_template=gitignore_template, has_issues=has_issues, has_wiki=has_wiki, homepage=homepage, license_template=license_template, name=name, private=private, team_id=team_id)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def create_team(self, name, repo_names=None, permission=None):
        """
        Calls the `POST /orgs/:org/teams <http://developer.github.com/v3/orgs/teams#create-team>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param repo_names: optional :class:`list` of :class:`.Repository` or :class:`string` (its :attr:`.Repository.full_name`) or :class:`(string, string)` (its owner's :attr:`.Entity.login` and :attr:`.Repository.name`)
        :param permission: optional "admin" or "pull" or "push"
        :rtype: :class:`.Team`
        """
        import PyGithub.Blocking.Team

        name = _snd.normalizeString(name)
        if repo_names is not None:
            repo_names = _snd.normalizeList(_snd.normalizeRepositoryFullName, repo_names)
        if permission is not None:
            permission = _snd.normalizeEnum(permission, "admin", "pull", "push")

        url = uritemplate.expand("https://api.github.com/orgs/{org}/teams", org=self.login)
        postArguments = _snd.dictionary(name=name, permission=permission, repo_names=repo_names)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team)(None, r.json(), r.headers.get("ETag"))

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
            billing_email = _snd.normalizeString(billing_email)
        if blog is not None:
            blog = _snd.normalizeStringReset(blog)
        if company is not None:
            company = _snd.normalizeStringReset(company)
        if email is not None:
            email = _snd.normalizeStringReset(email)
        if location is not None:
            location = _snd.normalizeStringReset(location)
        if name is not None:
            name = _snd.normalizeStringReset(name)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(billing_email=billing_email, blog=blog, company=company, email=email, location=location, name=name)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_members(self, filter=None, per_page=None):
        """
        Calls the `GET /orgs/:org/members <http://developer.github.com/v3/orgs/members#members-list>`__ end point.

        This is the only method calling this end point.

        :param filter: optional "2fa_disabled" or "all"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.User`
        """
        import PyGithub.Blocking.User

        if filter is not None:
            filter = _snd.normalizeEnum(filter, "2fa_disabled", "all")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.members_url)
        urlArguments = _snd.dictionary(filter=filter, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

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
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.public_members_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

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

        repo = _snd.normalizeString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=self.login, repo=repo)
        r = self.Session._request("GET", url)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def get_repos(self, type=None, per_page=None):
        """
        Calls the `GET /orgs/:org/repos <http://developer.github.com/v3/repos#list-organization-repositories>`__ end point.

        This is the only method calling this end point.

        :param type: optional "all" or "forks" or "member" or "private" or "public" or "sources"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if type is not None:
            type = _snd.normalizeEnum(type, "all", "forks", "member", "private", "public", "sources")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.repos_url)
        urlArguments = _snd.dictionary(per_page=per_page, type=type)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

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
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/orgs/{org}/teams", org=self.login)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team))(None, r)

    def has_in_members(self, username):
        """
        Calls the `GET /orgs/:org/members/:username <http://developer.github.com/v3/orgs/members#check-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: :class:`bool`
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.members_url, member=username)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def has_in_public_members(self, username):
        """
        Calls the `GET /orgs/:org/public_members/:username <http://developer.github.com/v3/orgs/members#check-public-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: :class:`bool`
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.public_members_url, member=username)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def remove_from_members(self, username):
        """
        Calls the `DELETE /orgs/:org/members/:username <http://developer.github.com/v3/orgs/members#remove-a-member>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.members_url, member=username)
        r = self.Session._request("DELETE", url)

    def remove_from_public_members(self, username):
        """
        Calls the `DELETE /orgs/:org/public_members/:username <http://developer.github.com/v3/orgs/members#conceal-a-users-membership>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = _snd.normalizeUserLogin(username)

        url = uritemplate.expand(self.public_members_url, member=username)
        r = self.Session._request("DELETE", url)
