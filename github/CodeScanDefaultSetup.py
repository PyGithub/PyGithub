############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from datetime import datetime
from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CodeScanDefaultSetup(NonCompletableGithubObject):
    """
    This class represents a repository's code scanning default setup configuration.

    The reference can be found here
    https://docs.github.com/en/rest/code-scanning/code-scanning#get-a-code-scanning-default-setup-configuration

    The OpenAPI schema can be found at

    - /components/schemas/code-scanning-default-setup

    """

    def _initAttributes(self) -> None:
        self._state: Attribute[str] = NotSet
        self._languages: Attribute[list[str]] = NotSet
        self._query_suite: Attribute[str] = NotSet
        self._threat_model: Attribute[str] = NotSet
        self._runner_type: Attribute[str] = NotSet
        self._runner_label: Attribute[str | None] = NotSet
        self._schedule: Attribute[str | None] = NotSet
        self._updated_at: Attribute[datetime | None] = NotSet

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def languages(self) -> list[str]:
        return self._languages.value

    @property
    def query_suite(self) -> str:
        return self._query_suite.value

    @property
    def threat_model(self) -> str:
        return self._threat_model.value

    @property
    def runner_type(self) -> str:
        return self._runner_type.value

    @property
    def runner_label(self) -> str | None:
        return self._runner_label.value

    @property
    def schedule(self) -> str | None:
        return self._schedule.value

    @property
    def updated_at(self) -> datetime | None:
        return self._updated_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "languages" in attributes:  # pragma no branch
            self._languages = self._makeListOfStringsAttribute(attributes["languages"])
        if "query_suite" in attributes:  # pragma no branch
            self._query_suite = self._makeStringAttribute(attributes["query_suite"])
        if "threat_model" in attributes:  # pragma no branch
            self._threat_model = self._makeStringAttribute(attributes["threat_model"])
        if "runner_type" in attributes:  # pragma no branch
            self._runner_type = self._makeStringAttribute(attributes["runner_type"])
        if "runner_label" in attributes:  # pragma no branch
            self._runner_label = self._makeStringAttribute(attributes["runner_label"])
        if "schedule" in attributes:  # pragma no branch
            self._schedule = self._makeStringAttribute(attributes["schedule"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
