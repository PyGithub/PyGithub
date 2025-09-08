############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Jens Keiner <jens.keiner@gmail.com>                           #
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

from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    is_defined,
    is_optional,
    is_optional_list,
)
from github.Rule import Rule

if TYPE_CHECKING:
    pass


class Ruleset(CompletableGithubObject):
    """
    This class represents Rulesets. A ruleset is a set of rules that are applied when specified conditions
    are met.

    The reference can be found here https://docs.github.com/en/rest/repos/rules

    """

    def _initAttributes(self) -> None:
        self.__links: Attribute[dict[str, Any]] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._target: Attribute[str] = NotSet
        self._source_type: Attribute[str] = NotSet
        self._source: Attribute[str] = NotSet
        self._enforcement: Attribute[str] = NotSet
        self._bypass_actors: Attribute[list[dict[str, Any]]] = NotSet
        self._conditions: Attribute[dict[str, Any]] = NotSet
        self._rules: Attribute[list[Rule]] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._current_user_can_bypass: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def _links(self) -> dict[str, Any]:
        """
        :type: dict
        :return: URLs related to the ruleset, including self URL and optional html URL
        """
        return self.__links.value

    @property
    def id(self) -> int:
        """
        :type: integer
        :return: The unique identifier of the ruleset
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        """
        :type: string
        :return: The name of the ruleset
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def target(self) -> str:
        """
        :type: string
        :return: The target of the ruleset (branch, tag, push, or repository)
        """
        self._completeIfNotSet(self._target)
        return self._target.value

    @property
    def source_type(self) -> str:
        """
        :type: string
        :return: The type of the source of the ruleset (Repository, Organization, or Enterprise)
        """
        self._completeIfNotSet(self._source_type)
        return self._source_type.value

    @property
    def source(self) -> str:
        """
        :type: string
        :return: The name of the source where the ruleset was created
        """
        self._completeIfNotSet(self._source)
        return self._source.value

    @property
    def enforcement(self) -> str:
        """
        :type: string
        :return: The enforcement status of the ruleset (active, disabled, or evaluate)
        """
        self._completeIfNotSet(self._enforcement)
        return self._enforcement.value

    @property
    def bypass_actors(self) -> list[dict[str, Any]]:
        """
        :type: list[dict]
        :return: The actors that can bypass the rules in this ruleset
        """
        self._completeIfNotSet(self._bypass_actors)
        return self._bypass_actors.value

    @property
    def conditions(self) -> dict[str, Any]:
        """
        :type: dict
        :return: The conditions that determine when the ruleset will be enforced
        """
        self._completeIfNotSet(self._conditions)
        return self._conditions.value

    @property
    def rules(self) -> list[Rule]:
        """
        :type: list[:class:`github.Rule.Rule`]
        :return: The list of rules included in this ruleset
        """
        self._completeIfNotSet(self._rules)
        return self._rules.value

    @property
    def created_at(self) -> datetime:
        """
        :type: datetime
        :return: The date and time when the ruleset was created
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        """
        :type: datetime
        :return: The date and time when the ruleset was last updated
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def node_id(self) -> str:
        """
        :type: string
        :return: The node ID of the ruleset
        """
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def current_user_can_bypass(self) -> str:
        """
        :type: string
        :return: The bypass type of the current user for this ruleset (always, pull_requests_only, or never)
        """
        self._completeIfNotSet(self._current_user_can_bypass)
        return self._current_user_can_bypass.value

    @property
    def url(self) -> str:
        """
        :type: string
        :return: The API URL of the ruleset
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def update(
        self,
        name: Opt[str] = NotSet,
        target: Opt[str] = NotSet,
        enforcement: Opt[str] = NotSet,
        bypass_actors: Opt[list[dict[str, Any]]] = NotSet,
        conditions: Opt[dict[str, Any]] = NotSet,
        rules: Opt[list[dict[str, Any]]] = NotSet,
    ) -> Ruleset:
        """
        :calls: `PUT /repos/{owner}/{repo}/rulesets/{ruleset_id} <https://docs.github.com/en/rest/repos/rules#update-a-repository-ruleset>`_
        :param name: string
        :param target: string
        :param enforcement: string
        :param bypass_actors: list of dict
        :param conditions: dict
        :param rules: list of dict
        :rtype: :class:`github.Ruleset.Ruleset`
        """
        assert is_optional(name, str), name
        assert is_optional(target, str), target
        if is_defined(target):
            assert target in ["branch", "tag", "push"], target
        assert is_optional(enforcement, str), enforcement
        if is_defined(enforcement):
            assert enforcement in ["active", "disabled", "evaluate"], enforcement
        assert is_optional_list(bypass_actors, dict), bypass_actors
        assert is_optional(conditions, dict), conditions
        assert is_optional_list(rules, dict), rules

        put_parameters = NotSet.remove_unset_items(
            {
                "name": name,
                "target": target,
                "enforcement": enforcement,
                "bypass_actors": bypass_actors,
                "conditions": conditions,
                "rules": rules,
            }
        )

        headers, data = self._requester.requestJsonAndCheck("PUT", self.url, input=put_parameters)
        return Ruleset(self._requester, headers, data, completed=True)

    def delete(self) -> bool:
        """
        :calls: `DELETE /repos/{owner}/{repo}/rulesets/{ruleset_id} <https://docs.github.com/en/rest/repos/rules#delete-a-repository-ruleset>`_
        :rtype: bool
        """
        status, _, _ = self._requester.requestJson("DELETE", self.url)
        return status == 204

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "_links" in attributes:  # pragma no branch
            self.__links = self._makeDictAttribute(attributes["_links"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "target" in attributes:  # pragma no branch
            self._target = self._makeStringAttribute(attributes["target"])
        if "source_type" in attributes:  # pragma no branch
            self._source_type = self._makeStringAttribute(attributes["source_type"])
        if "source" in attributes:  # pragma no branch
            self._source = self._makeStringAttribute(attributes["source"])
        if "enforcement" in attributes:  # pragma no branch
            self._enforcement = self._makeStringAttribute(attributes["enforcement"])
        if "bypass_actors" in attributes:  # pragma no branch
            self._bypass_actors = self._makeListOfDictsAttribute(attributes["bypass_actors"])
        if "conditions" in attributes:  # pragma no branch
            self._conditions = self._makeDictAttribute(attributes["conditions"])
        if "rules" in attributes:  # pragma no branch
            self._rules = self._makeListOfClassesAttribute(Rule, attributes["rules"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "current_user_can_bypass" in attributes:  # pragma no branch
            self._current_user_can_bypass = self._makeStringAttribute(attributes["current_user_can_bypass"])
        if (
            "_links" in attributes and "self" in attributes["_links"] and "href" in attributes["_links"]["self"]
        ):  # pragma no branch
            self._url = self._makeStringAttribute(attributes["_links"]["self"]["href"])
