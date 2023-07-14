############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Yugo Hino <henom06@gmail.com>                                 #
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

import github.Event
import github.Gist
import github.GithubObject
import github.NamedUser
import github.Organization
import github.PaginatedList
import github.Permissions
import github.Plan
import github.Repository


class NamedEnterpriseUser(github.GithubObject.CompletableGithubObject):
    """
    This class represents NamedEnterpriseUsers. The reference can be found here https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses
    """

    def __repr__(self):
        return self.get__repr__({"login": self._github_com_login.value})

    @property
    def github_com_login(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._github_com_login)
        return self._github_com_login.value

    @property
    def github_com_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._github_com_name)
        return self._github_com_name.value

    @property
    def enterprise_server_user_ids(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._enterprise_server_user_ids)
        return self._enterprise_server_user_ids.value

    @property
    def github_com_user(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._github_com_user)
        return self._github_com_user.value

    @property
    def enterprise_server_user(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._enterprise_server_user)
        return self._enterprise_server_user.value

    @property
    def visual_studio_subscription_user(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._visual_studio_subscription_user)
        return self._visual_studio_subscription_user.value

    @property
    def license_type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._license_type)
        return self._license_type.value

    @property
    def github_com_profile(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._github_com_profile)
        return self._github_com_profile.value

    @property
    def github_com_member_roles(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._github_com_member_roles)
        return self._github_com_member_roles.value

    @property
    def github_com_enterprise_roles(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._github_com_enterprise_roles)
        return self._github_com_enterprise_roles.value

    @property
    def github_com_verified_domain_emails(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._github_com_verified_domain_emails)
        return self._github_com_verified_domain_emails.value

    @property
    def github_com_saml_name_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._github_com_saml_name_id)
        return self._github_com_saml_name_id.value

    @property
    def github_com_orgs_with_pending_invites(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._github_com_orgs_with_pending_invites)
        return self._github_com_orgs_with_pending_invites.value

    @property
    def github_com_two_factor_auth(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._github_com_two_factor_auth)
        return self._github_com_two_factor_auth.value

    @property
    def enterprise_server_primary_emails(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._enterprise_server_primary_emails)
        return self._enterprise_server_primary_emails.value

    @property
    def visual_studio_license_status(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._visual_studio_license_status)
        return self._visual_studio_license_status.value

    @property
    def visual_studio_subscription_email(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._visual_studio_subscription_email)
        return self._visual_studio_subscription_email.value

    @property
    def total_user_accounts(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._total_user_accounts)
        return self._total_user_accounts.value

    def _initAttributes(self):
        self._github_com_login = github.GithubObject.NotSet
        self._github_com_name = github.GithubObject.NotSet
        self._enterprise_server_user_ids = github.GithubObject.NotSet
        self._github_com_user = github.GithubObject.NotSet
        self._enterprise_server_user = github.GithubObject.NotSet
        self._visual_studio_subscription_user = github.GithubObject.NotSet
        self._license_type = github.GithubObject.NotSet
        self._github_com_profile = github.GithubObject.NotSet
        self._github_com_member_roles = github.GithubObject.NotSet
        self._github_com_enterprise_roles = github.GithubObject.NotSet
        self._github_com_verified_domain_emails = github.GithubObject.NotSet
        self._github_com_saml_name_id = github.GithubObject.NotSet
        self._github_com_orgs_with_pending_invites = github.GithubObject.NotSet
        self._github_com_two_factor_auth = github.GithubObject.NotSet
        self._enterprise_server_primary_emails = github.GithubObject.NotSet
        self._visual_studio_license_status = github.GithubObject.NotSet
        self._visual_studio_subscription_email = github.GithubObject.NotSet
        self._total_user_accounts = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "github_com_login" in attributes:  # pragma no branch
            self._github_com_login = self._makeStringAttribute(attributes["github_com_login"])
        if "github_com_name" in attributes:  # pragma no branch
            self._github_com_name = self._makeStringAttribute(attributes["github_com_name"])
        if "enterprise_server_user_ids" in attributes:  # pragma no branch
            self._enterprise_server_user_ids = self._makeListOfStringsAttribute(
                attributes["enterprise_server_user_ids"]
            )
        if "github_com_user" in attributes:  # pragma no branch
            self._github_com_user = self._makeBoolAttribute(attributes["github_com_user"])
        if "enterprise_server_user" in attributes:  # pragma no branch
            self._enterprise_server_user = self._makeBoolAttribute(attributes["enterprise_server_user"])
        if "visual_studio_subscription_user" in attributes:  # pragma no branch
            self._visual_studio_subscription_user = self._makeBoolAttribute(
                attributes["visual_studio_subscription_user"]
            )
        if "license_type" in attributes:  # pragma no branch
            self._license_type = self._makeStringAttribute(attributes["license_type"])
        if "github_com_profile" in attributes:  # pragma no branch
            self._github_com_profile = self._makeStringAttribute(attributes["github_com_profile"])
        if "github_com_member_roles" in attributes:  # pragma no branch
            self._github_com_member_roles = self._makeListOfStringsAttribute(attributes["github_com_member_roles"])
        if "github_com_enterprise_roles" in attributes:  # pragma no branch
            self._github_com_enterprise_roles = self._makeListOfStringsAttribute(
                attributes["github_com_enterprise_roles"]
            )
        if "github_com_verified_domain_emails" in attributes:  # pragma no branch
            self._github_com_verified_domain_emails = self._makeListOfStringsAttribute(
                attributes["github_com_verified_domain_emails"]
            )
        if "github_com_saml_name_id" in attributes:  # pragma no branch
            self._github_com_saml_name_id = self._makeStringAttribute(attributes["github_com_saml_name_id"])
        if "github_com_orgs_with_pending_invites" in attributes:  # pragma no branch
            self._github_com_orgs_with_pending_invites = self._makeListOfStringsAttribute(
                attributes["github_com_orgs_with_pending_invites"]
            )
        if "github_com_two_factor_auth" in attributes:  # pragma no branch
            self._github_com_two_factor_auth = self._makeBoolAttribute(attributes["github_com_two_factor_auth"])
        if "enterprise_server_primary_emails" in attributes:  # pragma no branch
            self._enterprise_server_primary_emails = self._makeListOfStringsAttribute(
                attributes["enterprise_server_primary_emails"]
            )
        if "visual_studio_license_status" in attributes:  # pragma no branch
            self._visual_studio_license_status = self._makeStringAttribute(attributes["visual_studio_license_status"])
        if "visual_studio_subscription_email" in attributes:  # pragma no branch
            self._visual_studio_subscription_email = self._makeStringAttribute(
                attributes["visual_studio_subscription_email"]
            )
        if "total_user_accounts" in attributes:  # pragma no branch
            self._total_user_accounts = self._makeIntAttribute(attributes["total_user_accounts"])
