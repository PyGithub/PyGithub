############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Kyle Hornberg <khornberg@users.noreply.github.com>            #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Juan Manuel "Kang" Pérez <kangcoding@gmail.com>               #
# Copyright 2023 Kevin Grandjean <Muscaw@users.noreply.github.com>             #
# Copyright 2023 Paul Luna <paulluna0215@gmail.com>                            #
# Copyright 2023 Thomas Devoogdt <thomas@devoogdt.com>                         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 terenho <33275803+terenho@users.noreply.github.com>           #
# Copyright 2024 Benjamin K <53038537+treee111@users.noreply.github.com>       #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from typing import TYPE_CHECKING, Any

import github.BranchProtection
import github.Commit
import github.RequiredPullRequestReviews
import github.RequiredStatusChecks
from github import Consts
from github.GithubObject import (
    Attribute,
    NonCompletableGithubObject,
    NotSet,
    Opt,
    is_defined,
    is_optional,
    is_optional_list,
    is_undefined,
)

if TYPE_CHECKING:
    from github.BranchProtection import BranchProtection
    from github.Commit import Commit
    from github.NamedUser import NamedUser
    from github.PaginatedList import PaginatedList
    from github.RequiredPullRequestReviews import RequiredPullRequestReviews
    from github.RequiredStatusChecks import RequiredStatusChecks
    from github.Team import Team


class Branch(NonCompletableGithubObject):
    """
    This class represents Branches.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#branches

    """

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def commit(self) -> Commit:
        return self._commit.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def protected(self) -> bool:
        return self._protected.value

    @property
    def protection_url(self) -> str:
        return self._protection_url.value

    def _initAttributes(self) -> None:
        self._commit: Attribute[Commit] = github.GithubObject.NotSet
        self._name: Attribute[str] = github.GithubObject.NotSet
        self._protection_url: Attribute[str] = github.GithubObject.NotSet
        self._protected: Attribute[bool] = github.GithubObject.NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "commit" in attributes:  # pragma no branch
            self._commit = self._makeClassAttribute(github.Commit.Commit, attributes["commit"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "protection_url" in attributes:  # pragma no branch
            self._protection_url = self._makeStringAttribute(attributes["protection_url"])
        if "protected" in attributes:  # pragma no branch
            self._protected = self._makeBoolAttribute(attributes["protected"])

    def get_protection(self) -> BranchProtection:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self.protection_url,
            headers={"Accept": Consts.mediaTypeRequireMultipleApprovingReviews},
        )
        return github.BranchProtection.BranchProtection(self._requester, headers, data, completed=True)

    def edit_protection(
        self,
        strict: Opt[bool] = NotSet,
        contexts: Opt[list[str]] = NotSet,
        enforce_admins: Opt[bool] = NotSet,
        dismissal_users: Opt[list[str]] = NotSet,
        dismissal_teams: Opt[list[str]] = NotSet,
        dismissal_apps: Opt[list[str]] = NotSet,
        dismiss_stale_reviews: Opt[bool] = NotSet,
        require_code_owner_reviews: Opt[bool] = NotSet,
        required_approving_review_count: Opt[int] = NotSet,
        user_push_restrictions: Opt[list[str]] = NotSet,
        team_push_restrictions: Opt[list[str]] = NotSet,
        app_push_restrictions: Opt[list[str]] = NotSet,
        required_linear_history: Opt[bool] = NotSet,
        allow_force_pushes: Opt[bool] = NotSet,
        required_conversation_resolution: Opt[bool] = NotSet,
        lock_branch: Opt[bool] = NotSet,
        allow_fork_syncing: Opt[bool] = NotSet,
        users_bypass_pull_request_allowances: Opt[list[str]] = NotSet,
        teams_bypass_pull_request_allowances: Opt[list[str]] = NotSet,
        apps_bypass_pull_request_allowances: Opt[list[str]] = NotSet,
        block_creations: Opt[bool] = NotSet,
        require_last_push_approval: Opt[bool] = NotSet,
        allow_deletions: Opt[bool] = NotSet,
    ) -> BranchProtection:
        """
        :calls: `PUT /repos/{owner}/{repo}/branches/{branch}/protection <https://docs.github.com/en/rest/reference/repos#get-branch-protection>`_

        NOTE: The GitHub API groups strict and contexts together, both must
        be submitted. Take care to pass both as arguments even if only one is
        changing. Use edit_required_status_checks() to avoid this.
        """
        assert is_optional(strict, bool), strict
        assert is_optional_list(contexts, str), contexts
        assert is_optional(enforce_admins, bool), enforce_admins
        assert is_optional_list(dismissal_users, str), dismissal_users
        assert is_optional_list(dismissal_teams, str), dismissal_teams
        assert is_optional_list(dismissal_apps, str), dismissal_apps
        assert is_optional(dismiss_stale_reviews, bool), dismiss_stale_reviews
        assert is_optional(require_code_owner_reviews, bool), require_code_owner_reviews
        assert is_optional(required_approving_review_count, int), required_approving_review_count
        assert is_optional(required_linear_history, bool), required_linear_history
        assert is_optional(allow_force_pushes, bool), allow_force_pushes
        assert is_optional(required_conversation_resolution, bool), required_conversation_resolution
        assert is_optional(lock_branch, bool), lock_branch
        assert is_optional(allow_fork_syncing, bool), allow_fork_syncing
        assert is_optional_list(users_bypass_pull_request_allowances, str), users_bypass_pull_request_allowances
        assert is_optional_list(teams_bypass_pull_request_allowances, str), teams_bypass_pull_request_allowances
        assert is_optional_list(apps_bypass_pull_request_allowances, str), apps_bypass_pull_request_allowances
        assert is_optional(require_last_push_approval, bool), require_last_push_approval
        assert is_optional(allow_deletions, bool), allow_deletions

        post_parameters: dict[str, Any] = {}
        if is_defined(strict) or is_defined(contexts):
            if is_undefined(strict):
                strict = False
            if is_undefined(contexts):
                contexts = []
            post_parameters["required_status_checks"] = {
                "strict": strict,
                "contexts": contexts,
            }
        else:
            post_parameters["required_status_checks"] = None

        if is_defined(enforce_admins):
            post_parameters["enforce_admins"] = enforce_admins
        else:
            post_parameters["enforce_admins"] = None

        if (
            is_defined(dismissal_users)
            or is_defined(dismissal_teams)
            or is_defined(dismissal_apps)
            or is_defined(dismiss_stale_reviews)
            or is_defined(require_code_owner_reviews)
            or is_defined(required_approving_review_count)
            or is_defined(users_bypass_pull_request_allowances)
            or is_defined(teams_bypass_pull_request_allowances)
            or is_defined(apps_bypass_pull_request_allowances)
            or is_defined(require_last_push_approval)
        ):
            post_parameters["required_pull_request_reviews"] = {}
            if is_defined(dismiss_stale_reviews):
                post_parameters["required_pull_request_reviews"]["dismiss_stale_reviews"] = dismiss_stale_reviews
            if is_defined(require_code_owner_reviews):
                post_parameters["required_pull_request_reviews"][
                    "require_code_owner_reviews"
                ] = require_code_owner_reviews
            if is_defined(required_approving_review_count):
                post_parameters["required_pull_request_reviews"][
                    "required_approving_review_count"
                ] = required_approving_review_count
            if is_defined(require_last_push_approval):
                post_parameters["required_pull_request_reviews"][
                    "require_last_push_approval"
                ] = require_last_push_approval

            dismissal_restrictions = {}
            if is_defined(dismissal_users):
                dismissal_restrictions["users"] = dismissal_users
            if is_defined(dismissal_teams):
                dismissal_restrictions["teams"] = dismissal_teams
            if is_defined(dismissal_apps):
                dismissal_restrictions["apps"] = dismissal_apps

            if dismissal_restrictions:
                post_parameters["required_pull_request_reviews"]["dismissal_restrictions"] = dismissal_restrictions

            bypass_pull_request_allowances = {}
            if is_defined(users_bypass_pull_request_allowances):
                bypass_pull_request_allowances["users"] = users_bypass_pull_request_allowances
            if is_defined(teams_bypass_pull_request_allowances):
                bypass_pull_request_allowances["teams"] = teams_bypass_pull_request_allowances
            if is_defined(apps_bypass_pull_request_allowances):
                bypass_pull_request_allowances["apps"] = apps_bypass_pull_request_allowances

            if bypass_pull_request_allowances:
                post_parameters["required_pull_request_reviews"][
                    "bypass_pull_request_allowances"
                ] = bypass_pull_request_allowances
        else:
            post_parameters["required_pull_request_reviews"] = None
        if (
            is_defined(user_push_restrictions)
            or is_defined(team_push_restrictions)
            or is_defined(app_push_restrictions)
        ):
            if is_undefined(user_push_restrictions):
                user_push_restrictions = []
            if is_undefined(team_push_restrictions):
                team_push_restrictions = []
            if is_undefined(app_push_restrictions):
                app_push_restrictions = []
            post_parameters["restrictions"] = {
                "users": user_push_restrictions,
                "teams": team_push_restrictions,
                "apps": app_push_restrictions,
            }
        else:
            post_parameters["restrictions"] = None
        if is_defined(required_linear_history):
            post_parameters["required_linear_history"] = required_linear_history
        else:
            post_parameters["required_linear_history"] = None
        if is_defined(allow_force_pushes):
            post_parameters["allow_force_pushes"] = allow_force_pushes
        else:
            post_parameters["allow_force_pushes"] = None
        if is_defined(required_conversation_resolution):
            post_parameters["required_conversation_resolution"] = required_conversation_resolution
        else:
            post_parameters["required_conversation_resolution"] = None
        if is_defined(lock_branch):
            post_parameters["lock_branch"] = lock_branch
        else:
            post_parameters["lock_branch"] = None
        if is_defined(allow_fork_syncing):
            post_parameters["allow_fork_syncing"] = allow_fork_syncing
        else:
            post_parameters["allow_fork_syncing"] = None
        if is_defined(block_creations):
            post_parameters["block_creations"] = block_creations
        else:
            post_parameters["block_creations"] = None
        if is_defined(allow_deletions):
            post_parameters["allow_deletions"] = allow_deletions
        else:
            post_parameters["allow_deletions"] = None

        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.protection_url,
            headers={"Accept": Consts.mediaTypeRequireMultipleApprovingReviews},
            input=post_parameters,
        )

        return github.BranchProtection.BranchProtection(self._requester, headers, data, completed=True)

    def remove_protection(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.protection_url,
        )

    def get_required_status_checks(self) -> RequiredStatusChecks:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks <https://docs.github.com/en/rest/reference/repos#branches>`_
        :rtype: :class:`github.RequiredStatusChecks.RequiredStatusChecks`
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.protection_url}/required_status_checks")
        return github.RequiredStatusChecks.RequiredStatusChecks(self._requester, headers, data, completed=True)

    def edit_required_status_checks(
        self,
        strict: Opt[bool] = NotSet,
        contexts: Opt[list[str]] = NotSet,
    ) -> RequiredStatusChecks:
        """
        :calls: `PATCH /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        assert is_optional(strict, bool), strict
        assert is_optional_list(contexts, str), contexts

        post_parameters: dict[str, Any] = NotSet.remove_unset_items({"strict": strict, "contexts": contexts})
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            f"{self.protection_url}/required_status_checks",
            input=post_parameters,
        )

        return github.RequiredStatusChecks.RequiredStatusChecks(self._requester, headers, data, completed=True)

    def remove_required_status_checks(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            f"{self.protection_url}/required_status_checks",
        )

    def get_required_pull_request_reviews(self) -> RequiredPullRequestReviews:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            f"{self.protection_url}/required_pull_request_reviews",
            headers={"Accept": Consts.mediaTypeRequireMultipleApprovingReviews},
        )
        return github.RequiredPullRequestReviews.RequiredPullRequestReviews(
            self._requester, headers, data, completed=True
        )

    def edit_required_pull_request_reviews(
        self,
        dismissal_users: Opt[list[str]] = NotSet,
        dismissal_teams: Opt[list[str]] = NotSet,
        dismissal_apps: Opt[list[str]] = NotSet,
        dismiss_stale_reviews: Opt[bool] = NotSet,
        require_code_owner_reviews: Opt[bool] = NotSet,
        required_approving_review_count: Opt[int] = NotSet,
        require_last_push_approval: Opt[bool] = NotSet,
    ) -> RequiredStatusChecks:
        """
        :calls: `PATCH /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        assert is_optional_list(dismissal_users, str), dismissal_users
        assert is_optional_list(dismissal_teams, str), dismissal_teams
        assert is_optional(dismiss_stale_reviews, bool), dismiss_stale_reviews
        assert is_optional(require_code_owner_reviews, bool), require_code_owner_reviews
        assert is_optional(required_approving_review_count, int), required_approving_review_count
        assert is_optional(require_last_push_approval, bool), require_last_push_approval

        post_parameters: dict[str, Any] = NotSet.remove_unset_items(
            {
                "dismiss_stale_reviews": dismiss_stale_reviews,
                "require_code_owner_reviews": require_code_owner_reviews,
                "required_approving_review_count": required_approving_review_count,
                "require_last_push_approval": require_last_push_approval,
            }
        )

        dismissal_restrictions: dict[str, Any] = NotSet.remove_unset_items(
            {"users": dismissal_users, "teams": dismissal_teams, "apps": dismissal_apps}
        )

        if dismissal_restrictions:
            post_parameters["dismissal_restrictions"] = dismissal_restrictions

        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            f"{self.protection_url}/required_pull_request_reviews",
            headers={"Accept": Consts.mediaTypeRequireMultipleApprovingReviews},
            input=post_parameters,
        )

        return github.RequiredStatusChecks.RequiredStatusChecks(self._requester, headers, data, completed=True)

    def remove_required_pull_request_reviews(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            f"{self.protection_url}/required_pull_request_reviews",
        )

    def get_admin_enforcement(self) -> bool:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.protection_url}/enforce_admins")
        return data["enabled"]

    def set_admin_enforcement(self) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.protection_url}/enforce_admins")

    def remove_admin_enforcement(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.protection_url}/enforce_admins")

    def get_user_push_restrictions(self) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            f"{self.protection_url}/restrictions/users",
            None,
        )

    def get_team_push_restrictions(self) -> PaginatedList[Team]:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        return github.PaginatedList.PaginatedList(
            github.Team.Team,
            self._requester,
            f"{self.protection_url}/restrictions/teams",
            None,
        )

    def add_user_push_restrictions(self, *users: str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users <https://docs.github.com/en/rest/reference/repos#branches>`_
        :users: list of strings (user names)
        """
        assert all(isinstance(element, str) for element in users), users

        headers, data = self._requester.requestJsonAndCheck(
            "POST", f"{self.protection_url}/restrictions/users", input=users
        )

    def replace_user_push_restrictions(self, *users: str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users <https://docs.github.com/en/rest/reference/repos#branches>`_
        :users: list of strings (user names)
        """
        assert all(isinstance(element, str) for element in users), users

        headers, data = self._requester.requestJsonAndCheck(
            "PUT", f"{self.protection_url}/restrictions/users", input=users
        )

    def remove_user_push_restrictions(self, *users: str) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users <https://docs.github.com/en/rest/reference/repos#branches>`_
        :users: list of strings (user names)
        """
        assert all(isinstance(element, str) for element in users), users

        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", f"{self.protection_url}/restrictions/users", input=users
        )

    def add_team_push_restrictions(self, *teams: str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams <https://docs.github.com/en/rest/reference/repos#branches>`_
        :teams: list of strings (team slugs)
        """
        assert all(isinstance(element, str) for element in teams), teams

        headers, data = self._requester.requestJsonAndCheck(
            "POST", f"{self.protection_url}/restrictions/teams", input=teams
        )

    def replace_team_push_restrictions(self, *teams: str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams <https://docs.github.com/en/rest/reference/repos#branches>`_
        :teams: list of strings (team slugs)
        """
        assert all(isinstance(element, str) for element in teams), teams

        headers, data = self._requester.requestJsonAndCheck(
            "PUT", f"{self.protection_url}/restrictions/teams", input=teams
        )

    def remove_team_push_restrictions(self, *teams: str) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams <https://docs.github.com/en/rest/reference/repos#branches>`_
        :teams: list of strings (team slugs)
        """
        assert all(isinstance(element, str) for element in teams), teams

        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", f"{self.protection_url}/restrictions/teams", input=teams
        )

    def remove_push_restrictions(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.protection_url}/restrictions")

    def get_required_signatures(self) -> bool:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            f"{self.protection_url}/required_signatures",
            headers={"Accept": Consts.signaturesProtectedBranchesPreview},
        )
        return data["enabled"]

    def add_required_signatures(self) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.protection_url}/required_signatures",
            headers={"Accept": Consts.signaturesProtectedBranchesPreview},
        )

    def remove_required_signatures(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            f"{self.protection_url}/required_signatures",
            headers={"Accept": Consts.signaturesProtectedBranchesPreview},
        )

    def get_allow_deletions(self) -> bool:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch}/protection/allow_deletions <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.protection_url}/allow_deletions")
        return data["enabled"]

    def set_allow_deletions(self) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/branches/{branch}/protection/allow_deletions <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.protection_url}/allow_deletions")

    def remove_allow_deletions(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/branches/{branch}/protection/allow_deletions <https://docs.github.com/en/rest/reference/repos#branches>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.protection_url}/allow_deletions")
