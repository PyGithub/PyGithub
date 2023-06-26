############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
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


from __future__ import annotations

from github.GithubObject import NotSet, Opt, _NotSetType


class InputFileContent:
    """
    This class represents InputFileContents
    """

    def __init__(self, content: str, new_name: Opt[str] = NotSet):
        """
        :param content: string
        :param new_name: string
        """

        assert isinstance(content, str), content
        assert isinstance(new_name, (_NotSetType, str)), new_name
        self.__newName = new_name
        self.__content = content

    @property
    def _identity(self) -> dict[str, str]:
        identity: dict[str, str] = {
            "content": self.__content,
        }
        if not isinstance(self.__newName, _NotSetType):
            identity["filename"] = self.__newName
        return identity
