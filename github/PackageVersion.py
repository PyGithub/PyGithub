############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Bill Mill <bill.mill@gmail.com>                               #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 davidbrai <davidbrai@gmail.com>                               #
# Copyright 2014 Thialfihar <thi@thialfihar.org>                               #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Dan Vanderkam <danvdk@gmail.com>                              #
# Copyright 2015 Eliot Walker <eliot@lyft.com>                                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2018 Gilad Shefer <gshefer@redhat.com>                             #
# Copyright 2018 Joel Koglin <JoelKoglin@gmail.com>                            #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 netsgnut <284779+netsgnut@users.noreply.github.com>           #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Emir Hodzic <emir.hodzich@gmail.com>                          #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Andrew Dawes <53574062+AndrewJDawes@users.noreply.github.com> #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 YugoHino <henom06@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    _NotSetType,
    is_defined,
    is_optional,
    is_optional_list,
    is_undefined,
)



class PackageVersion(CompletableGithubObject):
    """
    This class represents PackageVersions.

    The reference can be found here
    https://docs.github.com/en/rest/packages/packages
    """

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def id(self) -> str:
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def package_html_url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._package_html_url)
        return self._package_html_url.value

    @property
    def license(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._license)
        return self._license.value

    @property
    def created_at(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def description(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def html_url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def metadata(self) -> dict:
        """
        :type: dict
        """
        self._completeIfNotSet(self._metadata)
        return self._metadata.value

    def _initAttributes(self):
        self._id: Opt[int] = NotSet
        self._name: Opt[str] = NotSet
        self._url: Opt[str] = NotSet
        self._package_html_url: Opt[str] = NotSet
        self._license: Opt[str] = NotSet
        self._created_at: Opt[str] = NotSet
        self._updated_at: Opt[str] = NotSet
        self._description: Opt[str] = NotSet
        self._html_url: Opt[str] = NotSet
        self._metadata: Opt[dict] = NotSet

    def _useAttributes(self, attributes: dict):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
        if "package_html_url" in attributes:
            self._package_html_url = self._makeStringAttribute(attributes["package_html_url"])
        if "license" in attributes:
            self._license = self._makeStringAttribute(attributes["license"])
        if "created_at" in attributes:
            self._created_at = self._makeStringAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeStringAttribute(attributes["updated_at"])
        if "description" in attributes:
            self._description = self._makeStringAttribute(attributes["description"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "metadata" in attributes:
            self._metadata = self._makeDictAttribute(attributes["metadata"])
