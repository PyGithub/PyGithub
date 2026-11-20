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
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_defined, is_optional

if TYPE_CHECKING:
    from github.PagesHttpsCertificate import PagesHttpsCertificate
    from github.PagesSource import PagesSource


class Pages(CompletableGithubObject):
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
        self._completeIfNotSet(self._build_type)
        return self._build_type.value

    @property
    def cname(self) -> str | None:
        self._completeIfNotSet(self._cname)
        return self._cname.value

    @property
    def custom_404(self) -> bool:
        self._completeIfNotSet(self._custom_404)
        return self._custom_404.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def https_certificate(self) -> PagesHttpsCertificate:
        self._completeIfNotSet(self._https_certificate)
        return self._https_certificate.value

    @property
    def https_enforced(self) -> bool:
        self._completeIfNotSet(self._https_enforced)
        return self._https_enforced.value

    @property
    def pending_domain_unverified_at(self) -> datetime | None:
        self._completeIfNotSet(self._pending_domain_unverified_at)
        return self._pending_domain_unverified_at.value

    @property
    def protected_domain_state(self) -> str | None:
        self._completeIfNotSet(self._protected_domain_state)
        return self._protected_domain_state.value

    @property
    def public(self) -> bool:
        self._completeIfNotSet(self._public)
        return self._public.value

    @property
    def source(self) -> PagesSource:
        self._completeIfNotSet(self._source)
        return self._source.value

    @property
    def status(self) -> str | None:
        self._completeIfNotSet(self._status)
        return self._status.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def edit(
        self,
        cname: Opt[str | None] = NotSet,
        https_enforced: Opt[bool] = NotSet,
        build_type: Opt[str] = NotSet,
        source: Opt[str] = NotSet,
        source_branch: Opt[str] = NotSet,
        source_path: Opt[str] = NotSet,
    ) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/pages <https://docs.github.com/en/rest/pages/pages#update-information-about-a-github-pages-site>`_
        :param cname: custom domain, None removes the custom domain
        :param https_enforced: whether HTTPS is enforced
        :param build_type: "legacy" or "workflow"
        :param source: "gh-pages", "master" or "master /docs", use source_branch and source_path for any other branch
        :param source_branch: branch to publish from, must be given together with source_path
        :param source_path: directory to publish from, "/" or "/docs", must be given together with source_branch
        :rtype: None
        """
        assert is_optional(cname, (str, type(None))), cname
        assert is_optional(https_enforced, bool), https_enforced
        assert is_optional(build_type, str), build_type
        assert is_optional(source, str), source
        assert is_optional(source_branch, str), source_branch
        assert is_optional(source_path, str), source_path
        assert is_defined(source_branch) == is_defined(source_path), "source_branch and source_path go together"
        assert not (is_defined(source) and is_defined(source_branch)), "source excludes source_branch and source_path"
        put_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {"cname": cname, "https_enforced": https_enforced, "build_type": build_type, "source": source}
        )
        if is_defined(source_branch):
            put_parameters["source"] = {"branch": source_branch, "path": source_path}
        headers, data = self._requester.requestJsonAndCheck("PUT", self.url, input=put_parameters)

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/pages <https://docs.github.com/en/rest/pages/pages#delete-a-github-pages-site>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

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
