############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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


from __future__ import annotations

from datetime import datetime, timezone
from operator import attrgetter

from . import Framework


class Topic(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.topics = list(self.g.search_topics("python"))

    def testAttributes(self):
        topic = self.topics[0]
        self.assertIsNone(topic.aliases)
        self.assertIsNone(topic.logo_url)

        self.assertEqual(topic.name, "python")
        self.assertEqual(topic.display_name, "Python")
        self.assertIsNone(topic.related)
        self.assertIsNone(topic.repository_count)
        self.assertEqual(
            topic.short_description,
            "Python is a dynamically typed programming language.",
        )
        self.assertEqual(
            topic.description,
            "Python is a dynamically-typed garbage-collected programming language "
            "developed by Guido van Rossum in the late 80s to replace ABC. Much like the "
            "programming language Ruby, Python was designed to be easily read by "
            "programmers. Because of its large following and many libraries, Python can "
            "be implemented and used to do anything from webpages to scientific research.",
        )
        self.assertEqual(topic.created_by, "Guido van Rossum")
        self.assertEqual(topic.released, "February 20, 1991")
        self.assertEqual(topic.created_at, datetime(2016, 12, 7, 0, 7, 2, tzinfo=timezone.utc))
        self.assertIsNone(topic.text_matches)
        self.assertEqual(topic.updated_at, datetime(2025, 1, 7, 9, 22, 52, tzinfo=timezone.utc))
        self.assertEqual(topic.featured, True)
        self.assertEqual(topic.curated, True)
        self.assertEqual(topic.score, 1.0)

        self.assertEqual(topic.__repr__(), 'Topic(name="python")')

    def testNamesFromSearchResults(self):
        expected_names = [
            "python",
            "django",
            "hacktoberfest",
            "flask",
            "python-script",
            "opencv-python",
            "numpy",
            "backend",
            "fastapi",
            "ruby",
            "python-library",
            "keras",
            "selenium-python",
            "tkinter-python",
            "scikit-learn",
            "pandas-python",
            "streamlit",
            "leetcode-python",
            "python36",
            "machinelearning-python",
            "nltk-python",
            "data-analysis-python",
            "micropython",
            "python37",
            "langchain-python",
            "learning-python",
            "oops-in-python",
            "python-telegram-bot",
            "python-package",
            "python-project",
        ]
        self.assertListKeyEqual(self.topics, attrgetter("name"), expected_names)
