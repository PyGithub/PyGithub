############################ Copyrights and license ############################
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

import github.GithubObject


class RepositoryReleaseNotes(github.GithubObject.CompletableGithubObject):
    """
    This class represents a GitHub generated release notes.
    The reference can be found here https://docs.github.com/en/rest/releases/releases#generate-release-notes-content-for-a-release
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "name": self._name.value,
                "body": self._body.value,
            }
        )

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    @property
    def body(self):
        """
        :type: string
        """
        return self._body.value

    def _initAttributes(self):
        self._name = github.GithubObject.NotSet
        self._body = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
