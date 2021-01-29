############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 @tmshn <tmshn@r.recruit.co.jp>                                #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 MarcoFalke <falke.marco@gmail.com>                            #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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


class PullRequest(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.pull = self.repo.get_pull(31)

        marco_repo = self.g.get_repo("MarcoFalke/PyGithub", lazy=True)
        self.pullIssue256Closed = marco_repo.get_pull(1)
        self.pullIssue256Merged = marco_repo.get_pull(2)
        self.pullIssue256Conflict = marco_repo.get_pull(3)
        self.pullIssue256Uncached = marco_repo.get_pull(4)

        flo_repo = self.g.get_repo("FlorentClarret/PyGithub")
        self.pullMaintainerCanModify = flo_repo.get_pull(2)

    def testAttributesIssue256(self):
        self.assertEqual(
            self.pullIssue256Closed.closed_at,
            datetime.datetime(2018, 5, 22, 14, 50, 43, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.pullIssue256Merged.closed_at,
            datetime.datetime(2018, 5, 22, 14, 53, 13, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.pullIssue256Conflict.closed_at, None)
        self.assertEqual(self.pullIssue256Uncached.closed_at, None)

        self.assertEqual(self.pullIssue256Closed.state, "closed")
        self.assertEqual(self.pullIssue256Merged.state, "closed")
        self.assertEqual(self.pullIssue256Conflict.state, "open")
        self.assertEqual(self.pullIssue256Uncached.state, "open")

        self.assertFalse(self.pullIssue256Closed.merged)
        self.assertTrue(self.pullIssue256Merged.merged)
        self.assertFalse(self.pullIssue256Conflict.merged)
        self.assertFalse(self.pullIssue256Uncached.merged)

        self.assertEqual(self.pullIssue256Closed.mergeable, None)
        self.assertEqual(self.pullIssue256Merged.mergeable, None)
        self.assertTrue(self.pullIssue256Conflict.mergeable)
        self.assertEqual(self.pullIssue256Uncached.mergeable, None)

        self.assertEqual(self.pullIssue256Closed.mergeable_state, "unknown")
        self.assertEqual(self.pullIssue256Merged.mergeable_state, "unknown")
        self.assertEqual(self.pullIssue256Conflict.mergeable_state, "clean")
        self.assertEqual(self.pullIssue256Uncached.mergeable_state, "unknown")

    def testAttributes(self):
        self.assertEqual(self.pull.additions, 511)
        self.assertEqual(self.pull.assignee.login, "jacquev6")
        self.assertListKeyEqual(
            self.pull.assignees, lambda a: a.login, ["stuglaser", "jacquev6"]
        )
        self.assertEqual(
            self.pull.base.label, "jacquev6:topic/RewriteWithGeneratedCode"
        )
        self.assertEqual(self.pull.base.sha, "ed866fc43833802ab553e5ff8581c81bb00dd433")
        self.assertEqual(self.pull.base.user.login, "jacquev6")
        self.assertEqual(self.pull.base.ref, "topic/RewriteWithGeneratedCode")
        self.assertEqual(self.pull.base.repo.full_name, "jacquev6/PyGithub")
        self.assertEqual(self.pull.body, "Body edited by PyGithub")
        self.assertEqual(self.pull.changed_files, 45)
        self.assertEqual(
            self.pull.closed_at,
            datetime.datetime(2012, 5, 27, 10, 29, 7, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.pull.comments, 1)
        self.assertEqual(self.pull.commits, 3)
        self.assertEqual(
            self.pull.created_at,
            datetime.datetime(2012, 5, 27, 9, 25, 36, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.pull.deletions, 384)
        self.assertEqual(
            self.pull.diff_url, "https://github.com/jacquev6/PyGithub/pull/31.diff"
        )
        self.assertEqual(self.pull.head.label, "BeaverSoftware:master")
        self.assertEqual(
            self.pull.html_url, "https://github.com/jacquev6/PyGithub/pull/31"
        )
        self.assertEqual(self.pull.id, 1436215)
        self.assertEqual(
            self.pull.issue_url,
            "https://api.github.com/repos/jacquev6/PyGithub/issues/31",
        )
        self.assertListKeyEqual(self.pull.labels, lambda a: a.name, ["refactoring"])
        self.assertFalse(self.pull.mergeable)
        self.assertFalse(self.pull.rebaseable)
        self.assertTrue(self.pull.merged)
        self.assertEqual(
            self.pull.merged_at,
            datetime.datetime(2012, 5, 27, 10, 29, 7, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.pull.merged_by.login, "jacquev6")
        self.assertEqual(self.pull.number, 31)
        self.assertEqual(
            self.pull.patch_url, "https://github.com/jacquev6/PyGithub/pull/31.patch"
        )
        self.assertEqual(self.pull.review_comments, 1)
        self.assertEqual(self.pull.state, "closed")
        self.assertEqual(self.pull.title, "Title edited by PyGithub")
        self.assertEqual(
            self.pull.updated_at,
            datetime.datetime(2012, 11, 3, 8, 19, 40, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.pull.url, "https://api.github.com/repos/jacquev6/PyGithub/pulls/31"
        )
        self.assertEqual(self.pull.user.login, "jacquev6")
        self.assertEqual(self.pull.draft, None)
        self.assertEqual(self.pull.maintainer_can_modify, None)
        self.assertEqual(
            repr(self.pull),
            'PullRequest(title="Title edited by PyGithub", number=31)',
        )
        self.assertEqual(
            repr(self.pull.base),
            'PullRequestPart(sha="ed866fc43833802ab553e5ff8581c81bb00dd433")',
        )
        self.assertTrue(self.pullIssue256Conflict.rebaseable)

    def testCreateComment(self):
        commit = self.repo.get_commit("8a4f306d4b223682dd19410d4a9150636ebe4206")
        comment = self.pull.create_comment(
            "Comment created by PyGithub", commit, "src/github/Issue.py", 5
        )
        self.assertEqual(comment.id, 886298)

    def testGetComments(self):
        self.assertListKeyEqual(self.pull.get_comments(), lambda c: c.id, [886298])

    def testCreateIssueComment(self):
        comment = self.pull.create_issue_comment("Issue comment created by PyGithub")
        self.assertEqual(comment.id, 8387331)

    def testGetIssueComments(self):
        self.assertListKeyEqual(
            self.pull.get_issue_comments(), lambda c: c.id, [8387331]
        )

    def testGetIssueComment(self):
        comment = self.pull.get_issue_comment(8387331)
        self.assertEqual(comment.body, "Issue comment created by PyGithub")

    def testGetIssueEvents(self):
        self.assertListKeyEqual(
            self.pull.get_issue_events(),
            lambda e: e.id,
            [16349963, 16350729, 16350730, 16350731, 28469043, 98136335],
        )

    def testGetReviewComments(self):
        epoch = datetime.datetime(1970, 1, 1, 0, 0)
        comments = self.pull.get_review_comments(since=epoch)
        self.assertListKeyEqual(comments, lambda c: c.id, [238127783])

    def testReviewRequests(self):
        self.pull.create_review_request(
            reviewers="sfdye", team_reviewers="pygithub-owners"
        )
        review_requests = self.pull.get_review_requests()
        self.assertListKeyEqual(review_requests[0], lambda c: c.login, ["sfdye"])
        self.assertListKeyEqual(
            review_requests[1], lambda c: c.slug, ["pygithub-owners"]
        )
        self.pull.delete_review_request(reviewers="sfdye")
        review_requests = self.pull.get_review_requests()
        self.assertEqual(list(review_requests[0]), [])
        self.assertListKeyEqual(
            review_requests[1], lambda c: c.slug, ["pygithub-owners"]
        )

    def testEditWithoutArguments(self):
        self.pull.edit()

    def testEditWithAllArguments(self):
        self.pullMaintainerCanModify.edit(
            "Title edited by PyGithub",
            "Body edited by PyGithub",
            "open",
            "master",
            True,
        )
        self.assertEqual(self.pullMaintainerCanModify.title, "Title edited by PyGithub")
        self.assertEqual(self.pullMaintainerCanModify.body, "Body edited by PyGithub")
        self.assertEqual(self.pullMaintainerCanModify.state, "open")
        self.assertEqual(self.pullMaintainerCanModify.base.ref, "master")
        self.assertTrue(self.pullMaintainerCanModify.maintainer_can_modify)

    def testGetCommits(self):
        self.assertListKeyEqual(
            self.pull.get_commits(),
            lambda c: c.sha,
            [
                "4aadfff21cdd2d2566b0e4bd7309c233b5f4ae23",
                "93dcae5cf207de376c91d0599226e7c7563e1d16",
                "8a4f306d4b223682dd19410d4a9150636ebe4206",
            ],
        )

    def testGetFiles(self):
        self.assertListKeyEqual(
            self.pull.get_files(),
            lambda f: f.filename,
            [
                "codegen/templates/GithubObject.py",
                "src/github/AuthenticatedUser.py",
                "src/github/Authorization.py",
                "src/github/Branch.py",
                "src/github/Commit.py",
                "src/github/CommitComment.py",
                "src/github/CommitFile.py",
                "src/github/CommitStats.py",
                "src/github/Download.py",
                "src/github/Event.py",
                "src/github/Gist.py",
                "src/github/GistComment.py",
                "src/github/GistHistoryState.py",
                "src/github/GitAuthor.py",
                "src/github/GitBlob.py",
                "src/github/GitCommit.py",
                "src/github/GitObject.py",
                "src/github/GitRef.py",
                "src/github/GitTag.py",
                "src/github/GitTree.py",
                "src/github/GitTreeElement.py",
                "src/github/Hook.py",
                "src/github/Issue.py",
                "src/github/IssueComment.py",
                "src/github/IssueEvent.py",
                "src/github/Label.py",
                "src/github/Milestone.py",
                "src/github/NamedUser.py",
                "src/github/Organization.py",
                "src/github/Permissions.py",
                "src/github/Plan.py",
                "src/github/PullRequest.py",
                "src/github/PullRequestComment.py",
                "src/github/PullRequestFile.py",
                "src/github/Repository.py",
                "src/github/RepositoryKey.py",
                "src/github/Tag.py",
                "src/github/Team.py",
                "src/github/UserKey.py",
                "test/Issue.py",
                "test/IssueEvent.py",
                "test/ReplayData/Issue.testAddAndRemoveLabels.txt",
                "test/ReplayData/Issue.testDeleteAndSetLabels.txt",
                "test/ReplayData/Issue.testGetLabels.txt",
                "test/ReplayData/IssueEvent.setUp.txt",
            ],
        )

    def testGetLabels(self):
        self.assertListKeyEqual(
            self.pull.get_labels(), lambda l: l.name, ["wip", "refactoring"]
        )

    def testAddAndRemoveLabels(self):
        wip = self.repo.get_label("wip")
        refactoring = self.repo.get_label("refactoring")
        self.assertListKeyEqual(
            self.pull.get_labels(),
            lambda l: l.name,
            ["wip", "refactoring", "improvement"],
        )
        self.pull.remove_from_labels(wip)
        self.assertListKeyEqual(
            self.pull.get_labels(), lambda l: l.name, ["refactoring", "improvement"]
        )
        self.pull.remove_from_labels(refactoring)
        self.assertListKeyEqual(
            self.pull.get_labels(), lambda l: l.name, ["improvement"]
        )
        self.pull.add_to_labels(wip, refactoring)
        self.assertListKeyEqual(
            self.pull.get_labels(),
            lambda l: l.name,
            ["wip", "refactoring", "improvement"],
        )

    def testAddAndRemoveLabelsWithStringArguments(self):
        wip = "wip"
        refactoring = "refactoring"
        self.assertListKeyEqual(
            self.pull.get_labels(),
            lambda l: l.name,
            ["wip", "refactoring", "improvement"],
        )
        self.pull.remove_from_labels(wip)
        self.assertListKeyEqual(
            self.pull.get_labels(), lambda l: l.name, ["refactoring", "improvement"]
        )
        self.pull.remove_from_labels(refactoring)
        self.assertListKeyEqual(
            self.pull.get_labels(), lambda l: l.name, ["improvement"]
        )
        self.pull.add_to_labels(wip, refactoring)
        self.assertListKeyEqual(
            self.pull.get_labels(),
            lambda l: l.name,
            ["wip", "refactoring", "improvement"],
        )

    def testDeleteAndSetLabels(self):
        wip = self.repo.get_label("wip")
        refactoring = self.repo.get_label("refactoring")
        self.assertListKeyEqual(
            self.pull.get_labels(),
            lambda l: l.name,
            ["wip", "refactoring", "improvement"],
        )
        self.pull.delete_labels()
        self.assertListKeyEqual(self.pull.get_labels(), None, [])
        self.pull.set_labels(wip, refactoring)
        self.assertListKeyEqual(
            self.pull.get_labels(), lambda l: l.name, ["wip", "refactoring"]
        )

    def testDeleteAndSetLabelsWithStringArguments(self):
        wip = "wip"
        refactoring = "refactoring"
        self.assertListKeyEqual(
            self.pull.get_labels(),
            lambda l: l.name,
            ["wip", "refactoring", "improvement"],
        )
        self.pull.delete_labels()
        self.assertListKeyEqual(self.pull.get_labels(), None, [])
        self.pull.set_labels(wip, refactoring)
        self.assertListKeyEqual(
            self.pull.get_labels(), lambda l: l.name, ["wip", "refactoring"]
        )

    def testMerge(self):
        self.assertFalse(self.pull.is_merged())
        status = self.pull.merge()
        self.assertEqual(status.sha, "688208b1a5a074871d0e9376119556897439697d")
        self.assertTrue(status.merged)
        self.assertEqual(status.message, "Pull Request successfully merged")
        self.assertTrue(self.pull.is_merged())
        self.assertEqual(
            repr(status),
            'PullRequestMergeStatus(sha="688208b1a5a074871d0e9376119556897439697d", merged=True)',
        )

    def testMergeWithCommitMessage(self):
        self.g.get_user().get_repo("PyGithub").get_pull(39).merge(
            "Custom commit message created by PyGithub"
        )

    def testAddAndRemoveAssignees(self):
        user1 = "jayfk"
        user2 = self.g.get_user("jzelinskie")
        self.assertListKeyEqual(
            self.pull.assignees, lambda a: a.login, ["stuglaser", "jacquev6"]
        )
        url = self.pull.url
        self.pull.add_to_assignees(user1, user2)
        self.assertListKeyEqual(
            self.pull.assignees,
            lambda a: a.login,
            ["jacquev6", "stuglaser", "jayfk", "jzelinskie"],
        )
        self.assertEqual(self.pull.url, url)
        self.pull.remove_from_assignees(user1, user2)
        self.assertListKeyEqual(
            self.pull.assignees, lambda a: a.login, ["jacquev6", "stuglaser"]
        )
        self.assertEqual(self.pull.url, url)

    def testUpdateBranch(self):
        self.assertTrue(
            self.pull.update_branch("addaebea821105cf6600441f05ff2b413ab21a36")
        )
        self.assertTrue(self.pull.update_branch())
