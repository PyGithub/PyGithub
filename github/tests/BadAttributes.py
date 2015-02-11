# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
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
# ##############################################################################

import datetime

import Framework
import github


# Replay data is forged to simulate bad things returned by Github
class BadAttributes(Framework.TestCase):
    def testBadSimpleAttribute(self):
        user = self.g.get_user("klmitch")
        self.assertEqual(user.created_at, datetime.datetime(2011, 3, 23, 15, 42, 9))

        raised = False
        try:
            user.name
        except github.BadAttributeException, e:
            raised = True
            self.assertEqual(e.actual_value, 42)
            self.assertEqual(e.expected_type, (str, unicode))
            self.assertEqual(e.transformation_exception, None)
        self.assertTrue(raised)

    def testBadAttributeTransformation(self):
        user = self.g.get_user("klmitch")
        self.assertEqual(user.name, "Kevin L. Mitchell")

        raised = False
        try:
            user.created_at
        except github.BadAttributeException, e:
            raised = True
            self.assertEqual(e.actual_value, "foobar")
            self.assertEqual(e.expected_type, (str, unicode))
            self.assertEqual(e.transformation_exception.__class__, ValueError)
            if Framework.atLeastPython26:
                self.assertEqual(e.transformation_exception.args, ("time data 'foobar' does not match format '%Y-%m-%dT%H:%M:%SZ'",))
            else:
                self.assertEqual(e.transformation_exception.args, ('time data did not match format:  data=foobar  fmt=%Y-%m-%dT%H:%M:%SZ',))
        self.assertTrue(raised)

    def testBadTransformedAttribute(self):
        user = self.g.get_user("klmitch")
        self.assertEqual(user.name, "Kevin L. Mitchell")

        raised = False
        try:
            user.updated_at
        except github.BadAttributeException, e:
            raised = True
            self.assertEqual(e.actual_value, 42)
            self.assertEqual(e.expected_type, (str, unicode))
            self.assertEqual(e.transformation_exception, None)
        self.assertTrue(raised)

    def testBadSimpleAttributeInList(self):
        hook = self.g.get_hook("activecollab")
        self.assertEqual(hook.name, "activecollab")

        raised = False
        try:
            hook.events
        except github.BadAttributeException, e:
            raised = True
            self.assertEqual(e.actual_value, ["push", 42])
            self.assertEqual(e.expected_type, [(str, unicode)])
            self.assertEqual(e.transformation_exception, None)
        self.assertTrue(raised)

    def testBadAttributeInClassAttribute(self):
        repo = self.g.get_repo("klmitch/turnstile")
        owner = repo.owner
        self.assertEqual(owner.id, 686398)

        raised = False
        try:
            owner.avatar_url
        except github.BadAttributeException, e:
            raised = True
            self.assertEqual(e.actual_value, 42)
        self.assertTrue(raised)

    def testBadTransformedAttributeInList(self):
        commit = self.g.get_repo("klmitch/turnstile").get_commit("38d9082a898d0822b5ccdfd78f3a536e2efa6c26")

        raised = False
        try:
            commit.files
        except github.BadAttributeException, e:
            raised = True
            self.assertEqual(e.actual_value, [42])
            self.assertEqual(e.expected_type, [dict])
            self.assertEqual(e.transformation_exception, None)
        self.assertTrue(raised)

    def testBadTransformedAttributeInDict(self):
        gist = self.g.get_gist("6437766")

        raised = False
        try:
            gist.files
        except github.BadAttributeException, e:
            raised = True
            self.assertEqual(e.actual_value, {"test.py": 42})
            self.assertEqual(e.expected_type, {(str, unicode): dict})
            self.assertEqual(e.transformation_exception, None)
        self.assertTrue(raised)

    def testIssue195(self):
        hooks = self.g.get_hooks()
        # We can loop on all hooks as long as we don't access circleci's events attribute
        self.assertListKeyEqual(hooks, lambda h: h.name, [u'activecollab', u'acunote', u'agilebench', u'agilezen', u'amazonsns', u'apiary', u'apoio', u'appharbor', u'apropos', u'asana', u'backlog', u'bamboo', u'basecamp', u'bcx', u'blimp', u'boxcar', u'buddycloud', u'bugherd', u'bugly', u'bugzilla', u'campfire', u'cia', u'circleci', u'codeclimate', u'codeportingcsharp2java', u'codeship', u'coffeedocinfo', u'conductor', u'coop', u'copperegg', u'cube', u'depending', u'deployhq', u'devaria', u'docker', u'ducksboard', u'email', u'firebase', u'fisheye', u'flowdock', u'fogbugz', u'freckle', u'friendfeed', u'gemini', u'gemnasium', u'geocommit', u'getlocalization', u'gitlive', u'grmble', u'grouptalent', u'grove', u'habitualist', u'hakiri', u'hall', u'harvest', u'hipchat', u'hostedgraphite', u'hubcap', u'hubci', u'humbug', u'icescrum', u'irc', u'irker', u'ironmq', u'ironworker', u'jabber', u'jaconda', u'jeapie', u'jenkins', u'jenkinsgit', u'jira', u'jqueryplugins', u'kanbanery', u'kickoff', u'leanto', u'lechat', u'lighthouse', u'lingohub', u'loggly', u'mantisbt', u'masterbranch', u'mqttpub', u'nma', u'nodejitsu', u'notifo', u'ontime', u'pachube', u'packagist', u'phraseapp', u'pivotaltracker', u'planbox', u'planio', u'prowl', u'puppetlinter', u'pushalot', u'pushover', u'pythonpackages', u'railsbp', u'railsbrakeman', u'rally', u'rapidpush', u'rationaljazzhub', u'rationalteamconcert', u'rdocinfo', u'readthedocs', u'redmine', u'rubyforge', u'scrumdo', u'shiningpanda', u'sifter', u'simperium', u'slatebox', u'snowyevening', u'socialcast', u'softlayermessaging', u'sourcemint', u'splendidbacon', u'sprintly', u'sqsqueue', u'stackmob', u'statusnet', u'talker', u'targetprocess', u'tddium', u'teamcity', u'tender', u'tenxer', u'testpilot', u'toggl', u'trac', u'trajectory', u'travis', u'trello', u'twilio', u'twitter', u'unfuddle', u'web', u'weblate', u'webtranslateit', u'yammer', u'youtrack', u'zendesk', u'zohoprojects'])
        for hook in hooks:
            if hook.name != "circleci":
                hook.events

        raised = False
        for hook in hooks:
            if hook.name == "circleci":
                try:
                    hook.events
                except github.BadAttributeException, e:
                    raised = True
                    self.assertEqual(e.actual_value, [["commit_comment", "create", "delete", "download", "follow", "fork", "fork_apply", "gist", "gollum", "issue_comment", "issues", "member", "public", "pull_request", "pull_request_review_comment", "push", "status", "team_add", "watch"]])
                    self.assertEqual(e.expected_type, [(str, unicode)])
                    self.assertEqual(e.transformation_exception, None)
        self.assertTrue(raised)
