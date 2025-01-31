Authentication
==============

Github supports various authentication methods. Depending on the entity that authenticates and the Github API endpoint
being called, only a subset of methods is available.

All authentication methods require this import:

.. code-block:: python

    >>> from github import Auth
    >>> from github import Github
    >>> from github import GithubIntegration

Login authentication
--------------------

Users can authenticate by a login and password:

.. code-block:: python

    >>> auth = Auth.Login("user_login", "password")
    >>> g = Github(auth=auth)
    >>> g.get_user().login
    'user_login'

OAuth token authentication
--------------------------

Users can authenticate by a token:

.. code-block:: python

    >>> auth = Auth.Token("access_token")
    >>> g = Github(auth=auth)
    >>> g.get_user().login
    'login'

Netrc authentication
--------------------

Write your credentials into a ``.netrc`` file:

.. code-block:: netrc

    machine api.github.com
    login token
    password <TOKEN>

You might need to create the environment variable ``NETRC`` with the path to this file.

Then, use a ``github.Auth.NetrcAuth`` instance to access these information:

.. code-block:: python

    >>> auth = Auth.NetrcAuth()
    >>> g = Github(auth=auth)
    >>> g.get_user().login
    'login'

App authentication
------------------

A Github Apps authenticate by an application id and a private key.

Note that there is only a limited set of endpoints that can be called when authenticated as a Github App.
Instead of using ``github.Github``, entry point ``github.GithubIntegration`` should be used
when authenticated as a Github App:

.. code-block:: python

    >>> auth = Auth.AppAuth(123456, private_key)
    >>> gi = GithubIntegration(auth=auth)
    >>> for installation in gi.get_installations():
    ...     installation.id
    '1234567'

Get a ``github.Github`` instance authenticated as an App installation:

.. code-block:: python

    >>> installation = gi.get_installations()[0]
    >>> g = installation.get_github_for_installation()
    >>> g.get_repo("user/repo").name
    'repo'

App installation authentication
-------------------------------

A specific installation of a Github App can use the Github API like a normal user.
It authenticates by the Github App authentication (see above) and the installation id.
The ``AppInstallationAuth`` fetches an access token for the installation and handles its
expiration timeout. The access token is refreshed automatically.

.. code-block:: python

    >>> auth = Auth.AppAuth(123456, private_key).get_installation_auth(installation_id, token_permissions)
    >>> g = Github(auth=auth)
    >>> g.get_repo("user/repo").name
    'repo'

Alternatively, the `github.Github` instance can be retrieved via `github.GithubIntegration`:

.. code-block:: python

    >>> auth = Auth.AppAuth(123456, private_key)
    >>> gi = GithubIntegration(auth=auth)
    >>> g = gi.get_github_for_installation(installation_id, token_permissions)
    >>> g.get_repo("user/repo").name
    'repo'

App user authentication
-----------------------

A Github App can authenticate on behalf of a user. For this, the user has to `generate a user access token for a Github App <https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user>`__.
This process completes with a one-time ``code``. Together with the ``client_id`` and ``client_secret`` of the app,
a Github App user token can be generated once:

.. code-block:: python

    >>> g = Github()
    >>> app = g.get_oauth_application(client_id, client_secret)
    >>> token = app.get_access_token(code)

Memorize the ``token.refresh_token``, as only this can be used to create new tokens for this user.
The ``token.token`` expires 8 hours, and the ``token.refresh_token`` expires 6 months after creation.

A token can be refreshed as follows. This invalidates the old token and old refresh token, and creates
a new set of token and refresh tokens:

.. code-block:: python

    >>> g = Github()
    >>> app = g.get_oauth_application(client_id, client_secret)
    >>> token = app.refresh_access_token(refresh_token)

You can authenticate with Github using this token:

.. code-block:: python

   >>> auth = app.get_app_user_auth(token)
   >>> g = Github(auth=auth)
   >>> g.get_user().login
   'user_login'

The ``auth`` instance will refresh the token automatically when ``auth.token`` is accessed.
