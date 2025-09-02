############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Bill Napier <napier@pobox.com>                                #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SelfHostedActionsRunnerApplication(NonCompletableGithubObject):
    """
    This class represents Self-hosted GitHub Actions Runners Applications.

    The reference can be found at
    https://docs.github.com/en/free-pro-team@latest/rest/reference/actions#self-hosted-runners

    The OpenAPI schema can be found at

    - /components/schemas/runner-application

    """

    def _initAttributes(self) -> None:
        self._architecture: Attribute[str] = NotSet
        self._download_url: Attribute[str] = NotSet
        self._filename: Attribute[str] = NotSet
        self._os: Attribute[str] = NotSet
        self._sha256_checksum: Attribute[str] = NotSet
        self._temp_download_token: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"os": self._os.value})

    @property
    def architecture(self) -> str:
        return self._architecture.value

    @property
    def download_url(self) -> str:
        return self._download_url.value

    @property
    def filename(self) -> str:
        return self._filename.value

    @property
    def os(self) -> str:
        return self._os.value

    @property
    def sha256_checksum(self) -> str:
        return self._sha256_checksum.value

    @property
    def temp_download_token(self) -> str:
        return self._temp_download_token.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "architecture" in attributes:  # pragma no branch
            self._architecture = self._makeStringAttribute(attributes["architecture"])
        if "download_url" in attributes:  # pragma no branch
            self._download_url = self._makeStringAttribute(attributes["download_url"])
        if "filename" in attributes:  # pragma no branch
            self._filename = self._makeStringAttribute(attributes["filename"])
        if "os" in attributes:
            self._os = self._makeStringAttribute(attributes["os"])
        if "sha256_checksum" in attributes:  # pragma no branch
            self._sha256_checksum = self._makeStringAttribute(attributes["sha256_checksum"])
        if "temp_download_token" in attributes:  # pragma no branch
            self._temp_download_token = self._makeStringAttribute(attributes["temp_download_token"])
