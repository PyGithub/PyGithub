import time

import deprecated
import jwt
import requests

import github.Installation
import github.InstallationAuthorization
import github.PaginatedList
import github.Requester

from . import Consts, GithubException


class GithubIntegration:
    """
    Main class to obtain tokens for a GitHub integration.
    """

    def __init__(self, integration_id, private_key, base_url=Consts.DEFAULT_BASE_URL):
        """
        :param base_url: string
        :param integration_id: int
        :param private_key: string
        """
        self.base_url = base_url
        self.integration_id = integration_id
        self.private_key = private_key
        assert isinstance(base_url, str), base_url

    def create_jwt(self, expiration=60):
        """
        Creates a signed JWT, valid for 60 seconds by default.
        The expiration can be extended beyond this, to a maximum of 600 seconds.

        :param expiration: int
        :return string:
        """
        now = int(time.time())
        payload = {"iat": now, "exp": now + expiration, "iss": self.integration_id}
        encrypted = jwt.encode(payload, key=self.private_key, algorithm="RS256")

        if isinstance(encrypted, bytes):
            encrypted = encrypted.decode("utf-8")

        return encrypted

    def get_access_token(self, installation_id, user_id=None):
        """
        Get an access token for the given installation id.
        POSTs https://api.github.com/app/installations/<installation_id>/access_tokens
        :param user_id: int
        :param installation_id: int
        :return: :class:`github.InstallationAuthorization.InstallationAuthorization`
        """
        body = {}
        if user_id:
            body = {"user_id": user_id}
        response = requests.post(
            f"{self.base_url}/app/installations/{installation_id}/access_tokens",
            headers={
                "Authorization": f"Bearer {self.create_jwt()}",
                "Accept": Consts.mediaTypeIntegrationPreview,
                "User-Agent": "PyGithub/Python",
            },
            json=body,
        )

        if response.status_code == 201:
            return github.InstallationAuthorization.InstallationAuthorization(
                requester=None,  # not required, this is a NonCompletableGithubObject
                headers={},  # not required, this is a NonCompletableGithubObject
                attributes=response.json(),
                completed=True,
            )
        elif response.status_code == 403:
            raise GithubException.BadCredentialsException(
                status=response.status_code, data=response.text
            )
        elif response.status_code == 404:
            raise GithubException.UnknownObjectException(
                status=response.status_code, data=response.text
            )
        raise GithubException.GithubException(
            status=response.status_code, data=response.text
        )

    @deprecated.deprecated("Use get_repo_installation")
    def get_installation(self, owner, repo):
        """
        :calls: `GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-installation>`_
        :param owner: str
        :param repo: str
        :rtype: :class:`github.Installation.Installation`
        """
        headers = {
            "Authorization": f"Bearer {self.create_jwt()}",
            "Accept": Consts.mediaTypeIntegrationPreview,
            "User-Agent": "PyGithub/Python",
        }

        response = requests.get(
            f"{self.base_url}/repos/{owner}/{repo}/installation",
            headers=headers,
        )
        response_dict = response.json()
        return github.Installation.Installation(None, headers, response_dict, True)

    def get_repo_installation(self, owner, repo):
        return self.get_installation(owner, repo)

    def get_installations(self):
        """
        :calls: GET /app/installations <https://docs.github.com/en/rest/reference/apps#list-installations-for-the-authenticated-app>
        :rtype: :class:`github.PaginatedList.PaginatedList[github.Installation.Installation]`
        """
        return github.PaginatedList.PaginatedList(
            contentClass=github.Installation.Installation,
            requester=github.Requester.Requester(
                login_or_token=None,
                password=None,
                jwt=self.create_jwt(),
                app_id=None,
                app_private_key=None,
                base_url=Consts.DEFAULT_BASE_URL,
                timeout=Consts.DEFAULT_TIMEOUT,
                user_agent="PyGithub/Python",
                per_page=Consts.DEFAULT_PER_PAGE,
                verify=True,
                retry=None,
                pool_size=None,
            ),
            firstUrl="/app/installations",
            firstParams=None,
            headers={
                "Authorization": f"Bearer {self.create_jwt()}",
                "User-Agent": "PyGithub/Python",
            },
            list_item="installations",
        )
