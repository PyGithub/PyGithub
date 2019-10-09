# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
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

from __future__ import absolute_import

from operator import attrgetter

from . import Framework


class Topic(Framework.TestCase):
    def testSearch(self):
        expected_names = [
            'python',
            'django',
            'flask',
            'python-script',
            'python36',
            'opencv-python',
            'ruby',
            'python-library',
            'scikit-learn',
            'python37',
            'selenium-python',
            'sublime-text',
            'leetcode-python',
            'learning-python',
            'tkinter-python',
            'python35',
            'machinelearning-python',
            'python-flask',
            'python-package',
            'python-telegram-bot',
            'python-wrapper',
            'python3-6',
            'opencv3-python',
            'hackerrank-python',
            'python-api',
            'python2-7',
            'pythonista',
            'haxe',
            'python-requests',
            'python-2-7',
        ]

        self.assertListKeyEqual(self.g.search_topics("python"), attrgetter("name"), expected_names)
