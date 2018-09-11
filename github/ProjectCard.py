# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 bbi-yggy <yossarian@blackbirdinteractive.com>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
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

import json

import github.GithubObject

# NOTE: There is currently no way to get cards "in triage" for a project.
# https://platform.github.community/t/moving-github-project-cards-that-are-in-triage/3784
#
# See also https://developer.github.com/v4/object/projectcard for the next generation GitHub API,
# which may point the way to where the API is likely headed and what might come back to v3. E.g. ProjectCard.content member.
class ProjectCard(github.GithubObject.CompletableGithubObject):
    """
    This class represents Project Cards. The reference can be found here https://developer.github.com/v3/projects/cards
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value})

    @property
    def archived(self):
        """
        :type: bool
        """
        return self._archived.value

    @property
    def column_url(self):
        """
        :type: string
        """
        return self._column_url.value

    @property
    def content_url(self):
        """
        :type: string
        """
        return self._content_url.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        return self._created_at.value

    @property
    def creator(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._creator.value

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id.value

    @property
    def node_id(self):
        """
        :type: string
        """
        return self._node_id.value

    @property
    def note(self):
        """
        :type: string
        """
        return self._note.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        return self._updated_at.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    # Note that the content_url for any card will be an "issue" URL, from
    # which you can retrieve either an Issue or a PullRequest. Unforunately
    # the API doesn't make it clear which you are dealing with.
    def get_content(self, content_type=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number <https://developer.github.com/v3/pulls/#get-a-single-pull-request>`_
        :rtype: :class:`github.PullRequest.PullRequest` or :class:`github.Issue.Issue`
        """
        if self.content_url == None:
            return None
            
        if content_type == "PullRequest":
            headers, data = self._requester.requestJsonAndCheck(
                "GET",
                self.content_url.replace("issues", "pulls")
            )
            return github.PullRequest.PullRequest(self._requester, headers, data, completed=True)
        elif content_type is github.GithubObject.NotSet or content_type == "Issue":
            headers, data = self._requester.requestJsonAndCheck(
                "GET",
                self.content_url
            )
            return github.Issue.Issue(self._requester, headers, data, completed=True)
        else:
            assert False, "Unknown content type: %s" % content_type

    def _initAttributes(self):
        self._archived = github.GithubObject.NotSet
        self._column_url = github.GithubObject.NotSet
        self._content_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._creator = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._node_id = github.GithubObject.NotSet
        self._note = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "archived" in attributes:  # pragma no branch
            self._archived = self._makeBoolAttribute(attributes["archived"])
        if "column_url" in attributes:  # pragma no branch
            self._column_url = self._makeStringAttribute(attributes["column_url"])
        if "content_url" in attributes:  # pragma no branch
            self._content_url = self._makeStringAttribute(attributes["content_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "note" in attributes:  # pragma no branch
            self._note = self._makeStringAttribute(attributes["note"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
