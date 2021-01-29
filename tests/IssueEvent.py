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

import datetime

from . import Framework


class IssueEvent(Framework.TestCase):
    def setUp(self):
        super().setUp()
        repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)

        # From Issue #30
        self.event_subscribed = repo.get_issues_event(16347479)
        self.event_assigned = repo.get_issues_event(16347480)
        self.event_referenced = repo.get_issues_event(16348656)
        self.event_closed = repo.get_issues_event(16351220)
        self.event_labeled = repo.get_issues_event(98136337)

        # From Issue 538
        self.event_mentioned = repo.get_issues_event(1009034767)
        self.event_merged = repo.get_issues_event(1015402964)
        self.event_review_requested = repo.get_issues_event(1011101309)

        # From Issue 857
        self.event_reopened = repo.get_issues_event(1782463023)
        self.event_unassigned = repo.get_issues_event(1782463379)
        self.event_unlabeled = repo.get_issues_event(1782463917)
        self.event_renamed = repo.get_issues_event(1782472556)
        self.event_base_ref_changed = repo.get_issues_event(1782915693)
        self.event_head_ref_deleted = repo.get_issues_event(1782917185)
        self.event_head_ref_restored = repo.get_issues_event(1782917299)
        self.event_milestoned = repo.get_issues_event(1783596418)
        self.event_demilestoned = repo.get_issues_event(1783596452)
        self.event_locked = repo.get_issues_event(1783596743)
        self.event_unlocked = repo.get_issues_event(1783596818)
        self.event_review_dismissed = repo.get_issues_event(1783605084)
        self.event_review_request_removed = repo.get_issues_event(1783779835)
        self.event_marked_as_duplicate = repo.get_issues_event(1783779725)
        self.event_unmarked_as_duplicate = repo.get_issues_event(1789228962)
        self.event_added_to_project = repo.get_issues_event(1791766828)
        self.event_moved_columns_in_project = repo.get_issues_event(1791767766)
        self.event_removed_from_project = repo.get_issues_event(1791768212)

        # From Issue 866
        self.event_converted_note_to_issue = repo.get_issues_event(1791769149)

    def testEvent_subscribed_Attributes(self):
        self.assertEqual(self.event_subscribed.actor.login, "jacquev6")
        self.assertEqual(self.event_subscribed.commit_id, None)
        self.assertEqual(
            self.event_subscribed.created_at,
            datetime.datetime(2012, 5, 27, 5, 40, 15, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_subscribed.event, "subscribed")
        self.assertEqual(self.event_subscribed.id, 16347479)
        self.assertEqual(self.event_subscribed.issue.number, 30)
        self.assertEqual(
            self.event_subscribed.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16347479",
        )
        self.assertEqual(
            self.event_subscribed.node_id, "MDE1OlN1YnNjcmliZWRFdmVudDE2MzQ3NDc5"
        )
        self.assertEqual(self.event_subscribed.commit_url, None)
        self.assertEqual(self.event_subscribed.label, None)
        self.assertEqual(self.event_subscribed.assignee, None)
        self.assertEqual(self.event_subscribed.assigner, None)
        self.assertEqual(self.event_subscribed.review_requester, None)
        self.assertEqual(self.event_subscribed.requested_reviewer, None)
        self.assertEqual(self.event_subscribed.milestone, None)
        self.assertEqual(self.event_subscribed.rename, None)
        self.assertEqual(self.event_subscribed.dismissed_review, None)
        self.assertEqual(self.event_subscribed.lock_reason, None)
        self.assertEqual(repr(self.event_subscribed), "IssueEvent(id=16347479)")

    def testEvent_assigned_Attributes(self):
        self.assertEqual(self.event_assigned.actor.login, "jacquev6")
        self.assertEqual(self.event_assigned.commit_id, None)
        self.assertEqual(
            self.event_assigned.created_at,
            datetime.datetime(2012, 5, 27, 5, 40, 15, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_assigned.event, "assigned")
        self.assertEqual(self.event_assigned.id, 16347480)
        self.assertEqual(self.event_assigned.issue.number, 30)
        self.assertEqual(
            self.event_assigned.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16347480",
        )
        self.assertEqual(
            self.event_assigned.node_id, "MDEzOkFzc2lnbmVkRXZlbnQxNjM0NzQ4MA=="
        )
        self.assertEqual(self.event_assigned.commit_url, None)
        self.assertEqual(self.event_assigned.label, None)
        self.assertEqual(self.event_assigned.assignee.login, "jacquev6")
        self.assertEqual(self.event_assigned.assigner.login, "ghost")
        self.assertEqual(self.event_assigned.review_requester, None)
        self.assertEqual(self.event_assigned.requested_reviewer, None)
        self.assertEqual(self.event_assigned.milestone, None)
        self.assertEqual(self.event_assigned.rename, None)
        self.assertEqual(self.event_assigned.dismissed_review, None)
        self.assertEqual(self.event_assigned.lock_reason, None)
        self.assertEqual(repr(self.event_assigned), "IssueEvent(id=16347480)")

    def testEvent_referenced_Attributes(self):
        self.assertEqual(self.event_referenced.actor.login, "jacquev6")
        self.assertEqual(
            self.event_referenced.commit_id, "ed866fc43833802ab553e5ff8581c81bb00dd433"
        )
        self.assertEqual(
            self.event_referenced.created_at,
            datetime.datetime(2012, 5, 27, 7, 29, 25, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_referenced.event, "referenced")
        self.assertEqual(self.event_referenced.id, 16348656)
        self.assertEqual(self.event_referenced.issue.number, 30)
        self.assertEqual(
            self.event_referenced.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16348656",
        )
        self.assertEqual(
            self.event_referenced.node_id, "MDE1OlJlZmVyZW5jZWRFdmVudDE2MzQ4NjU2"
        )
        self.assertEqual(
            self.event_referenced.commit_url,
            "https://api.github.com/repos/PyGithub/PyGithub/commits/ed866fc43833802ab553e5ff8581c81bb00dd433",
        )
        self.assertEqual(self.event_referenced.label, None)
        self.assertEqual(self.event_referenced.assignee, None)
        self.assertEqual(self.event_referenced.assigner, None)
        self.assertEqual(self.event_referenced.review_requester, None)
        self.assertEqual(self.event_referenced.requested_reviewer, None)
        self.assertEqual(self.event_referenced.milestone, None)
        self.assertEqual(self.event_referenced.rename, None)
        self.assertEqual(self.event_referenced.dismissed_review, None)
        self.assertEqual(self.event_referenced.lock_reason, None)
        self.assertEqual(repr(self.event_referenced), "IssueEvent(id=16348656)")

    def testEvent_closed_Attributes(self):
        self.assertEqual(self.event_closed.actor.login, "jacquev6")
        self.assertEqual(self.event_closed.commit_id, None)
        self.assertEqual(
            self.event_closed.created_at,
            datetime.datetime(2012, 5, 27, 11, 4, 25, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_closed.event, "closed")
        self.assertEqual(self.event_closed.id, 16351220)
        self.assertEqual(self.event_closed.issue.number, 30)
        self.assertEqual(
            self.event_closed.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/16351220",
        )
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
        self.assertEqual(self.event_closed.lock_reason, None)
        self.assertEqual(repr(self.event_closed), "IssueEvent(id=16351220)")

    def testEvent_labeled_Attributes(self):
        self.assertEqual(self.event_labeled.actor.login, "jacquev6")
        self.assertEqual(self.event_labeled.commit_id, None)
        self.assertEqual(
            self.event_labeled.created_at,
            datetime.datetime(2014, 3, 2, 18, 55, 10, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_labeled.event, "labeled")
        self.assertEqual(self.event_labeled.id, 98136337)
        self.assertEqual(self.event_labeled.issue.number, 30)
        self.assertEqual(
            self.event_labeled.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/98136337",
        )
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
        self.assertEqual(self.event_labeled.lock_reason, None)
        self.assertEqual(repr(self.event_labeled), "IssueEvent(id=98136337)")

    def testEvent_mentioned_Attributes(self):
        self.assertEqual(self.event_mentioned.actor.login, "jzelinskie")
        self.assertEqual(self.event_mentioned.commit_id, None)
        self.assertEqual(
            self.event_mentioned.created_at,
            datetime.datetime(2017, 3, 21, 17, 30, 14, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_mentioned.event, "mentioned")
        self.assertEqual(self.event_mentioned.id, 1009034767)
        self.assertEqual(self.event_mentioned.issue.number, 538)
        self.assertEqual(
            self.event_mentioned.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1009034767",
        )
        self.assertEqual(
            self.event_mentioned.node_id, "MDE0Ok1lbnRpb25lZEV2ZW50MTAwOTAzNDc2Nw=="
        )
        self.assertEqual(self.event_mentioned.commit_url, None)
        self.assertEqual(self.event_mentioned.label, None)
        self.assertEqual(self.event_mentioned.assignee, None)
        self.assertEqual(self.event_mentioned.assigner, None)
        self.assertEqual(self.event_mentioned.review_requester, None)
        self.assertEqual(self.event_mentioned.requested_reviewer, None)
        self.assertEqual(self.event_mentioned.milestone, None)
        self.assertEqual(self.event_mentioned.rename, None)
        self.assertEqual(self.event_mentioned.dismissed_review, None)
        self.assertEqual(self.event_mentioned.lock_reason, None)
        self.assertEqual(repr(self.event_mentioned), "IssueEvent(id=1009034767)")

    def testEvent_merged_Attributes(self):
        self.assertEqual(self.event_merged.actor.login, "jzelinskie")
        self.assertEqual(
            self.event_merged.commit_id, "2525515b094d7425f7018eb5b66171e21c5fbc10"
        )
        self.assertEqual(
            self.event_merged.created_at,
            datetime.datetime(2017, 3, 25, 16, 52, 49, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_merged.event, "merged")
        self.assertEqual(self.event_merged.id, 1015402964)
        self.assertEqual(self.event_merged.issue.number, 538)
        self.assertEqual(
            self.event_merged.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1015402964",
        )
        self.assertEqual(
            self.event_merged.node_id, "MDExOk1lcmdlZEV2ZW50MTAxNTQwMjk2NA=="
        )
        self.assertEqual(
            self.event_merged.commit_url,
            "https://api.github.com/repos/PyGithub/PyGithub/commits/2525515b094d7425f7018eb5b66171e21c5fbc10",
        )
        self.assertEqual(self.event_merged.label, None)
        self.assertEqual(self.event_merged.assignee, None)
        self.assertEqual(self.event_merged.assigner, None)
        self.assertEqual(self.event_merged.review_requester, None)
        self.assertEqual(self.event_merged.requested_reviewer, None)
        self.assertEqual(self.event_merged.milestone, None)
        self.assertEqual(self.event_merged.rename, None)
        self.assertEqual(self.event_merged.dismissed_review, None)
        self.assertEqual(self.event_merged.lock_reason, None)
        self.assertEqual(repr(self.event_merged), "IssueEvent(id=1015402964)")

    def testEvent_review_requested_Attributes(self):
        self.assertEqual(self.event_review_requested.actor.login, "jzelinskie")
        self.assertEqual(self.event_review_requested.commit_id, None)
        self.assertEqual(
            self.event_review_requested.created_at,
            datetime.datetime(2017, 3, 22, 19, 6, 44, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_review_requested.event, "review_requested")
        self.assertEqual(self.event_review_requested.id, 1011101309)
        self.assertEqual(self.event_review_requested.issue.number, 538)
        self.assertEqual(
            self.event_review_requested.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1011101309",
        )
        self.assertEqual(
            self.event_review_requested.node_id,
            "MDIwOlJldmlld1JlcXVlc3RlZEV2ZW50MTAxMTEwMTMwOQ==",
        )
        self.assertEqual(self.event_review_requested.commit_url, None)
        self.assertEqual(self.event_review_requested.label, None)
        self.assertEqual(self.event_review_requested.assignee, None)
        self.assertEqual(self.event_review_requested.assigner, None)
        self.assertEqual(
            self.event_review_requested.review_requester.login, "jzelinskie"
        )
        self.assertEqual(
            self.event_review_requested.requested_reviewer.login, "jzelinskie"
        )
        self.assertEqual(self.event_review_requested.milestone, None)
        self.assertEqual(self.event_review_requested.rename, None)
        self.assertEqual(self.event_review_requested.dismissed_review, None)
        self.assertEqual(self.event_review_requested.lock_reason, None)
        self.assertEqual(repr(self.event_review_requested), "IssueEvent(id=1011101309)")

    def testEvent_reopened_Attributes(self):
        self.assertEqual(self.event_reopened.actor.login, "sfdye")
        self.assertEqual(self.event_reopened.commit_id, None)
        self.assertEqual(
            self.event_reopened.created_at,
            datetime.datetime(2018, 8, 10, 13, 10, 9, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_reopened.event, "reopened")
        self.assertEqual(self.event_reopened.id, 1782463023)
        self.assertEqual(self.event_reopened.issue.number, 857)
        self.assertEqual(
            self.event_reopened.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782463023",
        )
        self.assertEqual(
            self.event_reopened.node_id, "MDEzOlJlb3BlbmVkRXZlbnQxNzgyNDYzMDIz"
        )
        self.assertEqual(self.event_reopened.commit_url, None)
        self.assertEqual(self.event_reopened.label, None)
        self.assertEqual(self.event_reopened.assignee, None)
        self.assertEqual(self.event_reopened.assigner, None)
        self.assertEqual(self.event_reopened.review_requester, None)
        self.assertEqual(self.event_reopened.requested_reviewer, None)
        self.assertEqual(self.event_reopened.milestone, None)
        self.assertEqual(self.event_reopened.rename, None)
        self.assertEqual(self.event_reopened.dismissed_review, None)
        self.assertEqual(self.event_reopened.lock_reason, None)
        self.assertEqual(repr(self.event_reopened), "IssueEvent(id=1782463023)")

    def testEvent_unassigned_Attributes(self):
        self.assertEqual(self.event_unassigned.actor.login, "sfdye")
        self.assertEqual(self.event_unassigned.commit_id, None)
        self.assertEqual(
            self.event_unassigned.created_at,
            datetime.datetime(2018, 8, 10, 13, 10, 21, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_unassigned.event, "unassigned")
        self.assertEqual(self.event_unassigned.id, 1782463379)
        self.assertEqual(self.event_unassigned.issue.number, 857)
        self.assertEqual(
            self.event_unassigned.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782463379",
        )
        self.assertEqual(
            self.event_unassigned.node_id, "MDE1OlVuYXNzaWduZWRFdmVudDE3ODI0NjMzNzk="
        )
        self.assertEqual(self.event_unassigned.commit_url, None)
        self.assertEqual(self.event_unassigned.label, None)
        self.assertEqual(self.event_unassigned.actor.login, "sfdye")
        self.assertEqual(self.event_unassigned.actor.login, "sfdye")
        self.assertEqual(self.event_unassigned.review_requester, None)
        self.assertEqual(self.event_unassigned.requested_reviewer, None)
        self.assertEqual(self.event_unassigned.milestone, None)
        self.assertEqual(self.event_unassigned.rename, None)
        self.assertEqual(self.event_unassigned.dismissed_review, None)
        self.assertEqual(self.event_unassigned.lock_reason, None)
        self.assertEqual(repr(self.event_unassigned), "IssueEvent(id=1782463379)")

    def testEvent_unlabeled_Attributes(self):
        self.assertEqual(self.event_unlabeled.actor.login, "sfdye")
        self.assertEqual(self.event_unlabeled.commit_id, None)
        self.assertEqual(
            self.event_unlabeled.created_at,
            datetime.datetime(2018, 8, 10, 13, 10, 38, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_unlabeled.event, "unlabeled")
        self.assertEqual(self.event_unlabeled.id, 1782463917)
        self.assertEqual(self.event_unlabeled.issue.number, 857)
        self.assertEqual(
            self.event_unlabeled.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782463917",
        )
        self.assertEqual(
            self.event_unlabeled.node_id, "MDE0OlVubGFiZWxlZEV2ZW50MTc4MjQ2MzkxNw=="
        )
        self.assertEqual(self.event_unlabeled.commit_url, None)
        self.assertEqual(self.event_unlabeled.label.name, "improvement")
        self.assertEqual(self.event_unlabeled.assignee, None)
        self.assertEqual(self.event_unlabeled.assigner, None)
        self.assertEqual(self.event_unlabeled.review_requester, None)
        self.assertEqual(self.event_unlabeled.requested_reviewer, None)
        self.assertEqual(self.event_unlabeled.milestone, None)
        self.assertEqual(self.event_unlabeled.rename, None)
        self.assertEqual(self.event_unlabeled.dismissed_review, None)
        self.assertEqual(self.event_unlabeled.lock_reason, None)
        self.assertEqual(repr(self.event_unlabeled), "IssueEvent(id=1782463917)")

    def testEvent_renamed_Attributes(self):
        self.assertEqual(self.event_renamed.actor.login, "sfdye")
        self.assertEqual(self.event_renamed.commit_id, None)
        self.assertEqual(
            self.event_renamed.created_at,
            datetime.datetime(2018, 8, 10, 13, 15, 18, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_renamed.event, "renamed")
        self.assertEqual(self.event_renamed.id, 1782472556)
        self.assertEqual(self.event_renamed.issue.number, 857)
        self.assertEqual(
            self.event_renamed.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782472556",
        )
        self.assertEqual(
            self.event_renamed.node_id, "MDE3OlJlbmFtZWRUaXRsZUV2ZW50MTc4MjQ3MjU1Ng=="
        )
        self.assertEqual(self.event_renamed.commit_url, None)
        self.assertEqual(self.event_renamed.label, None)
        self.assertEqual(self.event_renamed.assignee, None)
        self.assertEqual(self.event_renamed.assigner, None)
        self.assertEqual(self.event_renamed.review_requester, None)
        self.assertEqual(self.event_renamed.requested_reviewer, None)
        self.assertEqual(self.event_renamed.milestone, None)
        self.assertEqual(
            self.event_renamed.rename,
            {
                "to": "Adding new attributes to IssueEvent",
                "from": "Adding new attributes to IssueEvent Object (DO NOT MERGE - SEE NOTES)",
            },
        )
        self.assertEqual(self.event_renamed.dismissed_review, None)
        self.assertEqual(self.event_renamed.lock_reason, None)
        self.assertEqual(repr(self.event_renamed), "IssueEvent(id=1782472556)")

    def testEvent_base_ref_changed_Attributes(self):
        self.assertEqual(self.event_base_ref_changed.actor.login, "allevin")
        self.assertEqual(self.event_base_ref_changed.commit_id, None)
        self.assertEqual(
            self.event_base_ref_changed.created_at,
            datetime.datetime(2018, 8, 10, 16, 38, 22, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_base_ref_changed.event, "base_ref_changed")
        self.assertEqual(self.event_base_ref_changed.id, 1782915693)
        self.assertEqual(self.event_base_ref_changed.issue.number, 857)
        self.assertEqual(
            self.event_base_ref_changed.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782915693",
        )
        self.assertEqual(
            self.event_base_ref_changed.node_id,
            "MDE5OkJhc2VSZWZDaGFuZ2VkRXZlbnQxNzgyOTE1Njkz",
        )
        self.assertEqual(self.event_base_ref_changed.commit_url, None)
        self.assertEqual(self.event_base_ref_changed.label, None)
        self.assertEqual(self.event_base_ref_changed.assignee, None)
        self.assertEqual(self.event_base_ref_changed.assigner, None)
        self.assertEqual(self.event_base_ref_changed.review_requester, None)
        self.assertEqual(self.event_base_ref_changed.requested_reviewer, None)
        self.assertEqual(self.event_base_ref_changed.milestone, None)
        self.assertEqual(self.event_head_ref_deleted.rename, None)
        self.assertEqual(self.event_base_ref_changed.dismissed_review, None)
        self.assertEqual(self.event_base_ref_changed.lock_reason, None)
        self.assertEqual(repr(self.event_base_ref_changed), "IssueEvent(id=1782915693)")

    def testEvent_head_ref_deleted_Attributes(self):
        self.assertEqual(self.event_head_ref_deleted.actor.login, "allevin")
        self.assertEqual(self.event_head_ref_deleted.commit_id, None)
        self.assertEqual(
            self.event_head_ref_deleted.created_at,
            datetime.datetime(2018, 8, 10, 16, 39, 20, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_head_ref_deleted.event, "head_ref_deleted")
        self.assertEqual(self.event_head_ref_deleted.id, 1782917185)
        self.assertEqual(self.event_head_ref_deleted.issue.number, 857)
        self.assertEqual(
            self.event_head_ref_deleted.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782917185",
        )
        self.assertEqual(
            self.event_head_ref_deleted.node_id,
            "MDE5OkhlYWRSZWZEZWxldGVkRXZlbnQxNzgyOTE3MTg1",
        )
        self.assertEqual(self.event_head_ref_deleted.commit_url, None)
        self.assertEqual(self.event_head_ref_deleted.label, None)
        self.assertEqual(self.event_head_ref_deleted.assignee, None)
        self.assertEqual(self.event_head_ref_deleted.assigner, None)
        self.assertEqual(self.event_head_ref_deleted.review_requester, None)
        self.assertEqual(self.event_head_ref_deleted.requested_reviewer, None)
        self.assertEqual(self.event_head_ref_deleted.milestone, None)
        self.assertEqual(self.event_head_ref_deleted.rename, None)
        self.assertEqual(self.event_head_ref_deleted.dismissed_review, None)
        self.assertEqual(self.event_head_ref_deleted.lock_reason, None)
        self.assertEqual(repr(self.event_head_ref_deleted), "IssueEvent(id=1782917185)")

    def testEvent_head_ref_restored_Attributes(self):
        self.assertEqual(self.event_head_ref_restored.actor.login, "allevin")
        self.assertEqual(self.event_head_ref_restored.commit_id, None)
        self.assertEqual(
            self.event_head_ref_restored.created_at,
            datetime.datetime(2018, 8, 10, 16, 39, 23, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_head_ref_restored.event, "head_ref_restored")
        self.assertEqual(self.event_head_ref_restored.id, 1782917299)
        self.assertEqual(self.event_head_ref_restored.issue.number, 857)
        self.assertEqual(
            self.event_head_ref_restored.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1782917299",
        )
        self.assertEqual(
            self.event_head_ref_restored.node_id,
            "MDIwOkhlYWRSZWZSZXN0b3JlZEV2ZW50MTc4MjkxNzI5OQ==",
        )
        self.assertEqual(self.event_head_ref_restored.commit_url, None)
        self.assertEqual(self.event_head_ref_restored.label, None)
        self.assertEqual(self.event_head_ref_restored.assignee, None)
        self.assertEqual(self.event_head_ref_restored.assigner, None)
        self.assertEqual(self.event_head_ref_restored.review_requester, None)
        self.assertEqual(self.event_head_ref_restored.requested_reviewer, None)
        self.assertEqual(self.event_head_ref_restored.milestone, None)
        self.assertEqual(self.event_head_ref_deleted.rename, None)
        self.assertEqual(self.event_head_ref_restored.dismissed_review, None)
        self.assertEqual(self.event_head_ref_deleted.lock_reason, None)
        self.assertEqual(
            repr(self.event_head_ref_restored), "IssueEvent(id=1782917299)"
        )

    def testEvent_milestoned_Attributes(self):
        self.assertEqual(self.event_milestoned.actor.login, "sfdye")
        self.assertEqual(self.event_milestoned.commit_id, None)
        self.assertEqual(
            self.event_milestoned.created_at,
            datetime.datetime(2018, 8, 11, 0, 46, 19, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_milestoned.event, "milestoned")
        self.assertEqual(self.event_milestoned.id, 1783596418)
        self.assertEqual(self.event_milestoned.issue.number, 857)
        self.assertEqual(
            self.event_milestoned.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1783596418",
        )
        self.assertEqual(
            self.event_milestoned.node_id, "MDE1Ok1pbGVzdG9uZWRFdmVudDE3ODM1OTY0MTg="
        )
        self.assertEqual(self.event_milestoned.commit_url, None)
        self.assertEqual(self.event_milestoned.label, None)
        self.assertEqual(self.event_milestoned.assignee, None)
        self.assertEqual(self.event_milestoned.assigner, None)
        self.assertEqual(self.event_milestoned.review_requester, None)
        self.assertEqual(self.event_milestoned.requested_reviewer, None)
        self.assertEqual(self.event_milestoned.milestone.title, "Version 1.25.0")
        self.assertEqual(self.event_milestoned.rename, None)
        self.assertEqual(self.event_milestoned.dismissed_review, None)
        self.assertEqual(self.event_milestoned.lock_reason, None)
        self.assertEqual(repr(self.event_milestoned), "IssueEvent(id=1783596418)")

    def testEvent_demilestoned_Attributes(self):
        self.assertEqual(self.event_demilestoned.actor.login, "sfdye")
        self.assertEqual(self.event_demilestoned.commit_id, None)
        self.assertEqual(
            self.event_demilestoned.created_at,
            datetime.datetime(2018, 8, 11, 0, 46, 22, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_demilestoned.event, "demilestoned")
        self.assertEqual(self.event_demilestoned.id, 1783596452)
        self.assertEqual(self.event_demilestoned.issue.number, 857)
        self.assertEqual(
            self.event_demilestoned.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1783596452",
        )
        self.assertEqual(
            self.event_demilestoned.node_id,
            "MDE3OkRlbWlsZXN0b25lZEV2ZW50MTc4MzU5NjQ1Mg==",
        )
        self.assertEqual(self.event_demilestoned.commit_url, None)
        self.assertEqual(self.event_demilestoned.label, None)
        self.assertEqual(self.event_demilestoned.assignee, None)
        self.assertEqual(self.event_demilestoned.assigner, None)
        self.assertEqual(self.event_demilestoned.review_requester, None)
        self.assertEqual(self.event_demilestoned.requested_reviewer, None)
        self.assertEqual(self.event_demilestoned.milestone.title, "Version 1.25.0")
        self.assertEqual(self.event_demilestoned.rename, None)
        self.assertEqual(self.event_demilestoned.dismissed_review, None)
        self.assertEqual(self.event_demilestoned.lock_reason, None)
        self.assertEqual(repr(self.event_demilestoned), "IssueEvent(id=1783596452)")

    def testEvent_locked_Attributes(self):
        self.assertEqual(self.event_locked.actor.login, "PyGithub")
        self.assertEqual(self.event_locked.commit_id, None)
        self.assertEqual(
            self.event_locked.created_at,
            datetime.datetime(2018, 8, 11, 0, 46, 56, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_locked.event, "locked")
        self.assertEqual(self.event_locked.id, 1783596743)
        self.assertEqual(self.event_locked.issue.number, 857)
        self.assertEqual(
            self.event_locked.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1783596743",
        )
        self.assertEqual(
            self.event_locked.node_id, "MDExOkxvY2tlZEV2ZW50MTc4MzU5Njc0Mw=="
        )
        self.assertEqual(self.event_locked.commit_url, None)
        self.assertEqual(self.event_locked.label, None)
        self.assertEqual(self.event_locked.assignee, None)
        self.assertEqual(self.event_locked.assigner, None)
        self.assertEqual(self.event_locked.review_requester, None)
        self.assertEqual(self.event_locked.requested_reviewer, None)
        self.assertEqual(self.event_locked.milestone, None)
        self.assertEqual(self.event_locked.rename, None)
        self.assertEqual(self.event_locked.dismissed_review, None)
        self.assertEqual(self.event_locked.lock_reason, "too heated")
        self.assertEqual(repr(self.event_locked), "IssueEvent(id=1783596743)")

    def testEvent_unlocked_Attributes(self):
        self.assertEqual(self.event_unlocked.actor.login, "PyGithub")
        self.assertEqual(self.event_unlocked.commit_id, None)
        self.assertEqual(
            self.event_unlocked.created_at,
            datetime.datetime(2018, 8, 11, 0, 47, 7, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_unlocked.event, "unlocked")
        self.assertEqual(self.event_unlocked.id, 1783596818)
        self.assertEqual(self.event_unlocked.issue.number, 857)
        self.assertEqual(
            self.event_unlocked.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1783596818",
        )
        self.assertEqual(
            self.event_unlocked.node_id, "MDEzOlVubG9ja2VkRXZlbnQxNzgzNTk2ODE4"
        )
        self.assertEqual(self.event_unlocked.commit_url, None)
        self.assertEqual(self.event_unlocked.label, None)
        self.assertEqual(self.event_unlocked.assignee, None)
        self.assertEqual(self.event_unlocked.assigner, None)
        self.assertEqual(self.event_unlocked.review_requester, None)
        self.assertEqual(self.event_unlocked.requested_reviewer, None)
        self.assertEqual(self.event_unlocked.milestone, None)
        self.assertEqual(self.event_unlocked.rename, None)
        self.assertEqual(self.event_unlocked.dismissed_review, None)
        self.assertEqual(self.event_unlocked.lock_reason, None)
        self.assertEqual(repr(self.event_unlocked), "IssueEvent(id=1783596818)")

    def testEvent_review_dismissed_Attributes(self):
        self.assertEqual(self.event_review_dismissed.actor.login, "sfdye")
        self.assertEqual(self.event_review_dismissed.commit_id, None)
        self.assertEqual(
            self.event_review_dismissed.created_at,
            datetime.datetime(2018, 8, 11, 1, 7, 10, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_review_dismissed.event, "review_dismissed")
        self.assertEqual(self.event_review_dismissed.id, 1783605084)
        self.assertEqual(self.event_review_dismissed.issue.number, 857)
        self.assertEqual(
            self.event_review_dismissed.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1783605084",
        )
        self.assertEqual(
            self.event_review_dismissed.node_id,
            "MDIwOlJldmlld0Rpc21pc3NlZEV2ZW50MTc4MzYwNTA4NA==",
        )
        self.assertEqual(self.event_review_dismissed.commit_url, None)
        self.assertEqual(self.event_review_dismissed.label, None)
        self.assertEqual(self.event_review_dismissed.assignee, None)
        self.assertEqual(self.event_review_dismissed.assigner, None)
        self.assertEqual(self.event_review_dismissed.review_requester, None)
        self.assertEqual(self.event_review_dismissed.requested_reviewer, None)
        self.assertEqual(self.event_review_dismissed.milestone, None)
        self.assertEqual(self.event_review_dismissed.rename, None)
        self.assertEqual(
            self.event_review_dismissed.dismissed_review,
            {
                "dismissal_message": "dismiss",
                "state": "changes_requested",
                "review_id": 145431295,
            },
        )
        self.assertEqual(self.event_review_dismissed.lock_reason, None)
        self.assertEqual(repr(self.event_review_dismissed), "IssueEvent(id=1783605084)")

    def testEvent_review_request_removed_Attributes(self):
        self.assertEqual(self.event_review_request_removed.actor.login, "sfdye")
        self.assertEqual(self.event_review_request_removed.commit_id, None)
        self.assertEqual(
            self.event_review_request_removed.created_at,
            datetime.datetime(2018, 8, 11, 12, 32, 59, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.event_review_request_removed.event, "review_request_removed"
        )
        self.assertEqual(self.event_review_request_removed.id, 1783779835)
        self.assertEqual(self.event_review_request_removed.issue.number, 857)
        self.assertEqual(
            self.event_review_request_removed.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1783779835",
        )
        self.assertEqual(
            self.event_review_request_removed.node_id,
            "MDI1OlJldmlld1JlcXVlc3RSZW1vdmVkRXZlbnQxNzgzNzc5ODM1",
        )
        self.assertEqual(self.event_review_request_removed.commit_url, None)
        self.assertEqual(self.event_review_request_removed.label, None)
        self.assertEqual(self.event_review_request_removed.assignee, None)
        self.assertEqual(self.event_review_request_removed.assigner, None)
        self.assertEqual(
            self.event_review_request_removed.review_requester.login, "sfdye"
        )
        self.assertEqual(
            self.event_review_request_removed.requested_reviewer.login, "jasonwhite"
        )
        self.assertEqual(self.event_review_request_removed.milestone, None)
        self.assertEqual(self.event_review_request_removed.rename, None)
        self.assertEqual(self.event_review_request_removed.dismissed_review, None)
        self.assertEqual(self.event_review_request_removed.lock_reason, None)
        self.assertEqual(
            repr(self.event_review_request_removed), "IssueEvent(id=1783779835)"
        )

    def testEvent_marked_as_duplicate_Attributes(self):
        self.assertEqual(self.event_marked_as_duplicate.actor.login, "sfdye")
        self.assertEqual(self.event_marked_as_duplicate.commit_id, None)
        self.assertEqual(
            self.event_marked_as_duplicate.created_at,
            datetime.datetime(2018, 8, 11, 12, 32, 35, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_marked_as_duplicate.event, "marked_as_duplicate")
        self.assertEqual(self.event_marked_as_duplicate.id, 1783779725)
        self.assertEqual(self.event_marked_as_duplicate.issue.number, 857)
        self.assertEqual(
            self.event_marked_as_duplicate.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1783779725",
        )
        self.assertEqual(
            self.event_marked_as_duplicate.node_id,
            "MDIyOk1hcmtlZEFzRHVwbGljYXRlRXZlbnQxNzgzNzc5NzI1",
        )
        self.assertEqual(self.event_marked_as_duplicate.commit_url, None)
        self.assertEqual(self.event_marked_as_duplicate.label, None)
        self.assertEqual(self.event_marked_as_duplicate.assignee, None)
        self.assertEqual(self.event_marked_as_duplicate.assigner, None)
        self.assertEqual(self.event_marked_as_duplicate.review_requester, None)
        self.assertEqual(self.event_marked_as_duplicate.requested_reviewer, None)
        self.assertEqual(self.event_marked_as_duplicate.milestone, None)
        self.assertEqual(self.event_marked_as_duplicate.rename, None)
        self.assertEqual(self.event_marked_as_duplicate.dismissed_review, None)
        self.assertEqual(self.event_marked_as_duplicate.lock_reason, None)
        self.assertEqual(
            repr(self.event_marked_as_duplicate), "IssueEvent(id=1783779725)"
        )

    def testEvent_unmarked_as_duplicate_Attributes(self):
        self.assertEqual(self.event_unmarked_as_duplicate.actor.login, "sfdye")
        self.assertEqual(self.event_unmarked_as_duplicate.commit_id, None)
        self.assertEqual(
            self.event_unmarked_as_duplicate.created_at,
            datetime.datetime(2018, 8, 15, 2, 57, 46, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.event_unmarked_as_duplicate.event, "unmarked_as_duplicate"
        )
        self.assertEqual(self.event_unmarked_as_duplicate.id, 1789228962)
        self.assertEqual(self.event_unmarked_as_duplicate.issue.number, 857)
        self.assertEqual(
            self.event_unmarked_as_duplicate.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1789228962",
        )
        self.assertEqual(
            self.event_unmarked_as_duplicate.node_id,
            "MDI0OlVubWFya2VkQXNEdXBsaWNhdGVFdmVudDE3ODkyMjg5NjI=",
        )
        self.assertEqual(self.event_unmarked_as_duplicate.commit_url, None)
        self.assertEqual(self.event_unmarked_as_duplicate.label, None)
        self.assertEqual(self.event_unmarked_as_duplicate.assignee, None)
        self.assertEqual(self.event_unmarked_as_duplicate.assigner, None)
        self.assertEqual(self.event_unmarked_as_duplicate.review_requester, None)
        self.assertEqual(self.event_unmarked_as_duplicate.requested_reviewer, None)
        self.assertEqual(self.event_unmarked_as_duplicate.milestone, None)
        self.assertEqual(self.event_unmarked_as_duplicate.rename, None)
        self.assertEqual(self.event_unmarked_as_duplicate.dismissed_review, None)
        self.assertEqual(self.event_unmarked_as_duplicate.lock_reason, None)
        self.assertEqual(
            repr(self.event_unmarked_as_duplicate), "IssueEvent(id=1789228962)"
        )

    def testEvent_added_to_project_Attributes(self):
        self.assertEqual(self.event_added_to_project.actor.login, "sfdye")
        self.assertEqual(self.event_added_to_project.commit_id, None)
        self.assertEqual(
            self.event_added_to_project.created_at,
            datetime.datetime(2018, 8, 16, 8, 13, 24, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_added_to_project.event, "added_to_project")
        self.assertEqual(self.event_added_to_project.id, 1791766828)
        self.assertEqual(self.event_added_to_project.issue.number, 857)
        self.assertEqual(
            self.event_added_to_project.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1791766828",
        )
        self.assertEqual(
            self.event_added_to_project.node_id,
            "MDE5OkFkZGVkVG9Qcm9qZWN0RXZlbnQxNzkxNzY2ODI4",
        )
        self.assertEqual(self.event_added_to_project.commit_url, None)
        self.assertEqual(self.event_added_to_project.label, None)
        self.assertEqual(self.event_added_to_project.assignee, None)
        self.assertEqual(self.event_added_to_project.assigner, None)
        self.assertEqual(self.event_added_to_project.review_requester, None)
        self.assertEqual(self.event_added_to_project.requested_reviewer, None)
        self.assertEqual(self.event_added_to_project.milestone, None)
        self.assertEqual(self.event_added_to_project.rename, None)
        self.assertEqual(self.event_added_to_project.dismissed_review, None)
        self.assertEqual(self.event_added_to_project.lock_reason, None)
        self.assertEqual(repr(self.event_added_to_project), "IssueEvent(id=1791766828)")

    def testEvent_moved_columns_in_project_Attributes(self):
        self.assertEqual(self.event_moved_columns_in_project.actor.login, "sfdye")
        self.assertEqual(self.event_moved_columns_in_project.commit_id, None)
        self.assertEqual(
            self.event_moved_columns_in_project.created_at,
            datetime.datetime(2018, 8, 16, 8, 13, 55, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.event_moved_columns_in_project.event, "moved_columns_in_project"
        )
        self.assertEqual(self.event_moved_columns_in_project.id, 1791767766)
        self.assertEqual(self.event_moved_columns_in_project.issue.number, 857)
        self.assertEqual(
            self.event_moved_columns_in_project.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1791767766",
        )
        self.assertEqual(
            self.event_moved_columns_in_project.node_id,
            "MDI2Ok1vdmVkQ29sdW1uc0luUHJvamVjdEV2ZW50MTc5MTc2Nzc2Ng==",
        )
        self.assertEqual(self.event_moved_columns_in_project.commit_url, None)
        self.assertEqual(self.event_moved_columns_in_project.label, None)
        self.assertEqual(self.event_moved_columns_in_project.assignee, None)
        self.assertEqual(self.event_moved_columns_in_project.assigner, None)
        self.assertEqual(self.event_moved_columns_in_project.review_requester, None)
        self.assertEqual(self.event_moved_columns_in_project.requested_reviewer, None)
        self.assertEqual(self.event_moved_columns_in_project.milestone, None)
        self.assertEqual(self.event_moved_columns_in_project.rename, None)
        self.assertEqual(self.event_moved_columns_in_project.dismissed_review, None)
        self.assertEqual(self.event_moved_columns_in_project.lock_reason, None)
        self.assertEqual(
            repr(self.event_moved_columns_in_project), "IssueEvent(id=1791767766)"
        )

    def testEvent_removed_from_project_Attributes(self):
        self.assertEqual(self.event_removed_from_project.actor.login, "sfdye")
        self.assertEqual(self.event_removed_from_project.commit_id, None)
        self.assertEqual(
            self.event_removed_from_project.created_at,
            datetime.datetime(2018, 8, 16, 8, 14, 8, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.event_removed_from_project.event, "removed_from_project")
        self.assertEqual(self.event_removed_from_project.id, 1791768212)
        self.assertEqual(self.event_removed_from_project.issue.number, 857)
        self.assertEqual(
            self.event_removed_from_project.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1791768212",
        )
        self.assertEqual(
            self.event_removed_from_project.node_id,
            "MDIzOlJlbW92ZWRGcm9tUHJvamVjdEV2ZW50MTc5MTc2ODIxMg==",
        )
        self.assertEqual(self.event_removed_from_project.commit_url, None)
        self.assertEqual(self.event_removed_from_project.label, None)
        self.assertEqual(self.event_removed_from_project.assignee, None)
        self.assertEqual(self.event_removed_from_project.assigner, None)
        self.assertEqual(self.event_removed_from_project.review_requester, None)
        self.assertEqual(self.event_removed_from_project.requested_reviewer, None)
        self.assertEqual(self.event_removed_from_project.milestone, None)
        self.assertEqual(self.event_removed_from_project.rename, None)
        self.assertEqual(self.event_removed_from_project.dismissed_review, None)
        self.assertEqual(self.event_removed_from_project.lock_reason, None)
        self.assertEqual(
            repr(self.event_removed_from_project), "IssueEvent(id=1791768212)"
        )

    def testEvent_converted_note_to_issue_Attributes(self):
        self.assertEqual(self.event_converted_note_to_issue.actor.login, "sfdye")
        self.assertEqual(self.event_converted_note_to_issue.commit_id, None)
        self.assertEqual(
            self.event_converted_note_to_issue.created_at,
            datetime.datetime(2018, 8, 16, 8, 14, 34, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.event_converted_note_to_issue.event, "converted_note_to_issue"
        )
        self.assertEqual(self.event_converted_note_to_issue.id, 1791769149)
        self.assertEqual(self.event_converted_note_to_issue.issue.number, 866)
        self.assertEqual(
            self.event_converted_note_to_issue.url,
            "https://api.github.com/repos/PyGithub/PyGithub/issues/events/1791769149",
        )
        self.assertEqual(
            self.event_converted_note_to_issue.node_id,
            "MDI1OkNvbnZlcnRlZE5vdGVUb0lzc3VlRXZlbnQxNzkxNzY5MTQ5",
        )
        self.assertEqual(self.event_converted_note_to_issue.commit_url, None)
        self.assertEqual(self.event_converted_note_to_issue.label, None)
        self.assertEqual(self.event_converted_note_to_issue.assignee, None)
        self.assertEqual(self.event_converted_note_to_issue.assigner, None)
        self.assertEqual(self.event_converted_note_to_issue.review_requester, None)
        self.assertEqual(self.event_converted_note_to_issue.requested_reviewer, None)
        self.assertEqual(self.event_converted_note_to_issue.milestone, None)
        self.assertEqual(self.event_converted_note_to_issue.rename, None)
        self.assertEqual(self.event_converted_note_to_issue.dismissed_review, None)
        self.assertEqual(self.event_converted_note_to_issue.lock_reason, None)
        self.assertEqual(
            repr(self.event_converted_note_to_issue), "IssueEvent(id=1791769149)"
        )
