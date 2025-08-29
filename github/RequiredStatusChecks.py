############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from github.GithubObject import Attribute, CompletableGithubObject, NonCompletableGithubObject, NotSet


class Check(NonCompletableGithubObject):
    """
    This class represents Check.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#get-status-checks-protection

    The OpenAPI schema can be found at

    - /components/schemas/protected-branch-required-status-check/properties/checks/items
    - /components/schemas/status-check-policy/properties/checks/items

    """

    def _initAttributes(self) -> None:
        self._app_id: Attribute[int] = NotSet
        self._context: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"app_id": self._app_id.value, "context": self._context.value})

    @property
    def app_id(self) -> int:
        return self._app_id.value

    @property
    def context(self) -> str:
        return self._context.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "app_id" in attributes:  # pragma no branch
            self._app_id = self._makeIntAttribute(attributes["app_id"])
        if "context" in attributes:  # pragma no branch
            self._context = self._makeStringAttribute(attributes["context"])


class RequiredStatusChecks(CompletableGithubObject):
    """
    This class represents Required Status Checks.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#get-status-checks-protection

    The OpenAPI schema can be found at

    - /components/schemas/protected-branch-required-status-check
    - /components/schemas/status-check-policy

    """

    def _initAttributes(self) -> None:
        self._checks: Attribute[list[Check]] = NotSet
        self._contexts: Attribute[list[str]] = NotSet
        self._contexts_url: Attribute[str] = NotSet
        self._enforcement_level: Attribute[str] = NotSet
        self._strict: Attribute[bool] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"strict": self._strict.value, "url": self._url.value})

    @property
    def checks(self) -> list[Check]:
        self._completeIfNotSet(self._checks)
        return self._checks.value

    @property
    def contexts(self) -> list[str]:
        self._completeIfNotSet(self._contexts)
        return self._contexts.value

    @property
    def contexts_url(self) -> str:
        self._completeIfNotSet(self._contexts_url)
        return self._contexts_url.value

    @property
    def enforcement_level(self) -> str:
        self._completeIfNotSet(self._enforcement_level)
        return self._enforcement_level.value

    @property
    def strict(self) -> bool:
        self._completeIfNotSet(self._strict)
        return self._strict.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "checks" in attributes:  # pragma no branch
            self._checks = self._makeListOfClassesAttribute(Check, attributes["checks"])
        if "contexts" in attributes:  # pragma no branch
            self._contexts = self._makeListOfStringsAttribute(attributes["contexts"])
        if "contexts_url" in attributes:  # pragma no branch
            self._contexts_url = self._makeStringAttribute(attributes["contexts_url"])
        if "enforcement_level" in attributes:  # pragma no branch
            self._enforcement_level = self._makeStringAttribute(attributes["enforcement_level"])
        if "strict" in attributes:  # pragma no branch
            self._strict = self._makeBoolAttribute(attributes["strict"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
