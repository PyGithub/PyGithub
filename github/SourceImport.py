############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Hayden Fuss <wifu1234@gmail.com>                              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from github import Consts
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class SourceImport(CompletableGithubObject):
    """
    This class represents SourceImports.

    The reference can be found here
    https://docs.github.com/en/rest/reference/migrations#source-imports

    The OpenAPI schema can be found at
    - /components/schemas/import

    """

    def _initAttributes(self) -> None:
        self._authors_count: Attribute[int] = NotSet
        self._authors_url: Attribute[str] = NotSet
        self._commit_count: Attribute[int] = NotSet
        self._error_message: Attribute[str] = NotSet
        self._failed_step: Attribute[str] = NotSet
        self._has_large_files: Attribute[bool] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._import_percent: Attribute[int] = NotSet
        self._large_files_count: Attribute[int] = NotSet
        self._large_files_size: Attribute[int] = NotSet
        self._message: Attribute[str] = NotSet
        self._project_choices: Attribute[list[dict[str, Any]]] = NotSet
        self._push_percent: Attribute[int] = NotSet
        self._repository_url: Attribute[str] = NotSet
        self._status: Attribute[str] = NotSet
        self._status_text: Attribute[str] = NotSet
        self._svc_root: Attribute[str] = NotSet
        self._svn_root: Attribute[str] = NotSet
        self._tfvc_project: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._use_lfs: Attribute[str] = NotSet
        self._vcs: Attribute[str] = NotSet
        self._vcs_url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "vcs_url": self._vcs_url.value,
                "repository_url": self._repository_url.value,
                "status": self._status.value,
                "url": self._url.value,
            }
        )

    @property
    def authors_count(self) -> int:
        self._completeIfNotSet(self._authors_count)
        return self._authors_count.value

    @property
    def authors_url(self) -> str:
        self._completeIfNotSet(self._authors_url)
        return self._authors_url.value

    @property
    def commit_count(self) -> int:
        self._completeIfNotSet(self._commit_count)
        return self._commit_count.value

    @property
    def error_message(self) -> str:
        self._completeIfNotSet(self._error_message)
        return self._error_message.value

    @property
    def failed_step(self) -> str:
        self._completeIfNotSet(self._failed_step)
        return self._failed_step.value

    @property
    def has_large_files(self) -> bool:
        self._completeIfNotSet(self._has_large_files)
        return self._has_large_files.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def import_percent(self) -> int:
        self._completeIfNotSet(self._import_percent)
        return self._import_percent.value

    @property
    def large_files_count(self) -> int:
        self._completeIfNotSet(self._large_files_count)
        return self._large_files_count.value

    @property
    def large_files_size(self) -> int:
        self._completeIfNotSet(self._large_files_size)
        return self._large_files_size.value

    @property
    def message(self) -> str:
        self._completeIfNotSet(self._message)
        return self._message.value

    @property
    def project_choices(self) -> list[dict[str, Any]]:
        self._completeIfNotSet(self._project_choices)
        return self._project_choices.value

    @property
    def push_percent(self) -> int:
        self._completeIfNotSet(self._push_percent)
        return self._push_percent.value

    @property
    def repository_url(self) -> str:
        self._completeIfNotSet(self._repository_url)
        return self._repository_url.value

    @property
    def status(self) -> str:
        self._completeIfNotSet(self._status)
        return self._status.value

    @property
    def status_text(self) -> str:
        self._completeIfNotSet(self._status_text)
        return self._status_text.value

    @property
    def svc_root(self) -> str:
        self._completeIfNotSet(self._svc_root)
        return self._svc_root.value

    @property
    def svn_root(self) -> str:
        self._completeIfNotSet(self._svn_root)
        return self._svn_root.value

    @property
    def tfvc_project(self) -> str:
        self._completeIfNotSet(self._tfvc_project)
        return self._tfvc_project.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def use_lfs(self) -> str:
        self._completeIfNotSet(self._use_lfs)
        return self._use_lfs.value

    @property
    def vcs(self) -> str:
        self._completeIfNotSet(self._vcs)
        return self._vcs.value

    @property
    def vcs_url(self) -> str:
        self._completeIfNotSet(self._vcs_url)
        return self._vcs_url.value

    def update(self, additional_headers: None | dict[str, Any] = None) -> bool:
        import_header = {"Accept": Consts.mediaTypeImportPreview}
        return super().update(additional_headers=import_header)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "authors_count" in attributes:  # pragma no branch
            self._authors_count = self._makeIntAttribute(attributes["authors_count"])
        if "authors_url" in attributes:  # pragma no branch
            self._authors_url = self._makeStringAttribute(attributes["authors_url"])
        if "commit_count" in attributes:  # pragma no branch
            self._commit_count = self._makeIntAttribute(attributes["commit_count"])
        if "error_message" in attributes:  # pragma no branch
            self._error_message = self._makeStringAttribute(attributes["error_message"])
        if "failed_step" in attributes:  # pragma no branch
            self._failed_step = self._makeStringAttribute(attributes["failed_step"])
        if "has_large_files" in attributes:  # pragma no branch
            self._has_large_files = self._makeBoolAttribute(attributes["has_large_files"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "import_percent" in attributes:  # pragma no branch
            self._import_percent = self._makeIntAttribute(attributes["import_percent"])
        if "large_files_count" in attributes:  # pragma no branch
            self._large_files_count = self._makeIntAttribute(attributes["large_files_count"])
        if "large_files_size" in attributes:  # pragma no branch
            self._large_files_size = self._makeIntAttribute(attributes["large_files_size"])
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
        if "project_choices" in attributes:  # pragma no branch
            self._project_choices = self._makeListOfDictsAttribute(attributes["project_choices"])
        if "push_percent" in attributes:  # pragma no branch
            self._push_percent = self._makeIntAttribute(attributes["push_percent"])
        if "repository_url" in attributes:  # pragma no branch
            self._repository_url = self._makeStringAttribute(attributes["repository_url"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "status_text" in attributes:  # pragma no branch
            self._status_text = self._makeStringAttribute(attributes["status_text"])
        if "svc_root" in attributes:  # pragma no branch
            self._svc_root = self._makeStringAttribute(attributes["svc_root"])
        if "svn_root" in attributes:  # pragma no branch
            self._svn_root = self._makeStringAttribute(attributes["svn_root"])
        if "tfvc_project" in attributes:  # pragma no branch
            self._tfvc_project = self._makeStringAttribute(attributes["tfvc_project"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "use_lfs" in attributes:  # pragma no branch
            self._use_lfs = self._makeStringAttribute(attributes["use_lfs"])
        if "vcs" in attributes:  # pragma no branch
            self._vcs = self._makeStringAttribute(attributes["vcs"])
        if "vcs_url" in attributes:  # pragma no branch
            self._vcs_url = self._makeStringAttribute(attributes["vcs_url"])
