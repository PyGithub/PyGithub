from __future__ import annotations

from typing import Any

from github.DependabotAlert import DependabotAlert
from github.GithubObject import Attribute, NotSet
from github.Repository import Repository


class OrganizationDependabotAlert(DependabotAlert):
    """
    This class represents a Dependabot alert on an organization. The reference can be found here https://docs.github.com/en/rest/dependabot/alerts#list-dependabot-alerts-for-an-organization
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._repository: Attribute[Repository] = NotSet

    @property
    def repository(self) -> Repository:
        return self._repository.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "repository" in attributes:
            self._repository = self._makeClassAttribute(Repository, attributes["repository"])
