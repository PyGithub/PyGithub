############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
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

import github.DependabotAlertDependencyPackage
import github.GithubObject
import github.NamedUser
import github.PaginatedList


class DependabotAlertDependency(github.GithubObject.NonCompletableGithubObject):

    def __repr__(self):
        return self.get__repr__({"package": self.package,
                                 "manifest_path": self.manifest_path,
                                 "scope": self.scope})

    @property
    def manifest_path(self):
        """
        :type: str
        """
        return self._manifest_path.value

    @property
    def scope(self):
        """
        :type: str
        """
        return self._scope.value

    @property
    def package(self):
        """
        :type: :class: github.DependabotAlertDependencyPackage.DependabotAlertDependencyPackage
        """
        return self._package.value

    def _initAttributes(self):
        self._manifest_path = github.GithubObject.NotSet
        self._scope = github.GithubObject.NotSet

        self._package = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "manifest_path" in attributes:  # pragma no branch
            self._manifest_path = self._makeStringAttribute(attributes["manifest_path"])
        if "scope" in attributes:  # pragma no branch
            self._scope = self._makeStringAttribute(attributes["scope"])

        if "package" in attributes:  # pragma no branch
            self._package = self._makeClassAttribute(
                github.DependabotAlertDependencyPackage.DependabotAlertDependencyPackage,
                attributes["package"],
            )
