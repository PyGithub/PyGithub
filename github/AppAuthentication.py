############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Denis Blanchette <denisblanchette@gmail.com>                  #
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


class AppAuthentication:
    def __init__(
        self,
        app_id,
        private_key,
        installation_id,
        token_permissions=None,
    ):
        assert isinstance(app_id, (int, str)), app_id
        assert isinstance(private_key, str)
        assert isinstance(installation_id, int), installation_id
        assert token_permissions is None or isinstance(
            token_permissions, dict
        ), token_permissions
        self.app_id = app_id
        self.private_key = private_key
        self.installation_id = installation_id
        self.token_permissions = token_permissions
