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

import PyGithub.Blocking.User


class AuthenticatedUser(PyGithub.Blocking.User.User):
    """
    Base class: :class:`.User`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Github.get_authenticated_user`
    """

    def add_to_following(self, username):
        """
        Calls the `PUT /user/following/:username <http://developer.github.com/v3/users/followers#follow-a-user>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand("https://api.github.com/user/following/{username}", username=username)
        r = self.Session._request("PUT", url)

    def add_to_starred(self, repo):
        """
        Calls the `PUT /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring#star-a-repository>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: None
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/starred/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("PUT", url)

    def add_to_subscriptions(self, repo):
        """
        Calls the `PUT /user/subscriptions/:owner/:repo <http://developer.github.com/v3/activity/watching#watch-a-repository-legacy>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: None
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/subscriptions/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("PUT", url)

    def create_fork(self, repo):
        """
        Calls the `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks#create-a-fork>`__ end point.

        The following methods also call this end point:
          * :meth:`.Organization.create_fork`

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/forks", owner=repo[0], repo=repo[1])
        r = self.Session._request("POST", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

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
            description = snd.normalizeString(description)
        if public is not None:
            public = snd.normalizeBool(public)

        url = uritemplate.expand("https://api.github.com/gists")
        postArguments = snd.dictionary(files=files, description=description, public=public)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist)(None, r.json(), r.headers.get("ETag"))

    def create_key(self, title, key):
        """
        Calls the `POST /user/keys <http://developer.github.com/v3/users/keys#create-a-public-key>`__ end point.

        This is the only method calling this end point.

        :param title: mandatory :class:`string`
        :param key: mandatory :class:`string`
        :rtype: :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        title = snd.normalizeString(title)
        key = snd.normalizeString(key)

        url = uritemplate.expand("https://api.github.com/user/keys")
        postArguments = snd.dictionary(title=title, key=key)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return rcv.StructureConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey)(None, r.json(), r.headers.get("ETag"))

    def create_repo(self, name, description=None, homepage=None, private=None, has_issues=None, has_wiki=None, has_downloads=None, auto_init=None, gitignore_template=None, license_template=None):
        """
        Calls the `POST /user/repos <http://developer.github.com/v3/repos#create>`__ end point.

        This is the only method calling this end point.

        :param name: mandatory :class:`string`
        :param description: optional :class:`string`
        :param homepage: optional :class:`string`
        :param private: optional :class:`bool`
        :param has_issues: optional :class:`bool`
        :param has_wiki: optional :class:`bool`
        :param has_downloads: optional :class:`bool`
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
        if auto_init is not None:
            auto_init = snd.normalizeBool(auto_init)
        if gitignore_template is not None:
            gitignore_template = snd.normalizeGitIgnoreTemplateName(gitignore_template)
        if license_template is not None:
            license_template = snd.normalizeString(license_template)

        url = uritemplate.expand("https://api.github.com/user/repos")
        postArguments = snd.dictionary(name=name, description=description, homepage=homepage, private=private, has_downloads=has_downloads, has_issues=has_issues, has_wiki=has_wiki, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def create_subscription(self, repo, subscribed, ignored):
        """
        Calls the `PUT /repos/:owner/:repo/subscription <http://developer.github.com/v3/activity/watching#set-a-repository-subscription>`__ end point.

        The following methods also call this end point:
          * :meth:`.Subscription.edit`

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :param subscribed: mandatory :class:`bool`
        :param ignored: mandatory :class:`bool`
        :rtype: :class:`.Subscription`
        """
        import PyGithub.Blocking.Subscription

        repo = snd.normalizeRepositoryFullName(repo)
        subscribed = snd.normalizeBool(subscribed)
        ignored = snd.normalizeBool(ignored)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/subscription", owner=repo[0], repo=repo[1])
        postArguments = snd.dictionary(subscribed=subscribed, ignored=ignored)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Subscription.Subscription)(None, r.json(), r.headers.get("ETag"))

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
            name = snd.normalizeStringReset(name)
        if email is not None:
            email = snd.normalizeStringReset(email)
        if blog is not None:
            blog = snd.normalizeStringReset(blog)
        if company is not None:
            company = snd.normalizeStringReset(company)
        if location is not None:
            location = snd.normalizeStringReset(location)
        if hireable is not None:
            hireable = snd.normalizeBoolReset(hireable)

        url = uritemplate.expand("https://api.github.com/user")
        postArguments = snd.dictionary(blog=blog, company=company, email=email, hireable=hireable, location=location, name=name)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

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
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/followers")
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

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
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/following")
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User))(None, r)

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
            since = snd.normalizeDatetime(since)
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/gists")
        urlArguments = snd.dictionary(since=since, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist))(None, r)

    def get_key(self, id):
        """
        Calls the `GET /user/keys/:id <http://developer.github.com/v3/users/keys#get-a-single-public-key>`__ end point.

        This is the only method calling this end point.

        :param id: mandatory :class:`int`
        :rtype: :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        id = snd.normalizeInt(id)

        url = uritemplate.expand("https://api.github.com/user/keys/{id}", id=str(id))
        r = self.Session._request("GET", url)
        return rcv.StructureConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey)(None, r.json(), r.headers.get("ETag"))

    def get_keys(self):
        """
        Calls the `GET /user/keys <http://developer.github.com/v3/users/keys#list-your-public-keys>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`list` of :class:`.PublicKey`
        """
        import PyGithub.Blocking.PublicKey

        url = uritemplate.expand("https://api.github.com/user/keys")
        r = self.Session._request("GET", url)
        return rcv.ListConverter(rcv.StructureConverter(self.Session, PyGithub.Blocking.PublicKey.PublicKey))(None, r.json())

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
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/orgs")
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Organization.Organization))(None, r)

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

        repo = snd.normalizeString(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}", owner=self.login, repo=repo)
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository)(None, r.json(), r.headers.get("ETag"))

    def get_repos(self, sort=None, direction=None, type=None, per_page=None):
        """
        Calls the `GET /user/repos <http://developer.github.com/v3/repos#list-your-repositories>`__ end point.

        This is the only method calling this end point.

        :param sort: optional "created" or "updated" or "pushed" or "full_name"
        :param direction: optional "asc" or "desc"
        :param type: optional "all" or "owner" or "public" or "private" or "member"
        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Repository`
        """
        import PyGithub.Blocking.Repository

        if sort is not None:
            sort = snd.normalizeEnum(sort, "created", "updated", "pushed", "full_name")
        if direction is not None:
            direction = snd.normalizeEnum(direction, "asc", "desc")
        if type is not None:
            type = snd.normalizeEnum(type, "all", "owner", "public", "private", "member")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/repos")
        urlArguments = snd.dictionary(sort=sort, direction=direction, type=type, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

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
            sort = snd.normalizeEnum(sort, "created", "updated")
        if direction is not None:
            direction = snd.normalizeEnum(direction, "asc", "desc")
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/starred")
        urlArguments = snd.dictionary(sort=sort, direction=direction, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

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
            since = snd.normalizeDatetime(since)
        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/gists/starred")
        urlArguments = snd.dictionary(since=since, per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Gist.Gist))(None, r)

    def get_subscription(self, repo):
        """
        Calls the `GET /repos/:owner/:repo/subscription <http://developer.github.com/v3/activity/watching#get-a-repository-subscription>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: :class:`.Subscription`
        """
        import PyGithub.Blocking.Subscription

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/subscription", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.Subscription.Subscription)(None, r.json(), r.headers.get("ETag"))

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
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/subscriptions")
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Repository.Repository))(None, r)

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
            per_page = snd.normalizeInt(per_page)

        url = uritemplate.expand("https://api.github.com/user/teams")
        urlArguments = snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return rcv.PaginatedListConverter(self.Session, rcv.ClassConverter(self.Session, PyGithub.Blocking.Team.Team))(None, r)

    def has_in_following(self, username):
        """
        Calls the `GET /user/following/:username <http://developer.github.com/v3/users/followers#check-if-you-are-following-a-user>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: :class:`bool`
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand("https://api.github.com/user/following/{username}", username=username)
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)

    def has_in_starred(self, repo):
        """
        Calls the `GET /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring#check-if-you-are-starring-a-repository>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: :class:`bool`
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/starred/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)

    def has_in_subscriptions(self, repo):
        """
        Calls the `GET /user/subscriptions/:owner/:repo <http://developer.github.com/v3/activity/watching#check-if-you-are-watching-a-repository-legacy>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: :class:`bool`
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/subscriptions/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("GET", url, accept404=True)
        return rcv.BoolConverter(None, r.status_code == 204)

    def remove_from_following(self, username):
        """
        Calls the `DELETE /user/following/:username <http://developer.github.com/v3/users/followers#unfollow-a-user>`__ end point.

        This is the only method calling this end point.

        :param username: mandatory :class:`.User` or :class:`string` (its :attr:`.User.login`)
        :rtype: None
        """

        username = snd.normalizeUserLogin(username)

        url = uritemplate.expand("https://api.github.com/user/following/{username}", username=username)
        r = self.Session._request("DELETE", url)

    def remove_from_starred(self, repo):
        """
        Calls the `DELETE /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring#unstar-a-repository>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: None
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/starred/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("DELETE", url)

    def remove_from_subscriptions(self, repo):
        """
        Calls the `DELETE /user/subscriptions/:owner/:repo <http://developer.github.com/v3/activity/watching#stop-watching-a-repository-legacy>`__ end point.

        This is the only method calling this end point.

        :param repo: mandatory :class:`.Repository` or :class:`string` or :class:`(string, string)` (its :attr:`.Repository.full_name`)
        :rtype: None
        """

        repo = snd.normalizeRepositoryFullName(repo)

        url = uritemplate.expand("https://api.github.com/user/subscriptions/{owner}/{repo}", owner=repo[0], repo=repo[1])
        r = self.Session._request("DELETE", url)
