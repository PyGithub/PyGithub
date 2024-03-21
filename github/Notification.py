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
import github.Issue
import github.NotificationSubject
import github.PullRequest
import github.Repository
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class Notification(CompletableGithubObject):
    """
    This class represents Notifications.

    The reference can be found here
    https://docs.github.com/en/rest/reference/activity#notifications

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[str] = NotSet
        self._last_read_at: Attribute[datetime] = NotSet
        self._repository: Attribute[github.Repository.Repository] = NotSet
        self._subject: Attribute[github.NotificationSubject.NotificationSubject] = NotSet
        self._reason: Attribute[str] = NotSet
        self._subscription_url: Attribute[str] = NotSet
        self._unread: Attribute[bool] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "subject": self._subject.value})

    @property
    def id(self) -> str:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def last_read_at(self) -> datetime:
        self._completeIfNotSet(self._last_read_at)
        return self._last_read_at.value

    @property
    def repository(self) -> github.Repository.Repository:
        self._completeIfNotSet(self._repository)
        return self._repository.value

    @property
    def subject(self) -> github.NotificationSubject.NotificationSubject:
        self._completeIfNotSet(self._subject)
        return self._subject.value

    @property
    def reason(self) -> str:
        self._completeIfNotSet(self._reason)
        return self._reason.value

    @property
    def subscription_url(self) -> str:
        self._completeIfNotSet(self._subscription_url)
        return self._subscription_url.value

    @property
    def unread(self) -> bool:
        self._completeIfNotSet(self._unread)
        return self._unread.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def mark_as_read(self) -> None:
        """
        :calls: `PATCH /notifications/threads/{id} <https://docs.github.com/en/rest/reference/activity#notifications>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
        )

    def get_pull_request(self) -> github.PullRequest.PullRequest:
        headers, data = self._requester.requestJsonAndCheck("GET", self.subject.url)
        return github.PullRequest.PullRequest(self._requester, headers, data, completed=True)

    def get_issue(self) -> github.Issue.Issue:
        headers, data = self._requester.requestJsonAndCheck("GET", self.subject.url)
        return github.Issue.Issue(self._requester, headers, data, completed=True)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "last_read_at" in attributes:  # pragma no branch
            self._last_read_at = self._makeDatetimeAttribute(attributes["last_read_at"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "subject" in attributes:  # pragma no branch
            self._subject = self._makeClassAttribute(
                github.NotificationSubject.NotificationSubject, attributes["subject"]
            )
        if "reason" in attributes:  # pragma no branch
            self._reason = self._makeStringAttribute(attributes["reason"])
        if "subscription_url" in attributes:  # pragma no branch
            self._subscription_url = self._makeStringAttribute(attributes["subscription_url"])
        if "unread" in attributes:  # pragma no branch
            self._unread = self._makeBoolAttribute(attributes["unread"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
