############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Kyle Hornberg <khornberg@users.noreply.github.com>            #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Benjamin K <53038537+treee111@users.noreply.github.com>       #
# Copyright 2024 Benjamin K. <53038537+treee111@users.noreply.github.com>      #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

import github

from . import Framework


class Branch(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.branch = self.repo.get_branch("topic/RewriteWithGeneratedCode")
        self.protected_branch = self.repo.get_branch("integrations")
        self.organization_branch = self.g.get_repo("PyGithub/PyGithub", lazy=True).get_branch("master")

    def testAttributes(self):
        self.assertEqual(
            self.branch._links,
            {
                "self": "https://api.github.com/repos/jacquev6/PyGithub/branches/topic/RewriteWithGeneratedCode",
                "html": "https://github.com/jacquev6/PyGithub/tree/topic/RewriteWithGeneratedCode",
            },
        )
        self.assertEqual(self.branch.commit.sha, "f23da453917a36c8bd48ab8d99e5fa7221884342")
        self.assertEqual(self.branch.name, "topic/RewriteWithGeneratedCode")
        self.assertEqual(self.branch.commit.sha, "f23da453917a36c8bd48ab8d99e5fa7221884342")
        self.assertIsNone(self.branch.pattern)
        self.assertEqual(self.branch.protected, False)
        self.assertIsNone(self.branch.protection.url)
        self.assertEqual(
            self.branch.protection_url,
            "https://api.github.com/repos/jacquev6/PyGithub/branches/topic/RewriteWithGeneratedCode/protection",
        )
        self.assertFalse(self.branch.protected)
        self.assertEqual(repr(self.branch), 'Branch(name="topic/RewriteWithGeneratedCode")')
        self.assertIsNone(self.branch.required_approving_review_count)

    def testEditProtection(self):
        self.protected_branch.edit_protection(
            strict=True,
            require_code_owner_reviews=True,
            required_approving_review_count=2,
            require_last_push_approval=True,
        )
        branch_protection = self.protected_branch.get_protection()
        self.assertTrue(branch_protection.required_status_checks.strict)
        self.assertEqual(branch_protection.required_status_checks.checks, [])
        self.assertEqual(branch_protection.required_status_checks.contexts, [])
        self.assertEqual(
            branch_protection.required_status_checks.contexts_url,
            "https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_status_checks/contexts",
        )
        self.assertTrue(branch_protection.enforce_admins)
        self.assertFalse(branch_protection.required_linear_history)
        self.assertFalse(branch_protection.allow_deletions)
        self.assertFalse(branch_protection.required_pull_request_reviews.dismiss_stale_reviews)
        self.assertTrue(branch_protection.required_pull_request_reviews.require_code_owner_reviews)
        self.assertEqual(
            branch_protection.required_pull_request_reviews.required_approving_review_count,
            2,
        )
        self.assertTrue(branch_protection.required_pull_request_reviews.require_last_push_approval)
        self.assertEqual(
            branch_protection.required_pull_request_reviews.url,
            "https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_pull_request_reviews",
        )

    def testEditProtectionDismissalUsersWithUserOwnedBranch(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_protection(dismissal_users=["jacquev6"])
        self.assertEqual(raisedexp.exception.message, "Validation Failed")
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/repos/branches/#update-branch-protection",
                "message": "Validation Failed",
                "errors": ["Only organization repositories can have users and team restrictions"],
            },
        )

    def testEditProtectionPushRestrictionsWithUserOwnedBranch(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_protection(user_push_restrictions=["jacquev6"], team_push_restrictions=[])
        self.assertEqual(raisedexp.exception.message, "Validation Failed")
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/repos/branches/#update-branch-protection",
                "message": "Validation Failed",
                "errors": ["Only organization repositories can have users and team restrictions"],
            },
        )

    def testEditProtectionPushRestrictionsAndDismissalUser(self):
        self.organization_branch.edit_protection(dismissal_users=["jacquev6"], user_push_restrictions=["jacquev6"])
        branch_protection = self.organization_branch.get_protection()
        self.assertListKeyEqual(
            branch_protection.required_pull_request_reviews.dismissal_users,
            lambda u: u.login,
            ["jacquev6"],
        )
        self.assertListKeyEqual(
            branch_protection.required_pull_request_reviews.dismissal_teams,
            lambda u: u.slug,
            [],
        )
        self.assertListKeyEqual(
            branch_protection.get_user_push_restrictions(),
            lambda u: u.login,
            ["jacquev6"],
        )
        self.assertListKeyEqual(branch_protection.get_team_push_restrictions(), lambda u: u.slug, [])

    def testRemoveProtection(self):
        self.assertTrue(self.protected_branch.protected)
        self.protected_branch.remove_protection()
        protected_branch = self.repo.get_branch("integrations")
        self.assertFalse(protected_branch.protected)
        with self.assertRaises(github.GithubException) as raisedexp:
            protected_branch.get_protection()
        self.assertEqual(raisedexp.exception.message, "Branch not protected")
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/repos/branches/#get-branch-protection",
                "message": "Branch not protected",
            },
        )

    def testEditRequiredStatusChecks(self):
        self.protected_branch.edit_required_status_checks(strict=True)
        required_status_checks = self.protected_branch.get_required_status_checks()
        self.assertTrue(required_status_checks.strict)
        self.assertEqual(required_status_checks.contexts, ["foo/bar"])

    def testEditRequiredStatusChecksContexts(self):
        self.protected_branch.edit_required_status_checks(contexts=["check1", "check2"])
        required_status_checks = self.protected_branch.get_required_status_checks()
        self.assertEqual(required_status_checks.contexts, ["check1", "check2"])

    def testEditRequiredStatusChecksChecks(self):
        self.protected_branch.edit_required_status_checks(checks=["check1", ("check2", -1), ("check3", 123456)])
        required_status_checks = self.protected_branch.get_required_status_checks()
        self.assertEqual(required_status_checks.contexts, ["check1", "check2", "check3"])

    def testRemoveRequiredStatusChecks(self):
        self.protected_branch.remove_required_status_checks()
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.get_required_status_checks()
        self.assertEqual(raisedexp.exception.message, "Required status checks not enabled")
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/repos/branches/#get-required-status-checks-of-protected-branch",
                "message": "Required status checks not enabled",
            },
        )

    def testEditRequiredPullRequestReviews(self):
        self.protected_branch.edit_required_pull_request_reviews(
            dismiss_stale_reviews=True,
            required_approving_review_count=2,
        )
        required_pull_request_reviews = self.protected_branch.get_required_pull_request_reviews()
        self.assertTrue(required_pull_request_reviews.dismiss_stale_reviews)
        self.assertTrue(required_pull_request_reviews.require_code_owner_reviews)
        self.assertEqual(required_pull_request_reviews.required_approving_review_count, 2)

    def testEditRequiredPullRequestReviewsWithTooLargeApprovingReviewCount(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_required_pull_request_reviews(required_approving_review_count=9)
        self.assertEqual(raisedexp.exception.message, "Invalid request.\n\n9 must be less than or equal to 6.")
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/repos/branches/#update-pull-request-review-enforcement-of-protected-branch",
                "message": "Invalid request.\n\n9 must be less than or equal to 6.",
            },
        )

    def testEditRequiredPullRequestReviewsWithUserBranchAndDismissalUsers(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_required_pull_request_reviews(dismissal_users=["jacquev6"])
        self.assertEqual(
            raisedexp.exception.message,
            "Dismissal restrictions are supported only for repositories owned by an organization.",
        )
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/repos/branches/#update-pull-request-review-enforcement-of-protected-branch",
                "message": "Dismissal restrictions are supported only for repositories owned by an organization.",
            },
        )

    def testRemoveRequiredPullRequestReviews(self):
        self.protected_branch.remove_required_pull_request_reviews()
        required_pull_request_reviews = self.protected_branch.get_required_pull_request_reviews()
        self.assertFalse(required_pull_request_reviews.dismiss_stale_reviews)
        self.assertFalse(required_pull_request_reviews.require_code_owner_reviews)
        self.assertEqual(required_pull_request_reviews.required_approving_review_count, 1)
        self.assertFalse(required_pull_request_reviews.require_last_push_approval)

    def testAdminEnforcement(self):
        self.protected_branch.remove_admin_enforcement()
        self.assertFalse(self.protected_branch.get_admin_enforcement())
        self.protected_branch.set_admin_enforcement()
        self.assertTrue(self.protected_branch.get_admin_enforcement())

    def testAllowDeletions(self):
        self.protected_branch.set_allow_deletions()
        self.assertTrue(self.protected_branch.get_allow_deletions())
        self.protected_branch.remove_allow_deletions()
        self.assertFalse(self.protected_branch.get_allow_deletions())

    def testAddUserPushRestrictions(self):
        self.organization_branch.add_user_push_restrictions("sfdye")
        self.assertListKeyEqual(
            self.organization_branch.get_user_push_restrictions(),
            lambda u: u.login,
            ["jacquev6", "sfdye"],
        )

    def testReplaceUserPushRestrictions(self):
        self.assertListKeyEqual(
            self.organization_branch.get_user_push_restrictions(),
            lambda u: u.login,
            ["jacquev6"],
        )
        self.organization_branch.replace_user_push_restrictions("sfdye")
        self.assertListKeyEqual(
            self.organization_branch.get_user_push_restrictions(),
            lambda u: u.login,
            ["sfdye"],
        )

    def testRemoveUserPushRestrictions(self):
        self.organization_branch.remove_user_push_restrictions("jacquev6")
        self.assertListKeyEqual(
            self.organization_branch.get_user_push_restrictions(),
            lambda u: u.login,
            ["sfdye"],
        )

    def testAddTeamPushRestrictions(self):
        self.organization_branch.add_team_push_restrictions("pygithub-owners")
        self.assertListKeyEqual(
            self.organization_branch.get_team_push_restrictions(),
            lambda t: t.slug,
            ["pygithub-owners"],
        )

    def testReplaceTeamPushRestrictions(self):
        self.assertListKeyEqual(
            self.organization_branch.get_team_push_restrictions(),
            lambda t: t.slug,
            ["pygithub-owners"],
        )
        self.organization_branch.replace_team_push_restrictions("org-team")
        self.assertListKeyEqual(
            self.organization_branch.get_team_push_restrictions(),
            lambda t: t.slug,
            ["org-team"],
        )

    def testRemoveTeamPushRestrictions(self):
        self.organization_branch.remove_team_push_restrictions("org-team")
        self.assertListKeyEqual(
            self.organization_branch.get_team_push_restrictions(),
            lambda t: t.slug,
            ["pygithub-owners"],
        )

    def testRemovePushRestrictions(self):
        self.organization_branch.remove_push_restrictions()
        with self.assertRaises(github.GithubException) as raisedexp:
            list(self.organization_branch.get_user_push_restrictions())
        self.assertEqual(raisedexp.exception.message, "Push restrictions not enabled")
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(
            raisedexp.exception.data,
            {
                "documentation_url": "https://developer.github.com/v3/repos/branches/#list-team-restrictions-of-protected-branch",
                "message": "Push restrictions not enabled",
            },
        )

    def testGetRequiredSignatures(self):
        required_signature = self.protected_branch.get_required_signatures()
        assert required_signature

    def testRemoveRequiredSignatures(self):
        self.protected_branch.remove_required_signatures()

    def testAddRequiredSignatures(self):
        self.protected_branch.add_required_signatures()
