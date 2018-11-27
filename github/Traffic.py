# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2018 Ivan Minno <iminno@andrew.cmu.edu>                            #
# Copyright 2018 Zilei Gu <zileig@andrew.cmu.edu>                              #
# Copyright 2018 Yves Zumbach <yzumbach@andrew.cmu.edu>                        #
# Copyright 2018 Leying Chen <leyingc@andrew.cmu.edu>                          #
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


class Traffic(github.GithubObject.CompletableGithubObject):
    """
    This class represents Traffic for a GitHub repository.
    The reference can be found here https://developer.github.com/v3/repos/traffic/
    """

    def __repr__(self):
        return self.get__repr__({
            !!!!!!
        })

    @property
    def top_paths(self):
        """
        :type: list of :class:`github.Path.Path`
        """
        self._completeIfNotSet(self._top_paths)
        return self._top_paths.value

    @property
    def top_referrers(self):
        """
        :type: list of :class:`github.Referrer.Referrer`
        """
        self._completeIfNotSet(self._top_referrers)
        return self._top_referrers.value

    @property
    def views_per_week(self):
        """
        :type: list of :class:`github.TrafficForDate.TrafficForDate`
        """
        self._completeIfNotSet(self._views_per_week)
        return self._views_per_week.value

    @property
    def views_per_day(self):
        """
        :type: list of :class:`github.TrafficForDate.TrafficForDate`
        """
        self._completeIfNotSet(self._views_per_day)
        return self._views_per_day.value

    @property
    def view_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._view_count)
        return self._view_count.value

    @property
    def view_uniques(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._view_uniques)
        return self._view_uniques.value

    @property
    def clones_per_week(self):
        """
        :type: list of :class:`github.TrafficForDate.TrafficForDate`
        """
        self._completeIfNotSet(self._clones_per_week)
        return self._clones_per_week.value

    @property
    def clones_per_day(self):
        """
        :type: list of :class:`github.TrafficForDate.TrafficForDate`
        """
        self._completeIfNotSet(self._clones_per_day)
        return self._clones_per_day.value

    @property
    def clone_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._clone_count)
        return self._clone_count.value

    @property
    def clone_uniques(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._clone_uniques)
        return self._clone_uniques.value

    def _initAttributes(self):
        self._top_paths = github.GithubObject.NotSet
        self._top_referrers = github.GithubObject.NotSet
        self._views_per_week = github.GithubObject.NotSet
        self._views_per_day = github.GithubObject.NotSet
        self._view_count = github.GithubObject.NotSet
        self._view_uniques = github.GithubObject.NotSet
        self._clones_per_week = github.GithubObject.NotSet
        self._clones_per_day = github.GithubObject.NotSet
        self._clone_count = github.GithubObject.NotSet
        self._clone_uniques = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "top_paths" in attributes:  # pragma no branch
            self._top_paths = self._makeListOfClassesAttribute(github.Path.Path, attributes["top_paths"])
        if "top_referrers" in attributes:  # pragma no branch
            self._top_paths = self._makeListOfClassesAttribute(github.Referrer.Referrer, attributes["top_referrers"])
        if "views_per_week" in attributes:  # pragma no branch
            self._views_per_week = self._makeListOfClassesAttribute(github.TrafficForDate.TrafficForDate, attributes["views_per_week"])
        if "views_per_day" in attributes:  # pragma no branch
            self._views_per_day = self._makeListOfClassesAttribute(github.TrafficForDate.TrafficForDate, attributes["views_per_day"])
        if "view_count" in attributes:  # pragma no branch
            self._view_count = self._makeIntAttribute(attributes["view_count"])
        if "view_uniques" in attributes:  # pragma no branch
            self._view_uniques = self._makeIntAttribute(attributes["view_uniques"])
        if "clones_per_week" in attributes:  # pragma no branch
            self._clones_per_week = self._makeListOfClassesAttribute(github.TrafficForDate.TrafficForDate, attributes["clones_per_week"])
        if "clones_per_day" in attributes:  # pragma no branch
            self._clones_per_day = self._makeListOfClassesAttribute(github.TrafficForDate.TrafficForDate, attributes["clones_per_day"])
        if "clone_count" in attributes:  # pragma no branch
            self._clone_count = self._makeIntAttribute(attributes["clone_count"])
        if "clone_uniques" in attributes:  # pragma no branch
            self._clone_uniques = self._makeIntAttribute(attributes["clone_uniques"])
