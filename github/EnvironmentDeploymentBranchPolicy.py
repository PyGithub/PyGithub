############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 alson <git@alm.nufan.net>                                     #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class EnvironmentDeploymentBranchPolicy(NonCompletableGithubObject):
    """
    This class represents a deployment branch policy for an environment.

    The reference can be found here
    https://docs.github.com/en/rest/reference/deployments#environments

    """

    def _initAttributes(self) -> None:
        self._protected_branches: Attribute[bool] = NotSet
        self._custom_branch_policies: Attribute[bool] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({})

    @property
    def protected_branches(self) -> bool:
        return self._protected_branches.value

    @property
    def custom_branch_policies(self) -> bool:
        return self._custom_branch_policies.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "protected_branches" in attributes:  # pragma no branch
            self._protected_branches = self._makeBoolAttribute(attributes["protected_branches"])
        if "custom_branch_policies" in attributes:  # pragma no branch
            self._custom_branch_policies = self._makeBoolAttribute(attributes["custom_branch_policies"])


class EnvironmentDeploymentBranchPolicyParams:
    """
    This class presents the deployment branch policy parameters as can be configured for an Environment.
    """

    def __init__(self, protected_branches: bool = False, custom_branch_policies: bool = False):
        assert isinstance(protected_branches, bool)
        assert isinstance(custom_branch_policies, bool)
        self.protected_branches = protected_branches
        self.custom_branch_policies = custom_branch_policies

    def _asdict(self) -> dict:
        return {
            "protected_branches": self.protected_branches,
            "custom_branch_policies": self.custom_branch_policies,
        }
