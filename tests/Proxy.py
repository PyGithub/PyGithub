import sys
from github.MainClass import Github
from github.Requester import Requester
import github.MainClass

if sys.version_info[0] == 3:
    from unittest import mock
else:
    import mock

@mock.patch("github.MainClass.Requester", autospec=True)
def test_proxy_arg(requester_m):
    git_url = "https:/gitenterprise.local"
    git_token = "12345678910"
    proxy_dict = {"http": "proxy.mylocal:80", "https": "proxy.mylocal:80"}

    g = github.MainClass.Github(base_url=git_url, login_or_token=git_token, proxies=proxy_dict)

    requester_m.assert_called_once()
    requester_m.assert_called_with(git_token, None, None, git_url, 15, 'PyGithub/Python', 30, True, None, None,
                                   proxies=proxy_dict)
