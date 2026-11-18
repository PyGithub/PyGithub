############################ Copyrights and license ############################
#                                                                              #
# Copyright 2026 Enrico Minack <github@enrico.minack.dev>                      #
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

"""
Compatibility imports for names that are not available in the standard library of all supported Python versions.

Python 3.13 provides all these names in the standard library (``warnings.deprecated`` was added in 3.13), so
``typing-extensions`` is only a dependency for Python versions before 3.13 (see ``pyproject.toml``).

Import these names from here rather than from ``typing`` / ``warnings`` / ``typing_extensions``::

    from github.compat import deprecated

"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 13):
    from typing import NotRequired, Self, TypedDict
    from warnings import deprecated
else:
    from typing_extensions import NotRequired, Self, TypedDict, deprecated

__all__ = [
    "NotRequired",
    "Self",
    "TypedDict",
    "deprecated",
]
