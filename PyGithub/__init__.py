# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

"""
"""

Version = "2.0.0-alpha.4"
"A string representation of the version of PyGithub as described by `semantic versionning <http://semver.org>`_."

import PyGithub.Blocking._builder
BlockingBuilder = PyGithub.Blocking._builder.Builder
"An alias of :class:`.Builder` to make it easy to instanciate."
