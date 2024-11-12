############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Jeffrey Melvin <jeffrey.melvin@workiva.com>                   #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class File(NonCompletableGithubObject):
    """
    This class represents Files.
    """

    def _initAttributes(self) -> None:
        self._additions: Attribute[int] = NotSet
        self._blob_url: Attribute[str] = NotSet
        self._changes: Attribute[int] = NotSet
        self._contents_url: Attribute[str] = NotSet
        self._deletions: Attribute[int] = NotSet
        self._filename: Attribute[str] = NotSet
        self._patch: Attribute[str] = NotSet
        self._previous_filename: Attribute[str] = NotSet
        self._raw_url: Attribute[str] = NotSet
        self._sha: Attribute[str] = NotSet
        self._status: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value, "filename": self._filename.value})

    @property
    def additions(self) -> int:
        return self._additions.value

    @property
    def blob_url(self) -> str:
        return self._blob_url.value

    @property
    def changes(self) -> int:
        return self._changes.value

    @property
    def contents_url(self) -> str:
        return self._contents_url.value

    @property
    def deletions(self) -> int:
        return self._deletions.value

    @property
    def filename(self) -> str:
        return self._filename.value

    @property
    def patch(self) -> str:
        return self._patch.value

    @property
    def previous_filename(self) -> str:
        return self._previous_filename.value

    @property
    def raw_url(self) -> str:
        return self._raw_url.value

    @property
    def sha(self) -> str:
        return self._sha.value

    @property
    def status(self) -> str:
        return self._status.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "additions" in attributes:  # pragma no branch
            self._additions = self._makeIntAttribute(attributes["additions"])
        if "blob_url" in attributes:  # pragma no branch
            self._blob_url = self._makeStringAttribute(attributes["blob_url"])
        if "changes" in attributes:  # pragma no branch
            self._changes = self._makeIntAttribute(attributes["changes"])
        if "contents_url" in attributes:  # pragma no branch
            self._contents_url = self._makeStringAttribute(attributes["contents_url"])
        if "deletions" in attributes:  # pragma no branch
            self._deletions = self._makeIntAttribute(attributes["deletions"])
        if "filename" in attributes:  # pragma no branch
            self._filename = self._makeStringAttribute(attributes["filename"])
        if "patch" in attributes:  # pragma no branch
            self._patch = self._makeStringAttribute(attributes["patch"])
        if "previous_filename" in attributes:  # pragma no branch
            self._previous_filename = self._makeStringAttribute(attributes["previous_filename"])
        if "raw_url" in attributes:  # pragma no branch
            self._raw_url = self._makeStringAttribute(attributes["raw_url"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
