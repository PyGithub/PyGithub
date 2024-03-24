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
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from typing import Any

import github.GitAuthor
import github.GithubObject
import github.GitTree
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class GitCommit(CompletableGithubObject):
    """
    This class represents GitCommits.

    The reference can be found here
    https://docs.github.com/en/rest/reference/git#commits

    """

    def _initAttributes(self) -> None:
        self._author: Attribute[github.GitAuthor.GitAuthor] = NotSet
        self._committer: Attribute[github.GitAuthor.GitAuthor] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._message: Attribute[str] = NotSet
        self._parents: Attribute[list[GitCommit]] = NotSet
        self._sha: Attribute[str] = NotSet
        self._tree: Attribute[github.GitTree.GitTree] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value})

    @property
    def author(self) -> github.GitAuthor.GitAuthor:
        self._completeIfNotSet(self._author)
        return self._author.value

    @property
    def committer(self) -> github.GitAuthor.GitAuthor:
        self._completeIfNotSet(self._committer)
        return self._committer.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def message(self) -> str:
        self._completeIfNotSet(self._message)
        return self._message.value

    @property
    def parents(self) -> list[GitCommit]:
        self._completeIfNotSet(self._parents)
        return self._parents.value

    @property
    def sha(self) -> str:
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def tree(self) -> github.GitTree.GitTree:
        self._completeIfNotSet(self._tree)
        return self._tree.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def _identity(self) -> str:
        return self.sha

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(github.GitAuthor.GitAuthor, attributes["author"])
        if "committer" in attributes:  # pragma no branch
            self._committer = self._makeClassAttribute(github.GitAuthor.GitAuthor, attributes["committer"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
        if "parents" in attributes:  # pragma no branch
            self._parents = self._makeListOfClassesAttribute(GitCommit, attributes["parents"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "tree" in attributes:  # pragma no branch
            self._tree = self._makeClassAttribute(github.GitTree.GitTree, attributes["tree"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
