# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Michael Stead <michael.stead@gmail.com>                       #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
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

import github.NamedUser


class PullRequestComment(github.GithubObject.CompletableGithubObject):
    """
    This class represents PullRequestComments. The reference can be found here http://developer.github.com/v3/pulls/comments/
    """

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._NoneIfNotSet(self._body)

    @property
    def commit_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commit_id)
        return self._NoneIfNotSet(self._commit_id)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def diff_hunk(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._diff_hunk)
        return self._NoneIfNotSet(self._diff_hunk)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def original_commit_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._original_commit_id)
        return self._NoneIfNotSet(self._original_commit_id)

    @property
    def original_position(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._original_position)
        return self._NoneIfNotSet(self._original_position)

    @property
    def path(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._path)
        return self._NoneIfNotSet(self._path)

    @property
    def position(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._position)
        return self._NoneIfNotSet(self._position)

    @property
    def pull_request_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._pull_request_url)
        return self._NoneIfNotSet(self._pull_request_url)

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

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._user)
        return self._NoneIfNotSet(self._user)

    def delete(self):
        """
        :calls: `DELETE /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url
        )

    def edit(self, body):
        """
        :calls: `PATCH /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments>`_
        :param body: string
        :rtype: None
        """
        assert isinstance(body, (str, unicode)), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._body = github.GithubObject.NotSet
        self._commit_id = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._diff_hunk = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._original_commit_id = github.GithubObject.NotSet
        self._original_position = github.GithubObject.NotSet
        self._path = github.GithubObject.NotSet
        self._position = github.GithubObject.NotSet
        self._pull_request_url = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "body" in attributes:  # pragma no branch
            assert attributes["body"] is None or isinstance(attributes["body"], (str, unicode)), attributes["body"]
            self._body = attributes["body"]
        if "commit_id" in attributes:  # pragma no branch
            assert attributes["commit_id"] is None or isinstance(attributes["commit_id"], (str, unicode)), attributes["commit_id"]
            self._commit_id = attributes["commit_id"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "diff_hunk" in attributes:  # pragma no branch
            assert attributes["diff_hunk"] is None or isinstance(attributes["diff_hunk"], (str, unicode)), attributes["diff_hunk"]
            self._diff_hunk = attributes["diff_hunk"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "original_commit_id" in attributes:  # pragma no branch
            assert attributes["original_commit_id"] is None or isinstance(attributes["original_commit_id"], (str, unicode)), attributes["original_commit_id"]
            self._original_commit_id = attributes["original_commit_id"]
        if "original_position" in attributes:  # pragma no branch
            assert attributes["original_position"] is None or isinstance(attributes["original_position"], (int, long)), attributes["original_position"]
            self._original_position = attributes["original_position"]
        if "path" in attributes:  # pragma no branch
            assert attributes["path"] is None or isinstance(attributes["path"], (str, unicode)), attributes["path"]
            self._path = attributes["path"]
        if "position" in attributes:  # pragma no branch
            assert attributes["position"] is None or isinstance(attributes["position"], (int, long)), attributes["position"]
            self._position = attributes["position"]
        if "pull_request_url" in attributes:  # pragma no branch
            assert attributes["pull_request_url"] is None or isinstance(attributes["pull_request_url"], (str, unicode)), attributes["pull_request_url"]
            self._pull_request_url = attributes["pull_request_url"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "user" in attributes:  # pragma no branch
            assert attributes["user"] is None or isinstance(attributes["user"], dict), attributes["user"]
            self._user = None if attributes["user"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["user"], completed=False)
