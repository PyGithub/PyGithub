############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Stuart Glaser <stuglaser@gmail.com>                           #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 @tmshn <tmshn@r.recruit.co.jp>                                #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Matt Babineau <babineaum@users.noreply.github.com>            #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Nicolas Agustín Torres <nicolastrres@gmail.com>               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Filipe Laíns <filipe.lains@gmail.com>                         #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Huan-Cheng Chang <changhc84@gmail.com>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Nicolas Schweitzer <nicolas.schweitzer@datadoghq.com>         #
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

from . import Framework


class Issue(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.issue = self.repo.get_issue(28)

    def testAttributes(self):
        self.assertEqual(self.issue.assignee.login, "jacquev6")
        self.assertListKeyEqual(self.issue.assignees, lambda a: a.login, ["jacquev6", "stuglaser"])
        self.assertEqual(self.issue.body, "Body edited by PyGithub")
        self.assertEqual(
            self.issue.closed_at,
            datetime(2012, 5, 26, 14, 59, 33, tzinfo=timezone.utc),
        )
        self.assertEqual(self.issue.closed_by.login, "jacquev6")
        self.assertEqual(self.issue.comments, 0)
        self.assertEqual(
            self.issue.comments_url,
            "https://github.com/jacquev6/PyGithub/issues/28/comments",
        )
        self.assertEqual(
            self.issue.created_at,
            datetime(2012, 5, 19, 10, 38, 23, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.issue.events_url,
            "https://github.com/jacquev6/PyGithub/issues/28/events",
        )
        self.assertEqual(self.issue.html_url, "https://github.com/jacquev6/PyGithub/issues/28")
        self.assertEqual(self.issue.id, 4653757)
        self.assertListKeyEqual(
            self.issue.labels,
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )
        self.assertEqual(
            self.issue.labels_url,
            "https://github.com/jacquev6/PyGithub/issues/28/labels{/name}",
        )
        self.assertEqual(self.issue.milestone.title, "Version 0.4")
        self.assertEqual(self.issue.number, 28)
        self.assertEqual(self.issue.pull_request.diff_url, None)
        self.assertEqual(self.issue.pull_request.patch_url, None)
        self.assertEqual(self.issue.pull_request.html_url, None)
        self.assertEqual(self.issue.state, "closed")
        self.assertEqual(self.issue.state_reason, "completed")
        self.assertEqual(self.issue.title, "Issue created by PyGithub")
        self.assertEqual(
            self.issue.updated_at,
            datetime(2012, 5, 26, 14, 59, 33, tzinfo=timezone.utc),
        )
        self.assertEqual(self.issue.url, "https://api.github.com/repos/jacquev6/PyGithub/issues/28")
        self.assertFalse(self.issue.locked)
        self.assertIsNone(self.issue.active_lock_reason)
        self.assertEqual(self.issue.user.login, "jacquev6")
        self.assertEqual(self.issue.repository.name, "PyGithub")
        self.assertEqual(repr(self.issue), 'Issue(title="Issue created by PyGithub", number=28)')

    def testEditWithoutParameters(self):
        self.issue.edit()

    def testEditWithAllParameters(self):
        user = self.g.get_user("jacquev6")
        milestone = self.repo.get_milestone(2)
        self.issue.edit(
            "Title edited by PyGithub",
            "Body edited by PyGithub",
            user,
            "open",
            milestone,
            ["Bug"],
            ["jacquev6", "stuglaser"],
        )
        self.assertEqual(self.issue.assignee.login, "jacquev6")
        self.assertListKeyEqual(self.issue.assignees, lambda a: a.login, ["jacquev6", "stuglaser"])
        self.assertEqual(self.issue.body, "Body edited by PyGithub")
        self.assertEqual(self.issue.state, "open")
        self.assertEqual(self.issue.title, "Title edited by PyGithub")
        self.assertListKeyEqual(self.issue.labels, lambda lb: lb.name, ["Bug"])

    def testEditResetMilestone(self):
        self.assertEqual(self.issue.milestone.title, "Version 0.4")
        self.issue.edit(milestone=None)
        self.assertEqual(self.issue.milestone, None)

    def testEditResetAssignee(self):
        self.assertEqual(self.issue.assignee.login, "jacquev6")
        self.issue.edit(assignee=None)
        self.assertEqual(self.issue.assignee, None)

    def testEditWithStateReasonNotPlanned(self):
        self.issue.edit(state="closed", state_reason="not_planned")
        self.assertEqual(self.issue.state, "closed")
        self.assertEqual(self.issue.state_reason, "not_planned")

    def testEditWithStateReasonReopened(self):
        self.issue.edit(state="open", state_reason="reopened")
        self.assertEqual(self.issue.state, "open")
        self.assertEqual(self.issue.state_reason, "reopened")

    def testLock(self):
        self.issue.lock("resolved")

    def testUnlock(self):
        self.issue.unlock()

    def testCreateComment(self):
        comment = self.issue.create_comment("Comment created by PyGithub")
        self.assertEqual(comment.id, 5808311)

    def testGetComments(self):
        self.assertListKeyEqual(self.issue.get_comments(), lambda c: c.user.login, ["jacquev6", "roskakori"])

    def testGetCommentsSince(self):
        self.assertListKeyEqual(
            self.issue.get_comments(datetime(2012, 5, 26, 13, 59, 33, tzinfo=timezone.utc)),
            lambda c: c.user.login,
            ["jacquev6", "roskakori"],
        )

    def testGetEvents(self):
        self.assertListKeyEqual(self.issue.get_events(), lambda e: e.id, [15819975, 15820048])

    def testGetLabels(self):
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )

    def testAddAndRemoveAssignees(self):
        user1 = "jayfk"
        user2 = self.g.get_user("jzelinskie")
        self.assertListKeyEqual(self.issue.assignees, lambda a: a.login, ["jacquev6", "stuglaser"])
        self.issue.add_to_assignees(user1, user2)
        self.assertListKeyEqual(
            self.issue.assignees,
            lambda a: a.login,
            ["jacquev6", "stuglaser", "jayfk", "jzelinskie"],
        )
        self.issue.remove_from_assignees(user1, user2)
        self.assertListKeyEqual(self.issue.assignees, lambda a: a.login, ["jacquev6", "stuglaser"])

    def testAddAndRemoveLabels(self):
        bug = self.repo.get_label("Bug")
        question = self.repo.get_label("Question")
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )
        self.issue.remove_from_labels(bug)
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Project management", "Question"],
        )
        self.issue.remove_from_labels(question)
        self.assertListKeyEqual(self.issue.get_labels(), lambda lb: lb.name, ["Project management"])
        self.issue.add_to_labels(bug, question)
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )

    def testAddAndRemoveLabelsWithStringArguments(self):
        bug = "Bug"
        question = "Question"
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )
        self.issue.remove_from_labels(bug)
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Project management", "Question"],
        )
        self.issue.remove_from_labels(question)
        self.assertListKeyEqual(self.issue.get_labels(), lambda lb: lb.name, ["Project management"])
        self.issue.add_to_labels(bug, question)
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )

    def testDeleteAndSetLabels(self):
        bug = self.repo.get_label("Bug")
        question = self.repo.get_label("Question")
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )
        self.issue.delete_labels()
        self.assertListKeyEqual(self.issue.get_labels(), None, [])
        self.issue.set_labels(bug, question)
        self.assertListKeyEqual(self.issue.get_labels(), lambda lb: lb.name, ["Bug", "Question"])

    def testDeleteAndSetLabelsWithStringArguments(self):
        bug = "Bug"
        question = "Question"
        self.assertListKeyEqual(
            self.issue.get_labels(),
            lambda lb: lb.name,
            ["Bug", "Project management", "Question"],
        )
        self.issue.delete_labels()
        self.assertListKeyEqual(self.issue.get_labels(), None, [])
        self.issue.set_labels(bug, question)
        self.assertListKeyEqual(self.issue.get_labels(), lambda lb: lb.name, ["Bug", "Question"])

    def testGetReactions(self):
        reactions = self.issue.get_reactions()
        self.assertEqual(reactions[0].content, "+1")

    def testCreateReaction(self):
        reaction = self.issue.create_reaction("hooray")

        self.assertEqual(reaction.id, 16917472)
        self.assertEqual(reaction.content, "hooray")

    def testDeleteReaction(self):
        self.assertTrue(self.issue.delete_reaction(85740167))

    def testGetTimeline(self):
        expected_events = {
            "referenced",
            "cross-referenced",
            "locked",
            "unlocked",
            "closed",
            "assigned",
            "commented",
            "subscribed",
            "labeled",
        }
        events = self.issue.get_timeline()

        first = events[0]
        self.assertEqual(15819975, first.id)
        self.assertEqual("MDE1OlN1YnNjcmliZWRFdmVudDE1ODE5OTc1", first.node_id)
        self.assertEqual(
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/15819975",
            first.url,
        )
        self.assertEqual("jacquev6", first.actor.login)
        self.assertEqual(327146, first.actor.id)
        self.assertEqual("subscribed", first.event)
        self.assertIsNone(first.commit_id)
        self.assertIsNone(first.commit_url)
        self.assertEqual(repr(first), "TimelineEvent(id=15819975)")

        for event in events:
            self.assertIn(event.event, expected_events)
            self.assertIsNotNone(event.created_at)
            self.assertIsNotNone(event.actor)

            if event.event == "cross-referenced":
                # cross-referenced events don't include an event id or node_id
                self.assertIsNotNone(event.source)
                self.assertEqual(event.source.type, "issue")
                self.assertEqual(event.source.issue.number, 857)
                self.assertEqual(repr(event.source), 'TimelineEventSource(type="issue")')
            else:
                self.assertIsNotNone(event.id)
                self.assertIsNotNone(event.node_id)

                if event.event == "commented":
                    self.assertIsNotNone(event.body)
                else:
                    self.assertIsNone(event.source)
                    self.assertIsNotNone(event.actor)
