############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Andy Casey <acasey@mso.anu.edu.au>                            #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 John Eskew <jeskew@edx.org>                                   #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
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

from typing import Any, Dict, Optional, Union

from github.GithubObject import (
    CompletableGithubObject,
    NotSet,
    _BadAttribute,
    _NotSetType,
    _ValuedAttribute,
)


class HeadCommit(CompletableGithubObject):
    """
    This class represents a Head Commit
    """

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value})

    @property
    def sha(self) -> Optional[str]:
        """
        :type: string
        """
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def url(self) -> Optional[str]:
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def _initAttributes(self) -> None:
        self._sha: Union[_ValuedAttribute, _BadAttribute, _NotSetType] = NotSet
        self._url: Union[_ValuedAttribute, _BadAttribute, _NotSetType] = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]):
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])


class CommitHeadBranch(CompletableGithubObject):
    """
    This class represents a Commit Head Branch
    """

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def name(self) -> Optional[str]:
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def commit(self) -> Optional[HeadCommit]:
        """
        :type: :class:`github.CommitHeadBranch.HeadCommit`
        """
        self._completeIfNotSet(self._commit)
        return self._commit.value

    @property
    def protected(self) -> Optional[bool]:
        """
        :type: boolean
        """
        self._completeIfNotSet(self._protected)
        return self._protected.value

    def _initAttributes(self):
        self._name: Union[_ValuedAttribute, _BadAttribute, _NotSetType] = NotSet
        self._commit: Union[_ValuedAttribute, _BadAttribute, _NotSetType] = NotSet
        self._protected: Union[_ValuedAttribute, _BadAttribute, _NotSetType] = NotSet

    def _useAttributes(self, attributes):
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "commit" in attributes:  # pragma no branch
            self._commit = self._makeClassAttribute(HeadCommit, attributes["commit"])
        if "protected" in attributes:  # pragma no branch
            self._protected = self._makeBoolAttribute(attributes["protected"])
