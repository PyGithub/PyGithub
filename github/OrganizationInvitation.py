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

from typing import Any

from github.GithubObject import Attribute, NotSet
from github.NamedUser import NamedUser


class OrganizationInvitation(NamedUser):
    """
    This class represents OrganizationInvitation.

    The reference can be found here
    https://docs.github.com/en/rest/orgs/members

    The OpenAPI schema can be found at
    - /components/schemas/organization-invitation

    """

    def _initAttributes(self) -> None:
        super._initAttributes()
        self._failed_at: Attribute[str] = NotSet
        self._failed_reason: Attribute[str] = NotSet
        self._invitation_source: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def failed_at(self) -> str:
        return self._failed_at.value

    @property
    def failed_reason(self) -> str:
        return self._failed_reason.value

    @property
    def invitation_source(self) -> str:
        return self._invitation_source.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super._useAttributes(attributes)
        if "failed_at" in attributes:  # pragma no branch
            self._failed_at = self._makeStringAttribute(attributes["failed_at"])
        if "failed_reason" in attributes:  # pragma no branch
            self._failed_reason = self._makeStringAttribute(attributes["failed_reason"])
        if "invitation_source" in attributes:  # pragma no branch
            self._invitation_source = self._makeStringAttribute(attributes["invitation_source"])
