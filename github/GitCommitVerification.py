############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Tim Gates <tim.gates@iress.com>                               #
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


class GitCommitVerification(NonCompletableGithubObject):
    """
    This class represents commit verifications.

    The reference can be found here
    https://docs.github.com/en/rest/commits/commits

    The OpenAPI schema can be found at
    - /components/schemas/git-commit/properties/verification

    """

    def _initAttributes(self) -> None:
        self._verified: Attribute[bool] = NotSet
        self._verified_at: Attribute[datetime] = NotSet
        self._reason: Attribute[str] = NotSet
        self._signature: Attribute[str] = NotSet
        self._payload: Attribute[str] = NotSet

    @property
    def verified(self) -> bool:
        return self._verified.value

    @property
    def verified_at(self) -> datetime:
        return self._verified_at.value

    @property
    def reason(self) -> str:
        return self._reason.value

    @property
    def signature(self) -> str:
        return self._signature.value

    @property
    def payload(self) -> str:
        return self._payload.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "verified" in attributes:  # pragma no branch
            self._verified = self._makeBoolAttribute(attributes["verified"])
        if "verified_at" in attributes:  # pragma no branch
            self._verified_at = self._makeDatetimeAttribute(attributes["verified_at"])
        if "reason" in attributes:  # pragma no branch
            self._reason = self._makeStringAttribute(attributes["reason"])
        if "signature" in attributes:  # pragma no branch
            self._signature = self._makeStringAttribute(attributes["signature"])
        if "payload" in attributes:  # pragma no branch
            self._payload = self._makeStringAttribute(attributes["payload"])
