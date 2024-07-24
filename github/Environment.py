############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Andrew Dawes <53574062+AndrewJDawes@users.noreply.github.com> #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.EnvironmentDeploymentBranchPolicy
import github.EnvironmentProtectionRule
from github.GithubObject import Attribute, CompletableGithubObject, NotSet
from github.PaginatedList import PaginatedList
from github.PublicKey import PublicKey
from github.Secret import Secret
from github.Variable import Variable

if TYPE_CHECKING:
    from github.EnvironmentDeploymentBranchPolicy import EnvironmentDeploymentBranchPolicy
    from github.EnvironmentProtectionRule import EnvironmentProtectionRule


class Environment(CompletableGithubObject):
    """
    This class represents Environment.

    The reference can be found here
    https://docs.github.com/en/rest/reference/deployments#environments

    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._protection_rules: Attribute[list[EnvironmentProtectionRule]] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._environments_url: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._deployment_branch_policy: Attribute[EnvironmentDeploymentBranchPolicy] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def protection_rules(
        self,
    ) -> list[EnvironmentProtectionRule]:
        self._completeIfNotSet(self._protection_rules)
        return self._protection_rules.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def environments_url(self) -> str:
        """
        :type: string
        """
        return self._environments_url.value

    @property
    def url(self) -> str:
        """
        :type: string
        """
        # Construct url from environments_url and name, if self._url. is not set
        if self._url is NotSet:
            self._url = self._makeStringAttribute(self.environments_url + "/" + self.name)
        return self._url.value

    @property
    def deployment_branch_policy(
        self,
    ) -> EnvironmentDeploymentBranchPolicy:
        self._completeIfNotSet(self._deployment_branch_policy)
        return self._deployment_branch_policy.value

    def get_public_key(self) -> PublicKey:
        """
        :calls: `GET /repositories/{repository_id}/environments/{environment_name}/secrets/public-key <https://docs.github.com/en/rest/reference#get-a-repository-public-key>`_
        :rtype: :class:`PublicKey`
        """
        # https://stackoverflow.com/a/76474814
        # https://docs.github.com/en/rest/secrets?apiVersion=2022-11-28#get-an-environment-public-key
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/secrets/public-key")
        return PublicKey(self._requester, headers, data, completed=True)

    def create_secret(self, secret_name: str, unencrypted_value: str) -> Secret:
        """
        :calls: `PUT /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name} <https://docs.github.com/en/rest/secrets#get-a-repository-secret>`_
        """
        assert isinstance(secret_name, str), secret_name
        assert isinstance(unencrypted_value, str), unencrypted_value
        public_key = self.get_public_key()
        payload = public_key.encrypt(unencrypted_value)
        put_parameters = {
            "key_id": public_key.key_id,
            "encrypted_value": payload,
        }
        self._requester.requestJsonAndCheck("PUT", f"{self.url}/secrets/{secret_name}", input=put_parameters)
        return Secret(
            requester=self._requester,
            headers={},
            attributes={
                "name": secret_name,
                "url": f"{self.url}/secrets/{secret_name}",
            },
            completed=False,
        )

    def get_secrets(self) -> PaginatedList[Secret]:
        """
        Gets all repository secrets.
        """
        return PaginatedList(
            Secret,
            self._requester,
            f"{self.url}/secrets",
            None,
            attributesTransformer=PaginatedList.override_attributes({"secrets_url": f"{self.url}/secrets"}),
            list_item="secrets",
        )

    def get_secret(self, secret_name: str) -> Secret:
        """
        :calls: 'GET /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name} <https://docs.github.com/en/rest/secrets#get-an-organization-secret>`_
        """
        assert isinstance(secret_name, str), secret_name
        return Secret(
            requester=self._requester,
            headers={},
            attributes={"url": f"{self.url}/secrets/{secret_name}"},
            completed=False,
        )

    def create_variable(self, variable_name: str, value: str) -> Variable:
        """
        :calls: `POST /repositories/{repository_id}/environments/{environment_name}/variables/{variable_name} <https://docs.github.com/en/rest/variables#create-a-repository-variable>`_
        """
        assert isinstance(variable_name, str), variable_name
        assert isinstance(value, str), value
        post_parameters = {
            "name": variable_name,
            "value": value,
        }
        self._requester.requestJsonAndCheck("POST", f"{self.url}/variables", input=post_parameters)
        return Variable(
            self._requester,
            headers={},
            attributes={
                "name": variable_name,
                "value": value,
                "url": f"{self.url}/variables/{variable_name}",
            },
            completed=False,
        )

    def get_variables(self) -> PaginatedList[Variable]:
        """
        Gets all repository variables :rtype: :class:`PaginatedList` of :class:`Variable`
        """
        return PaginatedList(
            Variable,
            self._requester,
            f"{self.url}/variables",
            None,
            attributesTransformer=PaginatedList.override_attributes({"variables_url": f"{self.url}/variables"}),
            list_item="variables",
        )

    def get_variable(self, variable_name: str) -> Variable:
        """
        :calls: 'GET /orgs/{org}/variables/{variable_name} <https://docs.github.com/en/rest/variables#get-an-organization-variable>`_
        :param variable_name: string
        :rtype: Variable
        """
        assert isinstance(variable_name, str), variable_name
        return Variable(
            requester=self._requester,
            headers={},
            attributes={"url": f"{self.url}/variables/{variable_name}"},
            completed=False,
        )

    def delete_secret(self, secret_name: str) -> bool:
        """
        :calls: `DELETE /repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name} <https://docs.github.com/en/rest/reference#delete-a-repository-secret>`_
        :param secret_name: string
        :rtype: bool
        """
        assert isinstance(secret_name, str), secret_name
        status, headers, data = self._requester.requestJson("DELETE", f"{self.url}/secrets/{secret_name}")
        return status == 204

    def delete_variable(self, variable_name: str) -> bool:
        """
        :calls: `DELETE /repositories/{repository_id}/environments/{environment_name}/variables/{variable_name} <https://docs.github.com/en/rest/reference#delete-a-repository-variable>`_
        :param variable_name: string
        :rtype: bool
        """
        assert isinstance(variable_name, str), variable_name
        status, headers, data = self._requester.requestJson("DELETE", f"{self.url}/variables/{variable_name}")
        return status == 204

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "protection_rules" in attributes:  # pragma no branch
            self._protection_rules = self._makeListOfClassesAttribute(
                github.EnvironmentProtectionRule.EnvironmentProtectionRule,
                attributes["protection_rules"],
            )
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "environments_url" in attributes:
            self._environments_url = self._makeStringAttribute(attributes["environments_url"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "deployment_branch_policy" in attributes:  # pragma no branch
            self._deployment_branch_policy = self._makeClassAttribute(
                github.EnvironmentDeploymentBranchPolicy.EnvironmentDeploymentBranchPolicy,
                attributes["deployment_branch_policy"],
            )
