import sys
import time  # NOQA

import jwt
import requests  # NOQA

import github

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

    def testCreateJWT(self):
        self.origin_time = sys.modules["time"].time
        sys.modules["time"].time = lambda: 1550055331.7435968
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        token = github_integration.create_jwt()
        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": False},
        )
        self.assertDictEqual(
            payload, {"iat": 1550055271, "exp": 1550055631, "iss": APP_ID}
        )
        sys.modules["time"].time = self.origin_time

    def testCreateJWTWithExpiration(self):
        self.origin_time = sys.modules["time"].time
        sys.modules["time"].time = lambda: 1550055331.7435968
        github_integration = github.GithubIntegration(
            integration_id=APP_ID,
            private_key=PRIVATE_KEY,
            jwt_expiry=120,
            jwt_issued_at=-30,
        )
        token = github_integration.create_jwt(60)
        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": False},
        )
        self.assertDictEqual(
            payload, {"iat": 1550055301, "exp": 1550055391, "iss": APP_ID}
        )
        sys.modules["time"].time = self.origin_time

    def testGetInstallations(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        installations = github_integration.get_installations()

        self.assertEqual(len(list(installations)), 2)
        self.assertEqual(installations[0].id, self.org_installation_id)
        self.assertEqual(installations[1].id, self.repo_installation_id)

    def testGetAccessToken(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )

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
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        installation = github_integration.get_user_installation(username="ammarmallik")

        self.assertEqual(installation.id, self.user_installation_id)

    def testGetOrgInstallation(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        installation = github_integration.get_org_installation(org="GithubApp-Test-Org")

        self.assertEqual(installation.id, self.org_installation_id)

    def testGetRepoInstallation(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        installation = github_integration.get_repo_installation(
            owner="ammarmallik", repo="test-runner"
        )

        self.assertEqual(installation.id, self.repo_installation_id)

    def testGetAppInstallation(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        installation = github_integration.get_app_installation(
            installation_id=self.org_installation_id
        )

        self.assertEqual(installation.id, self.org_installation_id)

    def testGetInstallationNotFound(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        with self.assertRaises(github.UnknownObjectException) as raisedexp:
            github_integration.get_org_installation(org="GithubApp-Test-Org-404")

        self.assertEqual(raisedexp.exception.status, 404)

    def testGetInstallationWithExpiredJWT(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_org_installation(org="GithubApp-Test-Org")

        self.assertEqual(raisedexp.exception.status, 401)

    def testGetAccessTokenWithExpiredJWT(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(self.repo_installation_id)

        self.assertEqual(raisedexp.exception.status, 401)

    def testGetAccessTokenForNoInstallation(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        with self.assertRaises(github.UnknownObjectException) as raisedexp:
            github_integration.get_access_token(40432121)

        self.assertEqual(raisedexp.exception.status, 404)

    def testGetAccessTokenWithInvalidPermissions(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(
                self.repo_installation_id, permissions={"test-permissions": "read"}
            )

        self.assertEqual(raisedexp.exception.status, 422)

    def testGetAccessTokenWithInvalidData(self):
        github_integration = github.GithubIntegration(
            integration_id=APP_ID, private_key=PRIVATE_KEY
        )
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(
                self.repo_installation_id, permissions="invalid_data"
            )

        self.assertEqual(raisedexp.exception.status, 400)
