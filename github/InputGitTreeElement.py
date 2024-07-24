############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from github.GithubObject import NotSet, Opt, is_defined, is_optional


class InputGitTreeElement:
    """
    This class represents InputGitTreeElements.
    """

    def __init__(
        self,
        path: str,
        mode: str,
        type: str,
        content: Opt[str] = NotSet,
        sha: Opt[str | None] = NotSet,
    ):
        assert isinstance(path, str), path
        assert isinstance(mode, str), mode
        assert isinstance(type, str), type
        assert is_optional(content, str), content
        assert sha is None or is_optional(sha, str), sha
        self.__path = path
        self.__mode = mode
        self.__type = type
        self.__content = content
        self.__sha: Opt[str] | None = sha

    @property
    def _identity(self) -> dict[str, Any]:
        identity: dict[str, Any] = {
            "path": self.__path,
            "mode": self.__mode,
            "type": self.__type,
        }
        if is_defined(self.__sha):
            identity["sha"] = self.__sha
        if is_defined(self.__content):
            identity["content"] = self.__content
        return identity
