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

from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class DeploymentBranchPolicy(NonCompletableGithubObject):
    """
    This class represents a deployment branch or tag policy of an environment.

    The reference can be found here
    https://docs.github.com/en/rest/deployments/branch-policies

    The OpenAPI schema can be found at

    - /components/schemas/deployment-branch-policy

    """

    def _initAttributes(self) -> None:
        self._branch_policies_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._type: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "name": self._name.value})

    @property
    def branch_policies_url(self) -> str:
        return self._branch_policies_url.value

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def node_id(self) -> str:
        return self._node_id.value

    @property
    def type(self) -> str:
        return self._type.value

    @property
    def url(self) -> str:
        return f"{self.branch_policies_url}/{self.id}"

    def edit(self, name: str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} <https://docs.github.com/en/rest/deployments/branch-policies#update-a-deployment-branch-policy>`_
        :param name: new name pattern that branches or tags must match to be deployed to the environment
        """
        assert isinstance(name, str), name
        headers, data = self._requester.requestJsonAndCheck("PUT", self.url, input={"name": name})
        self._useAttributes(data)

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} <https://docs.github.com/en/rest/deployments/branch-policies#delete-a-deployment-branch-policy>`_
        """
        self._requester.requestJsonAndCheck("DELETE", self.url)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "branch_policies_url" in attributes:  # pragma no branch
            self._branch_policies_url = self._makeStringAttribute(attributes["branch_policies_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
