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

from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.PagesHttpsCertificate
import github.PagesSource
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.PagesHttpsCertificate import PagesHttpsCertificate
    from github.PagesSource import PagesSource


class Pages(NonCompletableGithubObject):
    """
    This class represents the GitHub Pages site of a repository.

    The reference can be found here
    https://docs.github.com/en/rest/pages/pages#get-a-github-pages-site

    The OpenAPI schema can be found at

    - /components/schemas/page

    """

    def _initAttributes(self) -> None:
        self._build_type: Attribute[str | None] = NotSet
        self._cname: Attribute[str | None] = NotSet
        self._custom_404: Attribute[bool] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._https_certificate: Attribute[PagesHttpsCertificate] = NotSet
        self._https_enforced: Attribute[bool] = NotSet
        self._pending_domain_unverified_at: Attribute[datetime | None] = NotSet
        self._protected_domain_state: Attribute[str | None] = NotSet
        self._public: Attribute[bool] = NotSet
        self._source: Attribute[PagesSource] = NotSet
        self._status: Attribute[str | None] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"html_url": self._html_url.value, "build_type": self._build_type.value})

    @property
    def build_type(self) -> str | None:
        return self._build_type.value

    @property
    def cname(self) -> str | None:
        return self._cname.value

    @property
    def custom_404(self) -> bool:
        return self._custom_404.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def https_certificate(self) -> PagesHttpsCertificate:
        return self._https_certificate.value

    @property
    def https_enforced(self) -> bool:
        return self._https_enforced.value

    @property
    def pending_domain_unverified_at(self) -> datetime | None:
        return self._pending_domain_unverified_at.value

    @property
    def protected_domain_state(self) -> str | None:
        return self._protected_domain_state.value

    @property
    def public(self) -> bool:
        return self._public.value

    @property
    def source(self) -> PagesSource:
        return self._source.value

    @property
    def status(self) -> str | None:
        return self._status.value

    @property
    def url(self) -> str:
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "build_type" in attributes:  # pragma no branch
            self._build_type = self._makeStringAttribute(attributes["build_type"])
        if "cname" in attributes:  # pragma no branch
            self._cname = self._makeStringAttribute(attributes["cname"])
        if "custom_404" in attributes:  # pragma no branch
            self._custom_404 = self._makeBoolAttribute(attributes["custom_404"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "https_certificate" in attributes:  # pragma no branch
            self._https_certificate = self._makeClassAttribute(
                github.PagesHttpsCertificate.PagesHttpsCertificate, attributes["https_certificate"]
            )
        if "https_enforced" in attributes:  # pragma no branch
            self._https_enforced = self._makeBoolAttribute(attributes["https_enforced"])
        if "pending_domain_unverified_at" in attributes:  # pragma no branch
            self._pending_domain_unverified_at = self._makeDatetimeAttribute(attributes["pending_domain_unverified_at"])
        if "protected_domain_state" in attributes:  # pragma no branch
            self._protected_domain_state = self._makeStringAttribute(attributes["protected_domain_state"])
        if "public" in attributes:  # pragma no branch
            self._public = self._makeBoolAttribute(attributes["public"])
        if "source" in attributes:  # pragma no branch
            self._source = self._makeClassAttribute(github.PagesSource.PagesSource, attributes["source"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
