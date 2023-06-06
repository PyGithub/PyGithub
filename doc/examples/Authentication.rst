Authentication
==============

Github supports various authentication methods. Depending on the entity that authenticates and the Github API endpoint
being called, only a subset of methods is available.

All authentication methods require this import:

.. code-block:: python

    >>> from github import Auth

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

App authentication
------------------

A Github Apps authenticate by an application id and a private key.

Note that there is only a limited set of endpoints that can be called when authenticated as a Github App.
Instead of using ``github.Github``, entry point ``github.GithubIntegration`` should be used
when authenticated as a Github App:

.. code-block:: python

    >>> gi = GithubIntegration(1234, private_key)
    >>> for installation in gi.get_installations():
    ...     installation.id
    '1234567'

App installation authentication
-------------------------------

A specific installation of a Github App can use the Github API like a normal user.
It authenticates by the Github App authentication (see above) and the installation id.
The ``AppInstallationAuth`` fetches an access token for the installation and handles its
expiration timeout. The access token is refreshed automatically.

.. code-block:: python

    >>> app_auth = Auth.AppAuth(123456, private_key)
    >>> auth = Auth.AppInstallationAuth(app_auth, installation.id)
    >>> g = Github(auth=auth)
    >>> g.get_repo("user/repo").name
    'repo'
