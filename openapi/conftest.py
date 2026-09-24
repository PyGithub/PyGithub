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

from . import Cli


def pytest_addoption(parser):
    parser.addoption("--keep", action="store_true", help="keep intermediate test results")
    parser.addoption("--approve", action="store_true", help="approve any actual results as expected")


def pytest_configure(config):
    if config.getoption("keep", default=False):
        Cli.keepMode()
    if config.getoption("approve", default=False):
        Cli.approveMode()
