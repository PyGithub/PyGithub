############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Jacky Lam <jacky.lam@r2studiohk.com>                          #
# Copyright 2024 Kian-Meng Ang <kianmeng.ang@gmail.com>                        #
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

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet, Opt, is_optional


class CustomProperty:
    """
    This class represents a CustomProperty for an Organization. Use this class to create a new post parameter object.

    The reference can be found here
    https://docs.github.com/en/rest/orgs/custom-properties#create-or-update-custom-properties-for-an-organization

    """

    def __init__(
        self,
        property_name: str,
        value_type: str,
        required: Opt[bool] = NotSet,
        default_value: Opt[None | str | list[str]] = NotSet,
        description: Opt[str | None] = NotSet,
        allowed_values: Opt[list[str] | None] = NotSet,
        values_editable_by: Opt[str | None] = NotSet,
    ):
        assert isinstance(property_name, str), property_name
        assert isinstance(value_type, str), value_type
        assert value_type in ["string", "single_select"], value_type
        assert is_optional(required, bool), required
        assert is_optional(default_value, (type(None), str, list)), default_value
        assert is_optional(description, (str, type(None))), description
        assert is_optional(allowed_values, (list, type(None))), allowed_values
        assert is_optional(values_editable_by, (str, type(None))), values_editable_by
        if values_editable_by is not NotSet:
            assert values_editable_by in ["org_actors", "org_and_repo_actors"], values_editable_by

        self.property_name = property_name
        self.value_type = value_type
        self.required = required
        self.default_value = default_value
        self.description = description
        self.allowed_values = allowed_values
        self.values_editable_by = values_editable_by

    def to_dict(self) -> dict[str, Any]:
        return NotSet.remove_unset_items(self.__dict__)


class OrganizationCustomProperty(NonCompletableGithubObject):
    """
    This class represents a CustomProperty for an Organization.

    The reference can be found here
    https://docs.github.com/en/rest/orgs/custom-properties

    The OpenAPI schema can be found at
    - /components/schemas/custom-property

    """

    def _initAttributes(self) -> None:
        self._allowed_values: Attribute[list[str]] = NotSet
        self._default_value: Attribute[str | list[str]] = NotSet
        self._description: Attribute[str] = NotSet
        self._property_name: Attribute[str] = NotSet
        self._required: Attribute[bool] = NotSet
        self._url: Attribute[str] = NotSet
        self._value_type: Attribute[str] = NotSet
        self._values_editable_by: Attribute[str] = NotSet

    @property
    def allowed_values(self) -> Opt[list[str] | None]:
        return self._allowed_values.value

    @property
    def default_value(self) -> Opt[str | list[str] | None]:
        return self._default_value.value

    @property
    def description(self) -> Opt[str | None]:
        return self._description.value

    @property
    def property_name(self) -> str:
        return self._property_name.value

    @property
    def required(self) -> Opt[bool | None]:
        return self._required.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def value_type(self) -> str:
        return self._value_type.value

    @property
    def values_editable_by(self) -> Opt[str | None]:
        return self._values_editable_by.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "allowed_values" in attributes:
            self._allowed_values = self._makeListOfStringsAttribute(attributes["allowed_values"])
        if "default_value" in attributes:
            self._default_value = self._makeStringAttribute(attributes["default_value"])
        if "description" in attributes:
            self._description = self._makeStringAttribute(attributes["description"])
        if "property_name" in attributes:  # pragma no branch
            self._property_name = self._makeStringAttribute(attributes["property_name"])
        if "required" in attributes:
            self._required = self._makeBoolAttribute(attributes["required"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "value_type" in attributes:  # pragma no branch
            self._value_type = self._makeStringAttribute(attributes["value_type"])
        if "values_editable_by" in attributes:
            self._values_editable_by = self._makeStringAttribute(attributes["values_editable_by"])


class RepositoryCustomPropertyValues(NonCompletableGithubObject):
    """
    This class represents CustomPropertyValues for a Repository.

    The reference can be found here
    https://docs.github.com/en/rest/orgs/custom-properties#list-custom-property-values-for-organization-repositories

    """

    def _initAttributes(self) -> None:
        self._properties: Attribute[dict[str, str]] = NotSet
        self._repository_full_name: Attribute[str] = NotSet
        self._repository_id: Attribute[int] = NotSet
        self._repository_name: Attribute[str] = NotSet

    @property
    def properties(self) -> dict[str, str]:
        return self._properties.value

    @property
    def repository_full_name(self) -> str:
        return self._repository_full_name.value

    @property
    def repository_name(self) -> str:
        return self._repository_name.value

    @property
    def repository_id(self) -> int:
        return self._repository_id.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        self._repository_id = self._makeIntAttribute(attributes["repository_id"])
        self._repository_name = self._makeStringAttribute(attributes["repository_name"])
        self._repository_full_name = self._makeStringAttribute(attributes["repository_full_name"])
        properties = {p["property_name"]: p["value"] for p in attributes["properties"]}
        self._properties = self._makeDictAttribute(properties)
