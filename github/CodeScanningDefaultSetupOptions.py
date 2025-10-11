############################ Copyrights and license ############################
#                                                                              #
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

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.GithubObject import NonCompletableGithubObject


class CodeScanningDefaultSetupOptions(NonCompletableGithubObject):
    """
    This class represents CodeScanningDefaultSetupOptions.

    The reference can be found here
    https://docs.github.com/en/rest

    The OpenAPI schema can be found at
    - /components/schemas/code-security-configuration/properties/code_scanning_default_setup_options

    """

    def _initAttributes(self) -> None:
        # TODO: remove if parent does not implement this
        super()._initAttributes()
        self._runner_label: Attribute[str] = NotSet
        self._runner_type: Attribute[str] = NotSet

    def __repr__(self) -> str:
        # TODO: replace "some_attribute" with uniquely identifying attributes in the dict, then run:
        return self.get__repr__({"some_attribute": self._some_attribute.value})

    @property
    def runner_label(self) -> str:
        return self._runner_label.value

    @property
    def runner_type(self) -> str:
        return self._runner_type.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # TODO: remove if parent does not implement this
        super()._useAttributes(attributes)
        if "runner_label" in attributes:  # pragma no branch
            self._runner_label = self._makeStringAttribute(attributes["runner_label"])
        if "runner_type" in attributes:  # pragma no branch
            self._runner_type = self._makeStringAttribute(attributes["runner_type"])
