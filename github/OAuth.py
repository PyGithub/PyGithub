from Requester import Requester

DEFAULT_TIMEOUT = 30
DEFAULT_USER_AGENT = 'PyGithub/Python'
BASE_URL = 'https://github.com/login'
AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
TOKEN_URL = 'https://github.com/login/oauth/access_token'


class OAuth(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.requester = Requester(
            client_id=self.client_id, client_secret=self.client_secret,
            base_url=BASE_URL, login_or_token=None, password=None,
            timeout=DEFAULT_TIMEOUT, user_agent=DEFAULT_USER_AGENT, per_page=0)

    def authorize_url(self):
        """First step of the authentication process -
            Redirect user to request GitHub access.
        """
        params = {'client_id': self.client_id}
        headers, data = self.requester.requestJsonAndCheck(
            verb="GET", url=AUTHORIZE_URL, parameters=params)
        return data

    def get_access_token(self, code):
        """Second step of the authentication process -
            GitHub redirects back to your site.
        A temporary `code` is given after the first step is successfully
        completed. Use the code to request an access token for the user.

        """
        params = {'client_id': self.client_id,
                  'client_secret': self.client_secret,
                  'code': code
                }
        headers, data = self.requester.requestJsonAndCheck(
            verb="POST", url=TOKEN_URL, parameters=params)
        return data
