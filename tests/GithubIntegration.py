import time  # NOQA

import requests  # NOQA
from urllib3.exceptions import InsecureRequestWarning

import github
from github import Consts
from github.Auth import AppInstallationAuth

from . import Framework

APP_ID = 243473
PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC+5ePolLv6VcWLp2f17g6r6vHl+eoLuodOOfUl8JK+MVmvXbPa
xDy0SS0pQhwTOMtB0VdSt++elklDCadeokhEoGDQp411o+kiOhzLxfakp/kewf4U
HJnu4M/A2nHmxXVe2lzYnZvZHX5BM4SJo5PGdr0Ue2JtSXoAtYr6qE9maQIDAQAB
AoGAFhOJ7sy8jG+837Clcihso+8QuHLVYTPaD+7d7dxLbBlS8NfaQ9Nr3cGUqm/N
xV9NCjiGa7d/y4w/vrPwGh6UUsA+CvndwDgBd0S3WgIdWvAvHM8wKgNh/GBLLzhT
Bg9BouRUzcT1MjAnkGkWqqCAgN7WrCSUMLt57TNleNWfX90CQQDjvVKTT3pOiavD
3YcLxwkyeGd0VMvKiS4nV0XXJ97cGXs2GpOGXldstDTnF5AnB6PbukdFLHpsx4sW
Hft3LRWnAkEA1pY15ke08wX6DZVXy7zuQ2izTrWSGySn7B41pn55dlKpttjHeutA
3BEQKTFvMhBCphr8qST7Wf1SR9FgO0tFbwJAEhHji2yy96hUyKW7IWQZhrem/cP8
p4Va9CQolnnDZRNgg1p4eiDiLu3dhLiJ547joXuWTBbLX/Y1Qvv+B+a74QJBAMCW
O3WbMZlS6eK6//rIa4ZwN00SxDg8I8FUM45jwBsjgVGrKQz2ilV3sutlhIiH82kk
m1Iq8LMJGYl/LkDJA10CQBV1C+Xu3ukknr7C4A/4lDCa6Xb27cr1HanY7i89A+Ab
eatdM6f/XVqWp8uPT9RggUV9TjppJobYGT2WrWJMkYw=
-----END RSA PRIVATE KEY-----
"""
PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+5ePolLv6VcWLp2f17g6r6vHl
+eoLuodOOfUl8JK+MVmvXbPaxDy0SS0pQhwTOMtB0VdSt++elklDCadeokhEoGDQ
p411o+kiOhzLxfakp/kewf4UHJnu4M/A2nHmxXVe2lzYnZvZHX5BM4SJo5PGdr0U
e2JtSXoAtYr6qE9maQIDAQAB
-----END PUBLIC KEY-----
"""


class GithubIntegration(Framework.BasicTestCase):
    def setUp(self):
        super().setUp()
        self.org_installation_id = 30614487
        self.repo_installation_id = 30614431
        self.user_installation_id = 30614431

    def testDeprecatedAppAuth(self):
        # Replay data copied from testGetInstallations to test authentication only
        with self.assertWarns(DeprecationWarning) as warning:
            github_integration = github.GithubIntegration(
                integration_id=APP_ID, private_key=PRIVATE_KEY
            )
        installations = github_integration.get_installations()
        self.assertEqual(len(list(installations)), 2)
        self.assertWarning(
            warning,
            "Arguments integration_id, private_key, jwt_expiry, jwt_issued_at and "
            "jwt_algorithm are deprecated, please use auth=github.Auth.AppAuth(...) "
            "instead",
        )

    def testRequiredAppAuth(self):
        # GithubIntegration requires AppAuth authentication.
        for auth in [self.oauth_token, self.jwt, self.login]:
            with self.assertRaises(AssertionError) as r:
                github.GithubIntegration(auth=auth)
            self.assertEqual(
                str(r.exception),
                f"GithubIntegration requires github.Auth.AppAuth authentication, not {type(auth)}",
            )

    def testAppAuth(self):
        # Replay data copied from testDeprecatedAppAuth to test parity
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installations = github_integration.get_installations()
        self.assertEqual(len(list(installations)), 2)

    def testNoneAppAuth(self):
        with self.assertRaises(AssertionError):
            github.GithubIntegration(auth=None)

    def testGetInstallations(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installations = github_integration.get_installations()

        self.assertEqual(len(list(installations)), 2)
        self.assertEqual(installations[0].id, self.org_installation_id)
        self.assertEqual(installations[1].id, self.repo_installation_id)

    def testGetGithubForInstallation(self):
        # with verify=False, urllib3.connectionpool rightly may issue an InsecureRequestWarning
        # we ignore InsecureRequestWarning from urllib3.connectionpool
        with self.ignoreWarning(
            category=InsecureRequestWarning, module="urllib3.connectionpool"
        ):
            auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
            github_integration = github.GithubIntegration(
                auth=auth,
                base_url="https://api.github.com",
                timeout=Consts.DEFAULT_TIMEOUT + 10,
                user_agent="PyGithub/Python-Test",
                per_page=Consts.DEFAULT_PER_PAGE + 10,
                verify=False,
                retry=3,
                pool_size=10,
            )

            g = github_integration.get_github_for_installation(36541767)

            self.assertIsInstance(g._Github__requester.auth, AppInstallationAuth)
            self.assertEqual(
                g._Github__requester._Requester__base_url, "https://api.github.com"
            )
            self.assertEqual(
                g._Github__requester._Requester__timeout, Consts.DEFAULT_TIMEOUT + 10
            )
            self.assertEqual(
                g._Github__requester._Requester__userAgent, "PyGithub/Python-Test"
            )
            self.assertEqual(
                g._Github__requester.per_page, Consts.DEFAULT_PER_PAGE + 10
            )
            self.assertEqual(g._Github__requester._Requester__verify, False)
            self.assertEqual(g._Github__requester._Requester__retry, 3)
            self.assertEqual(g._Github__requester._Requester__pool_size, 10)

            repo = g.get_repo("PyGithub/PyGithub")
            self.assertEqual(repo.full_name, "PyGithub/PyGithub")

    def testGetAccessToken(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)

        # Get repo installation access token
        repo_installation_authorization = github_integration.get_access_token(
            self.repo_installation_id
        )
        self.assertEqual(
            repo_installation_authorization.token,
            "ghs_1llwuELtXN5HDOB99XhpcTXdJxbOuF0ZlSmj",
        )
        self.assertDictEqual(
            repo_installation_authorization.permissions,
            {"issues": "read", "metadata": "read"},
        )
        self.assertEqual(
            repo_installation_authorization.repository_selection, "selected"
        )

        # Get org installation access token
        org_installation_authorization = github_integration.get_access_token(
            self.org_installation_id
        )
        self.assertEqual(
            org_installation_authorization.token,
            "ghs_V0xygF8yACXSDz5FM65QWV1BT2vtxw0cbgPw",
        )
        org_permissions = {
            "administration": "write",
            "issues": "write",
            "metadata": "read",
            "organization_administration": "read",
        }
        self.assertDictEqual(
            org_installation_authorization.permissions, org_permissions
        )
        self.assertEqual(
            org_installation_authorization.repository_selection, "selected"
        )

        # Get user installation access token
        user_installation_authorization = github_integration.get_access_token(
            self.user_installation_id
        )
        self.assertEqual(
            user_installation_authorization.token,
            "ghs_1llwuELtXN5HDOB99XhpcTXdJxbOuF0ZlSmj",
        )
        self.assertDictEqual(
            user_installation_authorization.permissions,
            {"issues": "read", "metadata": "read"},
        )
        self.assertEqual(
            user_installation_authorization.repository_selection, "selected"
        )

    def testGetUserInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_user_installation(username="ammarmallik")

        self.assertEqual(installation.id, self.user_installation_id)

    def testGetOrgInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_org_installation(org="GithubApp-Test-Org")

        self.assertEqual(installation.id, self.org_installation_id)

    def testGetRepoInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_repo_installation(
            owner="ammarmallik", repo="test-runner"
        )

        self.assertEqual(installation.id, self.repo_installation_id)

    def testGetAppInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_app_installation(
            installation_id=self.org_installation_id
        )

        self.assertEqual(installation.id, self.org_installation_id)

    def testGetInstallationNotFound(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.UnknownObjectException) as raisedexp:
            github_integration.get_org_installation(org="GithubApp-Test-Org-404")

        self.assertEqual(raisedexp.exception.status, 404)

    def testGetInstallationWithExpiredJWT(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_org_installation(org="GithubApp-Test-Org")

        self.assertEqual(raisedexp.exception.status, 401)

    def testGetAccessTokenWithExpiredJWT(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(self.repo_installation_id)

        self.assertEqual(raisedexp.exception.status, 401)

    def testGetAccessTokenForNoInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.UnknownObjectException) as raisedexp:
            github_integration.get_access_token(40432121)

        self.assertEqual(raisedexp.exception.status, 404)

    def testGetAccessTokenWithInvalidPermissions(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(
                self.repo_installation_id, permissions={"test-permissions": "read"}
            )

        self.assertEqual(raisedexp.exception.status, 422)

    def testGetAccessTokenWithInvalidData(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(
                self.repo_installation_id, permissions="invalid_data"
            )

        self.assertEqual(raisedexp.exception.status, 400)

    def testGetApp(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        app = github_integration.get_app()

        self.assertEqual(app.name, "PyGithubTest")
        self.assertEqual(app.url, "/apps/pygithubtest")
