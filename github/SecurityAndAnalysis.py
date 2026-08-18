############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Nikolay Yurin <yurinnick93@gmail.com>                         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Caleb McCombs <caleb@mccombalot.net>                          #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from typing import TYPE_CHECKING, Any

from typing_extensions import deprecated

import github.SecurityAndAnalysisFeature
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.SecurityAndAnalysisFeature import SecurityAndAnalysisFeature


class SecurityAndAnalysis(NonCompletableGithubObject):
    """
    This class represents Security and Analysis Settings.

    The OpenAPI schema can be found at

    - /components/schemas/security-and-analysis

    """

    def _initAttributes(self) -> None:
        self._advanced_security: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._code_security: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._dependabot_security_updates: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning_ai_detection: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning_delegated_alert_dismissal: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning_delegated_bypass: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning_delegated_bypass_options: Attribute[dict[str, Any]] = NotSet
        self._secret_scanning_non_provider_patterns: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning_push_protection: Attribute[SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning_validity_checks: Attribute[SecurityAndAnalysisFeature] = NotSet

    def __repr__(self) -> str:
        repr_attributes = {
            "advanced_security": repr(self._advanced_security.value),
            "code_security": repr(self._code_security.value),
            "dependabot_security_updates": repr(self._dependabot_security_updates.value),
            "secret_scanning": repr(self._secret_scanning.value),
            "secret_scanning_ai_detection": repr(self._secret_scanning_ai_detection.value),
            "secret_scanning_delegated_alert_dismissal": repr(self._secret_scanning_delegated_alert_dismissal.value),
            "secret_scanning_delegated_bypass": repr(self._secret_scanning_delegated_bypass.value),
            "secret_scanning_delegated_bypass_options": repr(self._secret_scanning_delegated_bypass_options.value),
            "secret_scanning_non_provider_patterns": repr(self._secret_scanning_non_provider_patterns.value),
            "secret_scanning_push_protection": repr(self._secret_scanning_push_protection.value),
            "secret_scanning_validity_checks": repr(self._secret_scanning_validity_checks.value),
        }

        return self.get__repr__(repr_attributes)

    @property
    def advanced_security(self) -> SecurityAndAnalysisFeature:
        return self._advanced_security.value

    @property
    def code_security(self) -> SecurityAndAnalysisFeature:
        return self._code_security.value

    @property
    def dependabot_security_updates(self) -> SecurityAndAnalysisFeature:
        return self._dependabot_security_updates.value

    @property
    def secret_scanning(self) -> SecurityAndAnalysisFeature:
        return self._secret_scanning.value

    @property
    def secret_scanning_ai_detection(self) -> SecurityAndAnalysisFeature:
        return self._secret_scanning_ai_detection.value

    @property
    def secret_scanning_delegated_alert_dismissal(self) -> SecurityAndAnalysisFeature:
        return self._secret_scanning_delegated_alert_dismissal.value

    @property
    def secret_scanning_delegated_bypass(self) -> SecurityAndAnalysisFeature:
        return self._secret_scanning_delegated_bypass.value

    @property
    def secret_scanning_delegated_bypass_options(self) -> dict[str, Any]:
        return self._secret_scanning_delegated_bypass_options.value

    @property
    def secret_scanning_non_provider_patterns(self) -> SecurityAndAnalysisFeature:
        return self._secret_scanning_non_provider_patterns.value

    @property
    def secret_scanning_push_protection(self) -> SecurityAndAnalysisFeature:
        return self._secret_scanning_push_protection.value

    @property
    @deprecated("Property secret_scanning_validity_checks is deprecated and will be removed")
    def secret_scanning_validity_checks(self) -> SecurityAndAnalysisFeature:
        return self._secret_scanning_validity_checks.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "advanced_security" in attributes:  # pragma no branch
            self._advanced_security = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature, attributes["advanced_security"]
            )
        if "code_security" in attributes:  # pragma no branch
            self._code_security = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature, attributes["code_security"]
            )
        if "dependabot_security_updates" in attributes:  # pragma no branch
            self._dependabot_security_updates = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature, attributes["dependabot_security_updates"]
            )
        if "secret_scanning" in attributes:  # pragma no branch
            self._secret_scanning = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature, attributes["secret_scanning"]
            )
        if "secret_scanning_ai_detection" in attributes:  # pragma no branch
            self._secret_scanning_ai_detection = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature, attributes["secret_scanning_ai_detection"]
            )
        if "secret_scanning_delegated_alert_dismissal" in attributes:  # pragma no branch
            self._secret_scanning_delegated_alert_dismissal = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature,
                attributes["secret_scanning_delegated_alert_dismissal"],
            )
        if "secret_scanning_delegated_bypass" in attributes:  # pragma no branch
            self._secret_scanning_delegated_bypass = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature,
                attributes["secret_scanning_delegated_bypass"],
            )
        if "secret_scanning_delegated_bypass_options" in attributes:  # pragma no branch
            self._secret_scanning_delegated_bypass_options = self._makeDictAttribute(
                attributes["secret_scanning_delegated_bypass_options"]
            )
        if "secret_scanning_non_provider_patterns" in attributes:  # pragma no branch
            self._secret_scanning_non_provider_patterns = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature,
                attributes["secret_scanning_non_provider_patterns"],
            )
        if "secret_scanning_push_protection" in attributes:  # pragma no branch
            self._secret_scanning_push_protection = self._makeClassAttribute(
                github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature,
                attributes["secret_scanning_push_protection"],
            )
