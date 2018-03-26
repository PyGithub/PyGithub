# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Kyle Hornberg <khornberg@users.noreply.github.com>            #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
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

import github.GithubObject

import github.Commit


class Branch(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Branches. The reference can be found here http://developer.github.com/v3/repos/#list-branches
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value})

    @property
    def commit(self):
        """
        :type: :class:`github.Commit.Commit`
        """
        return self._commit.value

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    @property
    def protected(self):
        """
        :type: bool
        """
        return self._protected.value

    @property
    def enforcement_level(self):
        """
        :type: string
        """
        return self._enforcement_level.value

    @property
    def contexts(self):
        """
        :type: list of strings
        """
        return self._contexts.value

    def _initAttributes(self):
        self._commit = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "commit" in attributes:  # pragma no branch
            self._commit = self._makeClassAttribute(github.Commit.Commit, attributes["commit"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "protection" in attributes:
            self._protected = self._makeBoolAttribute(attributes["protection"]["enabled"])
            self._enforcement_level = self._makeStringAttribute(attributes["protection"]["required_status_checks"]["enforcement_level"])
            self._contexts = self._makeListOfStringsAttribute(attributes["protection"]["required_status_checks"]["contexts"])
