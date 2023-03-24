import deprecated

from github import Consts
from github.AppAuthentication import AppAuthentication
from github.AppInstallationAuthentication import AppInstallationAuthentication
from github.Installation import Installation
from github.MainClass import Github
from github.PaginatedList import PaginatedList
from github.Requester import Requester


class GithubIntegration:
    """
    Main class to obtain tokens for a GitHub integration.
    """

    def __init__(
        self,
        app_id,
        private_key,
        base_url=Consts.DEFAULT_BASE_URL,
        timeout=Consts.DEFAULT_TIMEOUT,
        user_agent="PyGithub/Python",
        per_page=Consts.DEFAULT_PER_PAGE,
        verify=True,
        retry=None,
        pool_size=None,
    ):
        """
        :param app_id: int
        :param private_key: string
        :param base_url: string
        :param timeout: integer
        :param user_agent: string
        :param per_page: int
        :param verify: boolean or string
        :param retry: int or urllib3.util.retry.Retry object
        :param pool_size: int
        """
        assert isinstance(app_id, (int, str)), app_id
        assert isinstance(private_key, str), "supplied private key should be a string"

        self.app_id = app_id
        self.private_key = private_key
        self.app_auth = AppAuthentication(app_id, private_key)
        self.__base_url = base_url
        self.__timeout = timeout
        self.__user_agent = user_agent
        self.__per_page = per_page
        self.__verify = verify
        self.__retry = retry
        self.__pool_size = pool_size
        self.__requester = Requester(
            login_or_token=None,
            password=None,
            jwt=self.app_auth.create_jwt,
            app_auth=None,
            base_url=base_url,
            timeout=timeout,
            user_agent=user_agent,
            per_page=per_page,
            verify=verify,
            retry=retry,
            pool_size=pool_size,
        )

    # only here for backward compatibility
    @deprecated.deprecated(
        reason="""
        GithubIntegration.create_jwt() is deprecated, use
          GithubIntegration.app_auth.create_jwt() or
          AppAuthentication(app_id, private_key, jwt_expiry=expiration) or
          Github(jwt=AppAuthentication(app_id, private_key).create_jwt) instead.
        """
    )
    def create_jwt(self, expiration=None):
        if expiration is None:
            return self.app_auth.create_jwt()
        else:
            app_auth = AppAuthentication(
                self.app_id, self.private_key, jwt_expiry=expiration
            )
            return app_auth.create_jwt()

    def get_app_installation_authentication(
        self,
        installation_id,
        permissions=None,
        jwt_expiry=Consts.DEFAULT_JWT_EXPIRY,
        jwt_issued_at=Consts.DEFAULT_JWT_ISSUED_AT,
    ):
        """
        Get an app installation authentication.

        :param installation_id: int. App installation id
        :param permissions: Dict[str, str]
        :param jwt_expiry: int
        :param jwt_issued_at: int
        :rtype: :class:`github.Github`
        """
        return AppInstallationAuthentication(
            self.app_id,
            self.private_key,
            installation_id,
            permissions,
            jwt_expiry,
            jwt_issued_at,
        )._get_access_token_func(self.__requester)()

    def get_github_for_installation(
        self,
        installation_id,
        permissions=None,
        jwt_expiry=Consts.DEFAULT_JWT_EXPIRY,
        jwt_issued_at=Consts.DEFAULT_JWT_ISSUED_AT,
    ):
        """
        Get a Github instance authenticated as installation with this installation id.

        :param installation_id: int. App installation id
        :param permissions: Dict[str, str]
        :param jwt_expiry: int
        :param jwt_issued_at: int
        :rtype: :class:`github.Github`
        """
        app_auth = AppInstallationAuthentication(
            self.app_id,
            self.private_key,
            installation_id,
            permissions,
            jwt_expiry,
            jwt_issued_at,
        )

        return Github(
            login_or_token=None,
            password=None,
            jwt=None,
            app_auth=app_auth,
            base_url=self.__base_url,
            timeout=self.__timeout,
            user_agent=self.__user_agent,
            per_page=self.__per_page,
            verify=self.__verify,
            retry=self.__retry,
            pool_size=self.__pool_size,
        )

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
