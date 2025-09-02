############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
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

import github.SelfHostedActionsRunner
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SelfHostedActionsRunnerJitConfig(NonCompletableGithubObject):
    """
    This class represents Self-hosted GitHub Actions Runners JitConfig.

    The reference can be found at
    https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28#create-configuration-for-a-just-in-time-runner-for-a-repository

    The OpenAPI schema can be found at

    - /components/responses/actions_runner_jitconfig/content/"application/json"/schema

    """

    def _initAttributes(self) -> None:
        self._encoded_jit_config: Attribute[str] = NotSet
        self._runner: Attribute[github.SelfHostedActionsRunner.SelfHostedActionsRunner] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"encoded_jit_config": self._encoded_jit_config.value})

    @property
    def encoded_jit_config(self) -> str:
        return self._encoded_jit_config.value

    @property
    def runner(self) -> github.SelfHostedActionsRunner.SelfHostedActionsRunner:
        return self._runner.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "encoded_jit_config" in attributes:  # pragma no branch
            self._encoded_jit_config = self._makeStringAttribute(attributes["encoded_jit_config"])
        if "runner" in attributes:  # pragma no branch
            self._runner = self._makeClassAttribute(
                github.SelfHostedActionsRunner.SelfHostedActionsRunner, attributes["runner"]
            )
