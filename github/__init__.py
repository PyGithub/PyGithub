# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

"""
The primary class you will instanciate is :class:`github.Github.Github`.
From its ``get_``, ``create_`` methods, you will obtain instances of all Github objects
like :class:`github.NamedUser.NamedUser` or :class:`github.Repository.Repository`.
"""

import logging

from Github import Github
from GithubException import GithubException
from InputFileContent import InputFileContent
from InputGitAuthor import InputGitAuthor
from InputGitTreeElement import InputGitTreeElement


def enable_console_debug_logging():  # pragma no cover
    """
    This function sets up a very simple logging configuration (log everything on standard output) that is useful for troubleshooting.
    """

    logger = logging.getLogger("github")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
