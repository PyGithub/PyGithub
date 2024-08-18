############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CheckRunOutput(NonCompletableGithubObject):
    """
    This class represents the output of check run.
    """

    def _initAttributes(self) -> None:
        self._annotations_count: Attribute[int] = NotSet
        self._annotations_url: Attribute[str] = NotSet
        self._summary: Attribute[str] = NotSet
        self._text: Attribute[str] = NotSet
        self._title: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"title": self._title.value})

    @property
    def annotations_count(self) -> int:
        return self._annotations_count.value

    @property
    def annotations_url(self) -> str:
        return self._annotations_url.value

    @property
    def summary(self) -> str:
        return self._summary.value

    @property
    def text(self) -> str:
        return self._text.value

    @property
    def title(self) -> str:
        return self._title.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "annotations_count" in attributes:  # pragma no branch
            self._annotations_count = self._makeIntAttribute(attributes["annotations_count"])
        if "annotations_url" in attributes:  # pragma no branch
            self._annotations_url = self._makeStringAttribute(attributes["annotations_url"])
        if "summary" in attributes:  # pragma no branch
            self._summary = self._makeStringAttribute(attributes["summary"])
        if "text" in attributes:  # pragma no branch
            self._text = self._makeStringAttribute(attributes["text"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
