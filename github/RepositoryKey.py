############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Srijan Choudhary <srijan4@gmail.com>                          #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Jimmy Zelinskie <jimmy.zelinskie+git@gmail.com>               #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Laurent Raufaste <analogue@glop.org>                          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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
from datetime import datetime

import github.GithubObject


class RepositoryKey(github.GithubObject.CompletableGithubObject):
    """
    This class represents RepositoryKeys. The reference can be found here https://docs.github.com/en/rest/reference/repos#deploy-keys
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value, "title": self._title.value})

    @property
    def created_at(self) -> datetime:
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def id(self) -> int:
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def key(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._key)
        return self._key.value

    @property
    def title(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._title)
        return self._title.value

    @property
    def url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def verified(self) -> bool:
        """
        :type: bool
        """
        self._completeIfNotSet(self._verified)
        return self._verified.value

    @property
    def read_only(self) -> bool:
        """
        :type: bool
        """
        self._completeIfNotSet(self._read_only)
        return self._read_only.value

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/keys/{id} <https://docs.github.com/en/rest/reference/repos#deploy-keys>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def _initAttributes(self):
        self._created_at = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._key = github.GithubObject.NotSet
        self._title = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._verified = github.GithubObject.NotSet
        self._read_only = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "key" in attributes:  # pragma no branch
            self._key = self._makeStringAttribute(attributes["key"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "verified" in attributes:  # pragma no branch
            self._verified = self._makeBoolAttribute(attributes["verified"])
        if "read_only" in attributes:  # pragma no branch
            self._read_only = self._makeBoolAttribute(attributes["read_only"])
