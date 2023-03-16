import time

import deprecated
import jwt

from github import Consts
from github.Installation import Installation
from github.PaginatedList import PaginatedList
from github.Requester import Requester


def create_jwt(
        integration_id,
        private_key,
        expiration=Consts.DEFAULT_JWT_EXPIRY,
        issued_at=Consts.DEFAULT_JWT_ISSUED_AT,
):
    """
    Create a signed JWT
    https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app

    :return string:
    """
    if expiration is not None:
        assert isinstance(expiration, int), expiration
        assert (
                Consts.MIN_JWT_EXPIRY <= expiration <= Consts.MAX_JWT_EXPIRY
        ), expiration

    now = int(time.time())
    payload = {
        "iat": now + issued_at,
        "exp": now + expiration,
        "iss": integration_id,
    }
    encrypted = jwt.encode(payload, key=private_key, algorithm="RS256")

    if isinstance(encrypted, bytes):
        encrypted = encrypted.decode("utf-8")

    return encrypted


class GithubIntegration:
    """
    Class to obtain tokens for a GitHub integration.
    """
    def __init__(
        self,
        integration_id,
        private_key,
        requester: Requester,
    ):
        """
        :param integration_id: int
        :param private_key: string
        """
        assert isinstance(integration_id, (int, str)), integration_id
        assert isinstance(private_key, str), "supplied private key should be a string"

        self.integration_id = integration_id
        self.private_key = private_key
        self.__requester = requester.with_jwt(self.create_jwt)

    def create_jwt(self):
        return create_jwt(self.integration_id, self.private_key)

    def _get_installed_app(self, url):
        """
        Get installation for the given URL.

        :param url: str
        :rtype: :class:`github.Installation.Installation`
        """
        headers, response = self.__requester.requestJsonAndCheck(
            "GET", url, headers={"Accept": Consts.mediaTypeIntegrationPreview}
        )

        return Installation(
            requester=self.__requester,
            headers=headers,
            attributes=response,
            completed=True,
        )

    @deprecated.deprecated("Use get_repo_installation")
    def get_installation(self, owner, repo):
        """
        Deprecated by get_repo_installation

        :calls: `GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app>`
        :param owner: str
        :param repo: str
        :rtype: :class:`github.Installation.Installation`
        """
        return self._get_installed_app(url=f"/repos/{owner}/{repo}/installation")

    def get_installations(self):
        """
        :calls: GET /app/installations <https://docs.github.com/en/rest/reference/apps#list-installations-for-the-authenticated-app>
        :rtype: :class:`github.PaginatedList.PaginatedList[github.Installation.Installation]`
        """
        return PaginatedList(
            contentClass=Installation,
            requester=self.__requester,
            firstUrl="/app/installations",
            firstParams=None,
            headers={"Accept": Consts.mediaTypeIntegrationPreview},
            list_item="installations",
        )

    def get_org_installation(self, org):
        """
        :calls: `GET /orgs/{org}/installation <https://docs.github.com/en/rest/apps/apps#get-an-organization-installation-for-the-authenticated-app>`
        :param org: str
        :rtype: :class:`github.Installation.Installation`
        """
        return self._get_installed_app(url=f"/orgs/{org}/installation")

    def get_repo_installation(self, owner, repo):
        """
        :calls: `GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app>`
        :param owner: str
        :param repo: str
        :rtype: :class:`github.Installation.Installation`
        """
        return self._get_installed_app(url=f"/repos/{owner}/{repo}/installation")

    def get_user_installation(self, username):
        """
        :calls: `GET /users/{username}/installation <https://docs.github.com/en/rest/apps/apps#get-a-user-installation-for-the-authenticated-app>`
        :param username: str
        :rtype: :class:`github.Installation.Installation`
        """
        return self._get_installed_app(url=f"/users/{username}/installation")

    def get_app_installation(self, installation_id):
        """
        :calls: `GET /app/installations/{installation_id} <https://docs.github.com/en/rest/apps/apps#get-an-installation-for-the-authenticated-app>`
        :param installation_id: int
        :rtype: :class:`github.Installation.Installation`
        """
        return self._get_installed_app(url=f"/app/installations/{installation_id}")
