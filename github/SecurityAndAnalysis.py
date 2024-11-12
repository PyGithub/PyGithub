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

from typing import Any, Dict

import github.SecurityAndAnalysisFeature
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SecurityAndAnalysis(NonCompletableGithubObject):
    """
    This class represents Security and Analysis Settings.
    """

    def _initAttributes(self) -> None:
        self._advanced_security: Attribute[github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature] = NotSet
        self._dependabot_security_updates: Attribute[
            github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature
        ] = NotSet
        self._secret_scanning: Attribute[github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature] = NotSet
        self._secret_scanning_non_provider_patterns: Attribute[
            github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature
        ] = NotSet
        self._secret_scanning_push_protection: Attribute[
            github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature
        ] = NotSet
        self._secret_scanning_validity_checks: Attribute[
            github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature
        ] = NotSet

    def __repr__(self) -> str:
        repr_attributes = {
            "advanced_security": repr(self._advanced_security.value),
            "dependabot_security_updates": repr(self._dependabot_security_updates.value),
            "secret_scanning": repr(self._secret_scanning.value),
            "secret_scanning_non_provider_patterns": repr(self._secret_scanning_non_provider_patterns.value),
            "secret_scanning_push_protection": repr(self._secret_scanning_push_protection.value),
            "secret_scanning_validity_checks": repr(self._secret_scanning_validity_checks.value),
        }

        return self.get__repr__(repr_attributes)

    @property
    def advanced_security(self) -> github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature:
        return self._advanced_security.value

    @property
    def dependabot_security_updates(self) -> github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature:
        return self._dependabot_security_updates.value

    @property
    def secret_scanning(self) -> github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature:
        return self._secret_scanning.value

    @property
    def secret_scanning_non_provider_patterns(self) -> github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature:
        return self._secret_scanning_non_provider_patterns.value

    @property
    def secret_scanning_push_protection(self) -> github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature:
        return self._secret_scanning_push_protection.value

    @property
    def secret_scanning_validity_checks(self) -> github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature:
        return self._secret_scanning_validity_checks.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        def make_attribute(attribute_name: str) -> None:
            if attribute_name in attributes:
                setattr(
                    self,
                    f"_{attribute_name}",
                    self._makeClassAttribute(
                        github.SecurityAndAnalysisFeature.SecurityAndAnalysisFeature, attributes[attribute_name]
                    ),
                )

        make_attribute("advanced_security")
        make_attribute("dependabot_security_updates")
        make_attribute("secret_scanning")
        make_attribute("secret_scanning_non_provider_patterns")
        make_attribute("secret_scanning_push_protection")
        make_attribute("secret_scanning_validity_checks")
