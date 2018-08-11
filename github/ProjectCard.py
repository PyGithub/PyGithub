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

    # TODO: get issue if present, not just pull request
    def get_content(self):
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
        self._id = github.GithubObject.NotSet
        self._note = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "note" in attributes:  # pragma no branch
            self._note = self._makeStringAttribute(attributes["note"])
