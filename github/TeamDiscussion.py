############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Benoit Latinier <benoit@latinier.fr>                          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Yossarian King <yggy@blackbirdinteractive.com>                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any

from github.DiscussionBase import DiscussionBase
from github.GithubObject import Attribute, NotSet


class TeamDiscussion(DiscussionBase):
    """
    This class represents TeamDiscussions.

    The reference can be found here
    https://docs.github.com/en/rest/reference/teams#discussions

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._body_version: Attribute[str] = NotSet
        self._comments_count: Attribute[int] = NotSet
        self._comments_url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._pinned: Attribute[bool] = NotSet
        self._private: Attribute[bool] = NotSet
        self._team_url: Attribute[str] = NotSet

    @property
    def body_version(self) -> str:
        self._completeIfNotSet(self._body_version)
        return self._body_version.value

    @property
    def comments_count(self) -> int:
        self._completeIfNotSet(self._comments_count)
        return self._comments_count.value

    @property
    def comments_url(self) -> str:
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def pinned(self) -> bool:
        self._completeIfNotSet(self._pinned)
        return self._pinned.value

    @property
    def private(self) -> bool:
        self._completeIfNotSet(self._private)
        return self._private.value

    @property
    def team_url(self) -> str:
        self._completeIfNotSet(self._team_url)
        return self._team_url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "body_version" in attributes:  # pragma no branch
            self._body_version = self._makeStringAttribute(attributes["body_version"])
        if "comments_count" in attributes:  # pragma no branch
            self._comments_count = self._makeIntAttribute(attributes["comments_count"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "pinned" in attributes:  # pragma no branch
            self._pinned = self._makeBoolAttribute(attributes["pinned"])
        if "private" in attributes:  # pragma no branch
            self._private = self._makeBoolAttribute(attributes["private"])
        if "team_url" in attributes:  # pragma no branch
            self._team_url = self._makeStringAttribute(attributes["team_url"])
