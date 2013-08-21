This is a Python (2 and 3) library to access the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

It covers the **full** API (except recent additions, see "What's missing" bellow), and all methods are tested against the real Github site.

Should you have any question, any remark, or if you find a bug, or if there is something you can do with the API but not with PyGithub, please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

PyGithub is stable. I will maintain it up to date with the API, and fix bugs if any, but I don't plan new heavy developments.

What's new?
===========


`Version 1.18.0 <https://github.com/jacquev6/PyGithub/issues?milestone=30&state=closed>`_ (August ??th, 2013) (Bénodet edition)
-------------------------------------------------------------------------------------------------------------------------------

* `Issues <https://github.com/jacquev6/PyGithub/pull/181>`_' ``repository`` attribute will never be ``None``. Thank you `stuglaser <https://github.com/stuglaser>`_ for the pull request
* No more false assumption on `rate_limiting <https://github.com/jacquev6/PyGithub/pull/186>`_, and creation of ``rate_limiting_resettime``. Thank you `edjackson <https://github.com/edjackson>`_ for the pull request
* `New <https://github.com/jacquev6/PyGithub/pull/187>`_ parameters ``since`` and ``until`` to ``Repository.get_commits``. Thank you `apetresc <https://github.com/apetresc>`_ for the pull request
* `Catch <https://github.com/jacquev6/PyGithub/pull/182>`_ Json parsing exception for some internal server errors, and throw a better exception. Thank you `MarkRoddy <https://github.com/MarkRoddy>`_ for the pull request
* `Allow <https://github.com/jacquev6/PyGithub/pull/184>`_ reversed iteration of ``PaginatedList``s. Thank you `davidbrai <https://github.com/davidbrai>`_ for the pull request

What's missing?
===============

We now have automated ways to list URLs documented in `the reference of Github API v3 <http://developer.github.com>`_ and not covered by PyGithub.

Github API v3 URLs not (yet) covered by PyGithub
------------------------------------------------

* ``/applications/:client_id/tokens/:access_token`` (GET)
* ``/feeds`` (GET)
* ``/gists/:id/forks`` (POST)

  * instead, ``Gist.create_fork`` calls the old URL ``/gists/:id/fork``

* ``/meta`` (GET)
* ``/notifications`` (PUT)
* ``/notifications/emails`` (GET)
* ``/notifications/emails`` (PATCH)
* ``/notifications/global/emails`` (GET)
* ``/notifications/global/emails`` (PUT)
* ``/notifications/organization/:org/emails`` (GET)
* ``/notifications/organization/:org/emails`` (PUT)
* ``/notifications/settings`` (GET)
* ``/notifications/settings`` (PATCH)
* ``/notifications/threads/:id`` (PATCH)
* ``/notifications/threads/:id/subscription`` (DELETE)
* ``/notifications/threads/:id/subscription`` (GET)
* ``/notifications/threads/:id/subscription`` (PUT)
* ``/rate_limit`` (GET)

  * should be called in method ``Github.get_rate_limit``. See also ``Github.rate_limiting``

* ``/repos/:owner/:repo/contents/:path`` (DELETE)
* ``/repos/:owner/:repo/contents/:path`` (PUT)
* ``/repos/:owner/:repo/hooks/:id/tests`` (POST)

  * instead, ``Hook.test`` calls the old URL ``/repos/:owner/:repo/hooks/:id/test``

* ``/repos/:owner/:repo/notifications`` (GET)
* ``/repos/:owner/:repo/notifications`` (PUT)
* ``/repos/:owner/:repo/stats/code_frequency`` (GET)
* ``/repos/:owner/:repo/stats/commit_activity`` (GET)
* ``/repos/:owner/:repo/stats/contributors`` (GET)
* ``/repos/:owner/:repo/stats/participation`` (GET)
* ``/repos/:owner/:repo/stats/punch_card`` (GET)
* ``/repos/:owner/:repo/subscription`` (DELETE)
* ``/repos/:owner/:repo/subscription`` (GET)
* ``/repos/:owner/:repo/subscription`` (PUT)
* ``/repositories`` (GET)

  * should be called in method ``Github.get_repos``

* ``/search/code`` (GET)
* ``/search/issues`` (GET)
* ``/search/repositories`` (GET)
* ``/search/users`` (GET)
* ``/users/:user/following/:target_user`` (GET)

  * should be called in method ``NamedUser.has_in_following``

Documentation
=============

All the documentation is here: http://jacquev6.github.com/PyGithub.
