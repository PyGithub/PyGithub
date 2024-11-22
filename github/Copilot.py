from __future__ import annotations

from typing import TYPE_CHECKING, Any

import github.CopilotSeat
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.CopilotSeat import CopilotSeat
    from github.Requester import Requester


class Copilot(NonCompletableGithubObject):
    def __init__(self, requester: Requester, org_name: str) -> None:
        super().__init__(requester, {}, {"org_name": org_name}, True)

    def _initAttributes(self) -> None:
        self._org_name: Attribute[str] = NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "org_name" in attributes:  # pragma no branch
            self._org_name = self._makeStringAttribute(attributes["org_name"])

    def __repr__(self) -> str:
        return self.get__repr__({"org_name": self._org_name.value if self._org_name is not NotSet else NotSet})

    @property
    def org_name(self) -> str:
        return self._org_name.value

    def get_all_seats(self) -> PaginatedList[CopilotSeat]:
        """
        :calls: `GET /orgs/{org}/copilot/billing/seats <https://docs.github.com/en/rest/copilot/copilot-business>`_
        """
        url = f"/orgs/{self._org_name.value}/copilot/billing/seats"
        return PaginatedList(
            github.CopilotSeat.CopilotSeat,
            self._requester,
            url,
            None,
            list_item="seats",
        )

    def add_seat(self, selected_usernames: list[str]) -> int:
        """
        :calls: `POST /orgs/{org}/copilot/billing/selected_users <https://docs.github.com/en/rest/copilot/copilot-business>`_
        :param selected_usernames: List of usernames to add Copilot seats for
        :rtype: int
        :return: Number of seats created
        """
        url = f"/orgs/{self._org_name.value}/copilot/billing/selected_users"
        _, data = self._requester.requestJsonAndCheck(
            "POST",
            url,
            input={"selected_usernames": selected_usernames},
        )
        return data["seats_created"]

    def remove_seat(self, selected_usernames: list[str]) -> int:
        """
        :calls: `DELETE /orgs/{org}/copilot/billing/selected_users <https://docs.github.com/en/rest/copilot/copilot-business>`_
        :param selected_usernames: List of usernames to remove Copilot seats for
        :rtype: int
        :return: Number of seats cancelled
        """
        url = f"/orgs/{self._org_name.value}/copilot/billing/selected_users"
        _, data = self._requester.requestJsonAndCheck(
            "DELETE",
            url,
            input={"selected_usernames": selected_usernames},
        )
        return data["seats_cancelled"]
