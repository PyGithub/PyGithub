# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import datetime

import github.GithubObject
import github.PaginatedList

import github.Gist
import github.Repository
import github.NamedUser
import github.Plan
import github.Organization
import github.UserKey
import github.Issue
import github.Event
import github.Authorization


class AuthenticatedUser(github.GithubObject.CompletableGithubObject):
    """
    This class represents AuthenticatedUsers as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def avatar_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._avatar_url)
        return self._NoneIfNotSet(self._avatar_url)

    @property
    def bio(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._bio)
        return self._NoneIfNotSet(self._bio)

    @property
    def blog(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._blog)
        return self._NoneIfNotSet(self._blog)

    @property
    def collaborators(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._collaborators)
        return self._NoneIfNotSet(self._collaborators)

    @property
    def company(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._company)
        return self._NoneIfNotSet(self._company)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def disk_usage(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._disk_usage)
        return self._NoneIfNotSet(self._disk_usage)

    @property
    def email(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._email)
        return self._NoneIfNotSet(self._email)

    @property
    def followers(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._followers)
        return self._NoneIfNotSet(self._followers)

    @property
    def following(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._following)
        return self._NoneIfNotSet(self._following)

    @property
    def gravatar_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._gravatar_id)
        return self._NoneIfNotSet(self._gravatar_id)

    @property
    def hireable(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._hireable)
        return self._NoneIfNotSet(self._hireable)

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def location(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._location)
        return self._NoneIfNotSet(self._location)

    @property
    def login(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._login)
        return self._NoneIfNotSet(self._login)

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def owned_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._owned_private_repos)
        return self._NoneIfNotSet(self._owned_private_repos)

    @property
    def plan(self):
        """
        :type: :class:`github.Plan.Plan`
        """
        self._completeIfNotSet(self._plan)
        return self._NoneIfNotSet(self._plan)

    @property
    def private_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._private_gists)
        return self._NoneIfNotSet(self._private_gists)

    @property
    def public_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_gists)
        return self._NoneIfNotSet(self._public_gists)

    @property
    def public_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_repos)
        return self._NoneIfNotSet(self._public_repos)

    @property
    def total_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._total_private_repos)
        return self._NoneIfNotSet(self._total_private_repos)

    @property
    def type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._type)
        return self._NoneIfNotSet(self._type)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def add_to_emails(self, *emails):
        """
        :calls: `POST /user/emails <http://developer.github.com/v3/users/emails>`_
        :param email: string
        :rtype: None
        """
        assert all(isinstance(element, (str, unicode)) for element in emails), emails
        post_parameters = emails
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/user/emails",
            None,
            None,
            post_parameters
        )

    def add_to_following(self, following):
        """
        :calls: `PUT /user/following/:user <http://developer.github.com/v3/users/followers>`_
        :param following: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            "/user/following/" + following._identity,
            None,
            None,
            None
        )

    def add_to_starred(self, starred):
        """
        :calls: `PUT /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring>`_
        :param starred: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(starred, github.Repository.Repository), starred
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            "/user/starred/" + starred._identity,
            None,
            None,
            None
        )

    def add_to_subscriptions(self, subscription):
        """
        :calls: `PUT /user/subscriptions/:owner/:repo <http://developer.github.com/v3/activity/watching>`_
        :param subscription: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(subscription, github.Repository.Repository), subscription
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            "/user/subscriptions/" + subscription._identity,
            None,
            None,
            None
        )

    def add_to_watched(self, watched):
        """
        :calls: `PUT /user/watched/:owner/:repo <http://developer.github.com/v3/activity/starring>`_
        :param watched: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(watched, github.Repository.Repository), watched
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            "/user/watched/" + watched._identity,
            None,
            None,
            None
        )

    def create_authorization(self, scopes=github.GithubObject.NotSet, note=github.GithubObject.NotSet, note_url=github.GithubObject.NotSet, client_id=github.GithubObject.NotSet, client_secret=github.GithubObject.NotSet):
        """
        :calls: `POST /authorizations <http://developer.github.com/v3/oauth>`_
        :param scopes: list of string
        :param note: string
        :param note_url: string
        :param client_id: string
        :param client_secret: string
        :rtype: :class:`github.Authorization.Authorization`
        """
        assert scopes is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in scopes), scopes
        assert note is github.GithubObject.NotSet or isinstance(note, (str, unicode)), note
        assert note_url is github.GithubObject.NotSet or isinstance(note_url, (str, unicode)), note_url
        assert client_id is github.GithubObject.NotSet or isinstance(client_id, (str, unicode)), client_id
        assert client_secret is github.GithubObject.NotSet or isinstance(client_secret, (str, unicode)), client_secret
        post_parameters = dict()
        if scopes is not github.GithubObject.NotSet:
            post_parameters["scopes"] = scopes
        if note is not github.GithubObject.NotSet:
            post_parameters["note"] = note
        if note_url is not github.GithubObject.NotSet:
            post_parameters["note_url"] = note_url
        if client_id is not github.GithubObject.NotSet:
            post_parameters["client_id"] = client_id
        if client_secret is not github.GithubObject.NotSet:
            post_parameters["client_secret"] = client_secret
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/authorizations",
            None,
            None,
            post_parameters
        )
        return github.Authorization.Authorization(self._requester, headers, data, completed=True)

    def create_fork(self, repo):
        """
        :calls: `POST /repos/:owner/:repo/forks <http://developer.github.com/v3/repos/forks>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(repo, github.Repository.Repository), repo
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/repos/" + repo.owner.login + "/" + repo.name + "/forks",
            None,
            None,
            None
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def create_gist(self, public, files, description=github.GithubObject.NotSet):
        """
        :calls: `POST /gists <http://developer.github.com/v3/gists>`_
        :param public: bool
        :param files: dict of string to :class:`github.InputFileContent.InputFileContent`
        :param description: string
        :rtype: :class:`github.Gist.Gist`
        """
        assert isinstance(public, bool), public
        assert all(isinstance(element, github.InputFileContent) for element in files.itervalues()), files
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        post_parameters = {
            "public": public,
            "files": dict((key, value._identity) for key, value in files.iteritems()),
        }
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/gists",
            None,
            None,
            post_parameters
        )
        return github.Gist.Gist(self._requester, headers, data, completed=True)

    def create_key(self, title, key):
        """
        :calls: `POST /user/keys <http://developer.github.com/v3/users/keys>`_
        :param title: string
        :param key: string
        :rtype: :class:`github.UserKey.UserKey`
        """
        assert isinstance(title, (str, unicode)), title
        assert isinstance(key, (str, unicode)), key
        post_parameters = {
            "title": title,
            "key": key,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/user/keys",
            None,
            None,
            post_parameters
        )
        return github.UserKey.UserKey(self._requester, headers, data, completed=True)

    def create_repo(self, name, description=github.GithubObject.NotSet, homepage=github.GithubObject.NotSet, private=github.GithubObject.NotSet, has_issues=github.GithubObject.NotSet, has_wiki=github.GithubObject.NotSet, has_downloads=github.GithubObject.NotSet, auto_init=github.GithubObject.NotSet, gitignore_template=github.GithubObject.NotSet):
        """
        :calls: `POST /user/repos <http://developer.github.com/v3/repos>`_
        :param name: string
        :param description: string
        :param homepage: string
        :param private: bool
        :param has_issues: bool
        :param has_wiki: bool
        :param has_downloads: bool
        :param auto_init: bool
        :param gitignore_template: string
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(name, (str, unicode)), name
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert homepage is github.GithubObject.NotSet or isinstance(homepage, (str, unicode)), homepage
        assert private is github.GithubObject.NotSet or isinstance(private, bool), private
        assert has_issues is github.GithubObject.NotSet or isinstance(has_issues, bool), has_issues
        assert has_wiki is github.GithubObject.NotSet or isinstance(has_wiki, bool), has_wiki
        assert has_downloads is github.GithubObject.NotSet or isinstance(has_downloads, bool), has_downloads
        assert auto_init is github.GithubObject.NotSet or isinstance(auto_init, bool), auto_init
        assert gitignore_template is github.GithubObject.NotSet or isinstance(gitignore_template, (str, unicode)), gitignore_template
        post_parameters = {
            "name": name,
        }
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if homepage is not github.GithubObject.NotSet:
            post_parameters["homepage"] = homepage
        if private is not github.GithubObject.NotSet:
            post_parameters["private"] = private
        if has_issues is not github.GithubObject.NotSet:
            post_parameters["has_issues"] = has_issues
        if has_wiki is not github.GithubObject.NotSet:
            post_parameters["has_wiki"] = has_wiki
        if has_downloads is not github.GithubObject.NotSet:
            post_parameters["has_downloads"] = has_downloads
        if auto_init is not github.GithubObject.NotSet:
            post_parameters["auto_init"] = auto_init
        if gitignore_template is not github.GithubObject.NotSet:
            post_parameters["gitignore_template"] = gitignore_template
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/user/repos",
            None,
            None,
            post_parameters
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def edit(self, name=github.GithubObject.NotSet, email=github.GithubObject.NotSet, blog=github.GithubObject.NotSet, company=github.GithubObject.NotSet, location=github.GithubObject.NotSet, hireable=github.GithubObject.NotSet, bio=github.GithubObject.NotSet):
        """
        :calls: `PATCH /user <http://developer.github.com/v3/users>`_
        :param name: string
        :param email: string
        :param blog: string
        :param company: string
        :param location: string
        :param hireable: bool
        :param bio: string
        :rtype: None
        """
        assert name is github.GithubObject.NotSet or isinstance(name, (str, unicode)), name
        assert email is github.GithubObject.NotSet or isinstance(email, (str, unicode)), email
        assert blog is github.GithubObject.NotSet or isinstance(blog, (str, unicode)), blog
        assert company is github.GithubObject.NotSet or isinstance(company, (str, unicode)), company
        assert location is github.GithubObject.NotSet or isinstance(location, (str, unicode)), location
        assert hireable is github.GithubObject.NotSet or isinstance(hireable, bool), hireable
        assert bio is github.GithubObject.NotSet or isinstance(bio, (str, unicode)), bio
        post_parameters = dict()
        if name is not github.GithubObject.NotSet:
            post_parameters["name"] = name
        if email is not github.GithubObject.NotSet:
            post_parameters["email"] = email
        if blog is not github.GithubObject.NotSet:
            post_parameters["blog"] = blog
        if company is not github.GithubObject.NotSet:
            post_parameters["company"] = company
        if location is not github.GithubObject.NotSet:
            post_parameters["location"] = location
        if hireable is not github.GithubObject.NotSet:
            post_parameters["hireable"] = hireable
        if bio is not github.GithubObject.NotSet:
            post_parameters["bio"] = bio
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            "/user",
            None,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_authorization(self, id):
        """
        :calls: `GET /authorizations/:id <http://developer.github.com/v3/oauth>`_
        :param id: integer
        :rtype: :class:`github.Authorization.Authorization`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/authorizations/" + str(id),
            None,
            None,
            None
        )
        return github.Authorization.Authorization(self._requester, headers, data, completed=True)

    def get_authorizations(self):
        """
        :calls: `GET /authorizations <http://developer.github.com/v3/oauth>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Authorization.Authorization`
        """
        return github.PaginatedList.PaginatedList(
            github.Authorization.Authorization,
            self._requester,
            "/authorizations",
            None
        )

    def get_emails(self):
        """
        :calls: `GET /user/emails <http://developer.github.com/v3/users/emails>`_
        :rtype: list of string
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/user/emails",
            None,
            None,
            None
        )
        return data

    def get_events(self):
        """
        :calls: `GET /events <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            "/events",
            None
        )

    def get_followers(self):
        """
        :calls: `GET /user/followers <http://developer.github.com/v3/users/followers>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            "/user/followers",
            None
        )

    def get_following(self):
        """
        :calls: `GET /user/following <http://developer.github.com/v3/users/followers>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            "/user/following",
            None
        )

    def get_gists(self):
        """
        :calls: `GET /gists <http://developer.github.com/v3/gists>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Gist.Gist`
        """
        return github.PaginatedList.PaginatedList(
            github.Gist.Gist,
            self._requester,
            "/gists",
            None
        )

    def get_issues(self, filter=github.GithubObject.NotSet, state=github.GithubObject.NotSet, labels=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /issues <http://developer.github.com/v3/issues>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        :param filter: string
        :param state: string
        :param labels: list of :class:`github.Label.Label`
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert filter is github.GithubObject.NotSet or isinstance(filter, (str, unicode)), filter
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert labels is github.GithubObject.NotSet or all(isinstance(element, github.Label.Label) for element in labels), labels
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if filter is not github.GithubObject.NotSet:
            url_parameters["filter"] = filter
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        if labels is not github.GithubObject.NotSet:
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.Issue.Issue,
            self._requester,
            "/issues",
            url_parameters
        )

    def get_user_issues(self, filter=github.GithubObject.NotSet, state=github.GithubObject.NotSet, labels=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet, since=github.GithubObject.NotSet):
        """
        :calls: `GET /user/issues <http://developer.github.com/v3/issues>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        :param filter: string
        :param state: string
        :param labels: list of :class:`github.Label.Label`
        :param sort: string
        :param direction: string
        :param since: datetime.datetime
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert filter is github.GithubObject.NotSet or isinstance(filter, (str, unicode)), filter
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert labels is github.GithubObject.NotSet or all(isinstance(element, github.Label.Label) for element in labels), labels
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        assert since is github.GithubObject.NotSet or isinstance(since, datetime.datetime), since
        url_parameters = dict()
        if filter is not github.GithubObject.NotSet:
            url_parameters["filter"] = filter
        if state is not github.GithubObject.NotSet:
            url_parameters["state"] = state
        if labels is not github.GithubObject.NotSet:
            url_parameters["labels"] = ",".join(label.name for label in labels)
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.Issue.Issue,
            self._requester,
            "/issues",
            url_parameters
        )

    def get_key(self, id):
        """
        :calls: `GET /user/keys/:id <http://developer.github.com/v3/users/keys>`_
        :param id: integer
        :rtype: :class:`github.UserKey.UserKey`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/user/keys/" + str(id),
            None,
            None,
            None
        )
        return github.UserKey.UserKey(self._requester, headers, data, completed=True)

    def get_keys(self):
        """
        :calls: `GET /user/keys <http://developer.github.com/v3/users/keys>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.UserKey.UserKey`
        """
        return github.PaginatedList.PaginatedList(
            github.UserKey.UserKey,
            self._requester,
            "/user/keys",
            None
        )

    def get_notification(self, id):
        """
        :calls: `GET /notifications/threads/:id <http://developer.github.com/v3/activity/notifications>`_
        :rtype: :class:`github.Notification.Notification`
        """

        assert isinstance(id, (str, unicode)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/notifications/threads/" + id,
            None,
            None,
            None
        )
        return github.Notification.Notification(self._requester, headers, data, completed=True)

    def get_notifications(self, all=github.GithubObject.NotSet, participating=github.GithubObject.NotSet):
        """
        :calls: `GET /notifications <http://developer.github.com/v3/activity/notifications>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Notification.Notification`
        """

        assert all is github.GithubObject.NotSet or isinstance(all, bool), all
        assert participating is github.GithubObject.NotSet or isinstance(participating, bool), participating

        params = dict()
        if all is not github.GithubObject.NotSet:
            params["all"] = all
        if participating is not github.GithubObject.NotSet:
            params["participating"] = participating
        # TODO: implement parameter "since"

        return github.PaginatedList.PaginatedList(
            github.Notification.Notification,
            self._requester,
            "/notifications",
            params
        )

    def get_organization_events(self, org):
        """
        :calls: `GET /users/:user/events/orgs/:org <http://developer.github.com/v3/activity/events>`_
        :param org: :class:`github.Organization.Organization`
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        assert isinstance(org, github.Organization.Organization), org
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            "/users/" + self.login + "/events/orgs/" + org.login,
            None
        )

    def get_orgs(self):
        """
        :calls: `GET /user/orgs <http://developer.github.com/v3/orgs>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Organization.Organization`
        """
        return github.PaginatedList.PaginatedList(
            github.Organization.Organization,
            self._requester,
            "/user/orgs",
            None
        )

    def get_repo(self, name):
        """
        :calls: `GET /repos/:owner/:repo <http://developer.github.com/v3/repos>`_
        :param name: string
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(name, (str, unicode)), name
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            "/repos/" + self.login + "/" + name,
            None,
            None,
            None
        )
        return github.Repository.Repository(self._requester, headers, data, completed=True)

    def get_repos(self, type=github.GithubObject.NotSet, sort=github.GithubObject.NotSet, direction=github.GithubObject.NotSet):
        """
        :calls: `GET /user/repos <http://developer.github.com/v3/repos>`_
        :param type: string
        :param sort: string
        :param direction: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert type is github.GithubObject.NotSet or isinstance(type, (str, unicode)), type
        assert sort is github.GithubObject.NotSet or isinstance(sort, (str, unicode)), sort
        assert direction is github.GithubObject.NotSet or isinstance(direction, (str, unicode)), direction
        url_parameters = dict()
        if type is not github.GithubObject.NotSet:
            url_parameters["type"] = type
        if sort is not github.GithubObject.NotSet:
            url_parameters["sort"] = sort
        if direction is not github.GithubObject.NotSet:
            url_parameters["direction"] = direction
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            "/user/repos",
            url_parameters
        )

    def get_starred(self):
        """
        :calls: `GET /user/starred <http://developer.github.com/v3/activity/starring>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            "/user/starred",
            None
        )

    def get_starred_gists(self):
        """
        :calls: `GET /gists/starred <http://developer.github.com/v3/gists>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Gist.Gist`
        """
        return github.PaginatedList.PaginatedList(
            github.Gist.Gist,
            self._requester,
            "/gists/starred",
            None
        )

    def get_subscriptions(self):
        """
        :calls: `GET /user/subscriptions <http://developer.github.com/v3/activity/watching>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            "/user/subscriptions",
            None
        )

    def get_watched(self):
        """
        :calls: `GET /user/watched <http://developer.github.com/v3/activity/starring>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            "/user/watched",
            None
        )

    def has_in_following(self, following):
        """
        :calls: `GET /user/following/:user <http://developer.github.com/v3/users/followers>`_
        :param following: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        status, headers, data = self._requester.requestJson(
            "GET",
            "/user/following/" + following._identity,
            None,
            None,
            None
        )
        return status == 204

    def has_in_starred(self, starred):
        """
        :calls: `GET /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring>`_
        :param starred: :class:`github.Repository.Repository`
        :rtype: bool
        """
        assert isinstance(starred, github.Repository.Repository), starred
        status, headers, data = self._requester.requestJson(
            "GET",
            "/user/starred/" + starred._identity,
            None,
            None,
            None
        )
        return status == 204

    def has_in_subscriptions(self, subscription):
        """
        :calls: `GET /user/subscriptions/:owner/:repo <http://developer.github.com/v3/activity/watching>`_
        :param subscription: :class:`github.Repository.Repository`
        :rtype: bool
        """
        assert isinstance(subscription, github.Repository.Repository), subscription
        status, headers, data = self._requester.requestJson(
            "GET",
            "/user/subscriptions/" + subscription._identity,
            None,
            None,
            None
        )
        return status == 204

    def has_in_watched(self, watched):
        """
        :calls: `GET /user/watched/:owner/:repo <http://developer.github.com/v3/activity/starring>`_
        :param watched: :class:`github.Repository.Repository`
        :rtype: bool
        """
        assert isinstance(watched, github.Repository.Repository), watched
        status, headers, data = self._requester.requestJson(
            "GET",
            "/user/watched/" + watched._identity,
            None,
            None,
            None
        )
        return status == 204

    def remove_from_emails(self, *emails):
        """
        :calls: `DELETE /user/emails <http://developer.github.com/v3/users/emails>`_
        :param email: string
        :rtype: None
        """
        assert all(isinstance(element, (str, unicode)) for element in emails), emails
        post_parameters = emails
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            "/user/emails",
            None,
            None,
            post_parameters
        )

    def remove_from_following(self, following):
        """
        :calls: `DELETE /user/following/:user <http://developer.github.com/v3/users/followers>`_
        :param following: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            "/user/following/" + following._identity,
            None,
            None,
            None
        )

    def remove_from_starred(self, starred):
        """
        :calls: `DELETE /user/starred/:owner/:repo <http://developer.github.com/v3/activity/starring>`_
        :param starred: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(starred, github.Repository.Repository), starred
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            "/user/starred/" + starred._identity,
            None,
            None,
            None
        )

    def remove_from_subscriptions(self, subscription):
        """
        :calls: `DELETE /user/subscriptions/:owner/:repo <http://developer.github.com/v3/activity/watching>`_
        :param subscription: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(subscription, github.Repository.Repository), subscription
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            "/user/subscriptions/" + subscription._identity,
            None,
            None,
            None
        )

    def remove_from_watched(self, watched):
        """
        :calls: `DELETE /user/watched/:owner/:repo <http://developer.github.com/v3/activity/starring>`_
        :param watched: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(watched, github.Repository.Repository), watched
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            "/user/watched/" + watched._identity,
            None,
            None,
            None
        )

    def _initAttributes(self):
        self._avatar_url = github.GithubObject.NotSet
        self._bio = github.GithubObject.NotSet
        self._blog = github.GithubObject.NotSet
        self._collaborators = github.GithubObject.NotSet
        self._company = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._disk_usage = github.GithubObject.NotSet
        self._email = github.GithubObject.NotSet
        self._followers = github.GithubObject.NotSet
        self._following = github.GithubObject.NotSet
        self._gravatar_id = github.GithubObject.NotSet
        self._hireable = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._location = github.GithubObject.NotSet
        self._login = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._owned_private_repos = github.GithubObject.NotSet
        self._plan = github.GithubObject.NotSet
        self._private_gists = github.GithubObject.NotSet
        self._public_gists = github.GithubObject.NotSet
        self._public_repos = github.GithubObject.NotSet
        self._total_private_repos = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "avatar_url" in attributes:  # pragma no branch
            assert attributes["avatar_url"] is None or isinstance(attributes["avatar_url"], (str, unicode)), attributes["avatar_url"]
            self._avatar_url = attributes["avatar_url"]
        if "bio" in attributes:  # pragma no branch
            assert attributes["bio"] is None or isinstance(attributes["bio"], (str, unicode)), attributes["bio"]
            self._bio = attributes["bio"]
        if "blog" in attributes:  # pragma no branch
            assert attributes["blog"] is None or isinstance(attributes["blog"], (str, unicode)), attributes["blog"]
            self._blog = attributes["blog"]
        if "collaborators" in attributes:  # pragma no branch
            assert attributes["collaborators"] is None or isinstance(attributes["collaborators"], (int, long)), attributes["collaborators"]
            self._collaborators = attributes["collaborators"]
        if "company" in attributes:  # pragma no branch
            assert attributes["company"] is None or isinstance(attributes["company"], (str, unicode)), attributes["company"]
            self._company = attributes["company"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "disk_usage" in attributes:  # pragma no branch
            assert attributes["disk_usage"] is None or isinstance(attributes["disk_usage"], (int, long)), attributes["disk_usage"]
            self._disk_usage = attributes["disk_usage"]
        if "email" in attributes:  # pragma no branch
            assert attributes["email"] is None or isinstance(attributes["email"], (str, unicode)), attributes["email"]
            self._email = attributes["email"]
        if "followers" in attributes:  # pragma no branch
            assert attributes["followers"] is None or isinstance(attributes["followers"], (int, long)), attributes["followers"]
            self._followers = attributes["followers"]
        if "following" in attributes:  # pragma no branch
            assert attributes["following"] is None or isinstance(attributes["following"], (int, long)), attributes["following"]
            self._following = attributes["following"]
        if "gravatar_id" in attributes:  # pragma no branch
            assert attributes["gravatar_id"] is None or isinstance(attributes["gravatar_id"], (str, unicode)), attributes["gravatar_id"]
            self._gravatar_id = attributes["gravatar_id"]
        if "hireable" in attributes:  # pragma no branch
            assert attributes["hireable"] is None or isinstance(attributes["hireable"], bool), attributes["hireable"]
            self._hireable = attributes["hireable"]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "location" in attributes:  # pragma no branch
            assert attributes["location"] is None or isinstance(attributes["location"], (str, unicode)), attributes["location"]
            self._location = attributes["location"]
        if "login" in attributes:  # pragma no branch
            assert attributes["login"] is None or isinstance(attributes["login"], (str, unicode)), attributes["login"]
            self._login = attributes["login"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "owned_private_repos" in attributes:  # pragma no branch
            assert attributes["owned_private_repos"] is None or isinstance(attributes["owned_private_repos"], (int, long)), attributes["owned_private_repos"]
            self._owned_private_repos = attributes["owned_private_repos"]
        if "plan" in attributes:  # pragma no branch
            assert attributes["plan"] is None or isinstance(attributes["plan"], dict), attributes["plan"]
            self._plan = None if attributes["plan"] is None else github.Plan.Plan(self._requester, self._headers, attributes["plan"], completed=False)
        if "private_gists" in attributes:  # pragma no branch
            assert attributes["private_gists"] is None or isinstance(attributes["private_gists"], (int, long)), attributes["private_gists"]
            self._private_gists = attributes["private_gists"]
        if "public_gists" in attributes:  # pragma no branch
            assert attributes["public_gists"] is None or isinstance(attributes["public_gists"], (int, long)), attributes["public_gists"]
            self._public_gists = attributes["public_gists"]
        if "public_repos" in attributes:  # pragma no branch
            assert attributes["public_repos"] is None or isinstance(attributes["public_repos"], (int, long)), attributes["public_repos"]
            self._public_repos = attributes["public_repos"]
        if "total_private_repos" in attributes:  # pragma no branch
            assert attributes["total_private_repos"] is None or isinstance(attributes["total_private_repos"], (int, long)), attributes["total_private_repos"]
            self._total_private_repos = attributes["total_private_repos"]
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
