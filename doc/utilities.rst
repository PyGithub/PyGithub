Utilities
=========

Authentication
--------------

.. autoclass:: github.Auth.Login
.. autoclass:: github.Auth.Token
.. autoclass:: github.Auth.JWT
.. autoclass:: github.Auth.AppAuth
.. autoclass:: github.Auth.AppAuthToken
.. autoclass:: github.Auth.AppInstallationAuth
.. autoclass:: github.Auth.AppUserAuth
.. autoclass:: github.Auth.NetrcAuth

Logging
-------

.. autofunction:: github.enable_console_debug_logging

Error Handling
--------------

.. automodule:: github.GithubException

Default argument
----------------

:const:`github.NotSet` is a special value for arguments you don't want to provide. You should not have to manipulate it directly, because it's the default value of all parameters accepting it. Just note that it is different from :const:`None`, which is an allowed value for some parameters.

Pagination
----------

.. autoclass:: github.PaginatedList.PaginatedList()

Input classes
-------------

.. autoclass:: github.InputFileContent.InputFileContent
.. autoclass:: github.InputGitAuthor.InputGitAuthor
.. autoclass:: github.InputGitTreeElement.InputGitTreeElement
