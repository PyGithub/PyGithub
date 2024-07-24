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
# Copyright 2018 Michell Stuttgart <michellstut@gmail.com>                     #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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

from datetime import date, datetime
from typing import Any

import github.GithubObject
import github.Label
import github.NamedUser
import github.PaginatedList
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_defined
from github.PaginatedList import PaginatedList


class Milestone(CompletableGithubObject):
    """
    This class represents Milestones.

    The reference can be found here
    https://docs.github.com/en/rest/reference/issues#milestones

    """

    def _initAttributes(self) -> None:
        self._closed_issues: Attribute[int] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._creator: Attribute[github.NamedUser.NamedUser] = NotSet
        self._description: Attribute[str] = NotSet
        self._due_on: Attribute[datetime] = NotSet
        self._id: Attribute[int] = NotSet
        self._labels_url: Attribute[str] = NotSet
        self._number: Attribute[int] = NotSet
        self._open_issues: Attribute[int] = NotSet
        self._state: Attribute[str] = NotSet
        self._title: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self._number.value, "title": self._title.value})

    @property
    def closed_issues(self) -> int:
        self._completeIfNotSet(self._closed_issues)
        return self._closed_issues.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def creator(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._creator)
        return self._creator.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def due_on(self) -> datetime | None:
        self._completeIfNotSet(self._due_on)
        return self._due_on.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def labels_url(self) -> str:
        self._completeIfNotSet(self._labels_url)
        return self._labels_url.value

    @property
    def number(self) -> int:
        self._completeIfNotSet(self._number)
        return self._number.value

    @property
    def open_issues(self) -> int:
        self._completeIfNotSet(self._open_issues)
        return self._open_issues.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def title(self) -> str:
        self._completeIfNotSet(self._title)
        return self._title.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/milestones/{number} <https://docs.github.com/en/rest/reference/issues#milestones>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def edit(
        self, title: str, state: Opt[str] = NotSet, description: Opt[str] = NotSet, due_on: Opt[date] = NotSet
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/milestones/{number} <https://docs.github.com/en/rest/reference/issues#milestones>`_
        """
        assert isinstance(title, str), title
        assert state is NotSet or isinstance(state, str), state
        assert description is NotSet or isinstance(description, str), description
        assert due_on is NotSet or isinstance(due_on, date), due_on
        post_parameters = NotSet.remove_unset_items(
            {
                "title": title,
                "state": state,
                "description": description,
            }
        )

        if is_defined(due_on):
            post_parameters["due_on"] = due_on.strftime("%Y-%m-%d")

        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def get_labels(self) -> PaginatedList[github.Label.Label]:
        """
        :calls: `GET /repos/{owner}/{repo}/milestones/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        return PaginatedList(github.Label.Label, self._requester, f"{self.url}/labels", None)

    @property
    def _identity(self) -> int:
        return self.number

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "closed_issues" in attributes:  # pragma no branch
            self._closed_issues = self._makeIntAttribute(attributes["closed_issues"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "due_on" in attributes:  # pragma no branch
            self._due_on = self._makeDatetimeAttribute(attributes["due_on"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "labels_url" in attributes:  # pragma no branch
            self._labels_url = self._makeStringAttribute(attributes["labels_url"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "open_issues" in attributes:  # pragma no branch
            self._open_issues = self._makeIntAttribute(attributes["open_issues"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
