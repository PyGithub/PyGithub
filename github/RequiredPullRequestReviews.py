############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Benjamin K <53038537+treee111@users.noreply.github.com>       #
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

from typing import TYPE_CHECKING, Any

import github.NamedUser
import github.Team
from github.GithubObject import Attribute, CompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.NamedUser import NamedUser
    from github.Team import Team


class RequiredPullRequestReviews(CompletableGithubObject):
    """
    This class represents Required Pull Request Reviews.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#get-pull-request-review-protection

    """

    def _initAttributes(self) -> None:
        self._dismiss_stale_reviews: Attribute[bool] = NotSet
        self._require_code_owner_reviews: Attribute[bool] = NotSet
        self._required_approving_review_count: Attribute[int] = NotSet
        self._users: Attribute[list[NamedUser]] = NotSet
        self._teams: Attribute[list[Team]] = NotSet
        self._require_last_push_approval: Attribute[bool] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "url": self._url.value,
                "dismiss_stale_reviews": self._dismiss_stale_reviews.value,
                "require_code_owner_reviews": self._require_code_owner_reviews.value,
                "require_last_push_approval": self._require_last_push_approval.value,
            }
        )

    @property
    def dismiss_stale_reviews(self) -> bool:
        self._completeIfNotSet(self._dismiss_stale_reviews)
        return self._dismiss_stale_reviews.value

    @property
    def require_code_owner_reviews(self) -> bool:
        self._completeIfNotSet(self._require_code_owner_reviews)
        return self._require_code_owner_reviews.value

    @property
    def required_approving_review_count(self) -> int:
        self._completeIfNotSet(self._required_approving_review_count)
        return self._required_approving_review_count.value

    @property
    def require_last_push_approval(self) -> bool:
        self._completeIfNotSet(self._require_last_push_approval)
        return self._require_last_push_approval.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def dismissal_users(self) -> list[NamedUser]:
        self._completeIfNotSet(self._users)
        return self._users.value

    @property
    def dismissal_teams(self) -> list[Team]:
        self._completeIfNotSet(self._teams)
        return self._teams.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "dismissal_restrictions" in attributes:  # pragma no branch
            if "users" in attributes["dismissal_restrictions"]:
                self._users = self._makeListOfClassesAttribute(
                    github.NamedUser.NamedUser,
                    attributes["dismissal_restrictions"]["users"],
                )
            if "teams" in attributes["dismissal_restrictions"]:  # pragma no branch
                self._teams = self._makeListOfClassesAttribute(
                    github.Team.Team, attributes["dismissal_restrictions"]["teams"]
                )
        if "dismiss_stale_reviews" in attributes:  # pragma no branch
            self._dismiss_stale_reviews = self._makeBoolAttribute(attributes["dismiss_stale_reviews"])
        if "require_code_owner_reviews" in attributes:  # pragma no branch
            self._require_code_owner_reviews = self._makeBoolAttribute(attributes["require_code_owner_reviews"])
        if "required_approving_review_count" in attributes:  # pragma no branch
            self._required_approving_review_count = self._makeIntAttribute(
                attributes["required_approving_review_count"]
            )
        if "require_last_push_approval" in attributes:  # pragma no branch
            self._require_last_push_approval = self._makeBoolAttribute(attributes["require_last_push_approval"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
