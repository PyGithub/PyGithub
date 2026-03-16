# FILE AUTO GENERATED DO NOT TOUCH
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Peter Golm <golm.peter@gmail.com>                             #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Olof-Joachim Frahm (欧雅福) <olof@macrolet.net>                  #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Matthias Bilger <matthias@bilger.info>                        #
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

from . import GithubObject, Issue, NotificationSubject, PullRequest, Repository
from .GithubObject import Attribute, CompletableGithubObject, NotSet


class Notification(CompletableGithubObject):
    """
    This class represents Notifications.

    The reference can be found here
    https://docs.github.com/en/rest/reference/activity#notifications

    The OpenAPI schema can be found at

    - /components/schemas/thread

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[str] = NotSet
        self._last_read_at: Attribute[datetime] = NotSet
        self._reason: Attribute[str] = NotSet
        self._repository: Attribute[Repository.Repository] = NotSet
        self._subject: Attribute[NotificationSubject.NotificationSubject] = NotSet
        self._subscription_url: Attribute[str] = NotSet
        self._unread: Attribute[bool] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "subject": self._subject.value})

    @property
    async def id(self) -> str:
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def last_read_at(self) -> datetime:
        await self._completeIfNotSet(self._last_read_at)
        return self._last_read_at.value

    @property
    async def reason(self) -> str:
        await self._completeIfNotSet(self._reason)
        return self._reason.value

    @property
    async def repository(self) -> Repository.Repository:
        await self._completeIfNotSet(self._repository)
        return self._repository.value

    @property
    async def subject(self) -> NotificationSubject.NotificationSubject:
        await self._completeIfNotSet(self._subject)
        return self._subject.value

    @property
    async def subscription_url(self) -> str:
        await self._completeIfNotSet(self._subscription_url)
        return self._subscription_url.value

    @property
    async def unread(self) -> bool:
        await self._completeIfNotSet(self._unread)
        return self._unread.value

    @property
    async def updated_at(self) -> datetime:
        await self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    async def mark_as_read(self) -> None:
        """
        :calls: `PATCH /notifications/threads/{thread_id} <https://docs.github.com/en/rest/reference/activity#notifications>`_
        """
        headers, data = await self._requester.requestJsonAndCheck(
            "PATCH",
            await self.url,
        )

    async def mark_as_done(self) -> None:
        """
        :calls: `DELETE /notifications/threads/{thread_id} <https://docs.github.com/en/rest/reference/activity#notifications>`_
        """
        headers, data = await self._requester.requestJsonAndCheck(
            "DELETE",
            await self.url,
        )

    async def get_pull_request(self) -> PullRequest.PullRequest:
        return PullRequest.PullRequest(self._requester, url=(await self.subject).url)

    async def get_issue(self) -> Issue.Issue:
        return Issue.Issue(self._requester, url=(await self.subject).url)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "last_read_at" in attributes:  # pragma no branch
            self._last_read_at = self._makeDatetimeAttribute(attributes["last_read_at"])
        if "reason" in attributes:  # pragma no branch
            self._reason = self._makeStringAttribute(attributes["reason"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(Repository.Repository, attributes["repository"])
        if "subject" in attributes:  # pragma no branch
            self._subject = self._makeClassAttribute(NotificationSubject.NotificationSubject, attributes["subject"])
        if "subscription_url" in attributes:  # pragma no branch
            self._subscription_url = self._makeStringAttribute(attributes["subscription_url"])
        if "unread" in attributes:  # pragma no branch
            self._unread = self._makeBoolAttribute(attributes["unread"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
