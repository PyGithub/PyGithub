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


from datetime import datetime, timezone
from operator import attrgetter

from . import Framework


class Topic(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.topics = list(self.g.search_topics("python"))

    def testAllFields(self):
        topic = self.topics[0]

        self.assertEqual(topic.name, "python")
        self.assertEqual(topic.display_name, "Python")
        self.assertEqual(
            topic.short_description,
            "Python is a dynamically typed programming language.",
        )
        self.assertEqual(
            topic.description,
            "Python is a dynamically typed programming language designed by Guido van Rossum. Much like the programming language Ruby, Python was designed to be easily read by programmers. Because of its large following and many libraries, Python can be implemented and used to do anything from webpages to scientific research.",
        )
        self.assertEqual(topic.created_by, "Guido van Rossum")
        self.assertEqual(topic.released, "February 20, 1991")
        self.assertEqual(
            topic.created_at, datetime(2016, 12, 7, 0, 7, 2, tzinfo=timezone.utc)
        )
        self.assertEqual(
            topic.updated_at, datetime(2019, 10, 9, 20, 33, 49, tzinfo=timezone.utc)
        )
        self.assertEqual(topic.featured, True)
        self.assertEqual(topic.curated, True)
        self.assertEqual(topic.score, 7576.306)

        self.assertEqual(topic.__repr__(), 'Topic(name="python")')

    def testNamesFromSearchResults(self):
        expected_names = [
            "python",
            "django",
            "flask",
            "python-script",
            "python36",
            "opencv-python",
            "ruby",
            "python-library",
            "scikit-learn",
            "python37",
            "selenium-python",
            "sublime-text",
            "leetcode-python",
            "learning-python",
            "tkinter-python",
            "python35",
            "machinelearning-python",
            "python-flask",
            "python-package",
            "python-telegram-bot",
            "python-wrapper",
            "python3-6",
            "opencv3-python",
            "hackerrank-python",
            "python-api",
            "python2-7",
            "pythonista",
            "haxe",
            "python-requests",
            "python-2-7",
        ]

        self.assertListKeyEqual(self.topics, attrgetter("name"), expected_names)
