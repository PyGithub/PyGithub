# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
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
# ##############################################################################

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
import github.Notification


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
        return self._avatar_url.value

    @property
    def bio(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._bio)
        return self._bio.value

    @property
    def blog(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._blog)
        return self._blog.value

    @property
    def collaborators(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._collaborators)
        return self._collaborators.value

    @property
    def company(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._company)
        return self._company.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def disk_usage(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._disk_usage)
        return self._disk_usage.value

    @property
    def email(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._email)
        return self._email.value

    @property
    def events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    def followers(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._followers)
        return self._followers.value

    @property
    def followers_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._followers_url)
        return self._followers_url.value

    @property
    def following(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._following)
        return self._following.value

    @property
    def following_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._following_url)
        return self._following_url.value

    @property
    def gists_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._gists_url)
        return self._gists_url.value

    @property
    def gravatar_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._gravatar_id)
        return self._gravatar_id.value

    @property
    def hireable(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._hireable)
        return self._hireable.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def location(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._location)
        return self._location.value

    @property
    def login(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def organizations_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._organizations_url)
        return self._organizations_url.value

    @property
    def owned_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._owned_private_repos)
        return self._owned_private_repos.value

    @property
    def plan(self):
        """
        :type: :class:`github.Plan.Plan`
        """
        self._completeIfNotSet(self._plan)
        return self._plan.value

    @property
    def private_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._private_gists)
        return self._private_gists.value

    @property
    def public_gists(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_gists)
        return self._public_gists.value

    @property
    def public_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._public_repos)
        return self._public_repos.value

    @property
    def received_events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._received_events_url)
        return self._received_events_url.value

    @property
    def repos_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._repos_url)
        return self._repos_url.value

    @property
    def site_admin(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._site_admin)
        return self._site_admin.value

    @property
    def starred_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._starred_url)
        return self._starred_url.value

    @property
    def subscriptions_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._subscriptions_url)
        return self._subscriptions_url.value

    @property
    def total_private_repos(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._total_private_repos)
        return self._total_private_repos.value

    @property
    def type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._type)
        return self._type.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

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
            input=post_parameters
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
            "/user/following/" + following._identity
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
            "/user/starred/" + starred._identity
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
            "/user/subscriptions/" + subscription._identity
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
            "/user/watched/" + watched._identity
        )

    def create_authorization(self, scopes=github.GithubObject.NotSet, note=github.GithubObject.NotSet, note_url=github.GithubObject.NotSet, client_id=github.GithubObject.NotSet, client_secret=github.GithubObject.NotSet, onetime_password=None):
        """
        :calls: `POST /authorizations <http://developer.github.com/v3/oauth>`_
        :param scopes: list of string
        :param note: string
        :param note_url: string
        :param client_id: string
        :param client_secret: string
        :param onetime_password: string
        :rtype: :class:`github.Authorization.Authorization`
        """
        assert scopes is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in scopes), scopes
        assert note is github.GithubObject.NotSet or isinstance(note, (str, unicode)), note
        assert note_url is github.GithubObject.NotSet or isinstance(note_url, (str, unicode)), note_url
        assert client_id is github.GithubObject.NotSet or isinstance(client_id, (str, unicode)), client_id
        assert client_secret is github.GithubObject.NotSet or isinstance(client_secret, (str, unicode)), client_secret
        assert onetime_password is None or isinstance(onetime_password, (str, unicode)), onetime_password
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
        if onetime_password is not None:
            request_header = {'X-GitHub-OTP': onetime_password}  # pragma no cover (Should be covered)
        else:
            request_header = None
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "/authorizations",
            input=post_parameters,
            headers=request_header,
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
            "/repos/" + repo.owner.login + "/" + repo.name + "/forks"
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
            input=post_parameters
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
            input=post_parameters
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
            input=post_parameters
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
            input=post_parameters
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
            "/authorizations/" + str(id)
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
            "/user/emails"
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
            "/user/keys/" + str(id)
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
            "/notifications/threads/" + id
        )
        return github.Notification.Notification(self._requester, headers, data, completed=True)

    def get_notifications(self, all=github.GithubObject.NotSet, participating=github.GithubObject.NotSet):
        """
        :calls: `GET /notifications <http://developer.github.com/v3/activity/notifications>`_
        :param all: bool
        :param participating: bool
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
            "/repos/" + self.login + "/" + name
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

    def get_teams(self):
        """
        :calls: `GET /user/teams <http://developer.github.com/v3/orgs/teams>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Team.Team`
        """
        return github.PaginatedList.PaginatedList(
            github.Team.Team,
            self._requester,
            "/user/teams",
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
            "/user/following/" + following._identity
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
            "/user/starred/" + starred._identity
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
            "/user/subscriptions/" + subscription._identity
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
            "/user/watched/" + watched._identity
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
            input=post_parameters
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
            "/user/following/" + following._identity
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
            "/user/starred/" + starred._identity
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
            "/user/subscriptions/" + subscription._identity
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
            "/user/watched/" + watched._identity
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
        self._events_url = github.GithubObject.NotSet
        self._followers = github.GithubObject.NotSet
        self._followers_url = github.GithubObject.NotSet
        self._following = github.GithubObject.NotSet
        self._following_url = github.GithubObject.NotSet
        self._gists_url = github.GithubObject.NotSet
        self._gravatar_id = github.GithubObject.NotSet
        self._hireable = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._location = github.GithubObject.NotSet
        self._login = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._organizations_url = github.GithubObject.NotSet
        self._owned_private_repos = github.GithubObject.NotSet
        self._plan = github.GithubObject.NotSet
        self._private_gists = github.GithubObject.NotSet
        self._public_gists = github.GithubObject.NotSet
        self._public_repos = github.GithubObject.NotSet
        self._received_events_url = github.GithubObject.NotSet
        self._repos_url = github.GithubObject.NotSet
        self._site_admin = github.GithubObject.NotSet
        self._starred_url = github.GithubObject.NotSet
        self._subscriptions_url = github.GithubObject.NotSet
        self._total_private_repos = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "avatar_url" in attributes:  # pragma no branch
            self._avatar_url = self._makeStringAttribute(attributes["avatar_url"])
        if "bio" in attributes:  # pragma no branch
            self._bio = self._makeStringAttribute(attributes["bio"])
        if "blog" in attributes:  # pragma no branch
            self._blog = self._makeStringAttribute(attributes["blog"])
        if "collaborators" in attributes:  # pragma no branch
            self._collaborators = self._makeIntAttribute(attributes["collaborators"])
        if "company" in attributes:  # pragma no branch
            self._company = self._makeStringAttribute(attributes["company"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "disk_usage" in attributes:  # pragma no branch
            self._disk_usage = self._makeIntAttribute(attributes["disk_usage"])
        if "email" in attributes:  # pragma no branch
            self._email = self._makeStringAttribute(attributes["email"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "followers" in attributes:  # pragma no branch
            self._followers = self._makeIntAttribute(attributes["followers"])
        if "followers_url" in attributes:  # pragma no branch
            self._followers_url = self._makeStringAttribute(attributes["followers_url"])
        if "following" in attributes:  # pragma no branch
            self._following = self._makeIntAttribute(attributes["following"])
        if "following_url" in attributes:  # pragma no branch
            self._following_url = self._makeStringAttribute(attributes["following_url"])
        if "gists_url" in attributes:  # pragma no branch
            self._gists_url = self._makeStringAttribute(attributes["gists_url"])
        if "gravatar_id" in attributes:  # pragma no branch
            self._gravatar_id = self._makeStringAttribute(attributes["gravatar_id"])
        if "hireable" in attributes:  # pragma no branch
            self._hireable = self._makeBoolAttribute(attributes["hireable"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "location" in attributes:  # pragma no branch
            self._location = self._makeStringAttribute(attributes["location"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "organizations_url" in attributes:  # pragma no branch
            self._organizations_url = self._makeStringAttribute(attributes["organizations_url"])
        if "owned_private_repos" in attributes:  # pragma no branch
            self._owned_private_repos = self._makeIntAttribute(attributes["owned_private_repos"])
        if "plan" in attributes:  # pragma no branch
            self._plan = self._makeClassAttribute(github.Plan.Plan, attributes["plan"])
        if "private_gists" in attributes:  # pragma no branch
            self._private_gists = self._makeIntAttribute(attributes["private_gists"])
        if "public_gists" in attributes:  # pragma no branch
            self._public_gists = self._makeIntAttribute(attributes["public_gists"])
        if "public_repos" in attributes:  # pragma no branch
            self._public_repos = self._makeIntAttribute(attributes["public_repos"])
        if "received_events_url" in attributes:  # pragma no branch
            self._received_events_url = self._makeStringAttribute(attributes["received_events_url"])
        if "repos_url" in attributes:  # pragma no branch
            self._repos_url = self._makeStringAttribute(attributes["repos_url"])
        if "site_admin" in attributes:  # pragma no branch
            self._site_admin = self._makeBoolAttribute(attributes["site_admin"])
        if "starred_url" in attributes:  # pragma no branch
            self._starred_url = self._makeStringAttribute(attributes["starred_url"])
        if "subscriptions_url" in attributes:  # pragma no branch
            self._subscriptions_url = self._makeStringAttribute(attributes["subscriptions_url"])
        if "total_private_repos" in attributes:  # pragma no branch
            self._total_private_repos = self._makeIntAttribute(attributes["total_private_repos"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
