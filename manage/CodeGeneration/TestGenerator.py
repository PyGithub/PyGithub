# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
assert sys.hexversion >= 0x03040000


class TestGenerator:
    def generateAll(self, classes):
        for klass in classes:
            yield "from PyGithub.Blocking.tests.classes.{}TestCases import *".format(klass.name)

    def generateClass(self, klass):  # pragma no cover
        yield "from PyGithub.Blocking.tests.Framework import *"
        yield ""
        yield ""
        yield "class {}Attributes(TestCase):".format(klass.name)
        yield "    pass"
        yield ""
        yield ""
        yield "class {}EditUpdateDelete(TestCase):".format(klass.name)
        yield "    pass"
