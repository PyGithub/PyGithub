############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Mateusz Loskot <mateusz@loskot.net>                           #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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
import urllib.parse
from typing import Any, Dict

from github import Consts
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_optional


class Label(CompletableGithubObject):
    """
    This class represents Labels. The reference can be found here https://docs.github.com/en/rest/reference/issues#labels
    """

    def _initAttributes(self) -> None:
        self._color: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def color(self) -> str:
        self._completeIfNotSet(self._color)
        return self._color.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/labels/{name} <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def edit(self, name: str, color: str, description: Opt[str] = NotSet) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/labels/{name} <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert isinstance(name, str), name
        assert isinstance(color, str), color
        assert is_optional(description, str), description
        post_parameters = NotSet.remove_unset_items({"new_name": name, "color": color, "description": description})
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeLabelDescriptionSearchPreview},
        )
        self._useAttributes(data)

    @property
    def _identity(self) -> str:
        return urllib.parse.quote(self.name)

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "color" in attributes:  # pragma no branch
            self._color = self._makeStringAttribute(attributes["color"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
