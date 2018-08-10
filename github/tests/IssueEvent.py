# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import Framework

import datetime


class IssueEvent(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)

        # From Issue #30
        self.event_subscribed               = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16347479)
        self.event_assigned                 = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16347480)
        self.event_referenced               = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
        self.event_closed                   = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16351220)
        self.event_labeled                  = self.g.get_repo("PyGithub/PyGithub").get_issues_event(98136337)

        # From Issue 538
        self.event_mentioned                = self.g.get_repo("PyGithub/PyGithub").get_issues_event(1009034767)
        self.event_merged                   = self.g.get_repo("PyGithub/PyGithub").get_issues_event(1015402964)
        self.event_review_requested         = self.g.get_repo("PyGithub/PyGithub").get_issues_event(1011101309)

        # From Issue 857
        self.event_reopened                 = self.g.get_repo("PyGithub/PyGithub").get_issues_event(1782463023)
        self.event_unassigned               = self.g.get_repo("PyGithub/PyGithub").get_issues_event(1782463379)
        self.event_unlabeled                = self.g.get_repo("PyGithub/PyGithub").get_issues_event(1782463917)
        self.event_renamed                  = self.g.get_repo("PyGithub/PyGithub").get_issues_event(1782472556)

        # TODO:PENDING Events - To Be Tested
#        self.event_milestoned               = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_demilestoned             = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_locked                   = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_unlocked                 = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_head_ref_deleted         = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_head_ref_restored        = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_base_ref_changed         = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_review_dismissed         = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_review_request_removed   = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_marked_as_duplicate      = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_unmarked_as_duplicate    = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_added_to_project         = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_moved_columns_in_project = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_removed_from_project     = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)
#        self.event_converted_note_to_issue  = self.g.get_repo("PyGithub/PyGithub").get_issues_event(16348656)

    def testEvent_subscribed_Attributes(self):
        self.assertEqual(self.event_subscribed.actor.login, "jacquev6")
        self.assertEqual(self.event_subscribed.commit_id, None)
        self.assertEqual(self.event_subscribed.created_at, datetime.datetime(2012, 5, 27, 5, 40, 15))
        self.assertEqual(self.event_subscribed.event, "subscribed")
        self.assertEqual(self.event_subscribed.id, 16347479)
        self.assertEqual(self.event_subscribed.issue.number, 30)
        self.assertEqual(self.event_subscribed.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16347479")
        self.assertEqual(self.event_subscribed.node_id, "MDE1OlN1YnNjcmliZWRFdmVudDE2MzQ3NDc5")
        self.assertEqual(self.event_subscribed.commit_url, None)
        self.assertEqual(self.event_subscribed.label, None)
        self.assertEqual(self.event_subscribed.assignee, None)
        self.assertEqual(self.event_subscribed.assigner, None)
        self.assertEqual(self.event_subscribed.review_requester, None)
        self.assertEqual(self.event_subscribed.requested_reviewer, None)
        self.assertEqual(self.event_subscribed.milestone, None)
        self.assertEqual(self.event_subscribed.rename, None)
        self.assertEqual(self.event_subscribed.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_subscribed.__repr__(), 'IssueEvent(id=16347479)')

    def testEvent_assigned_Attributes(self):
        self.assertEqual(self.event_assigned.actor.login, "jacquev6")
        self.assertEqual(self.event_assigned.commit_id, None)
        self.assertEqual(self.event_assigned.created_at, datetime.datetime(2012, 5, 27, 5, 40, 15))
        self.assertEqual(self.event_assigned.event, "assigned")
        self.assertEqual(self.event_assigned.id, 16347480)
        self.assertEqual(self.event_assigned.issue.number, 30)
        self.assertEqual(self.event_assigned.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16347480")
        self.assertEqual(self.event_assigned.node_id, "MDEzOkFzc2lnbmVkRXZlbnQxNjM0NzQ4MA==")
        self.assertEqual(self.event_assigned.commit_url, None)
        self.assertEqual(self.event_assigned.label, None)
        self.assertEqual(self.event_assigned.assignee.login, "jacquev6")
        self.assertEqual(self.event_assigned.assigner.login, "ghost")
        self.assertEqual(self.event_assigned.review_requester, None)
        self.assertEqual(self.event_assigned.requested_reviewer, None)
        self.assertEqual(self.event_assigned.milestone, None)
        self.assertEqual(self.event_assigned.rename, None)
        self.assertEqual(self.event_assigned.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_assigned.__repr__(), 'IssueEvent(id=16347480)')

    def testEvent_referenced_Attributes(self):
        self.assertEqual(self.event_referenced.actor.login, "jacquev6")
        self.assertEqual(self.event_referenced.commit_id, "ed866fc43833802ab553e5ff8581c81bb00dd433")
        self.assertEqual(self.event_referenced.created_at, datetime.datetime(2012, 5, 27, 7, 29, 25))
        self.assertEqual(self.event_referenced.event, "referenced")
        self.assertEqual(self.event_referenced.id, 16348656)
        self.assertEqual(self.event_referenced.issue.number, 30)
        self.assertEqual(self.event_referenced.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16348656")
        self.assertEqual(self.event_referenced.node_id, "MDE1OlJlZmVyZW5jZWRFdmVudDE2MzQ4NjU2")
        self.assertEqual(self.event_referenced.commit_url, "https://api.github.com/repos/PyGithub/PyGithub/commits/ed866fc43833802ab553e5ff8581c81bb00dd433")
        self.assertEqual(self.event_referenced.label, None)
        self.assertEqual(self.event_referenced.assignee, None)
        self.assertEqual(self.event_referenced.assigner, None)
        self.assertEqual(self.event_referenced.review_requester, None)
        self.assertEqual(self.event_referenced.requested_reviewer, None)
        self.assertEqual(self.event_referenced.milestone, None)
        self.assertEqual(self.event_referenced.rename, None)
        self.assertEqual(self.event_referenced.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_referenced.__repr__(), 'IssueEvent(id=16348656)')

    def testEvent_closed_Attributes(self):
        self.assertEqual(self.event_closed.actor.login, "jacquev6")
        self.assertEqual(self.event_closed.commit_id, None)
        self.assertEqual(self.event_closed.created_at, datetime.datetime(2012, 5, 27, 11, 4, 25))
        self.assertEqual(self.event_closed.event, "closed")
        self.assertEqual(self.event_closed.id, 16351220)
        self.assertEqual(self.event_closed.issue.number, 30)
        self.assertEqual(self.event_closed.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16351220")
        self.assertEqual(self.event_closed.node_id, "MDExOkNsb3NlZEV2ZW50MTYzNTEyMjA=")
        self.assertEqual(self.event_closed.commit_url, None)
        self.assertEqual(self.event_closed.label, None)
        self.assertEqual(self.event_closed.assignee, None)
        self.assertEqual(self.event_closed.assigner, None)
        self.assertEqual(self.event_closed.review_requester, None)
        self.assertEqual(self.event_closed.requested_reviewer, None)
        self.assertEqual(self.event_closed.milestone, None)
        self.assertEqual(self.event_closed.rename, None)
        self.assertEqual(self.event_closed.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_closed.__repr__(), 'IssueEvent(id=16351220)')

    def testEvent_labeled_Attributes(self):
        self.assertEqual(self.event_labeled.actor.login, "jacquev6")
        self.assertEqual(self.event_labeled.commit_id, None)
        self.assertEqual(self.event_labeled.created_at, datetime.datetime(2014, 3, 2, 18, 55, 10))
        self.assertEqual(self.event_labeled.event, "labeled")
        self.assertEqual(self.event_labeled.id, 98136337)
        self.assertEqual(self.event_labeled.issue.number, 30)
        self.assertEqual(self.event_labeled.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/98136337")
        self.assertEqual(self.event_labeled.node_id, "MDEyOkxhYmVsZWRFdmVudDk4MTM2MzM3")
        self.assertEqual(self.event_labeled.commit_url, None)
        self.assertEqual(self.event_labeled.label.name, "v1")
        self.assertEqual(self.event_labeled.assignee, None)
        self.assertEqual(self.event_labeled.assigner, None)
        self.assertEqual(self.event_labeled.review_requester, None)
        self.assertEqual(self.event_labeled.requested_reviewer, None)
        self.assertEqual(self.event_labeled.milestone, None)
        self.assertEqual(self.event_labeled.rename, None)
        self.assertEqual(self.event_labeled.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_labeled.__repr__(), 'IssueEvent(id=98136337)')

    def testEvent_mentioned_Attributes(self):
        self.assertEqual(self.event_mentioned.actor.login, "jzelinskie")
        self.assertEqual(self.event_mentioned.commit_id, None)
        self.assertEqual(self.event_mentioned.created_at, datetime.datetime(2017, 3, 21, 17, 30, 14))
        self.assertEqual(self.event_mentioned.event, "mentioned")
        self.assertEqual(self.event_mentioned.id, 1009034767)
        self.assertEqual(self.event_mentioned.issue.number, 538)
        self.assertEqual(self.event_mentioned.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1009034767")
        self.assertEqual(self.event_mentioned.node_id, "MDE0Ok1lbnRpb25lZEV2ZW50MTAwOTAzNDc2Nw==")
        self.assertEqual(self.event_mentioned.commit_url, None)
        self.assertEqual(self.event_mentioned.label, None)
        self.assertEqual(self.event_mentioned.assignee, None)
        self.assertEqual(self.event_mentioned.assigner, None)
        self.assertEqual(self.event_mentioned.review_requester, None)
        self.assertEqual(self.event_mentioned.requested_reviewer, None)
        self.assertEqual(self.event_mentioned.milestone, None)
        self.assertEqual(self.event_mentioned.rename, None)
        self.assertEqual(self.event_mentioned.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_mentioned.__repr__(), 'IssueEvent(id=1009034767)')

    def testEvent_merged_Attributes(self):
        self.assertEqual(self.event_merged.actor.login, "jzelinskie")
        self.assertEqual(self.event_merged.commit_id, "2525515b094d7425f7018eb5b66171e21c5fbc10")
        self.assertEqual(self.event_merged.created_at, datetime.datetime(2017, 3, 25, 16, 52, 49))
        self.assertEqual(self.event_merged.event, "merged")
        self.assertEqual(self.event_merged.id, 1015402964)
        self.assertEqual(self.event_merged.issue.number, 538)
        self.assertEqual(self.event_merged.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1015402964")
        self.assertEqual(self.event_merged.node_id, "MDExOk1lcmdlZEV2ZW50MTAxNTQwMjk2NA==")
        self.assertEqual(self.event_merged.commit_url, "https://api.github.com/repos/PyGithub/PyGithub/commits/2525515b094d7425f7018eb5b66171e21c5fbc10")
        self.assertEqual(self.event_merged.label, None)
        self.assertEqual(self.event_merged.assignee, None)
        self.assertEqual(self.event_merged.assigner, None)
        self.assertEqual(self.event_merged.review_requester, None)
        self.assertEqual(self.event_merged.requested_reviewer, None)
        self.assertEqual(self.event_merged.milestone, None)
        self.assertEqual(self.event_merged.rename, None)
        self.assertEqual(self.event_merged.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_merged.__repr__(), 'IssueEvent(id=1015402964)')

    def testEvent_review_requested_Attributes(self):
        self.assertEqual(self.event_review_requested.actor.login, "jzelinskie")
        self.assertEqual(self.event_review_requested.commit_id, None)
        self.assertEqual(self.event_review_requested.created_at, datetime.datetime(2017, 3, 22, 19, 6, 44))
        self.assertEqual(self.event_review_requested.event, "review_requested")
        self.assertEqual(self.event_review_requested.id, 1011101309)
        self.assertEqual(self.event_review_requested.issue.number, 538)
        self.assertEqual(self.event_review_requested.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1011101309")
        self.assertEqual(self.event_review_requested.node_id, "MDIwOlJldmlld1JlcXVlc3RlZEV2ZW50MTAxMTEwMTMwOQ==")
        self.assertEqual(self.event_review_requested.commit_url, None)
        self.assertEqual(self.event_review_requested.label, None)
        self.assertEqual(self.event_review_requested.assignee, None)
        self.assertEqual(self.event_review_requested.assigner, None)
        self.assertEqual(self.event_review_requested.review_requester.login, "jzelinskie")
        self.assertEqual(self.event_review_requested.requested_reviewer.login, "jzelinskie")
        self.assertEqual(self.event_review_requested.milestone, None)
        self.assertEqual(self.event_review_requested.rename, None)
        self.assertEqual(self.event_review_requested.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_review_requested.__repr__(), 'IssueEvent(id=1011101309)')

    def testEvent_reopened_Attributes(self):
        self.assertEqual(self.event_reopened.actor.login, "sfdye")
        self.assertEqual(self.event_reopened.commit_id, None)
        self.assertEqual(self.event_reopened.created_at, datetime.datetime(2018, 8, 10, 13, 10, 9))
        self.assertEqual(self.event_reopened.event, "reopened")
        self.assertEqual(self.event_reopened.id, 1782463023)
        self.assertEqual(self.event_reopened.issue.number, 857)
        self.assertEqual(self.event_reopened.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782463023")
        self.assertEqual(self.event_reopened.node_id, "MDEzOlJlb3BlbmVkRXZlbnQxNzgyNDYzMDIz")
        self.assertEqual(self.event_reopened.commit_url, None)
        self.assertEqual(self.event_reopened.label, None)
        self.assertEqual(self.event_reopened.assignee, None)
        self.assertEqual(self.event_reopened.assigner, None)
        self.assertEqual(self.event_reopened.review_requester, None)
        self.assertEqual(self.event_reopened.requested_reviewer, None)
        self.assertEqual(self.event_reopened.milestone, None)
        self.assertEqual(self.event_reopened.rename, None)
        self.assertEqual(self.event_reopened.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_reopened.__repr__(), 'IssueEvent(id=1782463023)')

    def testEvent_unassigned_Attributes(self):
        self.assertEqual(self.event_unassigned.actor.login, "sfdye")
        self.assertEqual(self.event_unassigned.commit_id, None)
        self.assertEqual(self.event_unassigned.created_at, datetime.datetime(2018, 8, 10, 13, 10, 21))
        self.assertEqual(self.event_unassigned.event, "unassigned")
        self.assertEqual(self.event_unassigned.id, 1782463379)
        self.assertEqual(self.event_unassigned.issue.number, 857)
        self.assertEqual(self.event_unassigned.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782463379")
        self.assertEqual(self.event_unassigned.node_id, "MDE1OlVuYXNzaWduZWRFdmVudDE3ODI0NjMzNzk=")
        self.assertEqual(self.event_unassigned.commit_url, None)
        self.assertEqual(self.event_unassigned.label, None)
        self.assertEqual(self.event_unassigned.actor.login, "sfdye")
        self.assertEqual(self.event_unassigned.actor.login, "sfdye")
        self.assertEqual(self.event_unassigned.review_requester, None)
        self.assertEqual(self.event_unassigned.requested_reviewer, None)
        self.assertEqual(self.event_unassigned.milestone, None)
        self.assertEqual(self.event_unassigned.rename, None)
        self.assertEqual(self.event_unassigned.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_unassigned.__repr__(), 'IssueEvent(id=1782463379)')

    def testEvent_unlabeled_Attributes(self):
        self.assertEqual(self.event_unlabeled.actor.login, "sfdye")
        self.assertEqual(self.event_unlabeled.commit_id, None)
        self.assertEqual(self.event_unlabeled.created_at, datetime.datetime(2018, 8, 10, 13, 10, 38))
        self.assertEqual(self.event_unlabeled.event, "unlabeled")
        self.assertEqual(self.event_unlabeled.id, 1782463917)
        self.assertEqual(self.event_unlabeled.issue.number, 857)
        self.assertEqual(self.event_unlabeled.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782463917")
        self.assertEqual(self.event_unlabeled.node_id, "MDE0OlVubGFiZWxlZEV2ZW50MTc4MjQ2MzkxNw==")
        self.assertEqual(self.event_unlabeled.commit_url, None)
        self.assertEqual(self.event_unlabeled.label.name, "improvement")
        self.assertEqual(self.event_unlabeled.assignee, None)
        self.assertEqual(self.event_unlabeled.assigner, None)
        self.assertEqual(self.event_unlabeled.review_requester, None)
        self.assertEqual(self.event_unlabeled.requested_reviewer, None)
        self.assertEqual(self.event_unlabeled.milestone, None)
        self.assertEqual(self.event_unlabeled.rename, None)
        self.assertEqual(self.event_unlabeled.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_unlabeled.__repr__(), 'IssueEvent(id=1782463917)')

    def testEvent_renamed_Attributes(self):
        self.assertEqual(self.event_renamed.actor.login, "sfdye")
        self.assertEqual(self.event_renamed.commit_id, None)
        self.assertEqual(self.event_renamed.created_at, datetime.datetime(2018, 8, 10, 13, 15, 18))
        self.assertEqual(self.event_renamed.event, "renamed")
        self.assertEqual(self.event_renamed.id, 1782472556)
        self.assertEqual(self.event_renamed.issue.number, 857)
        self.assertEqual(self.event_renamed.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782472556")
        self.assertEqual(self.event_renamed.node_id, "MDE3OlJlbmFtZWRUaXRsZUV2ZW50MTc4MjQ3MjU1Ng==")
        self.assertEqual(self.event_renamed.commit_url, None)
        self.assertEqual(self.event_renamed.label, None)
        self.assertEqual(self.event_renamed.assignee, None)
        self.assertEqual(self.event_renamed.assigner, None)
        self.assertEqual(self.event_renamed.review_requester, None)
        self.assertEqual(self.event_renamed.requested_reviewer, None)
        self.assertEqual(self.event_renamed.milestone, None)
        self.assertEqual(self.event_renamed.rename, {u'to': u'Adding new attributes to IssueEvent', u'from': u'Adding new attributes to IssueEvent Object (DO NOT MERGE - SEE NOTES)'})
        self.assertEqual(self.event_renamed.dismissed_review, None)
        # test __repr__() based on this attributes
        self.assertEqual(self.event_renamed.__repr__(), 'IssueEvent(id=1782472556)')

