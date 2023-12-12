############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from . import Framework


class Markdown(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.text = "MyTitle\n=======\n\nIssue #1"
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testRenderMarkdown(self):
        self.assertEqual(
            self.g.render_markdown(self.text),
            '<h1><a name="mytitle" class="anchor" href="#mytitle"><span class="mini-icon mini-icon-link"></span></a>MyTitle</h1><p>Issue #1</p>',
        )

    def testRenderGithubFlavoredMarkdown(self):
        self.assertEqual(
            self.g.render_markdown(self.text, self.repo),
            '<h1>MyTitle</h1><p>Issue <a href="https://github.com/jacquev6/PyGithub/issues/1" class="issue-link" title="Gitub -&gt; Github everywhere">#1</a></p>',
        )
