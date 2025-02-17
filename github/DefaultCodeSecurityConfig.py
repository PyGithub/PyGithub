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

import github.CodeSecurityConfig
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class DefaultCodeSecurityConfig(NonCompletableGithubObject):
    """
    This class represents a Default Configurations for Code Security.

    The reference can be found here
    https://docs.github.com/en/rest/code-security/configurations.

    """

    def _initAttributes(self) -> None:
        self._configuration: Attribute[github.CodeSecurityConfig.CodeSecurityConfig] = NotSet
        self._default_for_new_repos: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "default_for_new_repos": self.default_for_new_repos,
            }
        )

    @property
    def configuration(self) -> github.CodeSecurityConfig.CodeSecurityConfig:
        return self._configuration.value

    @property
    def default_for_new_repos(self) -> str:
        return self._default_for_new_repos.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "configuration" in attributes:  # pragma no branch
            self._configuration = self._makeClassAttribute(
                github.CodeSecurityConfig.CodeSecurityConfig, attributes["configuration"]
            )
        if "default_for_new_repos" in attributes:  # pragma no branch
            self._default_for_new_repos = self._makeStringAttribute(attributes["default_for_new_repos"])
