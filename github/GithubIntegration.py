import time

import deprecated
import jwt

from github import Consts
from github.GithubException import GithubException
from github.Installation import Installation
from github.InstallationAuthorization import InstallationAuthorization
from github.PaginatedList import PaginatedList
from github.Requester import Requester


class GithubIntegration:
    """
    Main class to obtain tokens for a GitHub integration.
    """

    def __init__(
        self,
        integration_id,
        private_key,
        base_url=Consts.DEFAULT_BASE_URL,
        jwt_expiry=Consts.DEFAULT_JWT_EXPIRY,
        jwt_issued_at=Consts.DEFAULT_JWT_ISSUED_AT,
    ):
        """
        :param integration_id: int
        :param private_key: string
        :param base_url: string
        :param jwt_expiry: int. Expiry of the JWT used to get the information about this integration.
          The default expiration is in 5 minutes and is capped at 10 minutes according to GitHub documentation
          https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#generating-a-json-web-token-jwt
        :param jwt_issued_at: int. Number of seconds, relative to now, to set for the "iat" (issued at) parameter.
          The default value is -60 to protect against clock drift
        """
        assert isinstance(integration_id, (int, str)), integration_id
        assert isinstance(private_key, str), "supplied private key should be a string"
        assert isinstance(base_url, str), base_url
        assert isinstance(jwt_expiry, int), jwt_expiry
        assert Consts.MIN_JWT_EXPIRY <= jwt_expiry <= Consts.MAX_JWT_EXPIRY, jwt_expiry
        assert isinstance(jwt_issued_at, int)

        self.base_url = base_url
        self.integration_id = integration_id
        self.private_key = private_key
        self.jwt_expiry = jwt_expiry
        self.jwt_issued_at = jwt_issued_at
        self.__requester = Requester(
            login_or_token=None,
            password=None,
            jwt=self.create_jwt(),
            app_auth=None,
            base_url=self.base_url,
            timeout=Consts.DEFAULT_TIMEOUT,
            user_agent="PyGithub/Python",
            per_page=Consts.DEFAULT_PER_PAGE,
            verify=True,
            retry=None,
            pool_size=None,
        )

    def _get_headers(self):
        """
        Get headers for the requests.

        :return: dict
        """
        return {
            "Authorization": f"Bearer {self.create_jwt()}",
            "Accept": Consts.mediaTypeIntegrationPreview,
            "User-Agent": "PyGithub/Python",
        }

    def _get_installed_app(self, url):
        """
        Get installation for the given URL.

        :param url: str
        :rtype: :class:`github.Installation.Installation`
        """
        headers, response = self.__requester.requestJsonAndCheck(
            "GET", url, headers=self._get_headers()
        )

        return Installation(
            requester=self.__requester,
            headers=headers,
            attributes=response,
            completed=True,
        )

    def create_jwt(self, expiration=None):
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
            "iat": now + self.jwt_issued_at,
            "exp": now + (expiration if expiration is not None else self.jwt_expiry),
            "iss": self.integration_id,
        }
        encrypted = jwt.encode(payload, key=self.private_key, algorithm="RS256")

        if isinstance(encrypted, bytes):
            encrypted = encrypted.decode("utf-8")

        return encrypted

    def get_access_token(self, installation_id, permissions=None):
        """
        :calls: `POST /app/installations/{installation_id}/access_tokens <https://docs.github.com/en/rest/apps/apps#create-an-installation-access-token-for-an-app>`
        :param installation_id: int
        :param permissions: dict
        :return: :class:`github.InstallationAuthorization.InstallationAuthorization`
        """
        if permissions is None:
            permissions = {}

        if not isinstance(permissions, dict):
            raise GithubException(
                status=400, data={"message": "Invalid permissions"}, headers=None
            )

        body = {"permissions": permissions}
        headers, response = self.__requester.requestJsonAndCheck(
            "POST",
            f"/app/installations/{installation_id}/access_tokens",
            headers=self._get_headers(),
            input=body,
        )

        return InstallationAuthorization(
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
            headers=self._get_headers(),
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
