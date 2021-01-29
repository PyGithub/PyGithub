import datetime
import json
import sys
import time  # NOQA
import unittest

import jwt
import requests  # NOQA

from github.GithubObject import GithubObject

private_key = """
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

public_key = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+5ePolLv6VcWLp2f17g6r6vHl
+eoLuodOOfUl8JK+MVmvXbPaxDy0SS0pQhwTOMtB0VdSt++elklDCadeokhEoGDQ
p411o+kiOhzLxfakp/kewf4UHJnu4M/A2nHmxXVe2lzYnZvZHX5BM4SJo5PGdr0U
e2JtSXoAtYr6qE9maQIDAQAB
-----END PUBLIC KEY-----
"""


class GithubIntegration(unittest.TestCase):
    def setUp(self):
        # This flag ask requester to do some checking,
        # for debug and test purpose. But
        # `InstallationAuthorization.InstallationAuthorization` is a
        # `NonCompletableGithubObject`, it does not have requester.
        # So the check is not needed.
        # see `GithubIntegration.get_access_token`
        self.origin_check_after_init_flag = GithubObject.CHECK_AFTER_INIT_FLAG
        GithubObject.setCheckAfterInitFlag(False)

        self.origin_time = sys.modules["time"].time
        sys.modules["time"].time = lambda: 1550055331.7435968

        class Mock:
            def __init__(self):
                self.args = tuple()
                self.kwargs = dict()

            @property
            def status_code(self):
                return 201

            def json(self):
                return json.loads(self.text)

            @property
            def text(self):
                return (
                    '{"token": "v1.ce63424bc55028318325caac4f4c3a5378ca0038",'
                    '"expires_at": "2019-02-13T11:10:38Z"}'
                )

            def __call__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs
                return self

        self.origin_request_post = sys.modules["requests"].post
        self.mock = Mock()
        sys.modules["requests"].post = self.mock

        class GetMock:
            def __init__(self):
                self.args = tuple()
                self.kwargs = dict()
                self.calls = []

            @property
            def status_code(self):
                return 201

            def json(self):
                return json.loads(self.text)

            @property
            def text(self):
                return (
                    '{"id":111111,"account":{"login":"foo","id":11111111,'
                    '"node_id":"foobar",'
                    '"avatar_url":"https://avatars3.githubusercontent.com/u/11111111?v=4",'
                    '"gravatar_id":"","url":"https://api.github.com/users/foo",'
                    '"html_url":"https://github.com/foo",'
                    '"followers_url":"https://api.github.com/users/foo/followers",'
                    '"following_url":"https://api.github.com/users/foo/following{/other_user}",'
                    '"gists_url":"https://api.github.com/users/foo/gists{/gist_id}",'
                    '"starred_url":"https://api.github.com/users/foo/starred{/owner}{/repo}",'
                    '"subscriptions_url":"https://api.github.com/users/foo/subscriptions",'
                    '"organizations_url":"https://api.github.com/users/foo/orgs",'
                    '"repos_url":"https://api.github.com/users/foo/repos",'
                    '"events_url":"https://api.github.com/users/foo/events{/privacy}",'
                    '"received_events_url":"https://api.github.com/users/foo/received_events",'
                    '"type":"Organization","site_admin":false},"repository_selection":"all",'
                    '"access_tokens_url":"https://api.github.com/app/installations/111111/access_tokens",'
                    '"repositories_url":"https://api.github.com/installation/repositories",'
                    '"html_url":"https://github.com/organizations/foo/settings/installations/111111",'
                    '"app_id":11111,"target_id":11111111,"target_type":"Organization",'
                    '"permissions":{"issues":"write","pull_requests":"write","statuses":"write","contents":"read",'
                    '"metadata":"read"},"events":["pull_request","release"],"created_at":"2019-04-17T16:10:37.000Z",'
                    '"updated_at":"2019-05-03T06:27:48.000Z","single_file_name":null}'
                )

            def __call__(self, *args, **kwargs):
                self.calls.append((args, kwargs))
                self.args = args
                self.kwargs = kwargs
                return self

        self.origin_request_get = sys.modules["requests"].get
        self.get_mock = GetMock()
        sys.modules["requests"].get = self.get_mock

    def testCreateJWT(self):
        from github import GithubIntegration

        integration = GithubIntegration(25216, private_key)
        token = integration.create_jwt()
        payload = jwt.decode(
            token,
            key=public_key,
            algorithms=["RS256"],
            options={"verify_exp": False},
        )
        self.assertDictEqual(
            payload, {"iat": 1550055331, "exp": 1550055391, "iss": 25216}
        )

    def testGetAccessToken(self):
        from github import GithubIntegration

        integration = GithubIntegration(25216, private_key)
        auth_obj = integration.get_access_token(664281)
        self.assertEqual(
            self.mock.args[0],
            "https://api.github.com/app/installations/664281/access_tokens",
        )
        self.assertEqual(auth_obj.token, "v1.ce63424bc55028318325caac4f4c3a5378ca0038")
        self.assertEqual(
            auth_obj.expires_at,
            datetime.datetime(2019, 2, 13, 11, 10, 38, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            repr(auth_obj),
            "InstallationAuthorization(expires_at=2019-02-13 11:10:38+00:00)",
        )

    def test_get_installation(self):
        from github import GithubIntegration

        integr = GithubIntegration("11111", private_key)
        inst = integr.get_installation("foo", "bar")
        self.assertEqual(
            self.get_mock.calls[0][0],
            ("https://api.github.com/repos/foo/bar/installation",),
        )
        self.assertEqual(inst.id, 111111)

    def test_get_installation_custom_base_url(self):
        from github import GithubIntegration

        integr = GithubIntegration("11111", private_key, base_url="https://corp.com/v3")
        inst = integr.get_installation("foo", "bar")
        self.assertEqual(
            self.get_mock.calls[0][0],
            ("https://corp.com/v3/repos/foo/bar/installation",),
        )
        self.assertEqual(inst.id, 111111)

    def tearDown(self):
        GithubObject.setCheckAfterInitFlag(self.origin_check_after_init_flag)
        sys.modules["time"].time = self.origin_time
        sys.modules["requests"].post = self.origin_request_post
        sys.modules["requests"].get = self.origin_request_get
