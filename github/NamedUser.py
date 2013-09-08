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

import github.GithubObject
import github.PaginatedList

import github.Gist
import github.Repository
import github.NamedUser
import github.Plan
import github.Organization
import github.Event


class NamedUser(github.GithubObject.CompletableGithubObject):
    """
    This class represents NamedUsers as returned for example by http://developer.github.com/v3/todo
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
    def contributions(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._contributions)
        return self._NoneIfNotSet(self._contributions)

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
    def events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._events_url)
        return self._NoneIfNotSet(self._events_url)

    @property
    def followers(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._followers)
        return self._NoneIfNotSet(self._followers)

    @property
    def followers_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._followers_url)
        return self._NoneIfNotSet(self._followers_url)

    @property
    def following(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._following)
        return self._NoneIfNotSet(self._following)

    @property
    def following_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._following_url)
        return self._NoneIfNotSet(self._following_url)

    @property
    def gists_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._gists_url)
        return self._NoneIfNotSet(self._gists_url)

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
    def organizations_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._organizations_url)
        return self._NoneIfNotSet(self._organizations_url)

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
    def received_events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._received_events_url)
        return self._NoneIfNotSet(self._received_events_url)

    @property
    def repos_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._repos_url)
        return self._NoneIfNotSet(self._repos_url)

    @property
    def starred_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._starred_url)
        return self._NoneIfNotSet(self._starred_url)

    @property
    def subscriptions_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._subscriptions_url)
        return self._NoneIfNotSet(self._subscriptions_url)

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
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    # v2: Remove this method
    def create_gist(self, public, files, description=github.GithubObject.NotSet):
        """
        :calls: `POST /users/:user/gists <http://developer.github.com/v3/todo>`_
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
            self.url + "/gists",
            input=post_parameters
        )
        return github.Gist.Gist(self._requester, headers, data, completed=True)

    def get_events(self):
        """
        :calls: `GET /users/:user/events <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            self.url + "/events",
            None
        )

    def get_followers(self):
        """
        :calls: `GET /users/:user/followers <http://developer.github.com/v3/users/followers>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            NamedUser,
            self._requester,
            self.url + "/followers",
            None
        )

    def get_following(self):
        """
        :calls: `GET /users/:user/following <http://developer.github.com/v3/users/followers>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            NamedUser,
            self._requester,
            self.url + "/following",
            None
        )

    def get_gists(self):
        """
        :calls: `GET /users/:user/gists <http://developer.github.com/v3/gists>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Gist.Gist`
        """
        return github.PaginatedList.PaginatedList(
            github.Gist.Gist,
            self._requester,
            self.url + "/gists",
            None
        )

    def get_keys(self):
        """
        :calls: `GET /users/:user/keys <http://developer.github.com/v3/users/keys>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.UserKey.UserKey`
        """
        return github.PaginatedList.PaginatedList(
            github.UserKey.UserKey,
            self._requester,
            self.url + "/keys",
            None
        )

    def get_orgs(self):
        """
        :calls: `GET /users/:user/orgs <http://developer.github.com/v3/orgs>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Organization.Organization`
        """
        return github.PaginatedList.PaginatedList(
            github.Organization.Organization,
            self._requester,
            self.url + "/orgs",
            None
        )

    def get_public_events(self):
        """
        :calls: `GET /users/:user/events/public <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            self.url + "/events/public",
            None
        )

    def get_public_received_events(self):
        """
        :calls: `GET /users/:user/received_events/public <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            self.url + "/received_events/public",
            None
        )

    def get_received_events(self):
        """
        :calls: `GET /users/:user/received_events <http://developer.github.com/v3/activity/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """
        return github.PaginatedList.PaginatedList(
            github.Event.Event,
            self._requester,
            self.url + "/received_events",
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

    def get_repos(self, type=github.GithubObject.NotSet):
        """
        :calls: `GET /users/:user/repos <http://developer.github.com/v3/repos>`_
        :param type: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert type is github.GithubObject.NotSet or isinstance(type, (str, unicode)), type
        url_parameters = dict()
        if type is not github.GithubObject.NotSet:
            url_parameters["type"] = type
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            self.url + "/repos",
            url_parameters
        )

    def get_starred(self):
        """
        :calls: `GET /users/:user/starred <http://developer.github.com/v3/activity/starring>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            self.url + "/starred",
            None
        )

    def get_subscriptions(self):
        """
        :calls: `GET /users/:user/subscriptions <http://developer.github.com/v3/activity/watching>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            self.url + "/subscriptions",
            None
        )

    def get_watched(self):
        """
        :calls: `GET /users/:user/watched <http://developer.github.com/v3/activity/starring>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            self.url + "/watched",
            None
        )

    def has_in_following(self, following):
        """
        :calls: `GET /users/:user/following/:target_user <http://developer.github.com/v3/users/followers/#check-if-one-user-follows-another>`_
        :param following: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(following, github.NamedUser.NamedUser), following
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/following/" + following._identity
        )
        return status == 204

    @property
    def _identity(self):
        return self.login

    def _initAttributes(self):
        self._avatar_url = github.GithubObject.NotSet
        self._bio = github.GithubObject.NotSet
        self._blog = github.GithubObject.NotSet
        self._collaborators = github.GithubObject.NotSet
        self._company = github.GithubObject.NotSet
        self._contributions = github.GithubObject.NotSet
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
        self._starred_url = github.GithubObject.NotSet
        self._subscriptions_url = github.GithubObject.NotSet
        self._total_private_repos = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
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
        if "contributions" in attributes:  # pragma no branch
            assert attributes["contributions"] is None or isinstance(attributes["contributions"], (int, long)), attributes["contributions"]
            self._contributions = attributes["contributions"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "disk_usage" in attributes:  # pragma no branch
            assert attributes["disk_usage"] is None or isinstance(attributes["disk_usage"], (int, long)), attributes["disk_usage"]
            self._disk_usage = attributes["disk_usage"]
        if "email" in attributes:  # pragma no branch
            assert attributes["email"] is None or isinstance(attributes["email"], (str, unicode)), attributes["email"]
            self._email = attributes["email"]
        if "events_url" in attributes:  # pragma no branch
            assert attributes["events_url"] is None or isinstance(attributes["events_url"], (str, unicode)), attributes["events_url"]
            self._events_url = attributes["events_url"]
        if "followers" in attributes:  # pragma no branch
            assert attributes["followers"] is None or isinstance(attributes["followers"], (int, long)), attributes["followers"]
            self._followers = attributes["followers"]
        if "followers_url" in attributes:  # pragma no branch
            assert attributes["followers_url"] is None or isinstance(attributes["followers_url"], (str, unicode)), attributes["followers_url"]
            self._followers_url = attributes["followers_url"]
        if "following" in attributes:  # pragma no branch
            assert attributes["following"] is None or isinstance(attributes["following"], (int, long)), attributes["following"]
            self._following = attributes["following"]
        if "following_url" in attributes:  # pragma no branch
            assert attributes["following_url"] is None or isinstance(attributes["following_url"], (str, unicode)), attributes["following_url"]
            self._following_url = attributes["following_url"]
        if "gists_url" in attributes:  # pragma no branch
            assert attributes["gists_url"] is None or isinstance(attributes["gists_url"], (str, unicode)), attributes["gists_url"]
            self._gists_url = attributes["gists_url"]
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
        if "organizations_url" in attributes:  # pragma no branch
            assert attributes["organizations_url"] is None or isinstance(attributes["organizations_url"], (str, unicode)), attributes["organizations_url"]
            self._organizations_url = attributes["organizations_url"]
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
        if "received_events_url" in attributes:  # pragma no branch
            assert attributes["received_events_url"] is None or isinstance(attributes["received_events_url"], (str, unicode)), attributes["received_events_url"]
            self._received_events_url = attributes["received_events_url"]
        if "repos_url" in attributes:  # pragma no branch
            assert attributes["repos_url"] is None or isinstance(attributes["repos_url"], (str, unicode)), attributes["repos_url"]
            self._repos_url = attributes["repos_url"]
        if "starred_url" in attributes:  # pragma no branch
            assert attributes["starred_url"] is None or isinstance(attributes["starred_url"], (str, unicode)), attributes["starred_url"]
            self._starred_url = attributes["starred_url"]
        if "subscriptions_url" in attributes:  # pragma no branch
            assert attributes["subscriptions_url"] is None or isinstance(attributes["subscriptions_url"], (str, unicode)), attributes["subscriptions_url"]
            self._subscriptions_url = attributes["subscriptions_url"]
        if "total_private_repos" in attributes:  # pragma no branch
            assert attributes["total_private_repos"] is None or isinstance(attributes["total_private_repos"], (int, long)), attributes["total_private_repos"]
            self._total_private_repos = attributes["total_private_repos"]
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
