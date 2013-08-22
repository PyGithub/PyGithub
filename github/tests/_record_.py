# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
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

import sys
import unittest

import github.tests.Framework
import github.tests.AllTests


# #189: This seems equivalent to "python -m github.tests ClassName.methodName --record"


def main(argv):
    if len(argv) < 2:
        print "Run sepecified test in record mode."
        print "Usage:"
        print "_record_.py [module_name] [other_arg] ..."
        print "    e.g. _record_.py AllTests"
        return

    github.tests.Framework.activateRecordMode()
    module_to_run = argv.pop(1)

    print "module: " + module_to_run
    print "argv:  ",
    print argv

    unittest.main(module=module_to_run, argv=argv)


if __name__ == "__main__":
    main(sys.argv)
