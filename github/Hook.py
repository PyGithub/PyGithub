############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
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

from datetime import datetime
from typing import Any

import github.GithubObject
import github.HookResponse
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_optional, is_optional_list


class Hook(CompletableGithubObject):
    """
    This class represents Hooks.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#webhooks

    """

    def _initAttributes(self) -> None:
        self._active: Attribute[bool] = NotSet
        self._config: Attribute[dict] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._events: Attribute[list[str]] = NotSet
        self._id: Attribute[int] = NotSet
        self._last_response: Attribute[github.HookResponse.HookResponse] = NotSet
        self._name: Attribute[str] = NotSet
        self._test_url: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._ping_url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    def active(self) -> bool:
        self._completeIfNotSet(self._active)
        return self._active.value

    @property
    def config(self) -> dict:
        self._completeIfNotSet(self._config)
        return self._config.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def events(self) -> list[str]:
        self._completeIfNotSet(self._events)
        return self._events.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def last_response(self) -> github.HookResponse.HookResponse:
        self._completeIfNotSet(self._last_response)
        return self._last_response.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def test_url(self) -> str:
        self._completeIfNotSet(self._test_url)
        return self._test_url.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def ping_url(self) -> str:
        self._completeIfNotSet(self._ping_url)
        return self._ping_url.value

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/hooks/{id} <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def edit(
        self,
        name: str,
        config: dict,
        events: Opt[list[str]] = NotSet,
        add_events: Opt[list[str]] = NotSet,
        remove_events: Opt[list[str]] = NotSet,
        active: Opt[bool] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/hooks/{id} <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        """
        assert isinstance(name, str), name
        assert isinstance(config, dict), config
        assert is_optional_list(events, str), events
        assert is_optional_list(add_events, str), add_events
        assert is_optional_list(remove_events, str), remove_events
        assert is_optional(active, bool), active
        post_parameters = NotSet.remove_unset_items(
            {
                "name": name,
                "config": config,
                "events": events,
                "add_events": add_events,
                "remove_events": remove_events,
                "active": active,
            }
        )

        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def test(self) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/hooks/{id}/tests <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        """
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/tests")

    def ping(self) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/hooks/{id}/pings <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        """
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/pings")

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "active" in attributes:  # pragma no branch
            self._active = self._makeBoolAttribute(attributes["active"])
        if "config" in attributes:  # pragma no branch
            self._config = self._makeDictAttribute(attributes["config"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "events" in attributes:  # pragma no branch
            self._events = self._makeListOfStringsAttribute(attributes["events"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "last_response" in attributes:  # pragma no branch
            self._last_response = self._makeClassAttribute(
                github.HookResponse.HookResponse, attributes["last_response"]
            )
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "test_url" in attributes:  # pragma no branch
            self._test_url = self._makeStringAttribute(attributes["test_url"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "ping_url" in attributes:  # pragma no branch
            self._ping_url = self._makeStringAttribute(attributes["ping_url"])
