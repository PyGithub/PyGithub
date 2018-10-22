# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Kyle Hornberg <khornberg@users.noreply.github.com>            #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
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

import Framework

import github


class Branch(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.branch = self.repo.get_branch("topic/RewriteWithGeneratedCode")
        self.protected_branch = self.repo.get_branch("integrations")
        self.organization_branch = self.g.get_repo("PyGithub/PyGithub", lazy=True).get_branch("master")

    def testAttributes(self):
        self.assertEqual(self.branch.name, "topic/RewriteWithGeneratedCode")
        self.assertEqual(self.branch.commit.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a")
        self.assertEqual(self.branch.protection_url, "https://api.github.com/repos/jacquev6/PyGithub/branches/topic/RewriteWithGeneratedCode/protection")
        self.assertFalse(self.branch.protected)

        # test __repr__() based on this attributes
        self.assertEqual(self.branch.__repr__(), 'Branch(name="topic/RewriteWithGeneratedCode")')

    def testEditProtection(self):
        self.protected_branch.edit_protection(strict=True, require_code_owner_reviews=True, required_approving_review_count=2)
        branch_protection = self.protected_branch.get_protection()
        self.assertTrue(branch_protection.required_status_checks.strict)
        self.assertEqual(branch_protection.required_status_checks.contexts, [])
        self.assertTrue(branch_protection.enforce_admins)
        self.assertFalse(branch_protection.required_pull_request_reviews.dismiss_stale_reviews)
        self.assertTrue(branch_protection.required_pull_request_reviews.require_code_owner_reviews)
        self.assertEqual(branch_protection.required_pull_request_reviews.required_approving_review_count, 2)

    def testEditProtectionDismissalUsersWithUserOwnedBranch(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_protection(dismissal_users=["jacquev6"])
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data, {
                u'documentation_url': u'https://developer.github.com/v3/repos/branches/#update-branch-protection',
                u'message': u'Validation Failed',
                u'errors': [u'Only organization repositories can have users and team restrictions']
            }
        )

    def testEditProtectionPushRestrictionsWithUserOwnedBranch(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_protection(user_push_restrictions=["jacquev6"], team_push_restrictions=[])
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data, {
                u'documentation_url': u'https://developer.github.com/v3/repos/branches/#update-branch-protection',
                u'message': u'Validation Failed',
                u'errors': [u'Only organization repositories can have users and team restrictions']
            }
        )

    def testEditProtectionPushRestrictionsAndDismissalUser(self):
        self.organization_branch.edit_protection(dismissal_users=["jacquev6"], user_push_restrictions=["jacquev6"])
        branch_protection = self.organization_branch.get_protection()
        self.assertListKeyEqual(branch_protection.required_pull_request_reviews.dismissal_users, lambda u: u.login, ["jacquev6"])
        self.assertListKeyEqual(branch_protection.required_pull_request_reviews.dismissal_teams, lambda u: u.slug, [])
        self.assertListKeyEqual(branch_protection.get_user_push_restrictions(), lambda u: u.login, ["jacquev6"])
        self.assertListKeyEqual(branch_protection.get_team_push_restrictions(), lambda u: u.slug, [])

    def testRemoveProtection(self):
        self.assertTrue(self.protected_branch.protected)
        self.protected_branch.remove_protection()
        protected_branch = self.repo.get_branch("integrations")
        self.assertFalse(protected_branch.protected)
        with self.assertRaises(github.GithubException) as raisedexp:
            protected_branch.get_protection()
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(
            raisedexp.exception.data, {
                u'documentation_url': u'https://developer.github.com/v3/repos/branches/#get-branch-protection',
                u'message': u'Branch not protected'
            }
        )

    def testEditRequiredStatusChecks(self):
        self.protected_branch.edit_required_status_checks(strict=True)
        required_status_checks = self.protected_branch.get_required_status_checks()
        self.assertTrue(required_status_checks.strict)
        self.assertEqual(required_status_checks.contexts, ["foo/bar"])

    def testRemoveRequiredStatusChecks(self):
        self.protected_branch.remove_required_status_checks()
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.get_required_status_checks()
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(
            raisedexp.exception.data, {
                u'documentation_url': u'https://developer.github.com/v3/repos/branches/#get-required-status-checks-of-protected-branch',
                u'message': u'Required status checks not enabled'
            }
        )

    def testEditRequiredPullRequestReviews(self):
        self.protected_branch.edit_required_pull_request_reviews(dismiss_stale_reviews=True, required_approving_review_count=2)
        required_pull_request_reviews = self.protected_branch.get_required_pull_request_reviews()
        self.assertTrue(required_pull_request_reviews.dismiss_stale_reviews)
        self.assertTrue(required_pull_request_reviews.require_code_owner_reviews)
        self.assertEqual(required_pull_request_reviews.required_approving_review_count, 2)

    def testEditRequiredPullRequestReviewsWithTooLargeApprovingReviewCount(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_required_pull_request_reviews(required_approving_review_count=9)
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data, {
                u'documentation_url': u'https://developer.github.com/v3/repos/branches/#update-pull-request-review-enforcement-of-protected-branch',
                u'message': u'Invalid request.\n\n9 must be less than or equal to 6.'
            }
        )

    def testEditRequiredPullRequestReviewsWithUserBranchAndDismissalUsers(self):
        with self.assertRaises(github.GithubException) as raisedexp:
            self.protected_branch.edit_required_pull_request_reviews(dismissal_users=["jacquev6"])
        self.assertEqual(raisedexp.exception.status, 422)
        self.assertEqual(
            raisedexp.exception.data, {
                u'documentation_url': u'https://developer.github.com/v3/repos/branches/#update-pull-request-review-enforcement-of-protected-branch',
                u'message': u'Dismissal restrictions are supported only for repositories owned by an organization.'
            }
        )

    def testRemoveRequiredPullRequestReviews(self):
        self.protected_branch.remove_required_pull_request_reviews()
        required_pull_request_reviews = self.protected_branch.get_required_pull_request_reviews()
        self.assertFalse(required_pull_request_reviews.dismiss_stale_reviews)
        self.assertFalse(required_pull_request_reviews.require_code_owner_reviews)
        self.assertEqual(required_pull_request_reviews.required_approving_review_count, 1)

    def testAdminEnforcement(self):
        self.protected_branch.remove_admin_enforcement()
        self.assertFalse(self.protected_branch.get_admin_enforcement())
        self.protected_branch.set_admin_enforcement()
        self.assertTrue(self.protected_branch.get_admin_enforcement())

    def testEditUserPushRestrictions(self):
        self.organization_branch.edit_user_push_restrictions("sfdye")
        self.assertListKeyEqual(self.organization_branch.get_user_push_restrictions(), lambda u: u.login, ["jacquev6", "sfdye"])

    def testEditTeamPushRestrictions(self):
        self.organization_branch.edit_team_push_restrictions("pygithub-owners")
        self.assertListKeyEqual(self.organization_branch.get_team_push_restrictions(), lambda t: t.slug, ["pygithub-owners"])

    def testRemovePushRestrictions(self):
        self.organization_branch.remove_push_restrictions()
        with self.assertRaises(github.GithubException) as raisedexp:
            list(self.organization_branch.get_user_push_restrictions())
        self.assertEqual(raisedexp.exception.status, 404)
        self.assertEqual(
            raisedexp.exception.data, {
                u'documentation_url': u'https://developer.github.com/v3/repos/branches/#list-team-restrictions-of-protected-branch',
                u'message': u'Push restrictions not enabled'
            }
        )

    def testGetRequiredSignatures(self):
        required_signature = self.protected_branch.get_required_signatures()
        assert required_signature

    def testRemoveRequiredSignatures(self):
        self.protected_branch.remove_required_signatures()

    def testAddRequiredSignatures(self):
        self.protected_branch.add_required_signatures()
