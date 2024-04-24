############################ Copyrights and license ##########################
#                                                                              #
# Copyright 2024 Austin Lucas Lake <53884490+austinlucaslake@users.noreply.github.com>#
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

from typing import Any, Dict, List

import github.GithubObject
from github.GithubObject import Attribute


class UserGPGKey(github.GithubObject.CompletableGithubObject):
    """
    This class represents UserGPGKeys.

    The reference can be found here
    https://docs.github.com/en/rest/users/gpg-keys?apiVersion=2022-11-28 

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = github.GithubObject.NotSet
        self._name: Attribute[str] = github.GithubObject.NotSet
        self._primary_key_id: Attribute[int] = github.GithubObject.NotSet
        self._key_id: Attribute[str] = github.GithubObject.NotSet
        self._public_key: Attribute[str] = github.GithubObject.NotSet
        self._emails: Attribute[List[Dict[str, Any]]] = github.GithubObject.NotSet
        self._subkeys: Attribute[List[Dict[str, Any]]] = github.GithubObject.NotSet
        self._can_sign: Attribute[bool] = github.GithubObject.NotSet
        self._can_encrypt_comms: Attribute[bool] = github.GithubObject.NotSet
        self._can_encrypt_storage: Attribute[bool] = github.GithubObject.NotSet
        self._can_certify: Attribute[bool] = github.GithubObject.NotSet
        self._created_at: Attribute[str] = github.GithubObject.NotSet
        self._expires_at: Attribute[str] = github.GithubObject.NotSet
        self._revoked: Attribute[bool] = github.GithubObject.NotSet
        self._raw_key: Attribute[str] = github.GithubObject.NotSet
        

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "title": self._title.value})

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def primary_key_id(self) -> int:
        self._completeIfNotSet(self._primary_key_id)
        return self._primary_key_id.value

    @property
    def key_id(self) -> str:
        self._completeIfNotSet(self._key_id)
        return self._key_id.value

    @property
    def public_key(self) -> str:
        self._completeIfNotSet(self._public_key)
        return self._public_key.value

    @property
    def emails(self) -> List[Dict[str, Any]]:
        self._completeIfNotSet(self._emails)
        return self._emails.value

    @property
    def subkeys(self) -> List[Dict[str, Any]]:
        self._completeIfNotSet(self._subkeys)
        return self._subkeys.value

    @property
    def can_sign(self) -> bool:
        self._completeIfNotSet(self._can_sign)
        return self._can_sign.value

    @property
    def can_encrypt_comms(self) -> bool:
        self._completeIfNotSet(self._can_encrypt_comms)
        return self._can_encrypt_comms.value
    
    @property
    def can_encrypt_storage(self) -> bool:
        self._completeIfNotSet(self._can_encrypt_storage)
        return self._can_encrypt_storage.value

    @property
    def can_certify(self) -> bool:
        self._completeIfNotSet(self._can_certify)
        return self._can_certify.value

    @property
    def created_at(self) -> str:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def expires_at(self) -> str:
        self._completeIfNotSet(self._expires_at)
        return self._expires_at.value

    @property
    def revoked(self) -> bool:
        self._completeIfNotSet(self._revoked)
        return self._revoked.value

    @property
    def raw_key(self) -> str:
        self._completeIfNotSet(self._raw_key)
        return self._raw_key.value

    def delete(self) -> None:
        """
        :calls: `DELETE /user/keys/{gpg_key_id} <https://docs.github.com/en/rest/users/gpg-keys?apiVersion=2022-11-28#delete-a-gpg-key-for-the-authenticated-user>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"https://api.github.com/user/gpg_keys/{self.id}")

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "primary_key_id" in attributes:  # pragma no branch
            self._primary_key_id = self._makeIntAttribute(attributes["primary_key_id"])
        if "key_id" in attributes:  # pragma no branch
            self._key_id = self._makeStringAttribute(attributes["key_id"])
        if "public_key" in attributes:  # pragma no branch
            self._public_key = self._makeStringAttribute(attributes["public_key"])
        if "emails" in attributes:  # pragma no branch
            self._emails = self._makeListOfDictsAttribute(attributes["emails"])
        if "subkeys" in attributes:  # pragma no branch
            self._subkeys = self._makeListOfDictsAttribute(attributes["subkeys"])
        if "can_sign" in attributes:  # pragma no branch
            self._can_sign = self._makeBoolAttribute(attributes["can_sign"])
        if "can_encrypt_comms" in attributes:  # pragma no branch
            self._can_encrypt_comms = self._makeBoolAttribute(attributes["can_encrypt_comms"])
        if "can_encrypt_storage" in attributes:  # pragma no branch
            self._can_encrypt_storage = self._makeBoolAttribute(attributes["can_encrypt_storage"])
        if "can_certify" in attributes:  # pragma no branch
            self._can_certify = self._makeBoolAttribute(attributes["can_certify"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeStringAttribute(attributes["created_at"])
        if "expires_at" in attributes:  # pragma no branch
            self._expires_at = self._makeStringAttribute(attributes["expires_at"])
        if "revoked" in attributes:  # pragma no branch
            self._revoked = self._makeBoolAttribute(attributes["revoked"])
        if "raw_key" in attributes:  # pragma no branch
            self._raw_key = self._makeStringAttribute(attributes["raw_key"])
