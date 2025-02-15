############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Greg <31892308+jmgreg31@users.noreply.github.com>    #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from datetime import datetime
from typing import Any

import github.GithubObject
from github.GithubObject import Attribute, NotSet


class HookDeliverySummary(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents a Summary of HookDeliveries.

    The OpenAPI schema can be found at
    - /components/schemas/hook-delivery-item

    """

    def _initAttributes(self) -> None:
        self._action: Attribute[str] = NotSet
        self._delivered_at: Attribute[datetime] = NotSet
        self._duration: Attribute[float] = NotSet
        self._event: Attribute[str] = NotSet
        self._guid: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._installation_id: Attribute[int] = NotSet
        self._redelivery: Attribute[bool] = NotSet
        self._repository_id: Attribute[int] = NotSet
        self._status: Attribute[str] = NotSet
        self._status_code: Attribute[int] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def action(self) -> str | None:
        return self._action.value

    @property
    def delivered_at(self) -> datetime | None:
        return self._delivered_at.value

    @property
    def duration(self) -> float | None:
        return self._duration.value

    @property
    def event(self) -> str | None:
        return self._event.value

    @property
    def guid(self) -> str | None:
        return self._guid.value

    @property
    def id(self) -> int | None:
        return self._id.value

    @property
    def installation_id(self) -> int | None:
        return self._installation_id.value

    @property
    def redelivery(self) -> bool | None:
        return self._redelivery.value

    @property
    def repository_id(self) -> int | None:
        return self._repository_id.value

    @property
    def status(self) -> str | None:
        return self._status.value

    @property
    def status_code(self) -> int | None:
        return self._status_code.value

    @property
    def url(self) -> str | None:
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "action" in attributes:  # pragma no branch
            self._action = self._makeStringAttribute(attributes["action"])
        if "delivered_at" in attributes:  # pragma no branch
            self._delivered_at = self._makeDatetimeAttribute(attributes["delivered_at"])
        if "duration" in attributes:  # pragma no branch
            self._duration = self._makeFloatAttribute(attributes["duration"])
        if "event" in attributes:  # pragma no branch
            self._event = self._makeStringAttribute(attributes["event"])
        if "guid" in attributes:  # pragma no branch
            self._guid = self._makeStringAttribute(attributes["guid"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "installation_id" in attributes:  # pragma no branch
            self._installation_id = self._makeIntAttribute(attributes["installation_id"])
        if "redelivery" in attributes:  # pragma no branch
            self._redelivery = self._makeBoolAttribute(attributes["redelivery"])
        if "repository_id" in attributes:  # pragma no branch
            self._repository_id = self._makeIntAttribute(attributes["repository_id"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "status_code" in attributes:  # pragma no branch
            self._status_code = self._makeIntAttribute(attributes["status_code"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])


class HookDeliveryRequest(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents a HookDeliveryRequest.

    The OpenAPI schema can be found at
    - /components/schemas/hook-delivery/properties/request

    """

    def _initAttributes(self) -> None:
        self._payload: Attribute[dict] = NotSet
        self._request_headers: Attribute[dict] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"payload": self._payload.value})

    @property
    def headers(self) -> dict | None:
        return self._request_headers.value

    @property
    def payload(self) -> dict | None:
        return self._payload.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "headers" in attributes:  # pragma no branch
            self._request_headers = self._makeDictAttribute(attributes["headers"])
        if "payload" in attributes:  # pragma no branch
            self._payload = self._makeDictAttribute(attributes["payload"])


class HookDeliveryResponse(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents a HookDeliveryResponse.

    The OpenAPI schema can be found at
    - /components/schemas/hook-delivery/properties/response

    """

    def _initAttributes(self) -> None:
        self._payload: Attribute[str] = NotSet
        self._response_headers: Attribute[dict] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"payload": self._payload.value})

    @property
    def headers(self) -> dict | None:
        return self._response_headers.value

    @property
    def payload(self) -> str | None:
        return self._payload.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "headers" in attributes:  # pragma no branch
            self._response_headers = self._makeDictAttribute(attributes["headers"])
        if "payload" in attributes:  # pragma no branch
            self._payload = self._makeStringAttribute(attributes["payload"])


class HookDelivery(HookDeliverySummary):
    """
    This class represents a HookDelivery.

    The OpenAPI schema can be found at
    - /components/schemas/hook-delivery

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._request: Attribute[HookDeliveryRequest] = NotSet
        self._response: Attribute[HookDeliveryResponse] = NotSet
        self._throttled_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def request(self) -> HookDeliveryRequest | None:
        return self._request.value

    @property
    def response(self) -> HookDeliveryResponse | None:
        return self._response.value

    @property
    def throttled_at(self) -> datetime:
        return self._throttled_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "request" in attributes:  # pragma no branch
            self._request = self._makeClassAttribute(HookDeliveryRequest, attributes["request"])
        if "response" in attributes:  # pragma no branch
            self._response = self._makeClassAttribute(HookDeliveryResponse, attributes["response"])
            # self._response = self._makeDictAttribute(attributes["response"])
        if "throttled_at" in attributes:  # pragma no branch
            self._throttled_at = self._makeDatetimeAttribute(attributes["throttled_at"])
