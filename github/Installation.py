############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
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

import github.GithubObject
import github.NamedUser
import github.PaginatedList
import github.Repository


class Installation(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Installations.
    The reference can be found here https://docs.github.com/en/rest/reference/apps#installations
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value})

    @property
    def access_tokens_url(self):
        """
        :type: string
        """
        return self._access_tokens_url.value

    @property
    def account(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._account.value

    @property
    def app_id(self):
        """
        :type: integer
        """
        return self._app_id.value

    @property
    def app_slug(self):
        """
        :type: string
        """
        return self._app_slug.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        return self._created_at.value

    @property
    def events(self):
        """
        :type: list of string
        """
        return self._events.value

    @property
    def has_multiple_single_files(self):
        """
        :type: bool
        """
        return self._has_multiple_single_files.value

    @property
    def html_url(self):
        """
        :type: string
        """
        return self._html_url.value

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id.value

    @property
    def permissions(self):
        """
        :type: dict
        """
        return self._permissions.value

    @property
    def repositories_url(self):
        """
        :type: string
        """
        return self._repositories_url.value

    @property
    def repository_selection(self):
        """
        :type: string
        """
        return self._repository_selection.value

    @property
    def single_file_name(self):
        """
        :type: string or None
        """
        return self._single_file_name.value

    @property
    def single_file_paths(self):
        """
        :type: list of string
        """
        return self._single_file_paths.value

    @property
    def target_id(self):
        """
        :type: integer
        """
        return self._target_id.value

    @property
    def target_type(self):
        """
        :type: string
        """
        return self._target_type.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        return self._updated_at.value

    def get_repos(self):
        """
        :calls: `GET /installation/repositories <https://docs.github.com/en/rest/reference/apps#list-repositories-accessible-to-the-app-installation>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            contentClass=github.Repository.Repository,
            requester=self._requester,
            firstUrl=self.repositories_url,
            firstParams=None,
            headers={"Accept": "application/vnd.github.v3+json"},
            list_item="repositories",
        )

    def _initAttributes(self):
        self._access_tokens_url = github.GithubObject.NotSet
        self._account = github.GithubObject.NotSet
        self._app_id = github.GithubObject.NotSet
        self._app_slug = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._events = github.GithubObject.NotSet
        self._has_multiple_single_files = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._permissions = github.GithubObject.NotSet
        self._repositories_url = github.GithubObject.NotSet
        self._repository_selection = github.GithubObject.NotSet
        self._single_file_name = github.GithubObject.NotSet
        self._single_file_paths = github.GithubObject.NotSet
        self._target_id = github.GithubObject.NotSet
        self._target_type = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "access_tokens_url" in attributes:  # pragma no branch
            self._access_tokens_url = self._makeStringAttribute(
                attributes["access_tokens_url"]
            )
        if "account" in attributes:  # pragma no branch
            self._account = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["account"]
            )
        if "app_id" in attributes:  # pragma no branch
            self._app_id = self._makeIntAttribute(attributes["app_id"])
        if "app_slug" in attributes:  # pragma no branch
            self._app_slug = self._makeStringAttribute(attributes["app_slug"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "events" in attributes:  # pragma no branch
            self._events = self._makeListOfStringsAttribute(attributes["events"])
        if "has_multiple_single_files" in attributes:  # pragma no branch
            self._has_multiple_single_files = self._makeBoolAttribute(
                attributes["has_multiple_single_files"]
            )
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeDictAttribute(attributes["permissions"])
        if "repositories_url" in attributes:  # pragma no branch
            self._repositories_url = self._makeStringAttribute(
                attributes["repositories_url"]
            )
        if "repository_selection" in attributes:  # pragma no branch
            self._repository_selection = self._makeStringAttribute(
                attributes["repository_selection"]
            )
        if "single_file_name" in attributes:  # pragma no branch
            self._single_file_name = self._makeStringAttribute(
                attributes["single_file_name"]
            )
        if "single_file_paths" in attributes:  # pragma no branch
            self._single_file_paths = self._makeListOfStringsAttribute(
                attributes["single_file_paths"]
            )
        if "target_id" in attributes:  # pragma no branch
            self._target_id = self._makeIntAttribute(attributes["target_id"])
        if "target_type" in attributes:  # pragma no branch
            self._target_type = self._makeStringAttribute(attributes["target_type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
