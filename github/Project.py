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


# TODO: remaining Project properties
class Project(github.GithubObject.CompletableGithubObject):
    """
    This class represents Projects. The reference can be found here http://developer.github.com/v3/projects
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value})

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def creator(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._creator)
        return self._creator.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def number(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._number)
        return self._number.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def get_columns(self):
        """
        :calls: `GET /projects/:project_id/columns <https://developer.github.com/v3/projects/columns/#list-project-columns>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`ProjectColumn`
        """
        # 'Accept' header required while Github Projects API still in preview mode.
        headers = { 'Accept': "application/vnd.github.inertia-preview+json" }
        
        return github.PaginatedList.PaginatedList(
            ProjectColumn,
            self._requester,
            self.url + "/columns",
            None,
            headers
        )

    def _initAttributes(self):
        self._body = github.GithubObject.NotSet
        self._creator = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._number = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])

# TODO: remaining ProjectColumn properties
class ProjectColumn(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Project Columns. The reference can be found here http://developer.github.com/v3/projects/columns
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value})

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id.value

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    def get_cards(self,archived_state=github.GithubObject.NotSet):
        """
        :calls: `GET /projects/columns/:column_id/cards <https://developer.github.com/v3/projects/cards/#list-project-cards>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`ProjectCard`
        :param archived_state: string
        """
        assert archived_state is github.GithubObject.NotSet or isinstance(archived_state, (str, unicode)), archived_state
        
        url_parameters = dict()
        if archived_state is not github.GithubObject.NotSet:
            url_parameters["archived_state"] = archived_state
        
        # 'Accept' header required while Github Projects API still in preview mode.
        headers = { 'Accept': "application/vnd.github.inertia-preview+json" }
        
        return github.PaginatedList.PaginatedList(
            ProjectCard,
            self._requester,
            self.url + "/cards",
            url_parameters,
            headers
        )
        
    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])

# TODO: remaining ProjectCard properties
# NOTE: There is currently no current way to get cards "in triage" for a project.
# https://platform.github.community/t/moving-github-project-cards-that-are-in-triage/3784
#
# See also https://developer.github.com/v4/reference/object/projectcard for the next generation GitHub API,
# which may point the way to where the API is likely headed and what might come back to v3. E.g. ProjectCard.content member.
class ProjectCard(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Project Cards. The reference can be found here https://developer.github.com/v3/projects/cards
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value})

    # content_type is not a property of a returned card, but this property
    # is consistent with the parameters provided when creating cards, see:
    # https://developer.github.com/v3/projects/cards/#create-a-project-card
    @property
    def content_type(self):
        """
        :type: string
        """
        if not self.content_url:
            return None
        elif "/issues/" in self.content_url:
            return "Issue"
        elif "/pulls/" in self.content_url:
            return "PullRequest"
        else:
            return "Unknown"
            
    @property
    def content_url(self):
        """
        :type: string
        """
        return self._content_url.value
       
    @property
    def id(self):
        """
        :type: integer
        """
        return self._id.value

    @property
    def note(self):
        """
        :type: string
        """
        return self._note.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    # TODO: get issue from card, not just pull request ("get_content" method?)
    def get_pullrequest(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number <https://developer.github.com/v3/pulls/#get-a-single-pull-request>`_
        :rtype: :class:`github.PullRequest.PullRequest`
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.content_url
        )
        return github.PullRequest.PullRequest(self._requester, headers, data, completed=True)

    def _initAttributes(self):
        self._content_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._note = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "content_url" in attributes:  # pragma no branch
            self._content_url = self._makeStringAttribute(attributes["content_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "note" in attributes:  # pragma no branch
            self._note = self._makeStringAttribute(attributes["note"])
        if "url" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["url"])
